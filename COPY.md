# Bound for Oz: copy review sheet

The Home and About text and all of the Pack text (except the 10 sections) are the approved Lovable copy, **word for word**. This sheet lists only what differs from it and what's still missing, so one read-through covers everything.

Where copy lives: `theme/aus/patterns/*.php`. Once it's on WordPress, Jordan can edit any text directly in WP Admin → Pages.

## Changed from Lovable (please confirm)

| Page | Lovable | Now | Why |
|---|---|---|---|
| Pack | "What's inside" = 8 numbered guides | The **10 sections** from Jordan's screenshot, as expandable rows | Jordan's brief |
| Pack | Each row expands to… | "Step-by-step guide + checklist in the pack." | Shows the scope, keeps the method behind the paywall |
| Pack | — | Added: "✓ Every section comes with its own checklist, so you always know what's done and what's next." | Jordan wanted the checklist called out |
| Pack | — | Added the footnote from Jordan's screenshot: "Personal methods and detailed instructions are still being developed…" | Jordan's screenshot. **Remove before selling**: buyers paying £49 shouldn't read that the content isn't finished |
| Pack hero | "**Eight** practical guides covering…" | "**Ten** practical sections covering…" | Matches the 10 sections |
| Pack intro | "Each **guide** is the actual step-by-step process…" | "Each **section** is…" | Same |
| Pack price card | "**8** practical guides & checklists" | "**10** practical sections & checklists" | Same |
| Home | — | New video section under the hero, labelled "**The move, in 45 seconds**" | New copy, approve or replace |
| Home | — | New photo strip labelled "**Postcards from the move**" | New copy, approve or replace |
| About | "Not generic blog advice **,** specific…" | "Not generic blog advice, specific…" | Stray space removed. The original was probably a dash ("advice — specific"). Pick one |

## Worth a second look

- **Cost of living calculator**: it's in the price card, but it isn't one of the 10 sections. Either add it as an 11th section or confirm it's a bonus.
- **Home, "Banking & super"**: "moving your pension the smart way". Advising on UK pension transfers is FCA-regulated. Suggest "understanding your options for your UK pension". The site disclaimer helps, but this line reads like advice.
- **Home, "Healthcare & Medicare"** vs **Pack section 05**, "UK eligibility": both rely on the UK–Australia reciprocal health agreement. That's accurate, but link the official Services Australia page inside the pack.
- **"Your free call is credited against the Pack"**: that needs a mechanism (a discount code after the call). Confirm it's real before launch.

- **Highlight film**: confirm there are rights to the music for commercial use. A copyrighted track can get the site flagged, or muted if the video is also posted on social. If anyone speaks in it, add captions.

## Missing before launch

| Page | Needed |
|---|---|
| `/book/` | Booking link (Calendly or Cal.com, both free) to embed |
| `/checkout/` | Payment provider. Options: Stripe Payment Link, Lemon Squeezy (handles UK/EU VAT) or WooCommerce |
| `/free/` | Sign-up form for the first 50, and how the post-for-pack deal is tracked |
| Photos | All site photos are **stills cut from the Aussie Aussie film** (1280 px, so slightly soft on big screens). Swap in the full-res originals from the shared album / DaVinci Resolve exports: same filenames in `theme/aus/assets/photos/`, no code changes. Frames showing strangers' faces were left out on purpose. |
| Legal | Privacy policy and terms (required once you collect emails or payments) |
