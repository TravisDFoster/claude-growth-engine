# LinkedIn Writing Guide

> Voice and structure rules for LinkedIn posts. Per-post-type skeletons live in [`templates/`](templates/).

## Voice

Cerkl voice — matches the blog. Apply the [`seo-blog-editing` references](/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/skills/seo-blog-editing/references/) verbatim:

- No em-dashes
- No "actually," "really," "just," "genuinely," "simply"
- No "it's not X, it's Y" or "Not X. Y." binary contrasts
- No LLM filler ("at its core," "when it comes to," "in the world of")
- Direct, plain, zero-fluff
- Date format `YYYY-MM-DD`

**Open question:** Whether LinkedIn voice should diverge from blog voice (shorter sentences, more hook energy, more line breaks). For now they are identical.

## Universal structure

Every LinkedIn post has two pieces:

1. **Caption** — the text above the asset / poll / link card
2. **Asset or asset spec** — for carousels, statics, videos, this is the visual; for polls, it's the question + options; for link posts, it's the link card LinkedIn auto-renders

## Caption length rules

Brevity first. These are social posts, not articles. Lead with the hook, cut every line that does not earn its place, and stop once the point lands. When in doubt, make it shorter.

- **Asset-heavy posts (carousel, short video):** caption is very short. A tight hook and an optional 1-line setup. The visual carries the content.
- **Light-asset posts (static-theme, static-blog, poll):** the caption carries the argument, but keep it tight. Aim for 3–5 short paragraphs, never a wall of text. Use line breaks for scannability.

No fixed character cap, but the default instinct is to trim. A reader should get the whole point in one scroll.

## Hashtag policy

Skip hashtags. They clutter the caption without earning meaningful reach for our audience, so leave them out entirely. If a specific campaign ever calls for one, that is a deliberate exception the writer flags, not a default.

## Link policy

Put everything the reader needs in the caption, including the registration or destination link. Do not push links to the first comment. A reader should never have to hunt for the next step, and a post that makes them dig loses more than it gains. LinkedIn may show slightly less reach on an in-body link; that tradeoff is worth a frictionless path to the CTA.

## Per-post-type table

| Type | Asset weight | Caption length | Template |
|---|---|---|---|
| Carousel | Heavy (8–12 slides) | Very short (2–4 lines) | [`templates/carousel.md`](templates/carousel.md) |
| Static — theme | Light (1 graphic) | Tight (3–5 short paragraphs) | [`templates/static-theme.md`](templates/static-theme.md) |
| Static — blog link | Light (link card) | Tight (2–4 short paragraphs) | [`templates/static-blog.md`](templates/static-blog.md) |
| Poll | Light (poll widget) | Tight (3–4 short paragraphs) | [`templates/poll.md`](templates/poll.md) |
| Short video | Heavy (video) | Very short (2–3 lines) | [`templates/short-video.md`](templates/short-video.md) |

## Banned moves (from blog editing, carried over)

- Em-dashes (use periods or parentheses)
- Banned adverbs: "actually," "really," "just," "genuinely," "simply"
- Binary contrasts: "It's not X, it's Y" / "Not X. Y."
- Filler openers: "At its core," "when it comes to," "in the world of"
- Engagement-bait: "comment YES if you...", "tag someone who..."
- Lowercase-i-am-a-thought-leader voice
