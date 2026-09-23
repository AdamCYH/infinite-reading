# Scene generation prompts

One prompt per scene — **182, all published in `manifest.json`** — in a single style. The
filename is the only link between an image and its manifest entry, so getting it exactly
right is all the matching needs. **[FANTASTIC]** marks a scene whose subject does not exist (four
published, five more in the waves). **[PERIOD SET]** marks a real place that survives only as a ruin
or a reconstruction, shown as it stood. Everything else depicts somewhere that really exists.

**Handing this to an image agent?** Give it a handoff file, not this one: `HANDOFF.md`, or
`HANDOFF-WAVE-N.md` for a staged wave, holds the brief and the prompts and nothing else, built by
`build-handoff.py`.
The brief carries the rules that matter most — the single cinematic look, sharp masters,
brightness, no people, no legible text, period and culture, and the filename convention.

The section groupings below are historical, recording when each scene was added. They mean nothing
to the app and the numbering has gaps where scenes were retired.

## Writing a new prompt? Write its keywords, cues and examples too

A prompt makes the scene *exist*. Three fields in `manifest.json` are what make it get *chosen*,
and the moment to write them is while you still have the picture in your head.

- **`keywords`** — nouns naming the **place or part of one**: `bedroom`, `wardrobe`, `aisle`.
  These are also pooled across every scene into the vocabulary that decides whether a page
  describes anywhere at all, so they must name somewhere.
- **`cues`** — everything else a page set here would say: people, things, actions. `bed`,
  `pillow`, `duvet` for a bedroom; `judge`, `verdict` for a courtroom. Not pooled, so ordinary
  words are safe and wanted here.
- **`examples`** — two short passages written as a novel would read, not as a caption. A page
  finds the scene through these more than through the description.

A page whose text contains a keyword or cue, for a scene the matcher already ranks highly,
switches the background **on that page**. Nothing else in the system is that fast or that
reliable, so a scene with thin lists is close to invisible.

The check that catches a weak list: **each example should contain at least one keyword or cue.**
If a passage you wrote to be typical of the scene names none of them, a real page will not either.

Full rules and the reasoning behind them are in `README.md`.

## What these images are actually for

They are **full-screen backgrounds behind body text**, rendered with a 2.5dp blur and a ~65% dark
overlay on top. That changes what "good" means:

- **Fine detail is wasted.** Composition, tonal balance and colour carry everything. Do not chase
  sharpness or intricate texture — it disappears.
- **No people, no faces, no animals in the foreground.** Distracting behind text, and faces go
  uncanny under blur.
- **No text, signage, logos or watermarks.** Blurred lettering reads as a smudge artefact.
- **Even tonal distribution, aimed at the middle.** Avoid a single bright hotspot, especially
  centred — that is exactly where the text sits. But do not solve that by going dark: the overlay
  only subtracts light, so a near-black scene renders as a black rectangle and showing a
  background stops having any point. Spread moderate light over large areas rather than using a
  few bright points against darkness. Measured on the blurred scene before the overlay, the
  comfortable band is **0.09-0.20 mean relative luminance**; `prepare-images.py` warns below 0.07
  and when a scene is too bright to hold text.
- **Depth without clutter.** A clear foreground/midground/background separation blurs beautifully;
  a busy uniform texture blurs into mush.

## Settings

- **Portrait, as tall as the generator offers.** The image is centre-cropped to fill the screen,
  so the taller the source the less of its width is thrown away: 2:3 loses about a third of the
  width on a typical phone, 3:4 rather more, and a landscape source loses its edges entirely.
  Both batches so far came out 3:4 (896×1200 and 3584×4800), which is fine; prefer 2:3 if you
  can get it.
- **Resolution barely matters, so do not fight for it.** `prepare-images.py` downscales to
  1600px on the short edge and never upscales, and the app blurs the result at 2.5dp behind the
  text. A 896px master is visually indistinguishable from a 3584px one by the time a reader sees
  it — measured at RMS 0.38/255 through the full render — so it just encodes smaller. Take
  whatever the generator gives.
- Encode is **WebP q82**, which lands between 16 KB and 280 KB depending on how busy the scene is.
- Keep the **style suffix identical** across every scene. Switching backgrounds mid-chapter
  should feel like a change of place, not a change of medium.

### The style suffix — append to every prompt

> cinematic film still, photographic realism with an elevated filmic colour grade, natural
> motivated light, rich but restrained colour, strong foreground midground and background
> separation, fine natural grain, no people, no legible text, no watermark, no logo, no borders

### The negative prompt — use with every prompt

> people, human figures, faces, hands, legible text, readable signage, kanji, hanzi, hangul,
> latin lettering, brand logos, shop names, license plates, watermark, signature, frame, border,
> harsh centred highlight, blown-out highlights, crushed blacks, HDR halos, oversharpening,
> heavy vignette, lens flare, tilt-shift, fisheye, cartoon, anime, illustration, painterly
> brushwork, visible brush strokes, 3D render, video game screenshot

### One look, not two

Earlier versions split the catalog into a painterly track for historical scenes and a photoreal
track for modern ones. That is gone. Every scene now uses the single suffix above.

The split was a mistake for a specific reason. Its justification was that scenes are chosen by
what the book says, so a contemporary novel would stay among photographic scenes and a Victorian
one among painted scenes, making a mid-book medium change rare. That holds only for scenes that
belong to an era. Roughly a third of this catalog is era-neutral — deserts, forests, canyons,
coasts, moors — and those can be matched by a book of any period. They were the scenes most
likely to be matched by anyone, and they were exactly where the medium would have jumped.

Almost everything here is also photographable in reality. Cathedrals, cloisters, ruined abbeys,
stone circles, ryokan, river ghats, stepwells, Mughal courtyards, heritage railway carriages and
mill museums all still exist. Only four scenes depict something that cannot be photographed, and
those are marked **[FANTASTIC]** in the list below.

### Photographic, but not a snapshot

"Photographic" here does not mean plain or literal. These should look like **frames from a
beautifully shot film**: real materials and real light, but composed, lit and graded with
intent. Reach for atmosphere — weather, haze, reflected light, a considered palette, a strong
sense of place. Make them worth looking at.

What to avoid is the *other* medium: visible brushwork, illustration, anime, concept art, or a
game-engine render. If a viewer would call it artwork rather than a photograph of somewhere, it
has gone too far. The bar is a cinematographer's frame, not a painter's canvas and not a
holiday snap.

**[FANTASTIC] scenes** are the four whose subject does not exist. Render them exactly as the
others — as a film still — imagining a production that built the set for real: practical
materials, practical light sources, real dust and smoke. A fantasy film shot on a physical set,
not an illustration of one.

### On blur and sharpness

Masters stay sharp; the app does the blurring. An earlier note here claimed painterly was needed
because blurred photographs read as out-of-focus mistakes. That is only true of *flat*
photographs — a real one always has something in focus, so an evenly soft frame signals error.
What protects an image under blur is **depth**: genuine separation between foreground, midground
and background still reads as layered tone. Every prompt earns its softness through composition,
never through the lens.

---

## Batch one — 10 scenes

#### 1. `rain-window-city-night`

> Rain streaming down a dark window pane at night, seen from inside a quiet room. Beyond the glass,
> a city dissolved into soft smears of neon — cold blue and sodium amber — with indistinct tower
> blocks receding into haze. Sharp water droplets and rivulets on the glass in the near field,
> everything past it unresolved. Deep blue-black palette with restrained warm accents. Visual
> weight in the lower third and edges; the upper middle stays dim and open.

#### 2. `desert-dunes-noon`

> Vast wind-sculpted sand dunes under a high pale sky at midday, the horizon flattened by heat
> haze. Long sinuous crest lines dividing light and shadow across the frame, wind-feathered sand at
> the ridges. Bleached ochre, bone and faint rose; sky washed almost white at the horizon and
> deepening above. Emptiness, no structures, no vegetation, no tracks. Tonal interest in the dune
> ridges rather than the sky.

#### 3. `storm-at-sea`

> A heaving open ocean under a bruised storm sky, seen low near the waterline. Steep grey-green
> swells with spray torn off the crests, foam streaking down the wave faces, curtains of rain in
> the middle distance. Slate, iron-green and dirty white; a single weak break of pale light low on
> the horizon. No vessel, no land. Violent motion conveyed through wave shape, not detail.

#### 4. `candlelit-study`

> A cramped wood-panelled study at night, lit by a few candles. Stacked papers, ledgers and leather
> book spines on a heavy desk, brass instruments half in shadow, shutters closed against the dark.
> Warm amber light spreading widely from several candles across the desk, the panelling and the ceiling beams, so the whole room reads as a place rather than a pool in darkness. Intimate and enclosed, but never black in the corners. The brightest area sits off-centre and low.

#### 5. `snowbound-village`

> A small stone-and-timber village buried in deep snow at blue hour, seen from a slope above.
> Windows glowing faint gold, woodsmoke rising straight in still air, drifts softening every roof
> and wall, a single set of tracks through the snow. Cold blue-violet snow shadows against small
> warm window lights. Silent and remote, no figures. Warm accents small and scattered, never
> dominant.

#### 6. `grand-ballroom`

> A vast gilded ballroom seen from the upper edge of the room, empty of people. Crystal chandeliers
> throwing warm light across a polished parquet floor, tall mirrors and gold-leaf mouldings, heavy
> drapes at the windows. Champagne gold, ivory and deep crimson. Opulent and formal, faintly
> expectant. Chandeliers placed off-centre and upper frame; the floor mid-toned so the centre does
> not blow out.

#### 7. `ruined-abbey`

> The roofless nave of a ruined gothic abbey, open to a pale overcast sky. Broken stone arches and
> empty tracery windows, ivy climbing the columns, rubble and long grass underfoot, weak shafts of
> diffuse light. Cold grey stone, moss green, washed-out sky. Ancient, hollow, melancholy. Vertical
> rhythm of the arches carrying the composition; no single bright focal point.

#### 8. `steam-train-carriage`

> The interior of an early-twentieth-century railway carriage in motion, empty. Worn button-backed
> upholstery, brass luggage rails and fittings, a large window with countryside streaking past in
> horizontal motion blur. Warm interior browns and brass against cool daylight from the window.
> Enclosed and rhythmic, a sense of transit. Window placed to one side so its brightness is not
> centred.

#### 9. `battlefield-dawn`  **[FANTASTIC]**

> A wide open field under low grey dawn light before a battle. Drifting smoke and ground mist, the
> distant silhouette of massed spears and banners reduced to a dark textured band on the horizon,
> churned earth in the foreground. Desaturated umber, ash grey, dull steel; a thin cold band of
> light at the horizon. Grim and monumental, no identifiable figures, no gore. Tonal weight low in
> the frame.

#### 10. `tropical-harbour`

> A colonial-era tropical harbour in bright mid-morning heat, seen from the quayside. Wooden
> sailing ships at anchor on flat turquoise water, stacked crates and barrels along the stone quay,
> palms and low whitewashed buildings behind, rigging against a hazy sky. Sun-bleached white,
> turquoise, warm timber. Busy and mercantile but unpeopled. Haze lifting the distance; foreground
> quay slightly shaded to keep the middle from glaring.

---

---

## Batch two — 45 scenes

Same settings, same style suffix, same negative prompt as the ten above. Grouped only for
reading convenience — the groups mean nothing to the app.

### Wilderness and open country

#### 11. `bamboo-grove-mist` — Bamboo Grove in Mist

> A dense grove of towering green bamboo in early morning mist, seen from a narrow earth path running between the stems. Slender vertical culms with crisp leaf detail in the near field, ranks of paler stems receding into fog behind them, moss and fallen leaves on the path. Jade, sage and cool grey-green with no warm accent. Strong vertical rhythm throughout; light filters down evenly from above rather than forming a bright patch, and the upper middle stays open and hazy.

#### 12. `autumn-birch-forest` — Autumn Birch Forest

> A stand of slender white-barked birches in late autumn, low sun raking through the trunks from one side. Crisp peeling bark in the near trunks, a deep drift of gold leaf litter underfoot, further trunks dissolving into warm haze. Cream bark, amber and ochre canopy, dull violet shadow between the trees. Vertical trunks carry the frame; the sun stays off-frame so the light is a warm wash rather than a disc.

#### 13. `mangrove-swamp-dusk` — Mangrove Swamp at Dusk

> Brackish still water threading between tangled arching mangrove roots at dusk. Wet knotted root arches with bark detail in the near field, black water holding broken reflections, dense dark foliage closing overhead and a dull orange sky glimpsed only through small gaps. Murky olive, silt brown and tarnished orange. Intricate root shapes across the midground; the water carries a broad sheen of dusk sky so the lower third reads as a large softly lit plane rather than black, and the foliage stays legibly green rather than dropping to silhouette.

#### 14. `red-rock-canyon` — Red Rock Canyon

> A deep sandstone canyon in late afternoon light, seen from partway down one wall. Layered red and ochre strata with sharp erosion detail on the near cliff, the opposite wall softened by dust haze, a thin green river far below in shadow. Rust, terracotta, dusty violet shadow and a narrow band of warm lit rock high up. Weight in the cliff faces at both sides; the sunlit band sits high, leaving the central depth open and hazy.

#### 15. `limestone-cavern-pool` — Limestone Cavern

> A vast underground limestone chamber with a still reflecting pool, lit only by indirect daylight entering from an unseen opening. Ribbed flowstone and hanging stalactites above, stalagmites rising from the near shore, the pool perfectly still and doubling the roof. Bone white, wet grey and cold blue-green. The reflection splits the frame horizontally; the light source stays out of shot so illumination is soft and directionless, with no bright spot in the centre.

#### 16. `volcanic-badlands` — Volcanic Badlands

> A blasted plain of black basalt and cracked lava crust under a heavy overcast sky. Coarse clinker texture and sulphur-yellow mineral staining in the foreground, steam venting from fissures in the middle distance, a dull red glow deep in distant cracks, bare cinder cones on the horizon. Charcoal, ash grey, acid yellow and a restrained ember red. Detail concentrated in the ground plane; the sky kept dim, flat and low in contrast.

#### 17. `aurora-over-tundra` — Aurora Over Tundra

> Curtains of green and violet aurora rippling across a black star-scattered sky above an endless flat snow plain. Faint wind-carved sastrugi catching the light in the near snow, the plain running unbroken to a low horizon, no structures or vegetation anywhere. Deep indigo, luminous green and faint magenta over blue-white snow. Light concentrated in the upper frame as soft vertical curtains; the ground dark, simple and uncluttered.


#### 19. `highland-moor-fog` — Highland Moor

> Rolling heather moorland swallowed in thick fog. Wet dark peat and clumped heather with real texture in the near ground, a fragment of collapsed drystone wall half-seen in the middle distance, everything beyond it lost, no horizon at all. Muted purple-brown, grey and dull sage. Contrast very low and evenly spread, softening steadily with distance; nothing sharp past the near ground and no light source visible.

#### 20. `jungle-waterfall-basin` — Jungle Waterfall

> A tall waterfall dropping into a jade-green pool enclosed by dense rainforest. Wet black rock and broad glossy leaves in the near field, mist and spray hanging in visible shafts of light, the falls offset to one side, canopy closing over the top of the frame. Saturated deep greens with white falling water against dark rock. The canopy frames the upper edge; the white water is kept to a narrow vertical band rather than a broad bright mass.

#### 21. `olive-grove-terraces` — Olive Grove

> Gnarled ancient olive trees with silver-green foliage on dry stone terraces above a hazy valley, hot late afternoon. Deeply furrowed trunks and loose terrace stone in the near ground, parched grass and thistle between them, the valley below flattened by heat haze. Dusty olive, straw, warm limestone and bleached blue. Terrace lines lead back diagonally; the sky is held to a small hazy strip at the top with no bright sun.


#### 23. `frozen-lake-bare-trees` — Frozen Lake

> A wide frozen lake under flat overcast light, seen from out on the ice. Pressure cracks radiating through pale ice with a thin dusting of snow in the near field, bare black winter trees crowding the far shore as a dark band, low grey cloud above. Cold grey-blue, bone white and charcoal. A strong horizontal ice plane fills the lower two thirds; the treeline is a quiet dark stripe and the sky is even and featureless.

#### 24. `stone-circle-dawn` — Standing Stones

> A ring of weathered lichen-crusted standing stones on open grassland at dawn, several of them leaning. Pitted stone surfaces and long shadows raking across cropped turf in the near ground, low mist pooling between the further stones, a wide empty sky. Grey stone, dun grass, pale gold light and blue shadow. Stones spaced across the midground with gaps between them; the sun stays off-frame so shadows do the work and the sky stays restrained.

#### 25. `cliff-path-seabirds` — Cliff Path

> A narrow grass path along the crest of high sea cliffs under broken cloud. Wind-flattened turf and crumbling cliff edge in the near ground, seabirds wheeling small against the drop, white surf far below at the base of the rock, headlands receding into haze. Grey-green turf, slate rock and cold blue-grey sea. The cliff edge cuts diagonally across the frame; the sea is kept mid-toned and even so the foam does not glare.


### Rural and coastal settlement

#### 27. `fishing-village-quay` — Northern Fishing Village

> A small northern fishing village of painted timber houses stacked above a stone quay, overcast. Wet granite quay, coiled rope, stacked lobster pots and drying nets in the near ground, small boats at moorings in grey swell, houses rising behind, bare hills beyond. Muted oxblood, ochre and white against slate water. Houses bank up one side with harbour water opposite; flat even light and no bright reflection on the water.

#### 28. `lighthouse-headland` — Lighthouse on the Headland

> A white stone lighthouse on a bare rocky headland at dusk, its beam sweeping out through rain. Wet dark rock and salt-burnt grass in the near ground, heavy sea breaking white at the base, low ragged cloud dragging behind the tower. Slate grey, cold blue and a single warm lantern glow. The tower is offset and not tall in frame; the beam angles away from the viewer and stays soft, never a hard flare.

#### 29. `wheat-field-harvest` — Wheat Field at Harvest

> A wide field of ripe wheat bending under the wind in warm late afternoon light. Individual heads and stalks sharp in the near ground, the crop smoothing into a moving gold plane further back, a small weathered timber barn on the horizon, high thin cloud above. Straw gold, dry green, warm amber and soft blue. Wheat texture fills the lower two thirds; the barn is small and off-centre and the sky stays pale and untroubled.

#### 30. `vineyard-autumn` — Vineyard in Autumn

> Rows of vines turned red and gold on a hillside after harvest, early morning. Gnarled vine stocks, wire and stony soil in the near rows, mist pooled along the valley floor below, a stone farm building half-lost in it. Burgundy, amber, olive and soft grey mist. Vine rows converge steeply into the distance; the mist band flattens the middle of the frame and the light stays diffuse with no visible sun.


#### 32. `monastery-cloister` — Monastery Cloister

> A stone cloister arcade enclosing a plain grass garth, soft daylight from the open centre. Worn flagstones and a repeating run of carved arches receding along one side, simple paired columns, a bare garth with a single well head, plain roofline above. Pale limestone, cool grey shadow and restrained green. The arch rhythm carries one side of the frame; the lit garth is even and low in contrast, and the shadowed arcade gives depth without clutter.

#### 33. `orchard-blossom-spring` — Orchard in Blossom

> An old fruit orchard in full white and pink blossom under soft overcast light. Gnarled lichened trunks and long uncut grass in the near ground, petals drifting on the wind, blossom massing overhead and dissolving into pale haze at the back of the grove. Blossom white, pale pink, fresh green and grey-lilac shadow. The canopy fills the upper frame as a soft field; no sky gap bright enough to glare, the light flat and gentle.

#### 34. `shepherds-hut-highlands` — Shepherd's Hut

> A low drystone shepherd's hut on bare upland grazing, cloud shadow moving across the slope. Coarse tussock grass and loose stone in the near ground, the hut small and half-sunk into the hillside with thin smoke pulled sideways by wind, scattered sheep, a long bare ridge beyond. Grey stone, dun and bleached green under heavy cloud shadow. Weight sits in the hillside; the hut is small and low and the broad sky stays dim.

#### 35. `country-churchyard-mist` — Country Churchyard

> A small country churchyard of leaning weathered headstones beneath dark old yews, mist settling at day's end. Lichen and worn carving on the near stones, wet grass between them, the yews heavy and almost black, the church tower a dim shape behind. Grey stone, deep green-black foliage and pale mist. Headstones scattered irregularly through the midground; the tower is softened nearly to silhouette and the failing light is even.

### Towns and cities

#### 36. `medieval-market-square` — Medieval Market Square

> A cobbled medieval market square at midday, canvas stall awnings and stacked produce beneath leaning timber-framed houses. Wet cobbles with crate and barrel detail in the near ground, a row of awnings across the middle, jettied upper storeys and a church tower closing the background. Ochre, weathered oak, canvas cream and terracotta tile. Stalls occupy the midground and the upper storeys frame the top; light falls between the roofs in broad soft bands.

#### 37. `narrow-alley-lamplight` — Narrow Alley

> A narrow alley of wet cobbles between high stone walls at night, one iron bracket lamp burning. Slick cobbles holding a broken reflection in the near ground, damp render and shuttered doorways along both walls, washing lines strung overhead, the far end lost in dark. Warm amber over damp grey-brown, the shadows staying open brown rather than black. Strong one-point perspective down the alley. The lamp sits off-centre but its light spreads widely over the wet cobbles and both walls, and a faint sky glow reaches down between the roofs, so the whole alley reads rather than one bright point in black.

#### 38. `city-rooftops-dusk` — City Rooftops

> A sea of tiled rooftops and clustered chimney pots at dusk, seen from roof level. Wet slate and lead flashing on the near roofs, thin smoke rising straight, rooflines stepping away into soot haze, a distant church spire against a fading sky. Slate blue-grey, soot brown and a narrow warm dusk band. Roof geometry fills the lower two thirds and recedes. Dusk light still sits on the wet slate so the roofs read as a broad lit field rather than a silhouette, and the sky band carries warm colour; the streets are never visible.

#### 39. `grand-railway-station` — Grand Railway Station

> A vast Victorian iron-and-glass railway train shed, steam drifting under the vaulted roof. Empty platform edge and polished rails in the near ground, cast-iron columns and riveted arched ribs rising, a large clock high on the end wall, grimy glass panels diffusing daylight above. Sooty iron, pale glass light, brass and warm brick. The vault arch frames the image; light comes from overhead heavily diffused by steam, with no window blowing out.

#### 40. `textile-mill-floor` — Textile Mill

> A long industrial mill floor lined with cast-iron looms and overhead belt shafting. Oil-stained floorboards and machine detail in the near ground, rows of looms receding, lint and dust hanging in shafts falling from high windows along one side, leather belts running up to a turning shaft. Iron grey, oiled brown, brass and pale dusty light. Machines recede in strong perspective. The high windows are numerous enough that their light, thick with lint dust, fills the whole floor in a broad hazy wash, so the looms and boards read clearly the full length of the room.

#### 41. `dockside-warehouses-fog` — Dockside Warehouses

> Tall brick dockside warehouses along a black river in heavy fog at night. Wet cobbles, mooring bollards and stacked crates on the near wharf, timber loading cranes projecting overhead, warehouse windows blank, a single lamp haloed in the murk. Brick red muted almost to grey-brown, fog white and oily black water. The warehouse wall runs down one side with the river opposite; the lamp is small and diffused and everything else is low in contrast.

#### 42. `metro-platform-late` — Late Metro Platform

> An empty modern underground metro platform late at night. Scuffed concrete and a yellow safety line in the near ground, white tiled walls, fluorescent strips running the length of the ceiling, the tunnel mouth black at the far end, a single bench. Clinical white, tile grey, cold green-tinged light and a dark tunnel void. Perspective runs down the platform; lighting is flat and even with no hot spot, and the tunnel is a quiet dark anchor.

#### 43. `covered-bazaar-lanterns` — Covered Bazaar

> A vaulted covered bazaar hung with pierced brass lanterns and patterned carpets. Open sacks of coloured spice and stacked brass ware in the near ground, carpets draped from a rail overhead, the aisle running back beneath a brick vault, dusty shafts dropping through small high openings. Saffron, crimson, indigo, brass and deep shadow. Warm lamps are many rather than one, and together they light the carpets, the spice sacks and the brickwork of the vault to a readable glow across the whole frame, with dusty daylight shafts adding broad fill from above.

#### 44. `tenement-courtyard` — Tenement Courtyard

> A narrow courtyard enclosed on all sides by tall shabby tenement blocks. Damp cracked render, a standpipe and worn paving in the near ground, washing strung on lines across the gap, rusted balconies and irregular windows rising, a small square of pale sky far above. Grey render, faded laundry colour and cool shadow. Walls rise steeply on every side; the only light comes straight down, leaving the lower frame in even shade.

#### 45. `roadside-diner-night` — Roadside Diner

> A lone chrome-and-glass roadside diner glowing at night beside an empty two-lane highway, seen from across the lot. Cracked asphalt and faded parking lines in the near ground, the diner's lit windows and a tall neon sign at middle distance, dark scrub and telephone poles receding into deep blue night behind. Deep night blue, warm interior amber and restrained neon red. The building sits low and off-centre. Its windows throw a wide pool of light across the wet asphalt of the whole lot, and the sky carries a low band of town glow, so the frame reads as a lit place rather than one bright box in blackness.

### Interiors

#### 46. `cathedral-nave` — Cathedral Nave

> The nave of a gothic cathedral, empty and still. Worn flagstones and a column base in the near ground, immense clustered piers rising into shadow, ribbed vaulting barely visible above, stained glass casting scattered coloured pools across the floor. Cool grey stone, deep shadow and small jewelled reds and blues. Columns frame both sides. Daylight through the clerestory fills the nave with a broad cool wash so the stonework and vaulting read all the way up, with the jewelled colour pools as small accents on that lit floor rather than the only light.

#### 47. `panelled-courtroom` — Courtroom

> An empty oak-panelled courtroom with still dusty air. Worn benches and a polished wooden rail in the near ground, the raised judge's bench and its canopy at the far end, a clerk's table below, tall sash windows with net curtains along one wall. Warm oak brown, brass, green leather and pale window light. The bench sits off-centre at the back; window light is heavily diffused by the nets so no pane glares.

#### 48. `hospital-ward-night` — Hospital Ward at Night

> A long old-fashioned hospital ward at night. Iron bedsteads with tight white linen receding in two rows, a bare polished floor between them, tall dark windows down one side, a single shaded lamp burning at a desk at the far end. Cold white linen, deep blue-grey shadow and one small warm lamp. The bed rows converge strongly. Moonlight through the tall windows lays broad pale bands across the linen and the polished floor the full length of the ward, with the desk lamp a warm accent inside that; the ward reads clearly rather than dimly.

#### 49. `empty-theatre-stalls` — Empty Theatre

> An empty theatre auditorium seen from the back of the stalls, house lights very low. Rows of red velvet seats curving away in the near ground, gilt-fronted boxes stacked along both walls, ornate plasterwork and an unlit chandelier above, the stage curtain lowered. Deep crimson, tarnished gold and heavy shadow. Seat rows sweep across the lower frame. House lights at half throw a broad ambient wash over the velvet and the gilt boxes so the whole auditorium reads clearly; the stage is only slightly dimmer than the rest, never a black void.

#### 50. `farmhouse-kitchen-hearth` — Farmhouse Kitchen

> A rustic farmhouse kitchen with a fire burning low in a cast-iron range. A scrubbed wooden table with crockery in the near ground, herbs and copper pans hanging from low beams, flagstone floor, the range glowing to one side, a small deep-set window admitting grey daylight. Warm amber firelight, dark timber, stone grey and copper. The fire glow sits low and to one side, and daylight from the window gives the rest of the room a broad even fill, so the table, the beams and the flagstones all read clearly; nothing blows out and nothing falls to black.

#### 51. `dusty-attic-trunks` — Attic

> A cluttered attic beneath bare timber rafters. Old leather-bound trunks, a sheeted chair and stacked crates in the near ground, cobwebs strung between rafters, floorboards thick with dust, a single grimy dormer window admitting one angled shaft. Dust brown, faded sheet white, grey timber and pale cold light. The shaft enters from one side, and dust in the air spreads it into a broad haze that lights the trunks, the sheeted furniture and the rafters, so the whole attic reads rather than one beam in darkness.


#### 53. `throne-room-banners` — Throne Room

> A long stone hall hung with heraldic banners. A worn flagstone floor running the length of the frame, tall narrow windows down both walls throwing angled bars of light, iron braziers between them, a raised dais with a carved stone throne at the far end. Cold grey stone, heraldic crimson and gold, warm brazier glow. Strong perspective to the dais; the light bars are narrow and repeated rather than one broad wash.

#### 54. `stone-prison-cell` — Prison Cell

> A bare stone prison cell. Damp scarred masonry and scattered straw in the near ground, scratched tally marks cut into one wall, a heavy iron-bound door in shadow, a small barred slit high in the opposite wall admitting a single pale shaft. Cold grey stone, dull straw and one thin cold shaft. The shaft falls off-centre and lands low on the wall, and bounces off the flagstones into a soft grey ambient that fills the cell, so the masonry texture stays visible across the whole frame rather than dropping to black.

#### 55. `victorian-laboratory` — Victorian Laboratory

> A cluttered Victorian private laboratory at night. Dark wood benches crowded with brass instruments, retorts and glass tubing in the near ground, a low gas flame under a bubbling flask, shelves of murky specimen jars behind, charts pinned to the panelling. Brass, bottle-green glass, deep mahogany and a small warm flame. Apparatus fills the midground. A broad warm lamp wash lights the whole bench and the shelves behind it, with the gas flame a small accent inside that larger glow rather than the only light in the room.

#### 56. `glasshouse-conservatory` — Glasshouse

> A Victorian iron-framed glasshouse crowded with palms and ferns. Wet tiled path and broad leaves crowding both sides in the near ground, condensation running down the panes, white-painted iron ribs arching overhead, further foliage dissolving into green haze. Wet green, white iron, terracotta and pale diffused light. Ironwork arches across the top of the frame; light comes through misted glass so it is soft and completely even.

### Fantastic and speculative

#### 57. `wizards-workroom` — Wizard's Workroom  **[FANTASTIC]**

> A cramped tower workroom lit by a pale floating arcane glow rather than fire. A brass orrery and open bound tomes on a cluttered near table, chalked sigils across bare floorboards, shelves of murky specimen jars and hanging dried bundles behind, a narrow arched window showing night. Cold blue-green glow against dark oak, brass and dull parchment. The arcane glow sits off-centre but throws a wide cool light over the table, the chalked floorboards and the shelves behind, so the whole cluttered room reads, with a low warm fill keeping the corners off black.

#### 58. `torchlit-dungeon` — Dungeon Corridor  **[FANTASTIC]**

> A low vaulted dungeon corridor of damp rough-cut stone. Worn flags and standing puddles in the near ground, heavy iron-bound doors set along one wall, guttering torches in brackets spaced too far apart, the corridor bending away into warm gloom. Warm brown stone, rust and spreading orange torchlight. The corridor recedes in strong perspective. Torchlight spills broadly over the damp stone so whole stretches of wall and floor glow amber, the pools overlapping between brackets rather than leaving black gaps, and the full length stays readable.

#### 59. `airship-gondola-clouds` — Airship Gondola  **[FANTASTIC]**

> The interior of a riveted airship gondola above an endless floor of cloud. A brass-rimmed instrument panel and worn oxblood leather seating in the near ground, polished timber trim, a wide curved window running along one side onto pale sky and a cloud sea below, rigging lines visible outside. Brass, oxblood, warm timber and cloud white. The window sits to one side; the cloud light is bright but even, with no sun disc in frame.

#### 60. `overgrown-city-ruins` — Overgrown Ruins

> A ruined city street reclaimed by nature under soft overcast light. Cracked tarmac split by grass and saplings in the near ground, a rusted railing, vines swallowing concrete facades on both sides, empty window openings dark, young trees closing the street further back. Weathered concrete grey, rust and aggressive green. Facades frame both sides with greenery running up the middle; light is flat and diffuse with no sky gap glaring.

---

## Batch three — 45 scenes

Weighted toward modern and non-Western settings, which the first sixty barely covered.
Each is tagged with the style track to use.

### Modern East Asian cities

#### 61. `tokyo-backstreet-night` — Tokyo Backstreet

> A narrow Tokyo backstreet after midnight, photographed at eye level. Wet asphalt holding smeared coloured reflections in the near ground, a lit vending machine and red paper lanterns outside a shuttered izakaya, tangled overhead cables, bicycles against a railing, the lane narrowing into darkness. Warm red and amber against cold blue-black night. Light comes from many sources and spreads: wet asphalt carries broad coloured reflections down the whole lane, the vending machine washes the wall beside it, and faint sky glow sits above the roofline. Every sign is an unreadable coloured glow. The street reads as lit, not as points in blackness.

#### 62. `konbini-night` — Convenience Store at Night

> A Japanese convenience store glowing on a dark residential street, photographed from across the road. Damp pavement and a painted kerb in the near ground, the shopfront a flat wall of fluorescent white behind glass with stocked shelving visible, a parked bicycle, low dark buildings either side. Clinical white and pale green against near-black surroundings. The lit facade sits low and off-centre with all signage reduced to unreadable colour bands; the sky above is empty and black.

#### 63. `shinkansen-window-ricefields` — Bullet Train Window

> The interior window of a modern Japanese bullet train, photographed from the seat. A clean grey tray table and window frame sharp in the near field, beyond the glass flooded rice paddies and distant hills pulled into horizontal streaks by speed, an overcast sky. Muted grey interior against green and silver-water motion blur. The window fills one side; the blurred exterior stays soft and low in contrast with no bright sky patch.

#### 64. `japanese-apartment-small` — Small Tokyo Apartment

> A small single-room Japanese apartment photographed from the doorway in flat afternoon light. A low table and floor cushion on pale tatami in the near ground, a folded futon against one wall, a compact kitchenette, sliding glass doors onto a narrow balcony with hanging laundry beyond. Straw, off-white and grey with one muted colour accent. Balcony light enters from one side through net curtain; the room stays evenly lit and uncluttered.

#### 65. `shotengai-arcade` — Covered Shopping Street

> A covered Japanese shopping arcade photographed down its length in late afternoon. Tiled floor and a rolled-down steel shutter in the near ground, fabric banners and paper lanterns strung beneath a translucent vaulted roof, a few shops still lit further down, bicycles parked along one side. Faded red, cream and green under milky skylight. Strong perspective down the arcade; roof light is even and diffused with no hot spot, and all lettering is illegible.

#### 66. `hongkong-highrise-canyon` — Hong Kong High-Rises

> A narrow canyon between dense Hong Kong residential towers, photographed looking steeply upward. Weathered concrete and tiled facades rising on both sides, hundreds of air-conditioning units and bamboo drying poles hung with laundry projecting out, caged windows, a bright slot of overcast sky far above. Grey-green concrete, rust and faded laundry colour. Towers fill both sides; the sky slot is small and kept near the top so the mass of the frame stays mid-toned.

#### 67. `shanghai-bund-dusk` — Shanghai Riverfront

> The Shanghai riverfront at dusk photographed from the promenade. A stone balustrade and damp granite paving in the near ground, the dark river with a ferry wake crossing it, a skyline of lit glass towers on the far bank with haze softening their tops. Deep blue-grey water, warm tower light, smog-pink sky band. The skyline sits as a mid-frame band with dim sky above; tower lights read as many small points, none blown out.

#### 68. `shanghai-longtang-lane` — Shanghai Lane House

> A narrow Shanghai longtang lane between brick shikumen terraces, photographed down its length in soft morning light. Cracked concrete underfoot, a shared tap and stacked plastic stools in the near ground, bamboo poles of laundry projecting overhead across the lane, carved stone door frames, potted plants on the sills. Warm grey brick, faded laundry colour and muted green. Walls press in on both sides; the overhead laundry breaks the light into soft patches.

#### 69. `beijing-hutong-winter` — Beijing Hutong in Winter

> A Beijing hutong alley in winter, photographed at eye level under flat grey light. Frozen rutted ground and a parked bicycle in the near field, low grey brick courtyard walls running along both sides, a red-painted timber gate with faded paper couplets, bare trees showing above the roofline, cabbages stacked by a step. Cold grey brick, oxidised red and bare-branch brown. The low walls keep the frame horizontal and the pale sky is a thin strip above.

#### 70. `seoul-rooftop-night` — Seoul Rooftop

> A residential rooftop in Seoul at night, photographed across the parapet. Rough waterproofed decking, a steel water tank and satellite dishes in the near ground, a low parapet, then rank upon rank of lit apartment towers receding toward dark hills, small red neon crosses scattered among them. Cold blue-grey with warm window points and restrained red accents. The parapet anchors the lower frame. The towers form a dense field of lit windows bright enough to read as a city, and haze above the hills carries their glow, so the whole frame holds light rather than a few points.

### Modern everyday and domestic

#### 71. `modern-kitchen-morning` — Kitchen in the Morning

> A contemporary kitchen photographed in soft early morning light. A stone worktop with a single mug and a folded cloth in the near ground, flat-fronted cabinets, a stainless hob and kettle, a window above the sink showing pale garden green. Cool white, pale timber and grey with one small warm accent. Light enters horizontally from the window and is diffused; surfaces stay matte with no specular glare.

#### 72. `bedroom-morning-light` — Bedroom, Morning

> A modern bedroom photographed in soft morning light with the bed unmade. Rumpled white linen filling the near ground, a wooden chair with draped clothing, a bedside table holding a glass of water, half-drawn linen curtains admitting diffused light from one side. Warm white, oatmeal and pale grey. Light falls across the bed from the side with soft edges; the window itself stays out of frame so nothing blows out.

#### 73. `living-room-tv-glow` — Living Room at Night

> A dark living room at night lit only by an off-frame television, photographed from behind the sofa. The sofa back and a cushion in the near ground, a low table with a mug and a remote, flickering cool light washing one wall and the ceiling edge, the rest of the room in deep shadow. Cold blue-white over deep blue-grey, with a warm lamp adding a second glow in the background. The screen stays out of shot so its light arrives indirectly, but strongly enough to wash the sofa, the table and a broad area of wall and ceiling; the room's shapes stay clearly readable rather than dissolving into shadow.

#### 74. `apartment-balcony-city` — Balcony Above the City

> A small apartment balcony at night photographed from just inside the sliding door. A metal railing and a single folding chair in the near ground, a potted plant, then the city spread below as a field of small warm window lights and street lamps with low cloud catching the glow. Deep blue-black with scattered amber points. Railing and chair anchor the lower frame. The city below is a dense, even field of lights bright enough to read as a city, and low cloud above carries its orange glow, so the upper frame is lit rather than empty black.

#### 75. `coffee-shop-afternoon` — Café in the Afternoon

> The interior of a contemporary café photographed in mid-afternoon. A worn timber table with a cup, saucer and a closed laptop in the near ground, mismatched chairs, a tiled counter with an espresso machine and shelves of cups behind it, a large street window at one side admitting diffused daylight. Warm timber, matte black and cream. The counter sits in the midground; window light is soft and indirect and the frame is evenly lit.

#### 76. `supermarket-aisle-night` — Supermarket Aisle

> A supermarket aisle photographed down its length under hard fluorescent ceiling light, no shoppers. Polished vinyl floor reflecting the strip lights in the near ground, shelves stacked with plain unbranded packaging rising on both sides, a chilled cabinet glowing faintly at the far end. Cold white and pale green with desaturated packaging colour and no readable labels. Strong one-point perspective; lighting is flat and even throughout.

#### 77. `suburban-street-dusk` — Suburban Street

> A quiet suburban residential street photographed along the pavement at dusk. A kerb, a strip of mown grass and a parked car in the near ground, similar low houses with lit front windows receding on both sides, a street lamp just coming on, mature trees between them. Blue-grey dusk with small warm window rectangles. Perspective runs down the street; the sky is a dim strip and the window lights stay small and scattered.

#### 78. `motel-room-night` — Motel Room

> A cheap motel room at night photographed from the doorway. A patterned bedspread and a bedside table with a lamp in the near ground, a second bed beyond it, a dated wall unit and mirror, thin curtains with coloured neon glowing through from outside. Dull brown, mustard and a cold neon wash at the window. The neon arrives diffused through the curtain as a broad coloured wash across the bedspread and wall, the lamp adding a second spread of warm light, so the whole room including the ceiling stays readable.

#### 79. `night-highway-from-car` — Highway at Night

> A night highway photographed from the driver's viewpoint over a dim dashboard. The dashboard edge and a sliver of steering wheel dark in the near ground, wet asphalt and painted lane markings lit by headlights just ahead, reflective posts trailing away, small red tail lights in the distance, everything beyond softening into deep blue night. Deep blue night with cold headlight white and small red points. Headlights lay a broad spread of light across the road surface and the verge, and the sky above carries cloud lit by distant town glow, so the upper frame reads as sky; the scene is legible as a road at night, not a stripe in darkness.

#### 80. `airport-gate-late` — Departure Gate

> An airport departure gate late at night, photographed along the seating. Rows of empty moulded seats and carpet tile in the near ground, a bank of floor-to-ceiling glass, beyond it a dark apron with a parked aircraft and blue taxiway lights, ceiling downlights reflected softly in the glass. Cold grey and blue with small amber ground lights. Seats lead into the frame. Ceiling downlights give the gate a broad even wash over carpet and seating, and the apron beyond carries enough floodlight and taxiway colour to read as an airfield rather than a black panel.

### Modern institutional and working

#### 81. `open-plan-office-night` — Office After Hours

> A large open-plan office photographed after hours with the main lights off. Rows of empty desks with dark monitors and task chairs receding, one desk lamp burning at the far side, floor-to-ceiling windows showing a lit city beyond, carpet tile underfoot. Cold grey and blue-black with one warm lamp and distant city points. Desk rows recede in perspective. The city beyond the glass is bright enough to wash the whole floor in cool light, picking out desks, chairs and carpet across the frame, with the single desk lamp a warm accent inside that.

#### 82. `police-interview-room` — Interview Room

> A bare police interview room photographed from one corner under hard ceiling light. A scuffed table fixed to the floor in the near ground with a recording unit on it, two moulded chairs facing across it, acoustic wall panelling, a small high window of obscured glass, a door with a viewing panel. Institutional grey-green, beige and cold white. The table anchors the foreground; lighting is flat, even and almost shadowless.

#### 83. `hospital-corridor-modern` — Hospital Corridor

> A modern hospital corridor photographed down its length in the small hours. Polished vinyl flooring reflecting the overhead lights in the near ground, handrails along both walls, closed doors and a wall-mounted dispenser, a nurses' station lit further down, the corridor bending out of sight. Pale green, white and grey with one warmer lit station. Strong perspective; floor reflections are soft and the lighting is even with no hot spot.

#### 84. `server-room` — Server Room

> A data centre aisle photographed down its length. A perforated raised floor in the near ground, black equipment racks rising on both sides carrying hundreds of small green and amber indicators, bundled cabling overhead, a glass door at the far end. Cool blue-grey with fine green-amber points. Racks recede in strong perspective. Cool overhead lighting gives the aisle a broad even wash that picks out the rack faces and the floor grilles, with the indicator LEDs as fine texture inside it rather than the only light source.



#### 89. `hotel-corridor` — Hotel Corridor

> A hotel corridor photographed down its length under low wall lighting. Patterned carpet running away in the near ground, identical numbered doors receding on both sides, wall sconces at regular intervals, a mirror and side table at the far end, a fire door part way along. Muted gold, burgundy and brown with warm pooled sconce light. Strong repeating perspective. The sconces are frequent enough that their pools overlap into a continuous warm wash along the carpet and both walls, and the far end stays readable rather than dropping into shadow.


### Traditional East Asia

#### 91. `japanese-temple-garden` — Temple Garden

> A Japanese temple garden in soft overcast light. Deep green moss and a stone water basin in the near ground, raked gravel beyond it, clipped shrubs and the twisted trunks of old maples, a timber veranda with shoji screens running along one side. Moss green, wet grey stone and dark timber. The veranda edges one side of the frame; light is flat and diffuse with no sun patch and the detail sits low.

#### 92. `torii-path-forest` — Path of Torii Gates

> A path of vermilion torii gates climbing through dense cedar forest. Worn stone steps in the near ground, the gates standing close enough to form a receding tunnel, their posts weathered, tall dark cedar trunks pressing in on both sides, green light filtering from far above. Saturated vermilion against deep green-black and grey stone. The gate tunnel drives strong repeating perspective. Diffuse daylight comes down through the canopy along the whole climb, lighting the vermilion posts and mossy steps evenly, so the tunnel stays readable into the distance rather than darkening to black.

#### 93. `ryokan-tatami-room` — Ryokan Room

> A traditional ryokan tatami room in soft afternoon light. A low lacquered table with a tea set on pale tatami in the near ground, a folded cushion, a tokonoma alcove holding a hanging scroll and a single stem, shoji screens slid partly open onto green garden. Pale straw, off-white paper and dark timber framing. The shoji diffuse the light to an even glow; the garden beyond reads as layered green depth rather than detail.

#### 94. `onsen-town-snow` — Hot Spring Town

> A Japanese hot spring town under heavy snow at dusk. A stone-lined river steaming in the near ground with snow banked along it, three-storey timber inns crowding both banks with lit paper lanterns and glowing windows, a small arched bridge, steep snowy hills behind. Warm lantern amber against blue snow shadow and dark timber. Steam softens the midground; lantern lights are many and small rather than one bright source.

#### 95. `suzhou-garden-moongate` — Scholar's Garden

> A classical Chinese scholar's garden in soft light. A whitewashed wall with a circular moon gate in the near ground framing a further courtyard, weathered limestone rockery and a still pond with lotus pads to one side, a latticed pavilion window, banana leaf and bamboo. Whitewash, grey tile, pond green and dark timber. The moon gate frames a second depth; light is diffuse and the whitewashed wall is held to a soft mid-grey rather than bright.

#### 96. `siheyuan-courtyard` — Courtyard House

> A traditional Chinese siheyuan courtyard in late afternoon. Grey flagstones and a large glazed water vat in the near ground, single-storey wings with timber lattice windows and faded red-painted doors enclosing all four sides, a bare jujube tree at the centre, grey tiled roofs against a pale sky. Grey brick and tile, oxidised red and dull green lattice. Roofs frame the top, the open sky is a modest square and the light stays flat.

#### 97. `rice-terraces-morning` — Rice Terraces

> Flooded rice terraces stepping down a steep hillside at dawn. Curved mud bunds and shallow water holding a mirrored sky in the near terraces, the terraces repeating in nested curves down and away, mist lying along the valley, a small thatched shelter among them. Silver water, mud brown and new-shoot green under a pale sky. Terrace curves lead the eye down and back; the mirrored sky stays soft and mid-toned rather than bright.

#### 98. `tibetan-monastery-cliff` — Cliff Monastery

> A Tibetan monastery built into a high cliff face under a deep blue sky. Rough stone steps and a line of weathered prayer flags strung across the near ground, whitewashed walls with dark trapezoid windows and crimson and ochre bands stacked up the rock, bare brown mountains beyond. Whitewash, deep crimson and ochre against brown rock and saturated blue. The buildings climb one side; the sky is deep and dark-toned rather than bright.

### South Asia and the Middle East

#### 99. `indian-street-monsoon` — Monsoon Street

> A crowded Indian city street in heavy monsoon rain, photographed at street level. Ankle-deep water running over broken tarmac in the near ground with rain rings across it, open shopfronts under tarpaulin awnings on both sides, an auto-rickshaw at the kerb, tangled overhead cables, grey sheeting rain flattening the distance. Saturated awning colour against grey rain and dark wet road, signage illegible. Rain softens everything past the near ground and no bright sky shows.

#### 100. `varanasi-ghats-dawn` — River Ghats

> Wide stone ghat steps descending to a slow brown river at first light. Worn uneven steps and a moored wooden boat in the near ground, tiered palaces and shrines rising behind in faded ochre and rose, thin smoke drifting along the bank, mist dissolving the far shore. Ochre, rose, river brown and pale gold. Steps lead down and across the frame; the sun stays off-frame and the far bank fades to nothing.

#### 101. `stepwell-geometric` — Stepwell

> A vast Indian stepwell seen from the upper edge looking down. Symmetrical flights of sandstone steps crossing and recrossing as they descend in tiers, deep shadow gathering between them, still dark green water at the bottom, carved pillared niches in the side walls. Warm sandstone ochre against deep shadow and black-green water. Repeating geometry fills the frame. Bright sky above bounces down the sandstone so the steps stay legible all the way to the water, the lower tiers reading as cool shadow with visible detail rather than black.

#### 102. `caravanserai-night` — Caravanserai

> A desert caravanserai courtyard at night. Sand-dusted flagstones and stacked bundles in the near ground, couched camels in shadow, a double tier of arched brick arcades enclosing the court with small fires and oil lamps burning beneath them, a star-filled sky over the open centre. Warm firelight amber against cold blue night and mud-brick brown. Firelight spreads across the courtyard flagstones and up into the arcade arches so the architecture reads all the way round, and the night sky carries visible starfield and haze rather than flat black.

#### 103. `mughal-palace-courtyard` — Palace Courtyard

> A Mughal palace courtyard in the heat of the afternoon. A narrow marble water channel running away down the centre of the near ground, red sandstone arcades with scalloped arches on both sides, inlaid marble panels, a domed pavilion closing the far end, a bleached hazy sky. Red sandstone, cream marble and washed-out blue. Strong central symmetry; the water channel is kept dull rather than mirror-bright and the sky is hazed down.

### Africa, Latin America, Central Asia

#### 104. `savanna-acacia-dusk` — Savanna at Dusk

> Open African savanna at dusk. Dry tussock grass and a termite mound in the near ground, scattered flat-topped acacias in silhouette across the middle distance, a herd reduced to small dark shapes far off, a low escarpment on the horizon under a dust-thickened sky. Straw gold, burnt orange and deep violet shadow. Acacia silhouettes break the horizon; the sun stays off-frame with its glow spread widely across the sky, and that warm light still catches the grass so the whole ground plane reads golden rather than falling to silhouette.

#### 105. `mudbrick-town-sahel` — Mud-Brick Town

> A Sahelian mud-brick town in hard late afternoon light. A sculpted earthen wall with projecting timber beams in the near ground, narrow shaded lanes between rounded buildings, a stepped mosque tower rising behind, flat roofs stacked up the slope, dust haze over everything. A near-uniform earth ochre with deep blue-brown shadow. Wall texture carries the foreground; shadows are strong but the sky is small and hazed.

#### 106. `rift-valley-lake` — Soda Lake

> A shallow East African soda lake seen from the shore. Cracked white alkaline flats and a rim of crusted salt in the near ground, pale green shallow water beyond, a distant pink band of flamingos, a hazy volcanic escarpment across the far side under a high sky. Bone white, alkaline green and dusty violet. Horizontal banding dominates; the pink band is a thin accent and the sky is hazed to a flat pale tone.

#### 107. `colonial-plaza-siesta` — Colonial Plaza

> A Spanish colonial plaza in the dead heat of afternoon. Worn paving and the base of a stone fountain in the near ground, a deep shaded arcade running along one side, pastel stucco facades with closed timber shutters and wrought-iron balconies, a twin-towered church closing the far end, palms and hard shadow. Faded ochre, rose and cream against deep shade. Arcade shadow anchors one side and the sunlit facades stay warm rather than glaring.

#### 108. `andes-altiplano` — Altiplano

> A high Andean altiplano under an intense sky. Coarse tussock grass and scattered volcanic stone in the near ground, a flat pale plain running far back, a llama herd tiny in the middle distance, snow-capped volcanic cones along the horizon, a thin dirt track. Straw gold, mineral grey and deep saturated blue. The plain occupies the middle band and the sky is deep and dark-toned at the top rather than bright.

#### 109. `amazon-river-town` — River Town

> A small Amazonian river town of stilt houses seen from the water. Brown river surface and a moored wooden boat in the near ground, timber houses raised on tall stilts with corrugated roofs and plank walkways strung between them, a dense green forest wall behind, a grey rain squall advancing from one side. River brown, weathered timber and saturated forest green under heavy cloud. Houses run as a band across the midground and the sky stays dim.

#### 110. `steppe-yurt-mongolia` — Steppe

> A single white felt ger on open Mongolian steppe under an enormous sky. Cropped wind-flattened grass in the near ground, the ger with its orange-painted door and a tethered horse in the middle distance, a wisp of smoke from the crown, endless rolling grassland to a low horizon, towering cloud building far off. Felt white, grass ochre-green and slate cloud. The ger is small and off-centre; cloud fills the upper frame but stays grey rather than bright.

---

## Wave one — 30 scenes

Places from the three books that prompted this expansion — 白夜行, 庆余年 and The Odyssey — and
everyday places that almost any modern novel visits. Why each scene is here is in
[`docs/catalog-expansion-plan.md`](../docs/catalog-expansion-plan.md). Each scene's description,
keywords, cues and examples were written and checked against sample passages before any art was
made, and waited in `staged/` until the art existed. All three waves were published in catalog
version 8.

Two markers appear in the waves. **[FANTASTIC]** is as before: the subject does not exist.
**[PERIOD SET]** is new: the place was real but survives only as a ruin or a reconstruction, so it
is shown intact and in use, the way a period film would build it. The brief explains both.

### Imperial China

#### 111. `chinese-imperial-hall` — Imperial Audience Hall

> The great audience hall of a Chinese imperial palace, empty, photographed low along the central axis toward the throne. Polished dark stone floor in the near ground reflecting the columns, rows of massive vermilion lacquered pillars with gilded dragon ornament marching away on both sides, a gilded coffered ceiling overhead, and at the far end a raised platform with a carved golden dragon throne under a canopy, bronze incense burners and cranes flanking its steps. Deep vermilion, burnished gold and dark stone. Daylight from tall lattice doors along one side lays broad warm light across the floor and up the pillars so the whole hall reads, with the throne mid-toned and slightly off-centre rather than a bright focal point. Ming and Qing palace architecture only; no Japanese or Korean forms, no tourist barriers, and any plaque is a blank lacquered board.

#### 112. `ancient-chinese-street` — Ancient Capital Street  **[PERIOD SET]**

> A long street in an old imperial Chinese capital in soft morning light, deserted before the shops open. Worn stone flagstones and a wooden handcart in the near ground, two-storey timber shopfronts with carved lattice, upturned grey-tiled eaves and hanging cloth banners lining both sides and receding in strong perspective, red paper lanterns under the eaves, and a tall drum tower on a stone base closing the far end of the street. Weathered timber brown, grey tile, faded red and indigo cloth. Soft overcast light fills the street evenly and the far tower sits in gentle haze. Every banner, board and plaque is plain cloth or blank wood with no characters at all. No modern wires, lamps or tourists.

#### 113. `chinese-teahouse` — Teahouse Upstairs

> The empty upper floor of an old Chinese teahouse in the afternoon. A square table of dark lacquered wood with a clay teapot and cups in the near ground, more tables and benches receding across worn floorboards, a small raised storyteller's table with a folded fan at the far end, and a long run of carved lattice windows thrown open onto the grey tiled roofs of the street below. Dark timber, warm tea brown and soft jade green through the windows. Daylight pours in sideways through the open lattices and spreads across the floor and tables, so the room reads warm and even with no single bright window at centre. No characters on any plaque, menu board or banner.

#### 114. `wayside-inn` — Wayside Inn  **[PERIOD SET]**

> The common room of a roadside inn in old China at dusk, empty. A rough square wooden table with a pottery wine jar and bowls in the near ground, benches and more tables across a packed-earth floor, big glazed wine jars along the back wall, a counter with a cloth hung over it, and an open doorway onto a dusty yard where two horses stand tethered under a lantern. Smoke-darkened timber, clay ochre and the amber of oil lamps. Lamplight from several lamps and the last blue daylight from the doorway spread across the tables and walls so the room reads lived-in and warm rather than dark; the doorway sits to one side. The wine flag outside is plain cloth with no characters.

#### 115. `jiangnan-water-town` — Jiangnan Water Town

> A Jiangnan water town in soft grey morning light, photographed down a canal. Stone steps descending into still green water in the near ground, whitewashed houses with black tile roofs and dark timber windows rising straight from the water on both sides, a humped stone arch bridge crossing the canal in the middle distance, two black-awninged wooden boats moored below it and willows trailing over the water. Whitewash, ink-black tile, jade-green water and pale mist. Diffuse overcast light reflects evenly off the canal so the water carries the brightness low in the frame, and the sky is a narrow pale strip above the roofs. No signage, no modern fittings.

#### 116. `lantern-river-boats` — Lantern Boats on the River

> A river in an old southern Chinese city at night, photographed from the bank at water level. A stone quay edge and a mooring post in the near ground, a line of painted wooden pleasure boats with carved rails and gauze curtains moored along the river, strings of red lanterns hanging from their eaves and doubling in the black water, and lit two-storey waterfront pavilions with upturned eaves behind. Lantern red and warm amber against blue-black water and dark timber. The many lanterns and lit windows spread warm reflected light across the whole river surface, so the water glows as a broad band rather than points in darkness, and faint haze above the roofs carries the glow. No characters on lanterns or boats.

#### 117. `chinese-mountain-temple` — Mountain Temple in Mist

> A Chinese Buddhist temple on a steep forested mountainside in morning mist. Worn stone steps with moss at their edges climbing away from the near ground, a bronze incense burner with a thin thread of smoke to one side, grey-tiled temple halls with sweeping upturned eaves and red-painted timber stacked up the slope above, old pines and cypress around them, and further ridges fading into white mist. Moss green, vermilion, grey tile and pearl-white mist. The mist diffuses the light so the whole slope is softly and evenly lit, the halls reading in layers of decreasing contrast, with no bright sky patch. Chinese temple architecture only: no Japanese torii or pagodas.

#### 118. `yamen-archive-hall` — Imperial Archive Hall  **[PERIOD SET]**

> The archive hall of a secret imperial Chinese bureau, photographed down a long central aisle. A dark wooden desk with a brush, an inkstone and an oil lamp in the near ground, tall black-lacquered shelves packed with scroll cases, bound files and sealed boxes running away on both sides in deep perspective, heavy timber beams overhead and a small high lattice window far down the hall. Black lacquer, aged paper cream and the warm amber of lamplight. Oil lamps set along the desks at intervals spread warm light down the whole aisle and across the shelf faces, so the hall recedes in warm layers rather than black; the window is small and far off. Labels, tags and spines are blank.

#### 119. `southern-fishing-town` — Southern Fishing Town

> A small fishing town on a warm southern Chinese coast in soft overcast light, photographed from the beach. Grey sand, coiled rope and a tilted wooden fishing boat in the near ground, more boats pulled up along the shore, nets drying on tall bamboo poles, and a row of low stone houses with grey tile roofs and strings of salted fish hanging under their eaves, green hills behind. Wet grey sand, weathered timber, sea green and warm grey stone. Humid haze softens the light evenly, and the sea at one side carries a broad pale sheen low in the frame rather than glare. Traditional village only, no modern boats or signage.

### The classical Mediterranean

#### 120. `bronze-age-megaron` — Hall of a Bronze-Age King  **[PERIOD SET]**

> The great hall of a Bronze Age Greek palace, empty. Fleeces and a low wooden stool on a painted plaster floor in the near ground, a large round clay hearth in the centre with a low fire burning, four thick wooden columns painted deep red and tapering downward around it, plastered walls with painted friezes of spirals and hunting scenes, bronze shields and spears hanging on them, and smoke drifting up to an opening in the roof beams. Oxblood red, ochre, soot black and warm firelight. Firelight from the hearth and daylight falling through the roof opening together light the whole hall so the columns and walls read, with the hearth low and off-centre. Mycenaean architecture: timber, plaster and paint, not white marble classical temples.

#### 121. `ancient-ship-open-sea` — Ancient Ship on a Calm Sea  **[PERIOD SET]**

> An ancient Greek oared ship running on a calm open sea, photographed from its own deck near the stern. The worn timber of the steering oar and rowing benches, with the oars drawn in along the rail, in the near ground; the long black-painted hull stretching forward to a curved prow, a single large square linen sail bellied out on the mast, and a calm sea running to an empty horizon with no land in sight. Tarred black timber, sun-bleached linen, deep violet-blue sea and a hazy sky. Soft high haze spreads the light evenly across sail and sea; the sun is off-frame and the sky mid-toned rather than bright. No modern fittings.

#### 122. `aegean-island-cove` — Aegean Cove

> A small sheltered cove on a rocky Aegean island in clear afternoon light. Pale sand and smooth stones at the water's edge in the near ground, clear turquoise shallows over sand and dark weed, a black ancient wooden ship drawn up on the beach with its mast lowered, and low cliffs of pale rock with scrub and wild olive climbing above, a goat path up the slope. Pale sand, turquoise, sun-bleached rock and dusty green. The cliffs throw part of the beach into soft shade and the water reads as clear colour rather than glare; the sky is a modest strip at the top. No buildings, no modern boats.

#### 123. `greek-sanctuary` — Greek Sanctuary  **[PERIOD SET]**

> An ancient Greek sanctuary on a headland above the sea, intact. A stone altar blackened by fire with a thin rise of smoke in the near ground, a small temple of weathered limestone columns with traces of painted colour on its pediment beyond, twisted olive trees along the terrace, and the sea glittering far below under a hazy sky. Warm limestone, soot black, olive green and deep blue sea. Soft late light rakes across the stone and trees; the sea is a mid-toned band rather than a bright field and the sun stays off-frame. Not a ruin, not gleaming white marble, no fences or signs.

#### 124. `grotto-island-garden` — Island Grotto

> The mouth of a great cave on a lush Mediterranean island, photographed from the meadow outside. Clear spring water running between stones and wild flowers in the near ground, meadows of violets and wild herbs, the dark mouth of the grotto in a green hillside hung with a trailing vine heavy with grapes, dark cypress and alder crowding the slope above, and a glimpse of the sea to one side. Deep green, violet, grape purple and warm stone. Soft afternoon light fills the meadow and the vine so the cave mouth reads as dim shade rather than black, with light reaching a little way inside. No buildings.

#### 125. `underworld-shore` — Shore of the Dead  **[FANTASTIC]**

> A grey shore at the edge of the world where no sun reaches. Cold wet stones and a shallow pit dug at the water's edge in the near ground, a slow dark river sliding past, black poplars and willows standing along the far bank, mist crawling low over the water, and a pale sourceless twilight spread across everything. Ash grey, slate blue, black-green and bone white. The light is an even, overcast pewter glow with no visible source, lighting the stones, water and trees in soft layers rather than leaving the frame dark. No ghosts rendered, no skulls, nothing gory.

### 白夜行 and modern East Asia

#### 126. `school-classroom` — School Classroom

> An ordinary school classroom after lessons, empty, photographed from the back corner. Rows of plain wooden desks and chairs in the near ground, one chair pushed back, the rows receding toward a dark green chalkboard with faint smudged chalk marks, a teacher's desk at the front, and a wall of tall windows along one side with afternoon light falling in long shapes across the floor. Warm wood, chalkboard green, pale walls and golden afternoon light. The window light spreads across the floor and desks so the room is evenly lit; the windows sit along one side, not at centre, and the chalkboard carries no legible writing. Timeless enough to be Japanese, Chinese or Western.

#### 127. `abandoned-building` — Abandoned Building

> The inside of an abandoned concrete building, photographed from a stair landing. A broken stairwell choked with rubble, splintered boards and dust in the near ground, bare concrete walls with spreading water stains and peeling paint, empty window frames letting in grey daylight, and a dark doorway leading deeper in. Concrete grey, rust, damp brown and cold daylight. Diffuse daylight through several empty windows falls across the rubble and walls so the whole space reads in soft greys rather than black, with no single blinding window. No graffiti lettering.

#### 128. `cocktail-lounge` — Hostess Lounge

> A dim, expensive hostess lounge in a city nightlife district, empty before opening. A low glass table with a whisky bottle, an ice bucket and glasses in the near ground, curved deep velvet sofas in plum and midnight blue around low tables, a small bar with softly backlit bottles along one wall, a black grand piano in the corner, and low amber lamps on the side tables. Plum, midnight blue, brass and amber. The many low lamps and the backlit bar spread warm light across the velvet and the tables, so the room reads intimate but clearly visible rather than black, with no bright light at centre. No legible labels or signage.

#### 129. `izakaya-interior` — Izakaya

> The inside of a small Japanese izakaya in the evening, empty of customers, photographed from a stool at the counter. A worn wooden counter with a sake flask, small plates and chopsticks in the near ground, the cook's station behind it with skewers resting over a charcoal grill and a thin rise of smoke, strips of paper menu hung along the wall above, paper lanterns, and a noren curtain across the entrance. Honey wood, charcoal glow, off-white paper and smoky amber. Lantern light and the glow of the grill spread warm, even light across the counter and the wall. Menu strips and noren show no writing.

#### 130. `department-store` — Department Store

> The ground floor of a large department store before opening, empty. A glass cosmetics counter with neatly arranged bottles in the near ground, more glass counters receding across a polished pale floor, a tall central atrium rising floor above floor with a pair of escalators crossing it, and soft even lighting throughout. Ivory, champagne gold, glass and pale marble. The light is bright, soft and even across the whole floor and up the atrium, with no hotspot at centre and gentle reflections in the floor. No brand names or legible signs.

#### 131. `golf-driving-range` — Golf Driving Range

> A covered multi-storey golf driving range at dusk, empty, photographed from inside a hitting bay. A green hitting mat with a small pile of white golf balls and a club leaning against the partition in the near ground, a long row of identical bays stretching away under a tiered structure with floodlights along its roof edge, and beyond them a wide green field enclosed by very tall green netting on poles, distance marker flags scattered across the grass, under a dusky blue sky. Grass green, netting green, white balls and floodlight white against blue dusk. The floodlights wash evenly across the field and netting, so the outfield glows as a broad green plane rather than a black void. No legible signage.

#### 132. `tokyo-scramble-crossing` — Tokyo Crossing

> A huge scramble crossing in central Tokyo at night in light rain, deserted in the moment between signals, photographed from street level at one corner. Wet asphalt with white zebra stripes running in several directions in the near ground, the crossings meeting in the middle, and tall buildings on every side covered in giant video screens and lit facades. Electric blue, magenta, white and warm amber on wet black asphalt. The screens and facades throw broad coloured light across the entire wet road surface, so the whole frame glows rather than showing points in darkness, and the brightest screens sit high and to the sides. Every screen and sign is unreadable colour, with no letters and no pictures of people.

#### 133. `night-market` — Night Market

> A crowded East Asian night market lane just before it opens, empty of people, photographed down the aisle. A food stall counter with steel trays and skewers in the near ground, rows of stalls under canvas awnings stretching away on both sides, strings of bare bulbs and hanging lamps overhead, and woks and grills sending a haze of steam and smoke up into the lamplight. Warm tungsten orange, red awnings, steel and smoky haze against a deep blue night sky. The many bulbs spread warm light along the whole lane and across the awnings, so the market glows as a continuous corridor, and the haze catches the light above. Every sign and banner is unreadable colour with no characters.

### Any modern book

#### 134. `restaurant-dining-room` — Restaurant

> The dining room of a good restaurant in the evening before guests arrive. A table with a white cloth, a lit candle, polished glasses and folded napkins in the near ground, more tables set well apart receding into the room, warm wall lamps and a large mirror, and a kitchen door with a round window at the back. White linen, warm amber, deep burgundy and dark wood. Wall lamps and candles spread warm light across the tablecloths and walls so the room reads intimate and visible, with no single bright point at centre. No legible menus or signage.

#### 135. `bar-counter` — Bar

> A long wooden bar in a city pub late in the evening, empty, photographed along the bar from one end. The polished bar top with a half-finished pint on a beer mat in the near ground, a row of stools, brass taps, and shelves of bottles in front of a long mirror behind the bar, with low pendant lamps along its length. Dark mahogany, brass, amber beer and warm shadow. The pendant lamps and backlit shelves spread warm light down the whole length of the bar so it recedes as a glowing line, and the rest of the room is soft shadow, not black. No legible labels.

#### 136. `city-park` — City Park

> A large park in the middle of a city on a soft spring afternoon, photographed from a path. A gravel path, a park bench and an iron lamp post in the near ground, the path winding under tall old elms past a lawn sloping down to a pond, and the tops of city towers showing above the trees in the distance. Fresh green, gravel beige, soft grey water and a pale sky. Light filtered through the canopy lays soft dappled light across the lawn and path; the sky is a small band above the trees and the pond reflects it gently. No dogs or vehicles.

#### 137. `manhattan-avenue` — Manhattan Avenue

> A Manhattan avenue on a grey morning, photographed from the sidewalk looking up the avenue. A curb, a steaming street grate and the railing of a subway entrance in the near ground, the avenue running straight into the distance between towers of glass and old stone that form a deep canyon, a few yellow taxis in the traffic lanes, and a narrow strip of sky above. Stone grey, glass blue, taxi yellow and soft steam white. Overcast light reflects off the glass towers and the damp street so the canyon reads evenly from top to bottom, and the sky strip is pale but not bright. No legible signs, plates or advertising.

#### 138. `lecture-hall` — Lecture Hall

> A steep university lecture hall, empty, photographed from the top row. Curved rows of tiered wooden benches with fold-down desks in the near ground, descending toward a podium and a large blank projection screen at the bottom, high windows along one side letting in afternoon light, and a projector beam faintly visible in the dusty air. Honey wood, grey and warm afternoon light. Daylight from the high windows spreads across the tiers so the whole hall reads; the screen is blank and mid-toned, not bright, and sits below centre. No text on the screen or boards.

#### 139. `gym` — Gym

> A large modern gym early in the morning, empty, photographed from the free-weights area. A rack of dumbbells and a weight bench in the near ground, rubber floor mats, a long mirrored wall, and rows of treadmills further back facing tall windows with pale morning light coming in. Charcoal rubber, brushed steel, soft white light and one accent colour. The windows and ceiling lights fill the space with even light that reflects softly in the mirrors, with no hotspot at centre. No logos or legible signs.

#### 140. `airplane-cabin` — Airplane Cabin

> The cabin of a passenger airliner on a night flight, empty, photographed down the aisle. The edge of a seat and a folded blanket in the near ground, rows of seats receding under dim blue cabin lighting, most window blinds down, and one oval window open onto a sea of cloud lit by moonlight. Deep blue, grey upholstery and soft silver moonlight. The cabin's blue mood lighting fills the whole aisle evenly so the seats and ceiling read clearly; the moonlit window sits to one side and stays soft. No signage or screens with text.

---

## Wave two — 28 scenes

Places to play, public life, more cities, and the rest of the three books.

### Play

#### 141. `golf-course` — Golf Course

> A golf course on a still, misty morning, photographed from the edge of the fairway. Close-mown grass and a small white ball in the near ground, a smooth fairway curving between stands of tall pines toward a flag on a putting green, a pond and a white sand bunker beside it, and a low clubhouse just visible far behind in the haze. Deep green, sand white, soft grey water and misty blue. Morning mist diffuses the light so the whole course is evenly lit with gentle depth and no bright sky patch. No legible signs.

#### 142. `amusement-park` — Amusement Park

> An amusement park at dusk just after closing, empty, as the lights come on. A painted railing and a shuttered ticket booth in the near ground, a carousel with carved horses glowing under warm bulbs to one side, the midway lined with game stalls strung with lights, a large Ferris wheel lit up against the sky and the steel frame of a roller coaster crossing the background. Carnival red, warm bulb gold, teal and violet dusk. Thousands of small bulbs spread warm light across the midway and the rides so the whole park glows, and the dusk sky is deep but not black. No legible signage.

#### 143. `stadium` — Stadium

> A great sports stadium under floodlights before the gates open, empty, photographed from high in the upper tier. Rows of empty seats in the near ground falling away steeply, tier upon tier of seating wrapping around a brilliant green pitch with crisp white lines, banks of floodlights along the roof edge, and a dark evening sky above. Pitch green, seat red, floodlight white and deep blue sky. The floodlights pour even light across the whole bowl and pitch so the stadium reads completely; the lights themselves sit at the top edge, not at centre. No scoreboard text or legible signage.

#### 144. `swimming-pool` — Swimming Pool

> An indoor swimming pool early in the morning, empty, photographed from the end of a lane. Pale tiles and a starting block in the near ground, long lanes of still blue water divided by floating rope lines, wavering light thrown up across pale tiled walls, and a high glazed roof letting in soft daylight. Aqua blue, pale tile white and cool grey. Daylight from the glazed roof reflects evenly off the water so the whole hall glows softly, with no glare at centre. No lane numbers or legible signs.

#### 145. `tennis-court` — Tennis Court

> An outdoor clay tennis court at a private club on a summer afternoon, empty. Red clay with a crisp white baseline and a couple of tennis balls in the near ground, a slightly sagging net across the court, a tall green wire fence behind with a towel hung on it, and old trees throwing shade along one side. Terracotta, white lines, deep green and dappled light. Soft afternoon sun from one side lays long tree shadows across part of the court so the clay does not glare, and the sky is a small band above the trees.

#### 146. `museum-gallery` — Museum Gallery

> A quiet gallery in a great art museum, empty, photographed through a doorway into the room. A polished wooden floor and the edge of a doorframe in the near ground, a low bench in the middle of the room, tall walls hung with old oil landscapes and still lifes in heavy gilt frames, and further doorways opening onto more galleries beyond. Warm grey walls, gilt, dark oils and honey wood. Soft skylight from above spreads even light across the walls and floor, and the paintings read as dark rich tones rather than glare. No portraits with clear faces, no legible labels.

#### 147. `concert-hall` — Concert Hall

> A grand concert hall before the performance, empty, photographed from the stalls. Red velvet seat backs in the near ground, a lit stage with a black grand piano, rows of empty orchestra chairs and music stands, tiers of red seats and gilded balconies rising around it, and a great pipe organ at the back. Crimson, gilt, honey wood and warm stage light. Warm house lights and stage lighting fill the hall evenly so the balconies read all the way up; the stage is warm and mid-toned, not a bright hotspot. No legible text.

#### 148. `karaoke-room` — Karaoke Room

> A private karaoke room at night in an East Asian city, empty. A low table crowded with bottles, glasses, snacks and two microphones in the near ground, a U-shaped sofa around it, a large screen on the far wall showing only soft abstract colour, and coloured lights sweeping across the walls and ceiling. Magenta, violet, teal and warm amber. Coloured ambient light and the screen's glow fill the small room with saturated but even light so the furniture reads clearly; the screen sits off-centre and is not the brightest element. No lyrics, logos or legible text.

#### 149. `game-arcade` — Game Arcade

> A game arcade at night in a Japanese or Chinese city, empty of people. A claw crane machine full of plush toys glowing in the near ground, rows of arcade cabinets and rhythm-game machines stretching away, patterned carpet, and a low ceiling of lights. Neon pink, electric blue, lime and warm white. The many glowing machines spread colourful light across the floor and aisles so the whole room glows, and no single machine blows out. Every screen shows abstract colour; no legible text, logos or characters.

### Learning and institutions

#### 150. `school-library` — School Library

> A school library in the afternoon, empty, photographed between the shelves. Long wooden reading tables with a few books left on them in the near ground, rows of wooden shelves of coloured spines, curtains half drawn across tall windows letting in golden afternoon light, dust drifting in the beams, and a librarian's counter by the door. Honey wood, faded book colours, cream curtains and golden light. The half-drawn curtains diffuse the light into broad soft bands across the tables and shelves so the room reads evenly, with no bright window at centre. No legible spines or signs.

#### 151. `school-rooftop` — School Rooftop

> The flat concrete rooftop of an East Asian school building on a clear afternoon, empty. Weathered concrete and a painted line in the near ground, a tall green wire fence around the edge, a steel water tank on legs and the small stairwell hut with its door to one side, and a small town spread out below under a wide pale sky with distant hills. Concrete grey, fence green and pale blue sky. The sky is soft and hazy rather than bright; the fence and water tank break the frame vertically and the town below gives depth. No legible text.

#### 152. `police-squad-room` — Police Squad Room

> A crowded police squad room at night, empty of people. Steel desks pushed together in the near ground with phones, overflowing files and an ashtray, more desks receding under fluorescent tubes, and a large whiteboard on the far wall covered in pinned photographs, maps and marker arrows. Steel grey, fluorescent green-white and paper cream. Overhead fluorescent light fills the room evenly; the whiteboard is mid-toned and to one side. Nothing on the board or the files is legible, and no faces show in the photographs.

#### 153. `magistrate-court` — Magistrate's Court

> The hall of a county magistrate in old China, empty, photographed from the floor where the accused would kneel. Worn stone flags in the near ground, red-and-black wooden staves in racks along both sides, a raised platform at the far end with the magistrate's table draped in red cloth, a gavel block and a pot of tallies on it, a large hanging plaque above and a painted screen behind. Vermilion, black lacquer, grey stone and dusty daylight. Daylight from open doors behind the viewer spreads across the floor and up the platform so the hall reads evenly. The plaque is a blank lacquered board with no characters.

### Shops

#### 154. `bookshop` — Bookshop

> A narrow second-hand bookshop on a rainy afternoon, empty, photographed from the doorway. Stacks of books on the floor in the near ground, shelves climbing to the ceiling on both sides with a wooden ladder leaning against them, a counter at the back with a green-shaded lamp, and a rain-streaked shop window to one side. Warm book browns, green lamp glow and cool grey rain light. The lamp and the window spread warm and cool light along the shelves so the narrow shop reads end to end, with no hotspot at centre. No legible spines or signs.

#### 155. `boutique` — Boutique

> An expensive fashion boutique in the afternoon, empty, photographed from inside. A pale carpet and the corner of a glass counter in the near ground, only a few garments hung far apart on slim metal rails, a mirrored fitting room with its curtain drawn back, and a window display of three outfits facing a quiet street. Ivory, blush, soft black and brushed brass. Soft even lighting and diffused window light fill the room gently; the window is to one side and does not glare. No brand names or legible text, no mannequin faces.

#### 156. `pawnshop-counter` — Pawnshop

> A small pawnshop at dusk, empty, photographed from the customer's side. A high wooden counter with a steel grille in the near ground, a glass display case of watches and rings below it, shelves behind the grille crowded with pawned objects, tickets on a spike and a desk lamp over an open ledger. Dark wood, steel grey, brass and warm lamplight. The desk lamp and a bare ceiling bulb spread warm light across the grille and shelves so the shop reads and nothing goes black; the grille lines break the frame. No legible writing on tickets or ledger.

#### 157. `pharmacy` — Pharmacy

> A small neighbourhood pharmacy in the evening, empty. A counter with a small bell and a few paper bags in the near ground, white shelves of medicine boxes behind it, glass cabinets of old apothecary jars along one side, and the shop window showing a dark street and a softly glowing green cross outside. Clinical white, pale green, glass and warm counter light. Even overhead light fills the shop; the green cross outside is small and soft, not a bright point. No legible labels or signs.

### Homes

#### 158. `showa-wooden-apartment` — Old Wooden Apartment

> An old two-storey wooden apartment building in a Japanese city in the late afternoon, photographed along the open upper corridor. Worn floorboards with a pair of shoes and a folded umbrella outside a door in the near ground, a narrow open-air corridor of identical wooden doors running away, an iron staircase on the outside, laundry hanging over the rail and a jumble of low roofs and utility poles beyond. Weathered brown timber, rust, faded laundry colours and soft golden light. Low sun from the side washes the corridor and doors evenly and the sky is a pale strip. Nineteen-seventies and eighties details, no modern signage, no legible nameplates.

#### 159. `chinese-apartment` — Chinese Apartment Block

> The living room of a flat in an ageing Chinese apartment block in the afternoon, empty. A red-painted concrete floor and a thermos beside an enamel basin on a low table in the near ground, a sofa with a lace cover, a framed landscape print on the wall above it, a television on a wooden cabinet, and an open door onto a concrete stairwell with bicycles and boxes. Faded red, cream walls, wood brown and soft afternoon light. Daylight from a side window spreads across the floor and wall so the room reads warm and even. No legible calendars or characters.

### Cities

#### 160. `brooklyn-brownstone-street` — Brownstone Street

> A tree-lined Brooklyn street of brownstone townhouses on an autumn afternoon, empty. A stone stoop with fallen leaves on its steps and an iron railing in the near ground, a row of brownstones with high stoops and bay windows receding down the block, plane trees in yellow leaf, and parked cars along the curb. Brownstone red-brown, autumn gold, black iron and soft grey sky. Soft overcast light fills the street evenly and the sky is a small band above the trees. No legible house numbers or signs.

#### 161. `paris-cafe-terrace` — Paris Café Terrace

> The terrace of a Paris café on a grey afternoon, empty, photographed from among the tables. A small round marble table with an espresso cup and a folded newspaper in the near ground, rows of wicker chairs facing the boulevard under a dark red awning, the zinc bar glimpsed through the window, and cream stone apartment buildings with iron balconies across the street. Cream stone, oxblood awning, wicker gold and soft grey sky. Overcast light spreads evenly across the terrace and the facades, and the awning shades the foreground so nothing glares. No legible text on the awning, cup or newspaper.

#### 162. `pudong-skyline-night` — Shanghai Skyline at Night

> The skyline of Pudong in Shanghai at night, seen from a high observation deck. The edge of a window frame and a railing in the near ground, a dense forest of glass skyscrapers lit in blue and gold filling the middle of the frame, the Huangpu river curving below with boat lights on it, and the lit city running out to a hazy horizon. Electric blue, gold, deep violet sky and river black. The countless lit windows form a continuous field of light that fills the frame, and haze above the towers carries their glow, so nothing is a point in darkness. No legible signs, logos or text.

### The rest of the three books

#### 163. `palace-red-walls` — Red Palace Walls

> A long lane between high red walls inside an imperial Chinese palace, empty, after snowfall. Snow on grey stone flags in the near ground, tall vermilion walls on both sides running away in strong perspective, golden-yellow glazed roof tiles just showing along their tops, a narrow strip of pale grey sky, and a single gateway far down the lane. Vermilion, snow white, imperial yellow and cold grey. Soft overcast light and the snow's reflection fill the lane evenly, and the sky strip is pale and narrow. Forbidden City architecture only, no tourists or modern fittings.

#### 164. `examination-cells` — Examination Hall  **[PERIOD SET]**

> The imperial examination compound of old China, photographed down one narrow lane. Worn grey brick paving in the near ground, a long row of tiny open-fronted brick cells running away on one side, each with two wooden planks for desk and seat, an inkstone and brush left in the nearest, and a tall wooden watchtower rising at the end of the lane. Grey brick, weathered wood and a pale sky. Soft overcast light fills the lane evenly and reaches into the cells, and the sky is a narrow strip above. No numbers or characters on the cells.

#### 165. `city-gate-and-walls` — City Gate and Walls

> The great gate of a walled Chinese city in winter, photographed from the road outside. A snowy road with cart tracks in the near ground, massive grey brick walls running away on either side, a deep arched gate passage left of centre, and a tall gatehouse tower with upturned tiled eaves above it, banners on the battlements. Grey brick, snow white, dark timber and faded red banners. Soft overcast light and the snow's reflection fill the scene evenly; the arched passage is shadowed but reads. Ming-style city walls; banners and plaques carry no characters.

#### 166. `herders-cave` — Herder's Cave

> A vast cave in a rocky hillside used by a herdsman, photographed from inside toward the mouth. Rough rock floor, a low fire and wicker racks of round cheeses in the near ground, stone-walled pens for sheep and goats along the cave walls, and the wide cave mouth partly blocked by a huge boulder, with pale daylight beyond. Warm firelight orange, rough rock ochre and soft daylight. Firelight and the daylight from the mouth together light the whole interior so the walls and pens read; the mouth sits to one side and does not glare. At most a few sheep as dim shapes in the pens.

#### 167. `ancient-walled-city` — Bronze-Age Walled City  **[PERIOD SET]**

> The high stone walls of a Bronze Age city on a hill above a windy plain, intact. Dry grass and a rutted chariot track in the near ground, the massive sloping walls of fitted stone with towers and a great gate rising above the plain, and far off on the shore the dark hulls of a fleet drawn up in lines under a hazy sky. Warm stone, dry-grass gold, dark hulls and dusty blue. Soft late afternoon light rakes across the walls; the sky is mid-toned and hazy with the sun off-frame.

### Medieval Europe

#### 168. `medieval-tavern` — Medieval Tavern  **[PERIOD SET]**

> A low smoky tavern in a medieval town at night, empty of people. A rough wooden table with a tankard and a trencher in the near ground, benches and more tables across a floor strewn with rushes, a fire roaring in a wide stone hearth, casks stacked along the wall, and a wooden staircase climbing to rooms above. Firelight orange, smoky timber brown and tallow gold. The hearth and several candles spread warm light across the whole room and up the beams so it reads warm and full rather than dark, with the fire low and off-centre.

---

## Wave three — 24 scenes

The other worlds: old Japan, xianxia, Rome, medieval Europe, the imagined, and modern cities
beyond East Asia and the West.

### Old Japan

#### 169. `edo-street` — Edo Street  **[PERIOD SET]**

> A street in old Edo, Japan, in soft morning light, empty. Packed earth and a stone-lined drainage channel in the near ground, rows of two-storey wooden townhouses with lattice fronts and dark tiled roofs on both sides, indigo noren curtains hanging over the shop doorways, and a wooden fire watchtower rising above the roofs further down the street. Dark timber, indigo, grey tile and pale sky. Soft overcast light fills the street evenly and the tower sits in gentle haze. Edo-period architecture only: every noren and sign is plain cloth with no characters, and there are no modern wires.

#### 170. `castle-keep` — Japanese Castle

> A Japanese castle keep in the late afternoon, photographed across its moat. Still moat water and a stone embankment in the near ground, massive curving stone ramparts rising from the water, and the white plaster keep stacked in tiers above with dark wooden gables and upturned roofs at every level, old pines leaning over the moat. White plaster, dark timber, grey stone and deep green. Soft low sun lights the white walls warmly without glare, and the sky is hazy and mid-toned. No tourists or modern fittings.

#### 171. `samurai-residence` — Samurai Residence

> The inside of a samurai's house in old Japan on a rainy afternoon, empty. Dark polished floorboards at the edge of the tatami in the near ground, a tatami room under dark beams, a suit of samurai armour on its stand in one corner, a rack of two swords in the alcove beneath a hanging scroll, and shoji screens slid open onto a veranda and a raked gravel garden in the rain. Dark timber, straw tatami, lacquered armour and grey rain light. Soft grey daylight from the garden side spreads evenly into the room, with the open shoji to one side. The scroll shows abstract ink only, no characters.

#### 172. `tea-ceremony-room` — Tea Ceremony Room

> A tiny Japanese tea-ceremony room, empty, photographed from the host's place. An iron kettle steaming over a sunken hearth and a tea bowl with a bamboo whisk in the near ground, four and a half tatami mats, rough earthen clay walls, a small alcove holding a single flower in a vase and a plain hanging scroll, and a low crawl-through door with light through its paper. Straw, earth brown, charcoal and soft paper light. Diffused light through paper windows fills the tiny room evenly, with no dark corner and no bright window. The scroll carries no characters.

#### 173. `post-town-inn` — Post Town Inn

> A post town on an old Japanese highway at dusk, photographed down its stone-paved road. Worn flagstones and a wooden bench with a pair of straw sandals in the near ground, wooden two-storey inns lining both sides with lanterns lit under the eaves and straw travellers' hats hung by the entrances, and the road running on between tall cedars into dark mountains. Dark timber, lantern amber and cool blue dusk. The lanterns and lit paper windows spread warm light along the whole street and the dusk sky still holds light, so nothing is black. Lanterns and signs carry no characters.

### Xianxia

#### 174. `cloud-sea-peaks` — Cloud-Sea Peaks

> Sheer granite peaks rising out of a sea of cloud at sunrise, photographed from a ledge. A twisted pine clinging to rock in the near ground, jagged granite pinnacles rising out of a white rolling cloud sea in the middle distance, and on the highest summit a small pavilion with upturned eaves, a pair of cranes flying far off between the peaks. Warm granite, deep pine green, pearl-white cloud and pale gold light. Soft sunrise light from the side warms the rock and the tops of the clouds; the sun is off-frame and the sky above is gentle. No railings, cable cars or modern paths.

#### 175. `sect-hall` — Sect Hall  **[PERIOD SET]**

> The great hall of a martial arts sect on a mountaintop in early morning, empty. A wide stone training ground with a weapons rack in the near ground, a flight of steps up to a hall of dark timber and grey tiles with sweeping upturned eaves and a large hanging plaque over the doors, bronze censers smoking on either side, and mountains fading into mist behind. Dark timber, grey stone, bronze and pearl mist. Soft even morning light and the mist fill the scene with gentle depth and no bright sky. The plaque is a blank lacquered board with no characters.

#### 176. `cultivation-cave` — Cultivation Cave

> A hermit's meditation cave high in the Chinese mountains, photographed from inside. A smooth stone platform with a cushion in the near ground, a few scrolls and an oil lamp on a rock ledge, a trickle of spring water falling into a small rock pool, and the wide cave mouth opening onto mist and distant peaks. Pale grey stone, moss green, lamp amber and soft white mist. Soft daylight through the mist and the lamp's glow fill the cave evenly; the mouth is to one side and hazy rather than bright.

### Rome

#### 177. `roman-forum` — Roman Forum  **[PERIOD SET]**

> The forum of ancient Rome in its glory, intact and empty on a hot afternoon. Worn paving stones and the base of a bronze statue on a tall pedestal in the near ground, marble temples and colonnades framing a long paved square, a triumphal arch, and steps rising to a basilica, with painted details on the stone. Warm marble, travertine gold, bronze green and a hazy blue sky. Warm afternoon light rakes across the columns and the colonnades cast long shade over part of the square, with the sun off-frame. No ruins.

#### 178. `villa-atrium` — Roman Villa Atrium  **[PERIOD SET]**

> The atrium of a wealthy Roman villa in the afternoon, empty. A mosaic floor and the edge of a shallow rectangular pool open to the sky in the near ground, walls painted deep red and ochre with frescoes of gardens and birds, columns and doorways leading to further rooms, and a green garden court glimpsed beyond. Pompeian red, ochre, mosaic cream and soft green. Daylight falls through the opening in the roof onto the pool and spreads across the floor and walls; that opening's brightness sits at the top edge, not at centre.

#### 179. `amphitheatre` — Amphitheatre  **[PERIOD SET]**

> The arena of a great Roman amphitheatre, intact and empty, photographed from the arena floor. Raked sand in the near ground, the arena wall with barred gates, tier upon tier of stone seating rising all round in rows of arches, and coloured awnings stretched over the upper rim. Warm travertine, sand gold, awning red and a hazy sky. The awnings shade part of the seating so the bowl reads in soft light and shade, and the sky is a small hazy oval at the top. No ruins.

### Medieval Europe

#### 180. `castle-courtyard` — Castle Courtyard

> The inner courtyard of a medieval castle on a cold morning, empty. Worn cobbles and a stone well in the near ground, high curtain walls and towers of grey stone on every side, a smithy lean-to against one wall with a faint glow, wooden stairs up to the keep door, and a gatehouse with its portcullis raised. Cold grey stone, dark timber, muted banner colours and a pale sky. Soft overcast light fills the courtyard evenly and the sky is a pale square above the walls. Banners are plain fields of colour with no heraldic lettering.

#### 181. `great-hall-feast` — Great Hall Feast  **[PERIOD SET]**

> The great hall of a medieval castle laid for a feast, empty of people. The end of a long trestle table laden with roasts, bread, candles and goblets in the near ground, more tables stretching down the hall, a high table on a dais under hanging heraldic banners and tapestries, a fire roaring in a huge stone fireplace in the side wall, and a minstrels' gallery above. Candle gold, firelight orange, rich tapestry reds and stone grey. Hundreds of candles and the fire spread warm light down the whole hall and up the walls, with the fire to one side.

#### 182. `blacksmith-forge` — Blacksmith's Forge

> A village blacksmith's forge, empty, photographed from inside. An anvil on a tree stump with a hammer resting on it in the near ground, a stone forge hearth under a hood with coals glowing orange, tongs and hammers hanging from the beams, a quenching trough, and an open door with grey daylight beyond. Coal orange, iron black, smoky brown and cool daylight. The forge glow and the daylight from the door together light the smoky room so the tools and walls read; sparks are small accents and the hearth sits to one side.

### The imagined

#### 183. `space-station-corridor` — Space Station Corridor  **[FANTASTIC]**

> A curving corridor aboard an orbiting space station. Handrails and a closed hatch in the near ground, white wall panels lit softly from within curving away ahead, cable runs and small equipment lights, and a wide viewport along one side showing the curve of a blue planet with thin cloud below and black space above. White, soft blue, planet blue and graphite. The corridor's own panel lighting fills the space evenly; the planet is mid-toned and to the side, not a bright field. No text or logos.

#### 184. `alien-landscape` — Alien World  **[FANTASTIC]**

> The surface of an alien planet, staged as a film would stage it on a vast real location. Strange ridged rock and pale sand in the near ground, a plain stretching to towering mineral spires in the middle distance, two large moons low on the horizon, and a violet-and-amber sky. Violet, dusty rose, pale sand and deep indigo. Soft diffuse light from a hazy sky lights the whole plain evenly, and the moons are soft rather than glowing hotspots. No spacecraft.

#### 185. `magic-academy-hall` — Academy of Magic  **[FANTASTIC]**

> The dining hall of an old academy of magic in a mountain fortress, empty. The end of a long wooden table with stacked spellbooks and a pewter jug in the near ground, long tables receding under a high vaulted stone ceiling, tall arched windows full of evening light, and iron lanterns burning with a cold blue flame along the walls. Warm stone, dark oak, dusk gold and cold blue flame. Evening light from the windows and the lanterns spread light down the whole hall, with the windows to the sides. No crests, logos or legible titles; nothing that belongs to a particular book or film.

#### 186. `dragon-lair` — Dragon's Lair  **[FANTASTIC]**

> A vast cavern deep under a mountain. Gold coins, goblets and old armour spilling across the rock floor in the near ground, great heaps of treasure rising in the midground, the coils and folded wing of a sleeping dragon half seen in shadow beyond, and a thin shaft of daylight falling from a crack far above. Gold, bronze, dark scaled green and smoky grey. The shaft of light and the gold's reflected glow light the cavern in warm layers so it reads rather than going black, and the shaft falls to one side.

### Modern cities beyond East Asia and the West

#### 187. `lagos-market` — Lagos Market

> A vast open-air market in Lagos in the early morning before trading starts, empty of people. A stall with heaped red peppers and baskets in the near ground, narrow lanes between stalls under coloured umbrellas and patched tin roofs stretching away, bolts of bright patterned fabric hung on display, and yellow minibuses parked at the edge. Pepper red, fabric colours, tin grey and warm dusty light. Soft morning haze fills the lanes evenly and the umbrellas shade the foreground so nothing glares. No legible signs.

#### 188. `mexico-city-street` — Mexico City Street

> A street in the historic centre of Mexico City on a spring afternoon, empty. Cobbles and a taco stand under a striped awning in the near ground, colonial buildings painted ochre, pink and blue with iron balconies on both sides, jacaranda trees in purple flower, and the dome of a church at the end of the street. Ochre, rose, cobalt, jacaranda purple and warm stone. Soft afternoon light fills the street, and the jacaranda canopy and balconies shade parts of the frame so the sky stays a small band at the top. No legible signs.

#### 189. `istanbul-ferry` — Bosphorus Ferry

> The deck of a ferry crossing the Bosphorus on a grey afternoon, empty. The ferry's wooden rail with a small tulip-shaped tea glass on it in the near ground, a few gulls small in the distance over the wake, the domes and minarets of the old city on the far shore to one side, and wooden waterfront mansions along the other shore. Grey-blue water, tea amber, white gulls and soft stone. Overcast light spreads evenly over the water and the shores, and the sky is soft grey rather than bright.

#### 190. `cairo-rooftops` — Cairo Rooftops

> The rooftops of old Cairo at sunset, photographed from one roof. A flat rooftop with a pigeon coop, a water tank and satellite dishes in the near ground, a jumble of flat roofs, laundry lines and minarets stretching away, and the hazy outline of the pyramids on the horizon. Dusty gold, rose, sand and soft violet haze. The sunset light is warm and diffused by dust across the whole city, with the sun off-frame. No legible signs.

#### 191. `marrakech-riad` — Moroccan Riad

> The courtyard of a Moroccan riad in the late afternoon, empty. A zellige-tiled floor and cushions around a low brass table with a tea glass in the near ground, a tiled fountain left of centre surrounded by potted orange trees, carved plaster arches and painted cedar doors on every side, a gallery above, and a square of blue sky over it all. Terracotta, zellige green and blue, carved cream plaster and orange. Soft reflected daylight fills the courtyard evenly, and the square of sky sits at the top without glaring.

### An English great house

#### 192. `country-house-drawing-room` — Country House Drawing Room

> The drawing room of an English country house in the afternoon, empty. A tea tray with a silver pot and china cups on a low table in the near ground, sofas and armchairs grouped around a marble fireplace, landscapes in gilt frames on the walls, a piano to one side, and tall windows looking out onto a lawn and parkland. Soft green, cream, gilt and warm wood. Daylight from the tall windows spreads across the room; the windows sit to one side so the centre stays mid-toned.


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

For a staged wave, merge before measuring, because `prepare-images.py` records its measurements
only for scenes already in the manifest:

    ./merge-staged.py 1 <folder-of-generated-images>    # moves the scenes that have art
    ./prepare-images.py <folder-of-generated-images>

A scene whose image did not come back stays in `staged/` and is not published.

## If you add more scenes later

The description in `manifest.json` — not the prompt — is what gets matched against the book text.
They serve different jobs: the **prompt** is visual vocabulary for the image model, the
**description** is novel vocabulary for the embedder. Write the description the way the book would
describe the place, and see `README.md` for why near-duplicate descriptions actively hurt.
