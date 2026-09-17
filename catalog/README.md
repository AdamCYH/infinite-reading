# Environment catalog

Static content for the app's online scene catalog. **No backend** — the app fetches
`manifest.json` and the images directly over HTTPS.

Published from https://github.com/AdamCYH/infinite-reading under `catalog/`, alongside the privacy
policy. Publishing is just pushing to `main`:

    https://cdn.jsdelivr.net/gh/AdamCYH/infinite-reading@main/catalog/manifest.json
    https://adamcyh.github.io/infinite-reading/catalog/manifest.json
    https://raw.githubusercontent.com/AdamCYH/infinite-reading/main/catalog/manifest.json

The repo was previously named `immersialabs.github.io`. That name still resolves through GitHub's
rename redirect, but do not rely on it — the redirect dies as soon as anyone creates a repo under
the old name. Use the canonical name everywhere.

jsDelivr is primary because it is purpose-built as a public CDN for open-source assets. GitHub
Pages is second and propagates within about a minute of a push, so it is the one to hit when
checking a catalog you have just published; jsDelivr can be up to 12 hours behind.

Mirrors are tried in order and the first that answers wins; see `CatalogMirrors`.

Both point at `main` on purpose. Pinning a tag would mean every new catalog needed an app update
to point at the new tag, which defeats the point of a remote catalog. jsDelivr caches branch refs
for roughly 12 hours, so a push goes live within that; `raw.githubusercontent` is uncached, which
makes it the fast path when checking a manifest you just pushed.

## Adding a scene

1. Generate the art (see `PROMPTS.md`) at full resolution, named `<id>.<jpg|png>`.
2. Run `./prepare-images.py <folder-of-generated-images>` — re-encodes to WebP q82 at 1600px short
   edge, writes `scenes/<id>.webp`, and cross-checks every filename against `manifest.json`.
   It exits non-zero on a mismatch, which is the common mistake.
3. Add an entry to `manifest.json` with a matching `id` and `imageUrl`.
4. Bump `version` and push to `main`.

**Push the images and the manifest together.** A scene listed in `manifest.json` is eligible for
selection the moment the app fetches it, regardless of whether its `imageUrl` resolves. Publishing
a manifest entry ahead of its artwork therefore does not mean "the scene is unavailable" — it means
the matcher can pick that scene and then fall back to a bundled image, so the background stops
following the text. The manifest is the thing that goes live last.

**Do not rename a `.jpg` to `.webp`.** The bytes stay JPEG; Android sniffs content so it would
still decode, but the whole size benefit is lost and the served `Content-Type` would be wrong.
`prepare-images.py` does a real re-encode.

### Unused alternates

The image generator retried on failure, so 17 of the 60 scenes have a second master sitting in
`image-masters/` (gitignored, local only). One was picked per scene by eye; the other is still
there. A scene is matched on its `description`, never on its picture, so a scene can carry several
images without affecting selection at all — that would be a variety win rather than a correctness
risk, unlike near-duplicate descriptions. Nothing in the app reads more than one image per scene
today; `imageUrl` would need to grow an `imageUrls` sibling first.

Scenes with a spare master:

- `aurora-over-tundra`
- `cathedral-nave`
- `city-rooftops-dusk`
- `country-churchyard-mist`
- `empty-theatre-stalls`
- `farmhouse-kitchen-hearth`
- `highland-moor-fog`
- `limestone-cavern-pool`
- `mangrove-swamp-dusk`
- `metro-platform-late`
- `monastery-cloister`
- `olive-grove-terraces`
- `salt-flat-mirror`
- `tenement-courtyard`
- `textile-mill-floor`
- `victorian-laboratory`
- `wizards-workroom`

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
