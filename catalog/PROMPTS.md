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

- **Portrait, as tall as the generator offers.** The image is centre-cropped to fill the screen,
  so the taller the source the less of its width is thrown away: 2:3 loses about a third of the
  width on a typical phone, 3:4 rather more, and a landscape source loses its edges entirely.
  Both batches so far came out 3:4 (896×1200 and 3584×4800), which is fine; prefer 2:3 if you
  can get it.
- **Resolution barely matters, so do not fight for it.** `prepare-images.py` downscales to
  1600px on the short edge and never upscales, and the app blurs the result at 5dp behind the
  text. A 896px master is visually indistinguishable from a 3584px one by the time a reader sees
  it — it just encodes smaller. Take whatever the generator gives.
- Encode is **WebP q82**, which lands between 16 KB and 280 KB depending on how busy the scene is.
- Keep the **style suffix identical** across every scene. Switching backgrounds mid-chapter should feel
  like a change of place, not a change of medium.

### Style suffix A (painterly) — for historical and fantastic scenes

> atmospheric digital matte painting, painterly brushwork, soft diffused light, muted
> desaturated palette, cinematic depth of field, clear foreground midground and background
> separation, no people, no text, no watermark, no logo, no borders

Painterly rather than photoreal is deliberate: blurred photographs tend to read as *out-of-focus
photos* (i.e. a mistake), whereas a painting blurs into pleasing fields of colour.

### Negative prompt for suffix A

> people, human figures, faces, hands, text, letters, signage, watermark, logo, signature, frame,
> border, harsh centred highlight, blown-out highlights, high-frequency noise, busy clutter,
> lens flare, tilt-shift, fisheye

### Style suffix B (photoreal) — for contemporary scenes

> cinematic photograph, natural available light, 35mm, shallow depth of field, muted colour
> grade, fine film grain, clear foreground midground and background separation, no people,
> no legible text, no watermark, no logo, no borders

### Negative prompt for suffix B

> people, human figures, faces, hands, legible text, readable signage, kanji, hanzi, hangul,
> latin lettering, brand logos, shop names, license plates, watermark, signature, frame, border,
> harsh centred highlight, blown-out highlights, HDR halos, oversharpening, heavy vignette,
> lens flare, tilt-shift, fisheye

### Why two tracks

The first sixty scenes are all painterly, which made the whole catalog read as period drama even
where the subject was modern — look at `roadside-diner-night`. Contemporary scenes now use
suffix B instead. Every scene below is tagged **PAINT** or **PHOTO**; use the matching suffix and
negative prompt, and do not mix them within one image.

Mixing mediums across a catalog would normally be a mistake. Two things make it safe here. Scenes
are chosen by what the book says, so a contemporary novel stays among PHOTO scenes and a Victorian
one stays among PAINT scenes — switching tracks mid-book is rare. And every scene is blurred at
5dp under a dark overlay before anyone sees it, which flattens most of the difference between a
photograph and a painting anyway.

**What actually happened in batch three.** Suffix B did not take. The generator applied its own
painterly house style to the PHOTO scenes regardless of the photograph wording — compare
`motel-room-night` or `airport-gate-late` against any PAINT scene and the medium is the same. The
modern *subjects* arrived, which was the point, but not the photoreal rendering. Two consequences:
the medium-clash risk the tracks were designed around never materialised and the catalog still
reads as one medium, and if photoreal contemporary scenes are genuinely wanted they will need a
different image tool rather than a different prompt. The signage instruction, by contrast, worked
exactly as intended.

**Signage is the main failure mode for PHOTO scenes.** Image models produce garbled lettering, and
these settings are full of shopfronts. Every PHOTO prompt below already asks for signs as
unreadable colour; keep that, and weight the negative prompt heavily. A sign that is legibly
nonsense is worse than no sign.

---

## The first ten scenes

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

---

## The next fifty scenes

Same settings, same style suffix, same negative prompt as the ten above. Grouped only for
reading convenience — the groups mean nothing to the app.

### Wilderness and open country

#### 11. `bamboo-grove-mist` — Bamboo Grove in Mist

> A dense grove of towering green bamboo in early morning mist, seen from a narrow earth path running between the stems. Slender vertical culms with crisp leaf detail in the near field, ranks of paler stems receding into fog behind them, moss and fallen leaves on the path. Jade, sage and cool grey-green with no warm accent. Strong vertical rhythm throughout; light filters down evenly from above rather than forming a bright patch, and the upper middle stays open and hazy.

#### 12. `autumn-birch-forest` — Autumn Birch Forest

> A stand of slender white-barked birches in late autumn, low sun raking through the trunks from one side. Crisp peeling bark in the near trunks, a deep drift of gold leaf litter underfoot, further trunks dissolving into warm haze. Cream bark, amber and ochre canopy, dull violet shadow between the trees. Vertical trunks carry the frame; the sun stays off-frame so the light is a warm wash rather than a disc.

#### 13. `mangrove-swamp-dusk` — Mangrove Swamp at Dusk

> Brackish still water threading between tangled arching mangrove roots at dusk. Wet knotted root arches with bark detail in the near field, black water holding broken reflections, dense dark foliage closing overhead and a dull orange sky glimpsed only through small gaps. Murky olive, silt brown and tarnished orange. Intricate root shapes across the midground, the water plane in the lower third kept simple and dark, no open horizon.

#### 14. `red-rock-canyon` — Red Rock Canyon

> A deep sandstone canyon in late afternoon light, seen from partway down one wall. Layered red and ochre strata with sharp erosion detail on the near cliff, the opposite wall softened by dust haze, a thin green river far below in shadow. Rust, terracotta, dusty violet shadow and a narrow band of warm lit rock high up. Weight in the cliff faces at both sides; the sunlit band sits high, leaving the central depth open and hazy.

#### 15. `limestone-cavern-pool` — Limestone Cavern

> A vast underground limestone chamber with a still reflecting pool, lit only by indirect daylight entering from an unseen opening. Ribbed flowstone and hanging stalactites above, stalagmites rising from the near shore, the pool perfectly still and doubling the roof. Bone white, wet grey and cold blue-green. The reflection splits the frame horizontally; the light source stays out of shot so illumination is soft and unfocused, with no bright spot in the centre.

#### 16. `volcanic-badlands` — Volcanic Badlands

> A blasted plain of black basalt and cracked lava crust under a heavy overcast sky. Coarse clinker texture and sulphur-yellow mineral staining in the foreground, steam venting from fissures in the middle distance, a dull red glow deep in distant cracks, bare cinder cones on the horizon. Charcoal, ash grey, acid yellow and a restrained ember red. Detail concentrated in the ground plane; the sky kept dim, flat and low in contrast.

#### 17. `aurora-over-tundra` — Aurora Over Tundra

> Curtains of green and violet aurora rippling across a black star-scattered sky above an endless flat snow plain. Faint wind-carved sastrugi catching the light in the near snow, the plain running unbroken to a low horizon, no structures or vegetation anywhere. Deep indigo, luminous green and faint magenta over blue-white snow. Light concentrated in the upper frame as soft vertical curtains; the ground dark, simple and uncluttered.

#### 18. `salt-flat-mirror` — Salt Flat

> An endless white salt pan under a wide pale sky, a thin film of standing water turning the whole plain into a mirror. Faint polygonal salt crust visible at the very near edge, everything beyond it a flawless reflection, the horizon almost impossible to locate. Bone white, pale blue and soft lilac, almost no saturation. Extremely low contrast with the horizon near the middle; no focal object anywhere, the whole frame calm and open.

#### 19. `highland-moor-fog` — Highland Moor

> Rolling heather moorland swallowed in thick fog. Wet dark peat and clumped heather with real texture in the near ground, a fragment of collapsed drystone wall half-seen in the middle distance, everything beyond it lost, no horizon at all. Muted purple-brown, grey and dull sage. Contrast very low and evenly spread, softening steadily with distance; nothing sharp past the near ground and no light source visible.

#### 20. `jungle-waterfall-basin` — Jungle Waterfall

> A tall waterfall dropping into a jade-green pool enclosed by dense rainforest. Wet black rock and broad glossy leaves in the near field, mist and spray hanging in visible shafts of light, the falls offset to one side, canopy closing over the top of the frame. Saturated deep greens with white falling water against dark rock. The canopy frames the upper edge; the white water is kept to a narrow vertical band rather than a broad bright mass.

#### 21. `olive-grove-terraces` — Olive Grove

> Gnarled ancient olive trees with silver-green foliage on dry stone terraces above a hazy valley, hot late afternoon. Deeply furrowed trunks and loose terrace stone in the near ground, parched grass and thistle between them, the valley below flattened by heat haze. Dusty olive, straw, warm limestone and bleached blue. Terrace lines lead back diagonally; the sky is held to a small hazy strip at the top with no bright sun.

#### 22. `reed-marsh-dawn` — Reed Marsh at Dawn

> Flat shallow water and tall pale reeds at first light, low mist lying across the surface. Reed stems and seed heads silhouetted in the near field, mist thickening between the further stands, a narrow band of soft rose light at a very low horizon. Muted straw, grey-blue and faint pink. Reeds provide vertical texture at the sides; the water plane stays dark and calm and the bright band is kept thin and low.

#### 23. `frozen-lake-bare-trees` — Frozen Lake

> A wide frozen lake under flat overcast light, seen from out on the ice. Pressure cracks radiating through pale ice with a thin dusting of snow in the near field, bare black winter trees crowding the far shore as a dark band, low grey cloud above. Cold grey-blue, bone white and charcoal. A strong horizontal ice plane fills the lower two thirds; the treeline is a quiet dark stripe and the sky is even and featureless.

#### 24. `stone-circle-dawn` — Standing Stones

> A ring of weathered lichen-crusted standing stones on open grassland at dawn, several of them leaning. Pitted stone surfaces and long shadows raking across cropped turf in the near ground, low mist pooling between the further stones, a wide empty sky. Grey stone, dun grass, pale gold light and blue shadow. Stones spaced across the midground with gaps between them; the sun stays off-frame so shadows do the work and the sky stays restrained.

#### 25. `cliff-path-seabirds` — Cliff Path

> A narrow grass path along the crest of high sea cliffs under broken cloud. Wind-flattened turf and crumbling cliff edge in the near ground, seabirds wheeling small against the drop, white surf far below at the base of the rock, headlands receding into haze. Grey-green turf, slate rock and cold blue-grey sea. The cliff edge cuts diagonally across the frame; the sea is kept mid-toned and even so the foam does not glare.

#### 26. `becalmed-ship-doldrums` — Becalmed Ship

> A tall sailing ship lying motionless on a dead flat sea under a blank white-hot sky, sails hanging slack from the yards. Glassy oily water holding a soft inverted reflection in the near field, the ship seen broadside at middle distance, the horizon dissolved in haze with no cloud at all. Bleached bone, pale gold and washed-out blue-grey, very nearly colourless. Extremely low contrast; the ship small and offset, the water plane vast, still and untextured.

### Rural and coastal settlement

#### 27. `fishing-village-quay` — Northern Fishing Village

> A small northern fishing village of painted timber houses stacked above a stone quay, overcast. Wet granite quay, coiled rope, stacked lobster pots and drying nets in the near ground, small boats at moorings in grey swell, houses rising behind, bare hills beyond. Muted oxblood, ochre and white against slate water. Houses bank up one side with harbour water opposite; flat even light and no bright reflection on the water.

#### 28. `lighthouse-headland` — Lighthouse on the Headland

> A white stone lighthouse on a bare rocky headland at dusk, its beam sweeping out through rain. Wet dark rock and salt-burnt grass in the near ground, heavy sea breaking white at the base, low ragged cloud dragging behind the tower. Slate grey, cold blue and a single warm lantern glow. The tower is offset and not tall in frame; the beam angles away from the viewer and stays soft, never a hard flare.

#### 29. `wheat-field-harvest` — Wheat Field at Harvest

> A wide field of ripe wheat bending under the wind in warm late afternoon light. Individual heads and stalks sharp in the near ground, the crop smoothing into a moving gold plane further back, a small weathered timber barn on the horizon, high thin cloud above. Straw gold, dry green, warm amber and soft blue. Wheat texture fills the lower two thirds; the barn is small and off-centre and the sky stays pale and untroubled.

#### 30. `vineyard-autumn` — Vineyard in Autumn

> Rows of vines turned red and gold on a hillside after harvest, early morning. Gnarled vine stocks, wire and stony soil in the near rows, mist pooled along the valley floor below, a stone farm building half-lost in it. Burgundy, amber, olive and soft grey mist. Vine rows converge steeply into the distance; the mist band flattens the middle of the frame and the light stays diffuse with no visible sun.

#### 31. `water-mill-stream` — Water Mill

> An old stone water mill beside a fast shallow stream, dappled light through overhanging trees. Moss-furred wet stonework and a dark timber wheel mid-turn at one side, water breaking white over rocks in the near ground, the mill's small windows dark, trees closing in behind. Wet grey stone, moss green, dark timber and scattered light. The wheel is offset; the dappling is kept small and broken rather than one bright patch, the upper frame leafy and dim.

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

> A narrow alley of wet cobbles between high stone walls at night, one iron bracket lamp burning. Slick cobbles holding a broken reflection in the near ground, damp render and shuttered doorways along both walls, washing lines strung overhead, the far end lost in dark. Deep brown-black with a single pool of warm amber. Strong one-point perspective down the alley; the lamp is small, high and off-centre, and most of the frame is unlit.

#### 38. `city-rooftops-dusk` — City Rooftops

> A sea of tiled rooftops and clustered chimney pots at dusk, seen from roof level. Wet slate and lead flashing on the near roofs, thin smoke rising straight, rooflines stepping away into soot haze, a distant church spire against a fading sky. Slate blue-grey, soot brown and a narrow warm dusk band. Roof geometry fills the lower two thirds and recedes; the sky is a low strip and the streets are never visible.

#### 39. `grand-railway-station` — Grand Railway Station

> A vast Victorian iron-and-glass railway train shed, steam drifting under the vaulted roof. Empty platform edge and polished rails in the near ground, cast-iron columns and riveted arched ribs rising, a large clock high on the end wall, grimy glass panels diffusing daylight above. Sooty iron, pale glass light, brass and warm brick. The vault arch frames the image; light comes from overhead heavily diffused by steam, with no window blowing out.

#### 40. `textile-mill-floor` — Textile Mill

> A long industrial mill floor lined with cast-iron looms and overhead belt shafting. Oil-stained floorboards and machine detail in the near ground, rows of looms receding, lint and dust hanging in shafts falling from high windows along one side, leather belts running up to a turning shaft. Iron grey, oiled brown, brass and pale dusty light. Machines recede in strong perspective; the windows sit high and small so light enters at an angle.

#### 41. `dockside-warehouses-fog` — Dockside Warehouses

> Tall brick dockside warehouses along a black river in heavy fog at night. Wet cobbles, mooring bollards and stacked crates on the near wharf, timber loading cranes projecting overhead, warehouse windows blank, a single lamp haloed in the murk. Brick red muted almost to grey-brown, fog white and oily black water. The warehouse wall runs down one side with the river opposite; the lamp is small and diffused and everything else is low in contrast.

#### 42. `metro-platform-late` — Late Metro Platform

> An empty modern underground metro platform late at night. Scuffed concrete and a yellow safety line in the near ground, white tiled walls, fluorescent strips running the length of the ceiling, the tunnel mouth black at the far end, a single bench. Clinical white, tile grey, cold green-tinged light and a dark tunnel void. Perspective runs down the platform; lighting is flat and even with no hot spot, and the tunnel is a quiet dark anchor.

#### 43. `covered-bazaar-lanterns` — Covered Bazaar

> A vaulted covered bazaar hung with pierced brass lanterns and patterned carpets. Open sacks of coloured spice and stacked brass ware in the near ground, carpets draped from a rail overhead, the aisle running back beneath a brick vault, dusty shafts dropping through small high openings. Saffron, crimson, indigo, brass and deep shadow. Warm lamps read as many small points rather than one bright source; the vault above stays dim.

#### 44. `tenement-courtyard` — Tenement Courtyard

> A narrow courtyard enclosed on all sides by tall shabby tenement blocks. Damp cracked render, a standpipe and worn paving in the near ground, washing strung on lines across the gap, rusted balconies and irregular windows rising, a small square of pale sky far above. Grey render, faded laundry colour and cool shadow. Walls rise steeply on every side; the only light comes straight down, leaving the lower frame in even shade.

#### 45. `roadside-diner-night` — Roadside Diner

> A lone chrome-and-glass roadside diner glowing at night beside an empty two-lane highway, seen from across the lot. Cracked asphalt and faded parking lines in the near ground, the diner's lit windows and a tall neon sign at middle distance, dark scrub and telephone poles running away into black behind. Deep night blue, warm interior amber and restrained neon red. The building sits low and off-centre, the windows glow steadily rather than blowing out, and the sky above is empty and dark.

### Interiors

#### 46. `cathedral-nave` — Cathedral Nave

> The nave of a gothic cathedral, empty and still. Worn flagstones and a column base in the near ground, immense clustered piers rising into shadow, ribbed vaulting barely visible above, stained glass casting scattered coloured pools across the floor. Cool grey stone, deep shadow and small jewelled reds and blues. Columns frame both sides; the colour pools are kept small and low and the upper frame stays dark and open.

#### 47. `panelled-courtroom` — Courtroom

> An empty oak-panelled courtroom with still dusty air. Worn benches and a polished wooden rail in the near ground, the raised judge's bench and its canopy at the far end, a clerk's table below, tall sash windows with net curtains along one wall. Warm oak brown, brass, green leather and pale window light. The bench sits off-centre at the back; window light is heavily diffused by the nets so no pane glares.

#### 48. `hospital-ward-night` — Hospital Ward at Night

> A long old-fashioned hospital ward at night. Iron bedsteads with tight white linen receding in two rows, a bare polished floor between them, tall dark windows down one side, a single shaded lamp burning at a desk at the far end. Cold white linen, deep blue-grey shadow and one small warm lamp. The bed rows converge strongly; the lamp is distant and small and most of the frame stays quiet and dim.

#### 49. `empty-theatre-stalls` — Empty Theatre

> An empty theatre auditorium seen from the back of the stalls, house lights very low. Rows of red velvet seats curving away in the near ground, gilt-fronted boxes stacked along both walls, ornate plasterwork and an unlit chandelier above, the stage curtain lowered. Deep crimson, tarnished gold and heavy shadow. Seat rows sweep across the lower frame; the stage stays dim so nothing draws the eye to a bright centre.

#### 50. `farmhouse-kitchen-hearth` — Farmhouse Kitchen

> A rustic farmhouse kitchen with a fire burning low in a cast-iron range. A scrubbed wooden table with crockery in the near ground, herbs and copper pans hanging from low beams, flagstone floor, the range glowing to one side, a small deep-set window admitting grey daylight. Warm amber firelight, dark timber, stone grey and copper. The fire glow sits low and to one side; the rest of the room is lit softly and never blows out.

#### 51. `dusty-attic-trunks` — Attic

> A cluttered attic beneath bare timber rafters. Old leather-bound trunks, a sheeted chair and stacked crates in the near ground, cobwebs strung between rafters, floorboards thick with dust, a single grimy dormer window admitting one angled shaft. Dust brown, faded sheet white, grey timber and pale cold light. The shaft enters from one side and stays narrow and soft; the rest of the space falls away into dim clutter.

#### 52. `wine-cellar-vaults` — Wine Cellar

> A brick barrel-vaulted wine cellar, cool and windowless. Dusty racked bottles and a large oak cask in the near ground, a lantern standing on a barrel head, damp brick vaults receding in a row, the far arches lost in dark. Deep brick red, bottle green, oak brown and warm lantern amber. Arches recede in a repeating rhythm; the lantern pools light only in the near ground, leaving the depth unlit.

#### 53. `throne-room-banners` — Throne Room

> A long stone hall hung with heraldic banners. A worn flagstone floor running the length of the frame, tall narrow windows down both walls throwing angled bars of light, iron braziers between them, a raised dais with a carved stone throne at the far end. Cold grey stone, heraldic crimson and gold, warm brazier glow. Strong perspective to the dais; the light bars are narrow and repeated rather than one broad wash.

#### 54. `stone-prison-cell` — Prison Cell

> A bare stone prison cell. Damp scarred masonry and scattered straw in the near ground, scratched tally marks cut into one wall, a heavy iron-bound door in shadow, a small barred slit high in the opposite wall admitting a single pale shaft. Cold grey stone, dull straw and one thin cold shaft. The shaft falls off-centre and lands low on the wall; the great majority of the frame stays dark and simple.

#### 55. `victorian-laboratory` — Victorian Laboratory

> A cluttered Victorian private laboratory at night. Dark wood benches crowded with brass instruments, retorts and glass tubing in the near ground, a low gas flame under a bubbling flask, shelves of murky specimen jars behind, charts pinned to the panelling. Brass, bottle-green glass, deep mahogany and a small warm flame. Apparatus fills the midground; the flame is the only bright point and it is kept small and off-centre.

#### 56. `glasshouse-conservatory` — Glasshouse

> A Victorian iron-framed glasshouse crowded with palms and ferns. Wet tiled path and broad leaves crowding both sides in the near ground, condensation running down the panes, white-painted iron ribs arching overhead, further foliage dissolving into green haze. Wet green, white iron, terracotta and pale diffused light. Ironwork arches across the top of the frame; light comes through misted glass so it is soft and completely even.

### Fantastic and speculative

#### 57. `wizards-workroom` — Wizard's Workroom

> A cramped tower workroom lit by a pale floating arcane glow rather than fire. A brass orrery and open bound tomes on a cluttered near table, chalked sigils across bare floorboards, shelves of murky specimen jars and hanging dried bundles behind, a narrow arched window showing night. Cold blue-green glow against dark oak, brass and dull parchment. The glow is small, low and off-centre; the room falls away into shadowed clutter.

#### 58. `torchlit-dungeon` — Dungeon Corridor

> A low vaulted dungeon corridor of damp rough-cut stone. Worn flags and standing puddles in the near ground, heavy iron-bound doors set along one wall, guttering torches in brackets spaced too far apart, the corridor bending away into black. Black-brown stone, rust and small orange torch pools. The corridor recedes in strong perspective; torch pools are small, uneven and separated by long stretches of unlit wall.

#### 59. `airship-gondola-clouds` — Airship Gondola

> The interior of a riveted airship gondola above an endless floor of cloud. A brass-rimmed instrument panel and worn oxblood leather seating in the near ground, polished timber trim, a wide curved window running along one side onto pale sky and a cloud sea below, rigging lines visible outside. Brass, oxblood, warm timber and cloud white. The window sits to one side; the cloud light is bright but even, with no sun disc in frame.

#### 60. `overgrown-city-ruins` — Overgrown Ruins

> A ruined city street reclaimed by nature under soft overcast light. Cracked tarmac split by grass and saplings in the near ground, a rusted railing, vines swallowing concrete facades on both sides, empty window openings dark, young trees closing the street further back. Weathered concrete grey, rust and aggressive green. Facades frame both sides with greenery running up the middle; light is flat and diffuse with no sky gap glaring.

---

## The third fifty scenes

Weighted toward modern and non-Western settings, which the first sixty barely covered.
Each is tagged with the style track to use.

### Modern East Asian cities

#### 61. `tokyo-backstreet-night` — Tokyo Backstreet  **[PHOTO]**

> A narrow Tokyo backstreet after midnight, photographed at eye level. Wet asphalt holding smeared coloured reflections in the near ground, a lit vending machine and red paper lanterns outside a shuttered izakaya, tangled overhead cables, bicycles against a railing, the lane narrowing into darkness. Warm red and amber against cold blue-black night. Light comes from many small sources rather than one, and every sign is an unreadable coloured glow; the upper frame stays dark and cabled.

#### 62. `konbini-night` — Convenience Store at Night  **[PHOTO]**

> A Japanese convenience store glowing on a dark residential street, photographed from across the road. Damp pavement and a painted kerb in the near ground, the shopfront a flat wall of fluorescent white behind glass with stocked shelving visible, a parked bicycle, low dark buildings either side. Clinical white and pale green against near-black surroundings. The lit facade sits low and off-centre with all signage reduced to unreadable colour bands; the sky above is empty and black.

#### 63. `shinkansen-window-ricefields` — Bullet Train Window  **[PHOTO]**

> The interior window of a modern Japanese bullet train, photographed from the seat. A clean grey tray table and window frame sharp in the near field, beyond the glass flooded rice paddies and distant hills pulled into horizontal streaks by speed, an overcast sky. Muted grey interior against green and silver-water motion blur. The window fills one side; the blurred exterior stays soft and low in contrast with no bright sky patch.

#### 64. `japanese-apartment-small` — Small Tokyo Apartment  **[PHOTO]**

> A small single-room Japanese apartment photographed from the doorway in flat afternoon light. A low table and floor cushion on pale tatami in the near ground, a folded futon against one wall, a compact kitchenette, sliding glass doors onto a narrow balcony with hanging laundry beyond. Straw, off-white and grey with one muted colour accent. Balcony light enters from one side through net curtain; the room stays evenly lit and uncluttered.

#### 65. `shotengai-arcade` — Covered Shopping Street  **[PHOTO]**

> A covered Japanese shopping arcade photographed down its length in late afternoon. Tiled floor and a rolled-down steel shutter in the near ground, fabric banners and paper lanterns strung beneath a translucent vaulted roof, a few shops still lit further down, bicycles parked along one side. Faded red, cream and green under milky skylight. Strong perspective down the arcade; roof light is even and diffused with no hot spot, and all lettering is illegible.

#### 66. `hongkong-highrise-canyon` — Hong Kong High-Rises  **[PHOTO]**

> A narrow canyon between dense Hong Kong residential towers, photographed looking steeply upward. Weathered concrete and tiled facades rising on both sides, hundreds of air-conditioning units and bamboo drying poles hung with laundry projecting out, caged windows, a bright slot of overcast sky far above. Grey-green concrete, rust and faded laundry colour. Towers fill both sides; the sky slot is small and kept near the top so the mass of the frame stays mid-toned.

#### 67. `shanghai-bund-dusk` — Shanghai Riverfront  **[PHOTO]**

> The Shanghai riverfront at dusk photographed from the promenade. A stone balustrade and damp granite paving in the near ground, the dark river with a ferry wake crossing it, a skyline of lit glass towers on the far bank with haze softening their tops. Deep blue-grey water, warm tower light, smog-pink sky band. The skyline sits as a mid-frame band with dim sky above; tower lights read as many small points, none blown out.

#### 68. `shanghai-longtang-lane` — Shanghai Lane House  **[PHOTO]**

> A narrow Shanghai longtang lane between brick shikumen terraces, photographed down its length in soft morning light. Cracked concrete underfoot, a shared tap and stacked plastic stools in the near ground, bamboo poles of laundry projecting overhead across the lane, carved stone door frames, potted plants on the sills. Warm grey brick, faded laundry colour and muted green. Walls press in on both sides; the overhead laundry breaks the light into soft patches.

#### 69. `beijing-hutong-winter` — Beijing Hutong in Winter  **[PHOTO]**

> A Beijing hutong alley in winter, photographed at eye level under flat grey light. Frozen rutted ground and a parked bicycle in the near field, low grey brick courtyard walls running along both sides, a red-painted timber gate with faded paper couplets, bare trees showing above the roofline, cabbages stacked by a step. Cold grey brick, oxidised red and bare-branch brown. The low walls keep the frame horizontal and the pale sky is a thin strip above.

#### 70. `seoul-rooftop-night` — Seoul Rooftop  **[PHOTO]**

> A residential rooftop in Seoul at night, photographed across the parapet. Rough waterproofed decking, a steel water tank and satellite dishes in the near ground, a low parapet, then rank upon rank of lit apartment towers receding toward dark hills, small red neon crosses scattered among them. Cold blue-grey with warm window points and restrained red accents. The parapet anchors the lower frame; window lights read as fine texture rather than glare.

### Modern everyday and domestic

#### 71. `modern-kitchen-morning` — Kitchen in the Morning  **[PHOTO]**

> A contemporary kitchen photographed in soft early morning light. A stone worktop with a single mug and a folded cloth in the near ground, flat-fronted cabinets, a stainless hob and kettle, a window above the sink showing pale garden green. Cool white, pale timber and grey with one small warm accent. Light enters horizontally from the window and is diffused; surfaces stay matte with no specular glare.

#### 72. `bedroom-morning-light` — Bedroom, Morning  **[PHOTO]**

> A modern bedroom photographed in soft morning light with the bed unmade. Rumpled white linen filling the near ground, a wooden chair with draped clothing, a bedside table holding a glass of water, half-drawn linen curtains admitting diffused light from one side. Warm white, oatmeal and pale grey. Light falls across the bed from the side with soft edges; the window itself stays out of frame so nothing blows out.

#### 73. `living-room-tv-glow` — Living Room at Night  **[PHOTO]**

> A dark living room at night lit only by an off-frame television, photographed from behind the sofa. The sofa back and a cushion in the near ground, a low table with a mug and a remote, flickering cool light washing one wall and the ceiling edge, the rest of the room in deep shadow. Cold blue-white against near-black with one small warm lamp deep in the background. The screen stays out of shot so its light arrives indirectly and soft.

#### 74. `apartment-balcony-city` — Balcony Above the City  **[PHOTO]**

> A small apartment balcony at night photographed from just inside the sliding door. A metal railing and a single folding chair in the near ground, a potted plant, then the city spread below as a field of small warm window lights and street lamps with low cloud catching the glow. Deep blue-black with scattered amber points. Railing and chair anchor the lower frame; city lights stay fine and even with no bright sign among them.

#### 75. `coffee-shop-afternoon` — Café in the Afternoon  **[PHOTO]**

> The interior of a contemporary café photographed in mid-afternoon. A worn timber table with a cup, saucer and a closed laptop in the near ground, mismatched chairs, a tiled counter with an espresso machine and shelves of cups behind it, a large street window at one side admitting diffused daylight. Warm timber, matte black and cream. The counter sits in the midground; window light is soft and indirect and the frame is evenly lit.

#### 76. `supermarket-aisle-night` — Supermarket Aisle  **[PHOTO]**

> A supermarket aisle photographed down its length under hard fluorescent ceiling light, no shoppers. Polished vinyl floor reflecting the strip lights in the near ground, shelves stacked with plain unbranded packaging rising on both sides, a chilled cabinet glowing faintly at the far end. Cold white and pale green with desaturated packaging colour and no readable labels. Strong one-point perspective; lighting is flat and even throughout.

#### 77. `suburban-street-dusk` — Suburban Street  **[PHOTO]**

> A quiet suburban residential street photographed along the pavement at dusk. A kerb, a strip of mown grass and a parked car in the near ground, similar low houses with lit front windows receding on both sides, a street lamp just coming on, mature trees between them. Blue-grey dusk with small warm window rectangles. Perspective runs down the street; the sky is a dim strip and the window lights stay small and scattered.

#### 78. `motel-room-night` — Motel Room  **[PHOTO]**

> A cheap motel room at night photographed from the doorway. A patterned bedspread and a bedside table with a lamp in the near ground, a second bed beyond it, a dated wall unit and mirror, thin curtains with coloured neon glowing through from outside. Dull brown, mustard and a cold neon wash at the window. The neon arrives diffused through the curtain, the lamp is small and warm, and the ceiling stays dark.

#### 79. `night-highway-from-car` — Highway at Night  **[PHOTO]**

> A night highway photographed from the driver's viewpoint over a dim dashboard. The dashboard edge and a sliver of steering wheel dark in the near ground, wet asphalt and painted lane markings lit by headlights just ahead, reflective posts trailing away, small red tail lights in the distance, everything beyond swallowed black. Near-black with cold headlight white and small red points. Light falls only on the road surface; the upper two thirds stay dark.

#### 80. `airport-gate-late` — Departure Gate  **[PHOTO]**

> An airport departure gate late at night, photographed along the seating. Rows of empty moulded seats and carpet tile in the near ground, a bank of floor-to-ceiling glass, beyond it a dark apron with a parked aircraft and blue taxiway lights, ceiling downlights reflected softly in the glass. Cold grey and blue with small amber ground lights. Seats lead into the frame; the apron beyond stays dark and the reflections are gentle.

### Modern institutional and working

#### 81. `open-plan-office-night` — Office After Hours  **[PHOTO]**

> A large open-plan office photographed after hours with the main lights off. Rows of empty desks with dark monitors and task chairs receding, one desk lamp burning at the far side, floor-to-ceiling windows showing a lit city beyond, carpet tile underfoot. Cold grey and blue-black with one warm lamp and distant city points. Desk rows recede in perspective; the lamp is small and off-centre and the windows stay dim.

#### 82. `police-interview-room` — Interview Room  **[PHOTO]**

> A bare police interview room photographed from one corner under hard ceiling light. A scuffed table fixed to the floor in the near ground with a recording unit on it, two moulded chairs facing across it, acoustic wall panelling, a small high window of obscured glass, a door with a viewing panel. Institutional grey-green, beige and cold white. The table anchors the foreground; lighting is flat, even and almost shadowless.

#### 83. `hospital-corridor-modern` — Hospital Corridor  **[PHOTO]**

> A modern hospital corridor photographed down its length in the small hours. Polished vinyl flooring reflecting the overhead lights in the near ground, handrails along both walls, closed doors and a wall-mounted dispenser, a nurses' station lit further down, the corridor bending out of sight. Pale green, white and grey with one warmer lit station. Strong perspective; floor reflections are soft and the lighting is even with no hot spot.

#### 84. `server-room` — Server Room  **[PHOTO]**

> A data centre aisle photographed down its length. A perforated raised floor in the near ground, black equipment racks rising on both sides carrying hundreds of small green and amber indicators, bundled cabling overhead, a glass door at the far end. Near-black and cold blue with fine green-amber points. Racks recede in strong perspective; the indicators read as fine texture rather than glare and the aisle stays dark.

#### 85. `newsroom-evening` — Newsroom  **[PHOTO]**

> A working newsroom photographed across the desks in the evening. Cluttered desks with monitors, stacked paper and cold coffee in the near ground, a bank of muted wall screens showing indistinct footage, whiteboards covered in illegible scrawl, strip lighting overhead, glass-partitioned offices behind. Grey-blue with warm desk lamps and faint screen glow. Desks fill the foreground; screens are dim and their content unreadable.

#### 86. `container-yard-dawn` — Container Yard  **[PHOTO]**

> A shipping container yard photographed at first light. Wet concrete with painted markings in the near ground, stacks of weathered containers in rows three and four high, a gantry crane silhouetted behind them, floodlight masts still burning against a pale dawn sky. Rust red, faded blue and green against grey concrete. Container stacks form strong horizontal bands; floodlights are small and haloed and the sky stays pale and flat.

#### 87. `multistorey-carpark` — Parking Deck  **[PHOTO]**

> An almost empty multistorey car park deck photographed down the bays. Oil-stained concrete with faded painted bay lines in the near ground, squat columns marching away, two parked cars, sodium fittings on the low ceiling, open sides showing dark sky between the parapets. Concrete grey with spaced sodium amber pools. The low ceiling compresses the frame; light pools are uneven with long dim stretches between them.

#### 88. `indoor-pool-empty` — Empty Swimming Pool  **[PHOTO]**

> An empty indoor public swimming pool photographed from the poolside. Wet non-slip tiling and a lane rope reel in the near ground, perfectly still water holding rippled reflections with lane markings beneath, tiled walls and a high window band, a diving block at one end. Cold aqua, white tile and pale grey. Water fills the midground; reflected caustics play softly across wall and ceiling with no bright window in frame.

#### 89. `hotel-corridor` — Hotel Corridor  **[PHOTO]**

> A hotel corridor photographed down its length under low wall lighting. Patterned carpet running away in the near ground, identical numbered doors receding on both sides, wall sconces at regular intervals, a mirror and side table at the far end, a fire door part way along. Muted gold, burgundy and brown with warm pooled sconce light. Strong repeating perspective; the sconces make regular small pools and the far end falls into shadow.

#### 90. `university-lecture-hall` — Lecture Theatre  **[PHOTO]**

> An empty raked university lecture theatre photographed from the lowest tier looking up. A lectern and a long whiteboard carrying faint illegible writing in the near ground, tiered rows of fixed timber seats and desks rising steeply away, downlights over the aisles, acoustic panelling. Warm timber, grey-green upholstery and cold ceiling light. Seat tiers sweep upward filling the frame; lighting is even with no bright window.

### Traditional East Asia

#### 91. `japanese-temple-garden` — Temple Garden  **[PAINT]**

> A Japanese temple garden in soft overcast light. Deep green moss and a stone water basin in the near ground, raked gravel beyond it, clipped shrubs and the twisted trunks of old maples, a timber veranda with shoji screens running along one side. Moss green, wet grey stone and dark timber. The veranda edges one side of the frame; light is flat and diffuse with no sun patch and the detail sits low.

#### 92. `torii-path-forest` — Path of Torii Gates  **[PAINT]**

> A path of vermilion torii gates climbing through dense cedar forest. Worn stone steps in the near ground, the gates standing close enough to form a receding tunnel, their posts weathered, tall dark cedar trunks pressing in on both sides, green light filtering from far above. Saturated vermilion against deep green-black and grey stone. The gate tunnel drives strong repeating perspective; light enters only as soft patches from overhead.

#### 93. `ryokan-tatami-room` — Ryokan Room  **[PAINT]**

> A traditional ryokan tatami room in soft afternoon light. A low lacquered table with a tea set on pale tatami in the near ground, a folded cushion, a tokonoma alcove holding a hanging scroll and a single stem, shoji screens slid partly open onto green garden. Pale straw, off-white paper and dark timber framing. The shoji diffuse the light to an even glow and the garden beyond stays soft and unresolved.

#### 94. `onsen-town-snow` — Hot Spring Town  **[PAINT]**

> A Japanese hot spring town under heavy snow at dusk. A stone-lined river steaming in the near ground with snow banked along it, three-storey timber inns crowding both banks with lit paper lanterns and glowing windows, a small arched bridge, steep snowy hills behind. Warm lantern amber against blue snow shadow and dark timber. Steam softens the midground; lantern lights are many and small rather than one bright source.

#### 95. `suzhou-garden-moongate` — Scholar's Garden  **[PAINT]**

> A classical Chinese scholar's garden in soft light. A whitewashed wall with a circular moon gate in the near ground framing a further courtyard, weathered limestone rockery and a still pond with lotus pads to one side, a latticed pavilion window, banana leaf and bamboo. Whitewash, grey tile, pond green and dark timber. The moon gate frames a second depth; light is diffuse and the whitewashed wall is held to a soft mid-grey rather than bright.

#### 96. `siheyuan-courtyard` — Courtyard House  **[PAINT]**

> A traditional Chinese siheyuan courtyard in late afternoon. Grey flagstones and a large glazed water vat in the near ground, single-storey wings with timber lattice windows and faded red-painted doors enclosing all four sides, a bare jujube tree at the centre, grey tiled roofs against a pale sky. Grey brick and tile, oxidised red and dull green lattice. Roofs frame the top, the open sky is a modest square and the light stays flat.

#### 97. `rice-terraces-morning` — Rice Terraces  **[PAINT]**

> Flooded rice terraces stepping down a steep hillside at dawn. Curved mud bunds and shallow water holding a mirrored sky in the near terraces, the terraces repeating in nested curves down and away, mist lying along the valley, a small thatched shelter among them. Silver water, mud brown and new-shoot green under a pale sky. Terrace curves lead the eye down and back; the mirrored sky stays soft and mid-toned rather than bright.

#### 98. `tibetan-monastery-cliff` — Cliff Monastery  **[PAINT]**

> A Tibetan monastery built into a high cliff face under a deep blue sky. Rough stone steps and a line of weathered prayer flags strung across the near ground, whitewashed walls with dark trapezoid windows and crimson and ochre bands stacked up the rock, bare brown mountains beyond. Whitewash, deep crimson and ochre against brown rock and saturated blue. The buildings climb one side; the sky is deep and dark-toned rather than bright.

### South Asia and the Middle East

#### 99. `indian-street-monsoon` — Monsoon Street  **[PHOTO]**

> A crowded Indian city street in heavy monsoon rain, photographed at street level. Ankle-deep water running over broken tarmac in the near ground with rain rings across it, open shopfronts under tarpaulin awnings on both sides, an auto-rickshaw at the kerb, tangled overhead cables, grey sheeting rain flattening the distance. Saturated awning colour against grey rain and dark wet road, signage illegible. Rain softens everything past the near ground and no bright sky shows.

#### 100. `varanasi-ghats-dawn` — River Ghats  **[PAINT]**

> Wide stone ghat steps descending to a slow brown river at first light. Worn uneven steps and a moored wooden boat in the near ground, tiered palaces and shrines rising behind in faded ochre and rose, thin smoke drifting along the bank, mist dissolving the far shore. Ochre, rose, river brown and pale gold. Steps lead down and across the frame; the sun stays off-frame and the far bank fades to nothing.

#### 101. `stepwell-geometric` — Stepwell  **[PAINT]**

> A vast Indian stepwell seen from the upper edge looking down. Symmetrical flights of sandstone steps crossing and recrossing as they descend in tiers, deep shadow gathering between them, still dark green water at the bottom, carved pillared niches in the side walls. Warm sandstone ochre against deep shadow and black-green water. Repeating geometry fills the frame; sunlight catches only the upper tiers and the depths stay dark.

#### 102. `caravanserai-night` — Caravanserai  **[PAINT]**

> A desert caravanserai courtyard at night. Sand-dusted flagstones and stacked bundles in the near ground, couched camels in shadow, a double tier of arched brick arcades enclosing the court with small fires and oil lamps burning beneath them, a star-filled sky over the open centre. Warm firelight amber against cold blue night and mud-brick brown. Fires read as many small pools around the arcade and the open sky stays dark.

#### 103. `mughal-palace-courtyard` — Palace Courtyard  **[PAINT]**

> A Mughal palace courtyard in the heat of the afternoon. A narrow marble water channel running away down the centre of the near ground, red sandstone arcades with scalloped arches on both sides, inlaid marble panels, a domed pavilion closing the far end, a bleached hazy sky. Red sandstone, cream marble and washed-out blue. Strong central symmetry; the water channel is kept dull rather than mirror-bright and the sky is hazed down.

### Africa, Latin America, Central Asia

#### 104. `savanna-acacia-dusk` — Savanna at Dusk  **[PAINT]**

> Open African savanna at dusk. Dry tussock grass and a termite mound in the near ground, scattered flat-topped acacias in silhouette across the middle distance, a herd reduced to small dark shapes far off, a low escarpment on the horizon under a dust-thickened sky. Straw gold, burnt orange and deep violet shadow. Acacia silhouettes break the horizon; the sun stays off-frame with its glow spread across the sky band.

#### 105. `mudbrick-town-sahel` — Mud-Brick Town  **[PAINT]**

> A Sahelian mud-brick town in hard late afternoon light. A sculpted earthen wall with projecting timber beams in the near ground, narrow shaded lanes between rounded buildings, a stepped mosque tower rising behind, flat roofs stacked up the slope, dust haze over everything. A near-uniform earth ochre with deep blue-brown shadow. Wall texture carries the foreground; shadows are strong but the sky is small and hazed.

#### 106. `rift-valley-lake` — Soda Lake  **[PAINT]**

> A shallow East African soda lake seen from the shore. Cracked white alkaline flats and a rim of crusted salt in the near ground, pale green shallow water beyond, a distant pink band of flamingos, a hazy volcanic escarpment across the far side under a high sky. Bone white, alkaline green and dusty violet. Horizontal banding dominates; the pink band is a thin accent and the sky is hazed to a flat pale tone.

#### 107. `colonial-plaza-siesta` — Colonial Plaza  **[PAINT]**

> A Spanish colonial plaza in the dead heat of afternoon. Worn paving and the base of a stone fountain in the near ground, a deep shaded arcade running along one side, pastel stucco facades with closed timber shutters and wrought-iron balconies, a twin-towered church closing the far end, palms and hard shadow. Faded ochre, rose and cream against deep shade. Arcade shadow anchors one side and the sunlit facades stay warm rather than glaring.

#### 108. `andes-altiplano` — Altiplano  **[PAINT]**

> A high Andean altiplano under an intense sky. Coarse tussock grass and scattered volcanic stone in the near ground, a flat pale plain running far back, a llama herd tiny in the middle distance, snow-capped volcanic cones along the horizon, a thin dirt track. Straw gold, mineral grey and deep saturated blue. The plain occupies the middle band and the sky is deep and dark-toned at the top rather than bright.

#### 109. `amazon-river-town` — River Town  **[PAINT]**

> A small Amazonian river town of stilt houses seen from the water. Brown river surface and a moored wooden boat in the near ground, timber houses raised on tall stilts with corrugated roofs and plank walkways strung between them, a dense green forest wall behind, a grey rain squall advancing from one side. River brown, weathered timber and saturated forest green under heavy cloud. Houses run as a band across the midground and the sky stays dim.

#### 110. `steppe-yurt-mongolia` — Steppe  **[PAINT]**

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
