# Environment catalog

Static content for the app's online scene catalog. **No backend** — the app fetches
`manifest.json` and the images directly over HTTPS.

Lives in https://github.com/AdamCYH/infinite-reading under `catalog/`, alongside the privacy
policy. Publishing is just pushing to `main`:

    https://cdn.jsdelivr.net/gh/AdamCYH/infinite-reading@main/catalog/manifest.json
    https://raw.githubusercontent.com/AdamCYH/infinite-reading/main/catalog/manifest.json

Mirrors are tried in order and the first that answers wins; see `CatalogMirrors`.

Both point at `main` on purpose. Pinning a tag would mean every new catalog needed an app update
to point at the new tag, which defeats the point of a remote catalog. jsDelivr caches branch refs
for roughly 12 hours, so a push goes live within that; `raw.githubusercontent` is uncached, which
makes it the fast path when checking a manifest you just pushed.

## Adding a scene

1. Generate the art (see `PROMPTS.md`) at full resolution, named `<id>.<jpg|png>`.
2. Run `./prepare-images.py <folder-of-generated-images>` — re-encodes to WebP q82 at 640px short
   edge, writes `scenes/<id>.webp`, and cross-checks every filename against `manifest.json`.
   It exits non-zero on a mismatch, which is the common mistake.
3. Add an entry to `manifest.json` with a matching `id` and `imageUrl`.
4. Bump `version` and push to `main`.

**Do not rename a `.jpg` to `.webp`.** The bytes stay JPEG; Android sniffs content so it would
still decode, but the whole size benefit is lost and the served `Content-Type` would be wrong.
`prepare-images.py` does a real re-encode.

### What it does and does not touch

The **only** pixel operations are a proportional downscale to 1600px on the short edge and the
WebP re-encode. Specifically it does **not**:

- **crop** — screens vary (phones, tablets, foldables), so framing is the app's job at runtime;
- **blur** — the app blurs at 8dp itself, and blurring twice only destroys detail.

It does measure one thing. Scenes sit blurred under a dark overlay behind body text, and a bright
sky can leave that text below WCAG AA. Each scene is simulated exactly as the reader sees it —
centre-cropped to a phone (a worst case, since that aspect keeps the least of the frame), upscaled,
blurred 24px, overlaid — and the minimum overlay opacity that keeps the brightest 5% of the frame
at 4.5:1 is written into the manifest as `overlayAlpha`. Four of the first ten needed a nudge
(0.66–0.72); the rest use the default.

That value is **data, not baked pixels**: the art keeps its full brightness, and if the text colour
or the default overlay ever changes, re-run this instead of re-exporting art.

Keep the full-resolution originals outside this directory — they are the masters for any future
re-crop or re-encode, and they should not ship.

See `PROMPTS.md` for how the shipped scenes were generated and what makes an image work behind
blurred text.

## Writing descriptions

The description is the *only* thing matched against the book text, so it carries the whole
feature. Write for the embedder, not for a human browsing a gallery:

- Name the **place**, the **light/time**, and the **mood**, then list the **situations** it suits.
- Use the vocabulary a novel would use ("shipwreck", "courtship", "siege"), not photography
  vocabulary ("wide angle", "golden hour", "bokeh").
- Keep scenes **distinct from each other**. Two near-identical descriptions create a near-tie,
  and `EnvironmentSelectionPolicy`'s switch margin then suppresses *both* — a redundant catalog
  is worse than a smaller diverse one.

`embeddingModel` and per-scene `embedding` are reserved for phase 2. While `embeddingModel` is
null the app embeds descriptions on device, which is fine at this size.
