# All site copy lives here. Edit text, run `python3 tools/build-patterns.py`, commit.
# Overwrites theme/aus/parts + patterns, so make copy changes here, not in those files.
import os, html
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "theme", "aus")
e = html.escape

def p(text, cls="", color="", size="", align=""):
    a = {}
    if align: a["align"] = align
    if cls: a["className"] = cls
    if color: a["textColor"] = color
    if size: a["fontSize"] = size
    import json
    attrs = (" " + json.dumps(a)) if a else ""
    c = []
    if align: c.append(f"has-text-align-{align}")
    if cls: c.append(cls)
    if color: c += [f"has-{color}-color", "has-text-color"]
    if size: c.append(f"has-{size}-font-size")
    ca = f' class="{" ".join(c)}"' if c else ""
    return f"<!-- wp:paragraph{attrs} -->\n<p{ca}>{text}</p>\n<!-- /wp:paragraph -->"

def h(text, level=2, align="", cls=""):
    import json
    a = {}
    if align: a["textAlign"] = align
    if level != 2: a["level"] = level
    if cls: a["className"] = cls
    attrs = (" " + json.dumps(a)) if a else ""
    c = ["wp-block-heading"] + ([f"has-text-align-{align}"] if align else []) + ([cls] if cls else [])
    return f'<!-- wp:heading{attrs} -->\n<h{level} class="{" ".join(c)}">{text}</h{level}>\n<!-- /wp:heading -->'

def buttons(items, justify="left"):
    out = [f'<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"{justify}","flexWrap":"wrap"}}}} -->', '<div class="wp-block-buttons">']
    for label, href, outline in items:
        if outline:
            out.append(f'<!-- wp:button {{"className":"is-style-outline"}} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{href}">{label}</a></div>\n<!-- /wp:button -->')
        else:
            out.append(f'<!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{href}">{label}</a></div>\n<!-- /wp:button -->')
    out += ['</div>', '<!-- /wp:buttons -->']
    return "\n".join(out)

def ticks(items, cls="bfo-ticks"):
    li = "\n".join(f"<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->" for i in items)
    return f'<!-- wp:list {{"className":"{cls}"}} -->\n<ul class="wp-block-list {cls}">\n{li}\n</ul>\n<!-- /wp:list -->'

def section(inner, bg="", cls="", size="", pad="60"):
    import json
    a = {"align": "full", "style": {"spacing": {"padding": {"top": f"var:preset|spacing|{pad}", "bottom": f"var:preset|spacing|{pad}"}}}, "layout": {"type": "constrained"}}
    if bg: a["backgroundColor"] = bg
    if cls: a["className"] = cls
    if size: a["layout"]["contentSize"] = size
    c = ["wp-block-group", "alignfull"] + ([cls] if cls else []) + ([f"has-{bg}-background-color", "has-background"] if bg else [])
    st = f"padding-top:var(--wp--preset--spacing--{pad});padding-bottom:var(--wp--preset--spacing--{pad})"
    return f'<!-- wp:group {json.dumps(a)} -->\n<div class="{" ".join(c)}" style="{st}">\n{inner}\n</div>\n<!-- /wp:group -->'

def group(inner, cls="", layout='{"type":"default"}', align=""):
    a = []
    if align: a.append(f'"align":"{align}"')
    if cls: a.append(f'"className":"{cls}"')
    a.append(f'"layout":{layout}')
    c = ["wp-block-group"] + ([f"align{align}"] if align else []) + ([cls] if cls else [])
    return f'<!-- wp:group {{{",".join(a)}}} -->\n<div class="{" ".join(c)}">\n{inner}\n</div>\n<!-- /wp:group -->'

def grid(cards, min_w="20rem"):
    return group("\n".join(cards), cls="bfo-grid", layout=f'{{"type":"grid","minimumColumnWidth":"{min_w}"}}', align="wide")

def card(title, body, num=""):
    inner = (p(num, cls="bfo-num") + "\n" if num else "") + h(title, 3) + "\n" + p(body, color="muted")
    return group(inner, cls="is-style-card")

def pattern(slug, title, body):
    with open(f"{T}/patterns/{slug}.php", "w") as f:
        f.write(f"<?php\n/**\n * Title: {title}\n * Slug: aus/{slug}\n * Categories: aus\n * Inserter: yes\n */\n?>\n{body}\n")

def hero(eyebrow, title, lede, btns=None, note=""):
    parts = []
    if eyebrow: parts.append(p(eyebrow, cls="bfo-eyebrow", align="center"))
    parts += [h(title, 1, "center"), p(lede, color="muted", size="large", align="center")]
    if btns: parts.append(buttons(btns, "center"))
    if note: parts.append(p(note, color="muted", size="small", align="center"))
    return section("\n".join(parts), size="820px")

def cta(title, body, label, href, pre=""):
    return section("\n".join([h(title, 2, "center"), p(body, align="center"), buttons([(label, href, False)], "center")]), bg="contrast", cls="bfo-dark")

# ---------- parts ----------
open(f"{T}/parts/header.html", "w").write('''<!-- wp:group {"align":"full","className":"bfo-header","style":{"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull bfo-header" style="padding-top:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30)">
<!-- wp:group {"align":"wide","layout":{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap"}} -->
<div class="wp-block-group alignwide">
<!-- wp:group {"className":"bfo-brand","layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-group bfo-brand">
<!-- wp:paragraph {"className":"bfo-logo"} -->
<p class="bfo-logo"><a href="/" aria-hidden="true" tabindex="-1">OZ</a></p>
<!-- /wp:paragraph -->
<!-- wp:site-title {"level":0} /-->
</div>
<!-- /wp:group -->
<!-- wp:navigation {"overlayMenu":"mobile","layout":{"type":"flex","justifyContent":"right"}} -->
<!-- wp:navigation-link {"label":"Home","url":"/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"The Pack","url":"/pack/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"About","url":"/about/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Book a free call","url":"/book/","kind":"custom","className":"bfo-nav-cta"} /-->
<!-- /wp:navigation -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
''')

open(f"{T}/parts/footer.html", "w").write('''<!-- wp:group {"align":"full","backgroundColor":"surface","style":{"spacing":{"padding":{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|40"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-surface-background-color has-background" style="padding-top:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--40)">
<!-- wp:columns {"align":"wide"} -->
<div class="wp-block-columns alignwide">
<!-- wp:column {"width":"60%"} -->
<div class="wp-block-column" style="flex-basis:60%">
<!-- wp:group {"className":"bfo-brand","layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-group bfo-brand">
<!-- wp:paragraph {"className":"bfo-logo"} -->
<p class="bfo-logo">OZ</p>
<!-- /wp:paragraph -->
<!-- wp:site-title {"level":0} /-->
</div>
<!-- /wp:group -->
<!-- wp:paragraph {"textColor":"muted"} -->
<p class="has-muted-color has-text-color">Practical, one-to-one guidance for Brits building a life in Australia.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
<!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%">
<!-- wp:heading {"level":3,"className":"bfo-eyebrow"} -->
<h3 class="wp-block-heading bfo-eyebrow">Explore</h3>
<!-- /wp:heading -->
<!-- wp:navigation {"overlayMenu":"never","layout":{"type":"flex","orientation":"vertical"}} -->
<!-- wp:navigation-link {"label":"Home","url":"/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"The Pack","url":"/pack/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Checkout","url":"/checkout/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"About","url":"/about/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Book a free call","url":"/book/","kind":"custom"} /-->
<!-- /wp:navigation -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
<!-- wp:paragraph {"align":"left","className":"bfo-legal alignwide","textColor":"muted","fontSize":"small"} -->
<p class="has-text-align-left bfo-legal alignwide has-muted-color has-text-color has-small-font-size">© 2026 Bound for Oz. General guidance only, not financial, legal or immigration advice.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
''')

# ---------- home ----------
home = [
 hero("For Brits moving to Australia", "Moving to Australia? Skip the guesswork.",
      "Real-world advice on tax, banking, work, housing and settling in, from someone who’s been through the whole move. Start with a free consultation call, no strings attached.",
      [("Book a free consultation", "/book/", False), ("See what’s in the Pack", "/pack/", True)]),
 section(grid([card("Book a free call", "Tell me where you’re up to, visa, timeline, city ideas. No charge, no pressure.", "01"),
               card("Get your plan", "We map the practical steps: money, work, housing and the admin most people miss.", "02"),
               card("Land prepared", "Take the Settle-In Pack with you, and check back in whenever you hit a wall.", "03")]), pad="40"),
 section("\n".join([h("Everything the move actually involves", 2, "center"),
   p("Most guides cover visas. Almost none cover what happens the week after you land. That’s the gap we close together.", color="muted", align="center", cls="bfo-lede"),
   grid([card("Tax &amp; finances", "Registering with the ATO, tax file numbers, double taxation with HMRC, and getting your money organised before you land."),
         card("Banking &amp; super", "Opening an Australian bank account from the UK, understanding superannuation, and moving your pension the smart way."),
         card("Finding work", "How the Australian job market really works, writing a local CV, recruiters worth contacting, and interview culture."),
         card("Where to live", "City vs suburbs vs coastal towns, realistic rents, rental applications without local history, and choosing the right state."),
         card("Healthcare &amp; Medicare", "Enrolling in Medicare, private health cover, reciprocal agreements, and what to sort before you fly."),
         card("Making friends", "Meeting people as a newcomer, clubs and communities that actually welcome Brits, and beating the six-month wobble.")])]), bg="surface"),
 section('''<!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center">
<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center">
<!-- wp:image {"sizeSlug":"full","className":"bfo-photo"} -->
<figure class="wp-block-image size-full bfo-photo"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/pack-placeholder.svg' ) ); ?>" alt="Sunny beachside suburb in Australia with cafés and palm trees"/></figure>
<!-- /wp:image -->
</div>
<!-- /wp:column -->
<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center">
''' + "\n".join([p("The Settle-In Pack", cls="bfo-eyebrow"), h("A complete, practical playbook, in one download"),
  p("Checklists, step-by-step guides and honest tips for tax, banking, work, housing and daily life. Everything we’d cover on a call, written down so you can work through it at your own pace.", color="muted"),
  ticks(["Set-up checklists for your first 30 days", "Bank, super and tax guides written for Brits", "City and suburb comparison cheat sheets"]),
  buttons([("Explore the Pack", "/pack/", False)])]) + '''
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->'''),
 cta("Not sure where to start? Start with a conversation.", "Book a free 30-minute call and we’ll figure out exactly what you need to sort, and in what order.", "Book your free call", "/book/"),
]
pattern("home", "Home", "\n\n".join(home))

# ---------- pack ----------
SECTIONS = [
 ("Your first stay", "Short-term accommodation for your arrival"),
 ("Finding a longer-term home", "Share houses, rooms and rental properties"),
 ("Setting up a mobile number", "SIMs, eSIMs and getting connected"),
 ("Setting up a bank account", "Applications, identity checks and card access"),
 ("Setting up Medicare", "UK eligibility, documents and online enrolment"),
 ("Setting up a tax file number", "The TFN application and correspondence"),
 ("Making friends", "Local groups and building a social life"),
 ("Finding work", "Working holiday restrictions and staying longer"),
 ("Travel insurance and longer-term cover", "Initial cover, extended trips and health insurance"),
 ("Documents to bring and keep", "Before departure and as you settle in"),
]
acc = []
for t, s in SECTIONS:
    acc.append(f'''<!-- wp:details {{"className":"bfo-step"}} -->
<details class="wp-block-details bfo-step"><summary><strong>{e(t)}</strong><em>{e(s)}</em></summary><!-- wp:paragraph {{"textColor":"muted"}} -->
<p class="has-muted-color has-text-color">Step-by-step guide + checklist in the pack.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->''')
pack_contents = "\n".join([
  h("What’s inside", 2, "center"),
  p("No fluff, no recycled blog posts. Each section is the actual step-by-step process, with the details that only matter once you’re doing it.", color="muted", align="center", cls="bfo-lede"),
  group("\n".join(acc), cls="bfo-steps"),
  p("✓ Every section comes with its own checklist, so you always know what’s done and what’s next.", cls="bfo-callout"),
  p("Personal methods and detailed instructions are still being developed. Use the linked official guidance for current requirements.", color="muted", size="small", cls="bfo-footnote"),
])
pattern("pack-contents", "Pack contents (10 sections)", section(pack_contents, bg="surface"))

pack = [
 hero("The Settle-In Pack", "Everything you need to move well, in one download",
      "Ten practical sections covering money, work, housing and life in Australia, written specifically for people moving from the UK. Work through it before you fly, or keep it on hand for your first months.",
      [("Get it free (first 50 people)", "/free/", False), ("Buy the Pack for £49", "/checkout/", True)],
      "Our first 50 readers get the Pack free, in exchange for an honest post about it on their social channels."),
 '<!-- wp:pattern {"slug":"aus/pack-contents"} /-->',
 section('''<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide">
<!-- wp:column -->
<div class="wp-block-column">
''' + h("Who it’s for") + "\n" + ticks(["You have your visa (or nearly) and a move date in mind", "You’re researching before committing to the move", "You’ve just landed and feel like you’re playing catch-up"]) + '''
</div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column">
''' + group("\n".join([
   group(h("The Settle-In Pack", 3) + "\n" + p("£49", cls="bfo-price"), layout='{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap"}'),
   p("One payment. Lifetime access, including all future updates.", color="muted"),
   ticks(["10 practical sections &amp; checklists", "Cost of living calculator", "Free updates as rules change"]),
   buttons([("Claim it free (first 50)", "/free/", False), ("Buy the Pack for £49", "/checkout/", True)]),
   p('Prefer to talk it through first? <a href="/book/">Your free call</a> is credited against the Pack.', color="muted", size="small")]), cls="is-style-card bfo-price-card") + '''
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->'''),
]
pattern("pack", "The Pack page", "\n\n".join(pack))

def stub(slug, title, eyebrow, lede, extra=""):
    pattern(slug, title, hero(eyebrow, title, lede) + ("\n\n" + section(extra, pad="40") if extra else ""))

def photo(alt):
    return f'''<!-- wp:image {{"sizeSlug":"full","className":"bfo-photo"}} -->
<figure class="wp-block-image size-full bfo-photo"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/pack-placeholder.svg' ) ); ?>" alt="{alt}"/></figure>
<!-- /wp:image -->'''

about = [
 section("\n".join([p("About", cls="bfo-eyebrow"), h("Advice from someone who’s actually done the move", 1),
   p("I’m a Brit who made the move to Australia, and like most people, I found that the hard part wasn’t the visa. It was everything after: the tax file number, the bank that wouldn’t take my UK proof of address, the rental applications rejected for having no local history, the superannuation statements that might as well have been in code.", size="large"),
   p("Bound for Oz exists to close that gap. Not generic blog advice, specific, practical guidance on what to do, in what order, and what things really cost, for people moving from the UK specifically.", color="muted"),
   photo("Beachside café life on the Australian coast")]), size="760px"),
 section("\n".join([h("What I believe", 2, "center"),
   grid([card("Practical over inspirational", "“Follow your dream” doesn’t open a bank account. Every session ends with concrete next steps, real numbers and real names."),
         card("Honest, not salesy", "If Australia isn’t right for your situation, I’ll say so. The free call is genuinely free, no strings, no hard sell."),
         card("Built for Brits", "Pensions, HMRC, NHS records, UK credit history, the questions only someone from the UK knows to ask.")])]), bg="surface"),
 cta("Let’s talk about your move", "Thirty minutes, free, and you’ll leave with a clear plan.", "Book your free call", "/book/"),
]
pattern("about", "About", "\n\n".join(about))
stub("book", "Book a free call", "Free 30-minute call", "Tell me where you’re up to, visa, timeline, city ideas. No charge, no pressure.",
     p("[BOOKING LINK NEEDED — Calendly / Cal.com embed goes here]", cls="bfo-callout", align="center"))
stub("checkout", "Checkout", "The Settle-In Pack · £49", "[COPY NEEDED — payment provider not chosen yet]")
stub("free", "Get the Pack free", "First 50 people", "Our first 50 readers get the Pack free, in exchange for an honest post about it on their social channels.",
     p("[FORM NEEDED — sign-up form for the free 50]", cls="bfo-callout", align="center"))
print("generated")
