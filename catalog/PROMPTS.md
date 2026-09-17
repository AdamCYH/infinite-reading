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
