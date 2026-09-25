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

// Trim head noise.
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'wp_head', 'wp_generator' );
