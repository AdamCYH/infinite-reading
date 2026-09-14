# Scene generation prompts

One prompt per scene in `manifest.json`. **Save each result as `scenes/<id>.webp`** — the filename
is the only link between image and manifest entry, so getting it exactly right is all the matching
needs.

## What these images are actually for

They are **full-screen backgrounds behind body text**, rendered with an 8dp blur and a 65% dark
overlay on top. That changes what "good" means:

- **Fine detail is wasted.** Composition, tonal balance and colour carry everything. Do not chase
  sharpness or intricate texture — it disappears.
- **No people, no faces, no animals in the foreground.** Distracting behind text, and faces go
  uncanny under blur.
- **No text, signage, logos or watermarks.** Blurred lettering reads as a smudge artefact.
- **Even tonal distribution.** Avoid a single bright hotspot, especially centred — that is exactly
  where the text sits, and it will fight for attention even through the overlay. Aim for mid-to-dark
  values overall with contrast spread across the frame.
- **Depth without clutter.** A clear foreground/midground/background separation blurs beautifully;
  a busy uniform texture blurs into mush.

## Settings

- **Aspect ratio: 2:3 portrait** (e.g. 896×1344). Phones read in portrait and the image is
  centre-cropped, so a landscape source loses its edges.
- Generate large, then downscale to **640px on the short edge** and encode **WebP q82** (~70 KB).
- Keep the **style suffix identical** across all ten. Switching backgrounds mid-chapter should feel
  like a change of place, not a change of medium.

### Shared style suffix — append to every prompt

> atmospheric digital matte painting, painterly brushwork, soft diffused light, muted
> desaturated palette, cinematic depth of field, clear foreground midground and background
> separation, no people, no text, no watermark, no logo, no borders

Painterly rather than photoreal is deliberate: blurred photographs tend to read as *out-of-focus
photos* (i.e. a mistake), whereas a painting blurs into pleasing fields of colour.

### Shared negative prompt

> people, human figures, faces, hands, text, letters, signage, watermark, logo, signature, frame,
> border, harsh centred highlight, blown-out highlights, high-frequency noise, busy clutter,
> lens flare, tilt-shift, fisheye

---

## The ten scenes

### 1. `rain-window-city-night`

> Rain streaming down a dark window pane at night, seen from inside a quiet room. Beyond the glass,
> a city dissolved into soft smears of neon — cold blue and sodium amber — with indistinct tower
> blocks receding into haze. Sharp water droplets and rivulets on the glass in the near field,
> everything past it unresolved. Deep blue-black palette with restrained warm accents. Visual
> weight in the lower third and edges; the upper middle stays dim and open.

### 2. `desert-dunes-noon`

> Vast wind-sculpted sand dunes under a high pale sky at midday, the horizon flattened by heat
> haze. Long sinuous crest lines dividing light and shadow across the frame, wind-feathered sand at
> the ridges. Bleached ochre, bone and faint rose; sky washed almost white at the horizon and
> deepening above. Emptiness, no structures, no vegetation, no tracks. Tonal interest in the dune
> ridges rather than the sky.

### 3. `storm-at-sea`

> A heaving open ocean under a bruised storm sky, seen low near the waterline. Steep grey-green
> swells with spray torn off the crests, foam streaking down the wave faces, curtains of rain in
> the middle distance. Slate, iron-green and dirty white; a single weak break of pale light low on
> the horizon. No vessel, no land. Violent motion conveyed through wave shape, not detail.

### 4. `candlelit-study`

> A cramped wood-panelled study at night, lit by a few candles. Stacked papers, ledgers and leather
> book spines on a heavy desk, brass instruments half in shadow, shutters closed against the dark.
> Warm amber pooling close around the candles, falling off fast into deep brown and near-black at
> the edges. Intimate and enclosed. The light pool sits off-centre and low so the upper frame stays
> dark and calm.

### 5. `snowbound-village`

> A small stone-and-timber village buried in deep snow at blue hour, seen from a slope above.
> Windows glowing faint gold, woodsmoke rising straight in still air, drifts softening every roof
> and wall, a single set of tracks through the snow. Cold blue-violet snow shadows against small
> warm window lights. Silent and remote, no figures. Warm accents small and scattered, never
> dominant.

### 6. `grand-ballroom`

> A vast gilded ballroom seen from the upper edge of the room, empty of people. Crystal chandeliers
> throwing warm light across a polished parquet floor, tall mirrors and gold-leaf mouldings, heavy
> drapes at the windows. Champagne gold, ivory and deep crimson. Opulent and formal, faintly
> expectant. Chandeliers placed off-centre and upper frame; the floor mid-toned so the centre does
> not blow out.

### 7. `ruined-abbey`

> The roofless nave of a ruined gothic abbey, open to a pale overcast sky. Broken stone arches and
> empty tracery windows, ivy climbing the columns, rubble and long grass underfoot, weak shafts of
> diffuse light. Cold grey stone, moss green, washed-out sky. Ancient, hollow, melancholy. Vertical
> rhythm of the arches carrying the composition; no single bright focal point.

### 8. `steam-train-carriage`

> The interior of an early-twentieth-century railway carriage in motion, empty. Worn button-backed
> upholstery, brass luggage rails and fittings, a large window with countryside streaking past in
> horizontal motion blur. Warm interior browns and brass against cool daylight from the window.
> Enclosed and rhythmic, a sense of transit. Window placed to one side so its brightness is not
> centred.

### 9. `battlefield-dawn`

> A wide open field under low grey dawn light before a battle. Drifting smoke and ground mist, the
> distant silhouette of massed spears and banners reduced to a dark textured band on the horizon,
> churned earth in the foreground. Desaturated umber, ash grey, dull steel; a thin cold band of
> light at the horizon. Grim and monumental, no identifiable figures, no gore. Tonal weight low in
> the frame.

### 10. `tropical-harbour`

> A colonial-era tropical harbour in bright mid-morning heat, seen from the quayside. Wooden
> sailing ships at anchor on flat turquoise water, stacked crates and barrels along the stone quay,
> palms and low whitewashed buildings behind, rigging against a hazy sky. Sun-bleached white,
> turquoise, warm timber. Busy and mercantile but unpeopled. Haze lifting the distance; foreground
> quay slightly shaded to keep the middle from glaring.

---

## When the images are ready

Drop them in `scenes/` named exactly by id, then:

    catalog/
      manifest.json
      scenes/
        rain-window-city-night.webp
        desert-dunes-noon.webp
        ...

`CatalogManifestContentTest` validates the manifest on every build; a mismatch between an id and a
filename will show up as a scene that never loads, and the app falls back to a bundled scene
rather than showing nothing.

## If you add more scenes later

The description in `manifest.json` — not the prompt — is what gets matched against the book text.
They serve different jobs: the **prompt** is visual vocabulary for the image model, the
**description** is novel vocabulary for the embedder. Write the description the way the book would
describe the place, and see `README.md` for why near-duplicate descriptions actively hurt.
