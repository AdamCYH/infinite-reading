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

## Handing the scenes to an image agent

Give it a handoff file: the brief plus one prompt per scene, and nothing else.

- `HANDOFF.md` — every published scene, for regenerating any of them.
- `HANDOFF-TEST.md` — the five-scene test that settled the style of the first hundred.
- `HANDOFF-WAVE-N.md` — built when a new wave is staged, from `staged/wave-N.json`. Send a handful
  of its hardest scenes first (`--only`) and look at what comes back before sending the rest.

They are generated, so edit `IMAGE-AGENT-BRIEF.md` or `PROMPTS.md` and rebuild rather than editing
them directly:

    ./build-handoff.py                  # HANDOFF.md, from the ids in manifest.json
    ./build-handoff.py --wave 4         # HANDOFF-WAVE-4.md, from the ids in staged/wave-4.json
    ./build-handoff.py --wave 4 --only <id>,<id> --out HANDOFF-WAVE-4-TEST.md

`PROMPTS.md` keeps the project history — why the style changed, what previous batches got wrong.
That is for us, not for the agent, and sending it just costs tokens.

## Adding a scene

Scenes are written and checked before any art exists, wait in `staged/`, and go live with their
art.

1. **Write the prompt and the text together.** Start from `CATALOG-MAP.md`, which shows the holes.
   The prompt goes in `PROMPTS.md`. The entry — `id`, `name`, `world`, `kind`, `description`,
   `keywords`, `cues`, `examples` — goes in a wave file in `staged/`, with `world` and `kind` taken
   from `taxonomy.json`. The person who decides what is in the picture is the only one who knows
   what a page set there would say, and those fields are what make the scene findable. See the
   sections below.
2. **Check it before making art.** Add at least one passage a page set there would contain to
   `tools/embedder-bench/queries_coverage.json`, with the new id as its `proposed` scene, then:

       cd tools/embedder-bench && . venv/bin/activate
       python catalog_coverage.py --gate ../../catalog/staged/wave-1.json

   A scene passes when it finds its own passages (third place at worst, and still from each of
   its examples with that example held out), sits no closer than 0.77 to any other scene, meets
   the rules `CatalogManifestContentTest` enforces, and pushes no existing scene out of a passage
   it used to find. Rewriting the examples fixes most failures: name the place and the things in
   it plainly, with the nouns of its world.
3. **Generate the art** from the wave's handoff file (above), named `<id>.png`.
4. **Review the art, then merge the scenes that have it:** `./merge-staged.py 1
   <folder-of-generated-images>`. It moves only those scenes into `manifest.json`, with `imageUrl`
   set, leaves the rest staged, and rebuilds `CATALOG-MAP.md`. Image agents do not always follow
   the filename rule, so rename any file named from its prompt to `<id>.<ext>` first.
5. **Run `./prepare-images.py <folder-of-generated-images>`** — re-encodes to WebP q82 at 1600px
   short edge, writes `scenes/<id>.webp`, measures each scene's overlay into the manifest, and
   cross-checks every filename against `manifest.json`. It exits non-zero on a mismatch, which is
   the common mistake. Run it after the merge: it records measurements only for scenes already in
   the manifest.
6. Bump `version` and push to `main`.
7. **Purge the CDN**, or readers keep the old catalog for up to twelve hours:

       curl https://purge.jsdelivr.net/gh/AdamCYH/infinite-reading@main/catalog/manifest.json

   jsDelivr caches a branch at the edge for twelve hours (`s-maxage=43200`), and different edges
   expire independently, so "I can see the new file" does not mean a phone can. The app refuses a
   mirror that offers an older `version` than it already holds, so a stale edge can no longer undo
   a publish - but until the purge lands, a reader who has never fetched the new one still gets
   the old.

A scene with a good image and no naming words is close to invisible: it can only be reached by
the slow route, and only when several pages happen to agree on it.

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
- **blur** — the app blurs at 2.5dp itself, and blurring twice only destroys detail.

It does measure one thing. Scenes sit blurred under a dark overlay behind body text, and a bright
sky can leave that text below WCAG AA. Each scene is simulated exactly as the reader sees it —
centre-cropped to a phone (a worst case, since that aspect keeps the least of the frame), upscaled,
blurred 7.5px, overlaid — and the minimum overlay opacity that keeps the brightest 5% of the frame
at 4.5:1 is written into the manifest as `overlayAlpha`. Four of the first ten needed a nudge
(0.66–0.72); the rest use the default.

That value is **data, not baked pixels**: the art keeps its full brightness, and if the text colour
or the default overlay ever changes, re-run this instead of re-exporting art.

Keep the full-resolution originals outside this directory — they are the masters for any future
re-crop or re-encode, and they should not ship.

Because the masters live outside the repo, re-measuring after a change to `SCENE_BLUR_RADIUS`, the
text colour or the overlay colour uses `--measure-only`, which reads the published art in
`scenes/`, writes no image, and updates `overlayAlpha` alone:

    ./prepare-images.py --measure-only

See `PROMPTS.md` for how the shipped scenes were generated and what makes an image work behind
blurred text.

## Schema 2: render profiles

A measured number is only valid for the maths that reads it. `overlayAlpha` named a *mechanism*,
so when the reader's scrim changed from a lerp toward grey to a multiply toward black, the same
key silently meant something else — and 99 of 100 scenes fell under WCAG AA for everyone on the
older build. The schema exists to make that impossible.

A **profile id** names the whole contract: the scrim maths *and* the constants it was measured
against. Scenes carry one block per profile; a client pins one id and reads only that block.

    "profiles": {
      "scrim-multiply-1": {
        "summary":     "...",
        "calibration": { "blurDp": 2.5, "textColor": "#CFCFCF",
                         "ambientColor": "#050506", "minContrast": 4.5 },
        "defaults":    { "scrim": 0.65, "saturation": 1.0 }
      }
    },
    "scenes": [{
      "id": "...",
      "overlayAlpha": 0.63,                       // frozen mirror of scrim-lerp-1, for app 1.2
      "render": {
        "scrim-lerp-1":     { "scrim": 0.63 },
        "scrim-multiply-1": { "scrim": 0.58, "saturation": 1.2 }
      },
      "keywords": ["bedroom", "wardrobe"],        // pooled place vocabulary
      "cues":     ["bed", "pillow"],              // naming only; see below
      "examples": ["...", "..."]
    }]

The same discipline applies outside `render`. `cues` was added rather than widening `keywords`
because the two feed different measures, and a client that has never heard of `cues` keeps exactly
the vocabulary it was calibrated with. An unknown key is ignored; a key that quietly changes
meaning is the bug this schema exists to prevent.

The rules, in order of how much they matter:

1. **A profile's `calibration` is immutable once published.** Change the blur radius, the ambient
   floor, the text colour or the maths, and that is a **new profile id** — the old numbers are no
   longer valid for it, and clients in the field cannot be told otherwise. `prepare-images.py`
   refuses to publish a change to a shipped profile's calibration and tells you to add one.
2. **A client reads only its own profile**, and falls back to `profiles.<id>.defaults` and then to
   its own constants. Never to another profile's numbers — that is the original bug.
3. **Every profile is measured in one pass**, so projections cannot drift apart. This is the real
   enforcement; the rules above are what it enforces.
4. **A frozen profile keeps its published value** whenever that value still clears contrast, so a
   re-run cannot churn numbers already in users' hands over rounding noise.
5. **Additive only.** Never remove a key, a scene id, or a profile. Old parsers ignore keys they
   do not know, so adding is always safe.

The app pins its id in `SCENE_RENDER_PROFILE` (SceneGrade.kt), next to the maths it describes.
`CatalogManifestContentTest` guards the contract: every scene has every profile, the frozen mirror
still matches its profile, each profile stays inside its band, and the parser takes its own block
and ignores the others.

One file therefore serves every app version, and content — 99% of the bytes — is written once.

## `keywords` and `cues`: two lists, because there are two jobs

Words attached to a scene do two different things in the app, and a word can be right for one and
wrong for the other. That is why there are two fields.

**Naming one scene** is what both lists do. When a page's text contains one of them, and the
encoder has already ranked that scene in its top ten, the scene is lifted and the page counts as
*naming* it. A named scene becomes the background **on that page**, skipping the cooldown. This is
the fastest and most reliable route in the system, and it is why a page that says "walking into
the kitchen" shows a kitchen instead of waiting three pages for the slow route to agree.

**Deciding whether a page describes anywhere at all** is what `keywords` alone does. Every scene's
keywords are pooled into one vocabulary, and the share of a page's words drawn from it is half of
the place signal, which weights how much that page counts towards the running evidence.

The difference matters because the second job has no guard. Naming only ever applies to a scene
the matcher already likes, so `bed` is safe and correct for Bedroom, Morning. The same word in the
pooled vocabulary fires on a page about an illness, which depicts nowhere. Measured on the
labelled corpus: pooling the naming words drops separation from **0.877 to 0.824**, which is worse
than having no catalog vocabulary at all.

So:

| field | goes in the pooled place vocabulary | put here |
| --- | --- | --- |
| `keywords` | yes | words that name a **place or part of one**: `bedroom`, `wardrobe`, `aisle`, `ghat`, `izakaya` |
| `cues` | no | everything else a page set here would say: **people** (`judge`, `barista`), **things** (`bed`, `suitcase`, `kettle`), **actions** (`boarding`, `verdict`) |

A word belongs in exactly one of the two; a test fails if it appears in both.

### What to write

Ask: **what nouns would appear on a page set here?** Then sort them by the table above. Eight to
twelve across both lists is typical; more is not better.

For Bedroom, Morning: `keywords` are `bedroom`, `wardrobe`, `curtain`; `cues` are `bed`,
`blanket`, `duvet`, `mattress`, `pillow`, `sheet`.

- **Name the place, not the mood.** `cathedral`, `motel`, `ghat`, `izakaya` are evidence.
  `melancholy`, `vast`, `golden` are not, and adding them costs separation - measured.
- **The scene's name is vocabulary too.** "Supermarket Aisle" contributes `supermarket` and
  `aisle` without being listed. A scene called "Somewhere Quiet" contributes nothing.
- **Sharing a word with another scene is fine.** `courtyard` is on eight scenes. The encoder
  decides which is in play; the word only breaks the tie.
- **Plurals are handled**, including `birches`, `paddies` and `shelves`. Write the singular.

The check that catches a weak list: **each of the scene's two `examples` should contain at least
one of its keywords or cues.** A passage written to be typical of the scene that names none of
them means a real page will not either. `CatalogManifestContentTest` enforces this.

`prepare-images.py` seeds `keywords` for any scene that has none, from its name and the place
nouns already in its description, and **never overwrites an existing list** - delete the key to
have it reseeded. It never writes `cues` or `examples` at all. A seeded list is a starting point
and usually wants the furniture moved into `cues` by hand.

## Example passages are how a page finds a scene

A page of a novel is prose: *she rinsed the rice and set the pot on the ring.* A description is
not: *A clean contemporary kitchen in early light. Modern, domestic. Suits…* An encoder scores
register as much as content, so the page and the description sit further apart than they should.

Each scene therefore carries two `examples` — short passages written as a page set there would
read — and a page is matched against those alongside the description (mean of the best two
views). A cooking page finds the kitchen through *rinsed the rice and set the pot*, not through
*clean contemporary kitchen*.

Writing them:

- **Action and perception, in the third person, no names.** *He slid into a booth by the window.
  Outside, trucks went by on the road and the sign buzzed.*
- **Put the reader in it**, do not describe it from outside. The description already does that.
- **Concrete nouns the scene owns**: booth, sign, trucks. Not mood words.
- **One or two sentences, 15–35 words.** Longer drifts into a description again.
- **Exactly two per scene.** The matcher pools the best two views, and uneven counts bias it.

These are not seeded. `prepare-images.py` leaves `examples` alone entirely; there is no sensible
way to generate a novel's prose from a catalogue entry.

## Worlds and kinds

Every scene carries two tags. **`world`** is the time and culture a book lives in: imperial China,
modern East Asia, the classical Mediterranean. **`kind`** is what the reader sees: a home, a
street, somewhere to eat, a hall of power. Both vocabularies live in `taxonomy.json`, which also
tags the 14 scenes bundled with the app, since those are not in the manifest.

`CATALOG-MAP.md` lays every scene out as a grid of worlds by kinds. A hole is a kind of place that a
world's books visit and the catalog cannot show, which makes it the place to start when planning
new scenes. `catalog-map.py` builds it, and `merge-staged.py` runs that after every merge.

`CatalogManifestContentTest` fails on a scene without both tags, or with one `taxonomy.json` does
not define. To add a world or a kind, add it to `taxonomy.json` first. The app does not read the
tags yet; they are there for planning, and for grouping the scene picker by world when it needs it.

## Gaps worth filling

The three waves added in September 2026 filled most of what this section used to list — school,
library and bookshop, restaurant, bar and izakaya, city park, gym and stadium, airplane cabin, a
space station — and added imperial China, old Japan, the Odyssey's Greece, Rome and more cities.
Why each was chosen is in `docs/catalog-expansion-plan.md`; what is still missing, world by world,
is in `CATALOG-MAP.md`.

Also still missing: a forest at night, and a car interior at night. The bundled Beach is matched
poorly until the bundled scenes get examples and keywords (see the plan).

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
