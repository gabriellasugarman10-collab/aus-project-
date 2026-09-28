<?php
/**
 * AUS theme bootstrap.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'after_setup_theme', function () {
	add_theme_support( 'wp-block-styles' );
	add_theme_support( 'editor-styles' );
	add_editor_style( 'assets/theme.css' );
} );

add_action( 'wp_enqueue_scripts', function () {
	$ver = wp_get_theme()->get( 'Version' );
	wp_enqueue_style( 'aus', get_theme_file_uri( 'assets/theme.css' ), array(), $ver );
} );

add_action( 'init', function () {
	register_block_pattern_category( 'aus', array( 'label' => __( 'AUS', 'aus' ) ) );
} );

/**
 * One-click setup: on activation, create the site's pages and set the home page.
 * Idempotent — existing pages (matched by slug) are left untouched, so re-activating is safe.
 * Slugs mirror the Lovable routes so every CTA link resolves.
 */
add_action( 'after_switch_theme', function () {
	$pages = array(
		'home'     => 'Home',
		'pack'     => 'The Pack',
		'about'    => 'About',
		'book'     => 'Book a free call',
		'checkout' => 'Checkout',
		'free'     => 'Get the Pack free',
	);

	$ids = array();
	foreach ( $pages as $slug => $title ) {
		$existing = get_page_by_path( $slug, OBJECT, 'page' );
		if ( $existing ) {
			$ids[ $slug ] = $existing->ID;
			continue;
		}
		$ids[ $slug ] = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_status'  => 'publish',
				'post_name'    => $slug,
				'post_title'   => $title,
				'post_content' => '<!-- wp:pattern {"slug":"aus/' . $slug . '"} /-->',
				'meta_input'   => array( '_wp_page_template' => 'page-no-title' ),
			)
		);
	}

	if ( ! empty( $ids['home'] ) && ! is_wp_error( $ids['home'] ) ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_on_front', (int) $ids['home'] );
	}

	// Pretty URLs (/pack/, /about/…) — only if the site is still on the default "?p=123" links.
	if ( '' === get_option( 'permalink_structure' ) ) {
		update_option( 'permalink_structure', '/%postname%/' );
	}
	flush_rewrite_rules();
} );

// Trim head noise.
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'wp_head', 'wp_generator' );
