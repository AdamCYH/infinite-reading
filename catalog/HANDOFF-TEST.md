# Image brief

Background images for a reading app. Each sits full-screen behind paragraphs of light text and
is blurred and dimmed before anyone sees it. The reader looks *through* them at words — so
composition, light and colour carry everything, and fine detail is wasted.

## Style — append to every prompt

> cinematic film still, photographic realism with an elevated filmic colour grade, natural
> motivated light, rich but restrained colour, strong foreground midground and background
> separation, fine natural grain, no people, no legible text, no watermark, no logo, no borders

## Negative prompt — use with every prompt

> people, human figures, faces, hands, legible text, readable signage, kanji, hanzi, hangul,
> latin lettering, brand logos, shop names, license plates, watermark, signature, frame, border,
> harsh centred highlight, blown-out highlights, crushed blacks, HDR halos, oversharpening,
> heavy vignette, lens flare, tilt-shift, fisheye, cartoon, anime, illustration, painterly
> brushwork, visible brush strokes, 3D render, video game screenshot

Keep both identical on every image and in every batch, so a new scene sits beside the published
ones without a seam. Moving between scenes should feel like changing place, never like changing
medium.

## Photographic, but not a snapshot

Aim for **frames from a beautifully shot film**: real materials and real light, composed and graded
with intent. Reach for atmosphere and a consistent cinematographic voice across the set — style is
welcome, and better than a hundred neutral photographs.

The line is the *other* medium: no brushwork, illustration, anime, concept art or engine renders.
**If a viewer would call it artwork rather than a photograph of somewhere, it is wrong.** A
previous attempt returned competent digital paintings when asked for photographs — check every
image against this before delivering.

## Brightness — the rule most often got wrong

A dark overlay goes over every image and only ever *subtracts* light, so a scene that arrives
near-black renders as a black rectangle and the background stops having any purpose.

Aim for an **evenly lit, mid-toned** image: an overcast afternoon, or a room with the lights on.
Not dim, not sunlit.

Two rules that look opposed but are not:

- **No single bright hotspot, especially centred** — that is exactly where the text sits. Keep the
  sun off-frame.
- **Do not fix that by going dark.**

Both are satisfied the same way: **spread moderate light over large areas; never a few bright
points against darkness.** A night scene takes its light from wet road, sky glow, a lit facade,
fog, a row of windows — surfaces, not points. One lamp in blackness fails both rules at once.

Test: convert to greyscale and squint. You want a legible arrangement of light, medium and dark
shapes. One or two bright spots floating in black fails; a flat bright wash fails too.

## Also required

- **Depth.** Real separation between foreground, midground and background — it survives blurring,
  where a flat busy frame turns to mush.
- **Sharp.** Never pre-blur or soften. Softness comes from composition, not the lens.
- **No people.** No figures, faces or hands. Distant animals as small shapes are fine.
- **No legible text.** No signage, lettering, numbers, logos or readable titles. Where a scene is
  full of shopfronts, render signs as **unreadable panels of coloured light** — the glow and the
  shape, never the letters.
- **Portrait**, 2:3 preferred, 3:4 acceptable, never landscape or square. Native resolution is
  fine; do not trade composition for pixels.

## Empty, not abandoned

Many scenes are places usually full of people: a crossing, a market, a classroom, a stadium, a
restaurant. Show them at a real quiet moment — before opening, after closing, between signals —
with signs of use left behind: a cup on a table, a chair pushed back, a lamp still lit. They should
feel like somewhere people have just left, not somewhere eerie, derelict or post-apocalyptic. The
one scene meant to look abandoned is `abandoned-building`.

## Pictures inside the picture

Paintings, photographs, posters and screens inside a scene show landscapes, abstract colour or
nothing — never a face, never text. That includes television and video screens, whiteboards,
calendars, book spines, menu boards and the lids of boxes.

## Getting the period and the culture right

Image models blur neighbouring cultures and eras together. The common mistakes, and what to do
instead:

- **Imperial China.** Timber halls on stone platforms, red columns, carved brackets under deep
  upturned eaves, glazed roof tiles (yellow only for the palace), lattice doors and windows. No
  Japanese forms — no torii gates, tatami rooms or Japanese-style pagodas — and nothing Korean.
  Plaques, banners, couplets and lanterns are **blank**: a lacquered board, a plain cloth. Models
  add made-up characters to these unless told not to.
- **Old Japan.** Dark timber, lattice fronts, tiled roofs, paper screens, tatami. Noren curtains
  and lanterns are plain cloth and paper with no characters. No Chinese vermilion palace forms.
- **The Odyssey's Greece** is the Bronze Age, centuries before classical Athens. Halls are timber,
  plaster and paint: thick wooden columns painted red and wider at the top than at the foot, a
  big round hearth in the middle, painted walls, bronze weapons. Ships are long, black-hulled and
  oared, with one square sail. **Not** white marble temples, and not ruins.
- **Rome was painted.** Marble and travertine with coloured detail, bronze statues, frescoed walls,
  mosaic floors, bright awnings over the amphitheatre. Not bleached white stone.
- **Medieval Europe.** Stone, rough timber, rushes on the floor, candle and firelight. Banners and
  shields carry plain fields of colour, no lettering.
- **Recent decades.** The old wooden apartment is Japan in the 1970s and 80s; the Chinese flat is
  a block from the 1980s or 90s. Keep the details of that time: no flat-screen televisions, no
  smartphones.
- **Cities beyond East Asia and the West** — Lagos, Mexico City, Istanbul, Cairo, Marrakech. Show
  them as ordinary, lived-in and as handsome as any other city in the set, in the same colour
  grade as every other scene: **no yellow or sepia cast** for hot countries, no travel-poster
  gloss, no poverty framing.

## Filenames

Name each file exactly `<id>.png`, using the id from the list: `tokyo-backstreet-night.png`. The id
is the only link to the catalog entry, and names derived from prompt text have to be mapped back by
hand. **One image per scene** — deliver only your best attempt, not the retries.

## [FANTASTIC] scenes

Entries marked **[FANTASTIC]** show something that does not exist. Render them exactly like the
rest — as a film still — imagining a production that built the set for real, with practical
materials, practical light, real dust and smoke. Everything not marked is a real place.

A dragon's lair is the one scene where a creature may be more than a small distant shape. Keep it
mostly in shadow and half hidden by its treasure: coils and a folded wing, not a portrait.

## [PERIOD SET] scenes

Entries marked **[PERIOD SET]** are real places from the past that now survive only as ruins,
museums or reconstructions. Show each as it stood when it was in use — whole, painted and
furnished, fires lit, food on the tables, but no people — the way a well-funded period film would
build it. No ruins, scaffolding or museum ropes, no modern lamps, wires, fences or tourists. It is
still a photograph: a real set, lit and shot for real, not a painting of the past.

## Check each image before delivering

- Reads as a photograph, not as artwork?
- Any people, faces or hands — including in paintings, photographs and on screens?
- Any readable letters or logos, including on packaging, plaques, banners and in reflections?
- Right period and culture: no Japanese forms in a Chinese scene, no white-marble ruin where a
  period set was asked for, nothing modern in the past?
- A place that is usually crowded: empty at a quiet moment, not eerie?
- Greyscale and squint: layered light/medium/dark, nothing bright in the middle, not near-black,
  not a flat wash?
- Portrait, and the filename exactly the scene id?

---

# The 5 scenes

### 1. `cathedral-nave`

> The nave of a gothic cathedral, empty and still. Worn flagstones and a column base in the near ground, immense clustered piers rising into shadow, ribbed vaulting barely visible above, stained glass casting scattered coloured pools across the floor. Cool grey stone, deep shadow and small jewelled reds and blues. Columns frame both sides. Daylight through the clerestory fills the nave with a broad cool wash so the stonework and vaulting read all the way up, with the jewelled colour pools as small accents on that lit floor rather than the only light.

### 2. `torchlit-dungeon`  **[FANTASTIC]**

> A low vaulted dungeon corridor of damp rough-cut stone. Worn flags and standing puddles in the near ground, heavy iron-bound doors set along one wall, guttering torches in brackets spaced too far apart, the corridor bending away into warm gloom. Warm brown stone, rust and spreading orange torchlight. The corridor recedes in strong perspective. Torchlight spills broadly over the damp stone so whole stretches of wall and floor glow amber, the pools overlapping between brackets rather than leaving black gaps, and the full length stays readable.

### 3. `tokyo-backstreet-night`

> A narrow Tokyo backstreet after midnight, photographed at eye level. Wet asphalt holding smeared coloured reflections in the near ground, a lit vending machine and red paper lanterns outside a shuttered izakaya, tangled overhead cables, bicycles against a railing, the lane narrowing into darkness. Warm red and amber against cold blue-black night. Light comes from many sources and spreads: wet asphalt carries broad coloured reflections down the whole lane, the vending machine washes the wall beside it, and faint sky glow sits above the roofline. Every sign is an unreadable coloured glow. The street reads as lit, not as points in blackness.

### 4. `desert-dunes-noon`

> Vast wind-sculpted sand dunes under a high pale sky at midday, the horizon flattened by heat haze. Long sinuous crest lines dividing light and shadow across the frame, wind-feathered sand at the ridges. Bleached ochre, bone and faint rose; sky washed almost white at the horizon and deepening above. Emptiness, no structures, no vegetation, no tracks. Tonal interest in the dune ridges rather than the sky.

### 5. `modern-kitchen-morning`

> A contemporary kitchen photographed in soft early morning light. A stone worktop with a single mug and a folded cloth in the near ground, flat-fronted cabinets, a stainless hob and kettle, a window above the sink showing pale garden green. Cool white, pale timber and grey with one small warm accent. Light enters horizontally from the window and is diffused; surfaces stay matte with no specular glare.
