# Scene generation prompts

One prompt per scene in `manifest.json` — **100 scenes**, all in a single style. The
filename is the only link between an image and its manifest entry, so getting it exactly
right is all the matching needs. Four scenes are marked **[FANTASTIC]**; everything else
depicts somewhere that really exists.

**Handing this to an image agent?** Give it `IMAGE-AGENT-BRIEF.md` first, then the scene list
below. The brief carries the rules that matter most — the single cinematic look, sharp
masters, brightness, no people, no legible text, and the filename convention.

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
