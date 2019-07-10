# The MIT License (MIT)
#
# Copyright (c) 2019 Jonah Yolles-Murphy for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_html_colors`
================================================================================

html5 colors converted to displayio 24bit hex colors in CamelCaseNames and under_score_names.


* Author(s): Jonah Yolles-Murphy

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_html_colors.git"

#source data: https://www.computerhope.com/htmcolor.htm
black                    = Black                    = 0x000000
night                    = Night                    = 0x0c090a
gunmetal                 = Gunmetal                 = 0x2c3539
midnight                 = Midnight                 = 0x2b1b17
charcoal                 = Charcoal                 = 0x34282c
dark_slate_grey          = DarkSlateGrey            = 0x25383c
oil                      = Oil                      = 0x3b3131
black_cat                = BlackCat                 = 0x413839
iridium                  = Iridium                  = 0x3d3c3a
black_eel                = BlackEel                 = 0x463e3f
black_cow                = BlackCow                 = 0x4c4646
gray_wolf                = GrayWolf                 = 0x504a4b
vampire_gray             = VampireGray              = 0x565051
gray_dolphin             = GrayDolphin              = 0x5c5858
carbon_gray              = CarbonGray               = 0x625d5d
ash_gray                 = AshGray                  = 0x666362
cloudy_gray              = CloudyGray               = 0x6d6968
smokey_gray              = SmokeyGray               = 0x726e6d
gray                     = Gray                     = 0x736f6e
granite                  = Granite                  = 0x837e7c
battleship_gray          = BattleshipGray           = 0x848482
gray_cloud               = GrayCloud                = 0xb6b6b4
gray_goose               = GrayGoose                = 0xd1d0ce
platinum                 = Platinum                 = 0xe5e4e2
metallic_silver          = MetallicSilver           = 0xbcc6cc
blue_gray                = BlueGray                 = 0x98afc7
light_slate_gray         = LightSlateGray           = 0x6d7b8d
slate_gray               = SlateGray                = 0x657383
jet_gray                 = JetGray                  = 0x616d7e
mist_blue                = MistBlue                 = 0x646d7e
marble_blue              = MarbleBlue               = 0x566d7e
slate_blue               = SlateBlue                = 0x737ca1
steel_blue               = SteelBlue                = 0x4863a0
blue_jay                 = BlueJay                  = 0x2b547e
dark_slate_blue          = DarkSlateBlue            = 0x2b3856
midnight_blue            = MidnightBlue             = 0x151b54
navy_blue                = NavyBlue                 = 0x000080
blue_whale               = BlueWhale                = 0x342d7e
lapis_blue               = LapisBlue                = 0x15317e
denim_dark_blue          = DenimDarkBlue            = 0x151b8d
earth_blue               = EarthBlue                = 0x0000a0
cobalt_blue              = CobaltBlue               = 0x0020c2
blueberry_blue           = BlueberryBlue            = 0x0041c2
sapphire_blue            = SapphireBlue             = 0x2554c7
blue_eyes                = BlueEyes                 = 0x1569c7
royal_blue               = RoyalBlue                = 0x2b60de
blue_orchid              = BlueOrchid               = 0x1f45fc
blue_lotus               = BlueLotus                = 0x6960ec
light_slate_blue         = LightSlateBlue           = 0x736aff
windows_blue             = WindowsBlue              = 0x357ec7
glacial_blue_ice         = GlacialBlueIce           = 0x368bc1
silk_blue                = SilkBlue                 = 0x488ac7
blue_ivy                 = BlueIvy                  = 0x3090c7
blue_koi                 = BlueKoi                  = 0x659ec7
columbia_blue            = ColumbiaBlue             = 0x87afc7
baby_blue                = BabyBlue                 = 0x95b9c7
light_steel_blue         = LightSteelBlue           = 0x728fce
ocean_blue               = OceanBlue                = 0x2b65ec
blue_ribbon              = BlueRibbon               = 0x306eff
blue_dress               = BlueDress                = 0x157dec
dodger_blue              = DodgerBlue               = 0x1589ff
cornflower_blue          = CornflowerBlue           = 0x6495ed
sky_blue                 = SkyBlue                  = 0x6698ff
butterfly_blue           = ButterflyBlue            = 0x38acec
iceberg                  = Iceberg                  = 0x56a5ec
crystal_blue             = CrystalBlue              = 0x5cb3ff
deep_sky_blue            = DeepSkyBlue              = 0x3bb9ff
denim_blue               = DenimBlue                = 0x79baec
light_sky_blue           = LightSkyBlue             = 0x82cafa
day_sky_blue             = DaySkyBlue               = 0x82caff
jeans_blue               = JeansBlue                = 0xa0cfec
blue_angel               = BlueAngel                = 0xb7ceec
pastel_blue              = PastelBlue               = 0xb4cfec
sea_blue                 = SeaBlue                  = 0xc2dfff
powder_blue              = PowderBlue               = 0xc6deff
coral_blue               = CoralBlue                = 0xafdcec
light_blue               = LightBlue                = 0xaddfff
robin_egg_blue           = RobinEggBlue             = 0xbdedff
pale_blue_lily           = PaleBlueLily             = 0xcfecec
light_cyan               = LightCyan                = 0xe0ffff
water                    = Water                    = 0xebf4fa
aliceblue                = AliceBlue                = 0xf0f8ff
azure                    = Azure                    = 0xf0ffff
light_slate              = LightSlate               = 0xccffff
light_aquamarine         = LightAquamarine          = 0x93ffe8
electric_blue            = ElectricBlue             = 0x9afeff
aquamarine               = Aquamarine               = 0x7fffd4
cyan_or_aqua             = CyanorAqua               = 0x00ffff
tron_blue                = TronBlue                 = 0x7dfdfe
blue_zircon              = BlueZircon               = 0x57feff
blue_lagoon              = BlueLagoon               = 0x8eebec
celeste                  = Celeste                  = 0x50ebec
blue_diamond             = BlueDiamond              = 0x4ee2ec
tiffany_blue             = TiffanyBlue              = 0x81d8d0
cyan_opaque              = CyanOpaque               = 0x92c7c7
blue_hosta               = BlueHosta                = 0x77bfc7
northern_lights_blue     = NorthernLightsBlue       = 0x78c7c7
medium_turquoise         = MediumTurquoise          = 0x48cccd
turquoise                = Turquoise                = 0x43c6db
jellyfish                = Jellyfish                = 0x46c7c7
blue_green               = Bluegreen                = 0x7bccb5
macaw_blue_green         = MacawBlueGreen           = 0x43bfc7
light_sea_green          = LightSeaGreen            = 0x3ea99f
dark_turquoise           = DarkTurquoise            = 0x3b9c9c
sea_turtle_green         = SeaTurtleGreen           = 0x438d80
medium_aquamarine        = MediumAquamarine         = 0x348781
greenish_blue            = GreenishBlue             = 0x307d7e
grayish_turquoise        = GrayishTurquoise         = 0x5e7d7e
beetle_green             = BeetleGreen              = 0x4c787e
teal                     = Teal                     = 0x008080
sea_green                = SeaGreen                 = 0x4e8975
camouflage_green         = CamouflageGreen          = 0x78866b
sage_green               = SageGreen                = 0x848b79
hazel_green              = HazelGreen               = 0x617c58
venom_green              = VenomGreen               = 0x728c00
fern_green               = FernGreen                = 0x667c26
dark_forest_green        = DarkForestGreen          = 0x254117
medium_sea_green         = MediumSeaGreen           = 0x306754
medium_forest_green      = MediumForestGreen        = 0x347235
seaweed_green            = SeaweedGreen             = 0x437c17
pine_green               = PineGreen                = 0x387c44
jungle_green             = JungleGreen              = 0x347c2c
shamrock_green           = ShamrockGreen            = 0x347c17
medium_spring_green      = MediumSpringGreen        = 0x348017
forest_green             = ForestGreen              = 0x4e9258
green_onion              = GreenOnion               = 0x6aa121
spring_green             = SpringGreen              = 0x4aa02c
lime_green               = LimeGreen                = 0x41a317
clover_green             = CloverGreen              = 0x3ea055
green_snake              = GreenSnake               = 0x6cbb3c
alien_green              = AlienGreen               = 0x6cc417
green_apple              = GreenApple               = 0x4cc417
yellow_green             = YellowGreen              = 0x52d017
kelly_green              = KellyGreen               = 0x4cc552
zombie_green             = ZombieGreen              = 0x54c571
frog_green               = FrogGreen                = 0x99c68e
green_peas               = GreenPeas                = 0x89c35c
dollar_bill_green        = DollarBillGreen          = 0x85bb65
dark_sea_green           = DarkSeaGreen             = 0x8bb381
iguana_green             = IguanaGreen              = 0x9cb071
avocado_green            = AvocadoGreen             = 0xb2c248
pistachio_green          = PistachioGreen           = 0x9dc209
salad_green              = SaladGreen               = 0xa1c935
hummingbird_green        = HummingbirdGreen         = 0x7fe817
nebula_green             = NebulaGreen              = 0x59e817
stoplight_go_green       = StoplightGoGreen         = 0x57e964
algae_green              = AlgaeGreen               = 0x64e986
jade_green               = JadeGreen                = 0x5efb6e
green                    = Green                    = 0x00ff00
emerald_green            = EmeraldGreen             = 0x5ffb17
lawn_green               = LawnGreen                = 0x87f717
chartreuse               = Chartreuse               = 0x8afb17
dragon_green             = DragonGreen              = 0x6afb92
mint_green               = Mintgreen                = 0x98ff98
green_thumb              = GreenThumb               = 0xb5eaaa
light_jade               = LightJade                = 0xc3fdb8
tea_green                = TeaGreen                 = 0xccfb5d
green_yellow             = GreenYellow              = 0xb1fb17
slime_green              = SlimeGreen               = 0xbce954
goldenrod                = Goldenrod                = 0xedda74
harvest_gold             = HarvestGold              = 0xede275
sun_yellow               = SunYellow                = 0xffe87c
yellow                   = Yellow                   = 0xffff00
corn_yellow              = CornYellow               = 0xfff380
parchment                = Parchment                = 0xffffc2
cream                    = Cream                    = 0xffffcc
lemon_chiffon            = LemonChiffon             = 0xfff8c6
cornsilk                 = Cornsilk                 = 0xfff8dc
beige                    = Beige                    = 0xf5f5dc
blonde                   = Blonde                   = 0xfbf6d9
antiquewhite             = AntiqueWhite             = 0xfaebd7
champagne                = Champagne                = 0xf7e7ce
blanchedalmond           = BlanchedAlmond           = 0xffebcd
vanilla                  = Vanilla                  = 0xf3e5ab
tan_brown                = TanBrown                 = 0xece5b6
peach                    = Peach                    = 0xffe5b4
mustard                  = Mustard                  = 0xffdb58
rubber_ducky_yellow      = RubberDuckyYellow        = 0xffd801
bright_gold              = BrightGold               = 0xfdd017
golden_brown             = Goldenbrown              = 0xeac117
macaroni_and_cheese      = MacaroniandCheese        = 0xf2bb66
saffron                  = Saffron                  = 0xfbb917
beer                     = Beer                     = 0xfbb117
cantaloupe               = Cantaloupe               = 0xffa62f
bee_yellow               = BeeYellow                = 0xe9ab17
brown_sugar              = BrownSugar               = 0xe2a76f
burlywood                = BurlyWood                = 0xdeb887
deep_peach               = DeepPeach                = 0xffcba4
ginger_brown             = GingerBrown              = 0xc9be62
school_bus_yellow        = SchoolBusYellow          = 0xe8a317
sandy_brown              = SandyBrown               = 0xee9a4d
fall_leaf_brown          = FallLeafBrown            = 0xc8b560
orange_gold              = OrangeGold               = 0xd4a017
sand                     = Sand                     = 0xc2b280
cookie_brown             = CookieBrown              = 0xc7a317
caramel                  = Caramel                  = 0xc68e17
brass                    = Brass                    = 0xb5a642
khaki                    = Khaki                    = 0xada96e
camel_brown              = Camelbrown               = 0xc19a6b
bronze                   = Bronze                   = 0xcd7f32
tiger_orange             = TigerOrange              = 0xc88141
cinnamon                 = Cinnamon                 = 0xc58917
bullet_shell             = BulletShell              = 0xaf9b60
dark_goldenrod           = DarkGoldenrod            = 0xaf7817
copper                   = Copper                   = 0xb87333
wood                     = Wood                     = 0x966f33
oak_brown                = OakBrown                 = 0x806517
moccasin                 = Moccasin                 = 0x827839
army_brown               = ArmyBrown                = 0x827b60
sandstone                = Sandstone                = 0x786d5f
mocha                    = Mocha                    = 0x493d26
taupe                    = Taupe                    = 0x483c32
coffee                   = Coffee                   = 0x6f4e37
brown_bear               = BrownBear                = 0x835c3b
red_dirt                 = RedDirt                  = 0x7f5217
sepia                    = Sepia                    = 0x7f462c
orange_salmon            = OrangeSalmon             = 0xc47451
rust                     = Rust                     = 0xc36241
red_fox                  = RedFox                   = 0xc35817
chocolate                = Chocolate                = 0xc85a17
sedona                   = Sedona                   = 0xcc6600
papaya_orange            = PapayaOrange             = 0xe56717
halloween_orange         = HalloweenOrange          = 0xe66c2c
pumpkin_orange           = PumpkinOrange            = 0xf87217
construction_cone_orange = ConstructionConeOrange   = 0xf87431
sunrise_orange           = SunriseOrange            = 0xe67451
mango_orange             = MangoOrange              = 0xff8040
dark_orange              = DarkOrange               = 0xf88017
coral                    = Coral                    = 0xff7f50
basket_ball_orange       = BasketBallOrange         = 0xf88158
light_salmon             = LightSalmon              = 0xf9966b
tangerine                = Tangerine                = 0xe78a61
dark_salmon              = DarkSalmon               = 0xe18b6b
light_coral              = LightCoral               = 0xe77471
bean_red                 = BeanRed                  = 0xf75d59
valentine_red            = ValentineRed             = 0xe55451
shocking_orange          = ShockingOrange           = 0xe55b3c
red                      = Red                      = 0xff0000
scarlet                  = Scarlet                  = 0xff2400
ruby_red                 = RubyRed                  = 0xf62217
ferrari_red              = FerrariRed               = 0xf70d1a
fire_engine_red          = FireEngineRed            = 0xf62817
lava_red                 = LavaRed                  = 0xe42217
love_red                 = LoveRed                  = 0xe41b17
grapefruit               = Grapefruit               = 0xdc381f
chestnut_red             = ChestnutRed              = 0xc34a2c
cherry_red               = CherryRed                = 0xc24641
mahogany                 = Mahogany                 = 0xc04000
chilli_pepper            = ChilliPepper             = 0xc11b17
cranberry                = Cranberry                = 0x9f000f
red_wine                 = RedWine                  = 0x990012
burgundy                 = Burgundy                 = 0x8c001a
chestnut                 = Chestnut                 = 0x954535
blood_red                = BloodRed                 = 0x7e3517
sienna                   = Sienna                   = 0x8a4117
sangria                  = Sangria                  = 0x7e3817
firebrick                = Firebrick                = 0x800517
maroon                   = Maroon                   = 0x810541
plum_pie                 = PlumPie                  = 0x7d0541
velvet_maroon            = VelvetMaroon             = 0x7e354d
plum_velvet              = PlumVelvet               = 0x7d0552
rosy_finch               = RosyFinch                = 0x7f4e52
puce                     = Puce                     = 0x7f5a58
dull_purple              = DullPurple               = 0x7f525d
rosy_brown               = RosyBrown                = 0xb38481
khaki_rose               = KhakiRose                = 0xc5908e
pink_bow                 = PinkBow                  = 0xc48189
lipstick_pink            = LipstickPink             = 0xc48793
rose                     = Rose                     = 0xe8adaa
rose_gold                = RoseGold                 = 0xecc5c0
desert_sand              = DesertSand               = 0xedc9af
pig_pink                 = PigPink                  = 0xfdd7e4
cotton_candy             = CottonCandy              = 0xfcdfff
pink_bubble_gum          = PinkBubbleGum            = 0xffdfdd
misty_rose               = MistyRose                = 0xfbbbb9
pink                     = Pink                     = 0xfaafbe
light_pink               = LightPink                = 0xfaafba
flamingo_pink            = FlamingoPink             = 0xf9a7b0
pink_rose                = PinkRose                 = 0xe7a1b0
pink_daisy               = PinkDaisy                = 0xe799a3
cadillac_pink            = CadillacPink             = 0xe38aae
carnation_pink           = CarnationPink            = 0xf778a1
blush_red                = BlushRed                 = 0xe56e94
hot_pink                 = HotPink                  = 0xf660ab
watermelon_pink          = WatermelonPink           = 0xfc6c85
violet_red               = VioletRed                = 0xf6358a
deep_pink                = DeepPink                 = 0xf52887
pink_cupcake             = PinkCupcake              = 0xe45e9d
pink_lemonade            = PinkLemonade             = 0xe4287c
neon_pink                = NeonPink                 = 0xf535aa
magenta                  = Magenta                  = 0xff00ff
dimorphotheca_magenta    = DimorphothecaMagenta     = 0xe3319d
bright_neon_pink         = BrightNeonPink           = 0xf433ff
pale_violet_red          = PaleVioletRed            = 0xd16587
tulip_pink               = TulipPink                = 0xc25a7c
medium_violet_red        = MediumVioletRed          = 0xca226b
rogue_pink               = RoguePink                = 0xc12869
burnt_pink               = BurntPink                = 0xc12267
bashful_pink             = BashfulPink              = 0xc25283
dark_carnation_pink      = DarkCarnationPink        = 0xc12283
plum                     = Plum                     = 0xb93b8f
viola_purple             = ViolaPurple              = 0x7e587e
purple_iris              = PurpleIris               = 0x571b7e
plum_purple              = PlumPurple               = 0x583759
indigo                   = Indigo                   = 0x4b0082
purple_monster           = PurpleMonster            = 0x461b7e
purple_haze              = PurpleHaze               = 0x4e387e
eggplant                 = Eggplant                 = 0x614051
grape                    = Grape                    = 0x5e5a80
purple_jam               = PurpleJam                = 0x6a287e
dark_orchid              = DarkOrchid               = 0x7d1b7e
purple_flower            = PurpleFlower             = 0xa74ac7
medium_orchid            = MediumOrchid             = 0xb048b5
purple_amethyst          = PurpleAmethyst           = 0x6c2dc7
dark_violet              = DarkViolet               = 0x842dce
violet                   = Violet                   = 0x8d38c9
purple_sage_bush         = PurpleSageBush           = 0x7a5dc7
lovely_purple            = LovelyPurple             = 0x7f38ec
purple                   = Purple                   = 0x8e35ef
aztech_purple            = AztechPurple             = 0x893bff
medium_purple            = MediumPurple             = 0x8467d7
jasmine_purple           = JasminePurple            = 0xa23bec
purple_daffodil          = PurpleDaffodil           = 0xb041ff
tyrian_purple            = TyrianPurple             = 0xc45aec
crocus_purple            = CrocusPurple             = 0x9172ec
purple_mimosa            = PurpleMimosa             = 0x9e7bff
heliotrope_purple        = HeliotropePurple         = 0xd462ff
crimson                  = Crimson                  = 0xe238ec
purple_dragon            = PurpleDragon             = 0xc38ec7
lilac                    = Lilac                    = 0xc8a2c8
blush_pink               = BlushPink                = 0xe6a9ec
mauve                    = Mauve                    = 0xe0b0ff
wisteria_purple          = WisteriaPurple           = 0xc6aec7
blossom_pink             = BlossomPink              = 0xf9b7ff
thistle                  = Thistle                  = 0xd2b9d3
periwinkle               = Periwinkle               = 0xe9cfec
lavender_pinocchio       = LavenderPinocchio        = 0xebdde2
lavender_blue            = Lavenderblue             = 0xe3e4fa
pearl                    = Pearl                    = 0xfdeef4
seashell                 = SeaShell                 = 0xfff5ee
milk_white               = MilkWhite                = 0xfefcff
white                    = White                    = 0xffffff
