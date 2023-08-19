@namespace
class SpriteKind:
    demeral = SpriteKind.create()
    Pickup = SpriteKind.create()
    pickup2 = SpriteKind.create()
    Pickup3 = SpriteKind.create()
    Pickup4 = SpriteKind.create()
    Pickup5 = SpriteKind.create()
    Pickup6 = SpriteKind.create()
    Pickup7 = SpriteKind.create()
    Pickup8 = SpriteKind.create()
    Pickup9 = SpriteKind.create()
    Pickup10 = SpriteKind.create()
    Pickup11 = SpriteKind.create()
    Pickup12 = SpriteKind.create()
    pickup13 = SpriteKind.create()
    pickup14 = SpriteKind.create()
    Pickup15 = SpriteKind.create()
    pickup16 = SpriteKind.create()
    Pickup17 = SpriteKind.create()
    Pickup18 = SpriteKind.create()
    Pickup19 = SpriteKind.create()
    badguy001 = SpriteKind.create()
    pickup1 = SpriteKind.create()
    Pickup20 = SpriteKind.create()
    pickup21 = SpriteKind.create()
    pickup22 = SpriteKind.create()
    Pickup23 = SpriteKind.create()
    pickup24 = SpriteKind.create()
    Timer = SpriteKind.create()
    pickup25 = SpriteKind.create()
    thrusterbuster = SpriteKind.create()
    sign1 = SpriteKind.create()
    goldenshard = SpriteKind.create()
    goldenshardRE = SpriteKind.create()
    goldenshardSP = SpriteKind.create()
    Supergoldenshard = SpriteKind.create()
    Pickup26 = SpriteKind.create()

def on_overlap_tile(sprite, location):
    Hyper_the_dragon.set_position(20, 199)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_up_pressed():
    global lastdirection
    if Hyper_the_dragon.vy == 0:
        Hyper_the_dragon.set_image(assets.image("""
            look he jumping
        """))
        animation.run_image_animation(Hyper_the_dragon,
            assets.animation("""
                hes animated now
            """),
            70,
            True)
        Hyper_the_dragon.vy = -110
    lastdirection = 1
    music.jump_up.play()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite2, otherSprite):
    for index in range(1):
        music.ba_ding.play()
        otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup, on_on_overlap)

def on_on_overlap2(sprite3, otherSprite2):
    otherSprite2.destroy()
    info.change_score_by(1)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.goldenshard, on_on_overlap2)

def on_overlap_tile2(sprite4, location2):
    Hyper_the_dragon.set_position(20, 199)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile92
    """),
    on_overlap_tile2)

def Change_level(Level_Number: number):
    global welcome_to_crystal_tundra
    if Level_Number == 1:
        color.start_fade(color.black, color.original_palette)
        tiles.set_current_tilemap(tilemap("""
            Crystal Tundra
        """))
        effects.blizzard.start_screen_effect()
        welcome_to_crystal_tundra = sprites.create(assets.image("""
                welcome to crystal tundra
            """),
            SpriteKind.sign1)
        welcome_to_crystal_tundra.set_position(50, 200)
        scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
            assets.image("""
                crystal tundra backround
            """))
        scroller.scroll_background_with_camera(scroller.CameraScrollMode.ONLY_HORIZONTAL)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        blaze burn
    """), Hyper_the_dragon, 0, 0)
    projectile.set_velocity(-1000000, 0)
    music.beam_up.play()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap3(sprite5, otherSprite3):
    for index2 in range(1):
        music.ba_ding.play()
        otherSprite3.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup17, on_on_overlap3)

def on_on_overlap4(sprite6, otherSprite4):
    for index3 in range(1):
        otherSprite4.destroy()
        music.play_melody("C5 C F C B D F F ", 500)
        music.set_tempo(120)
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup3, on_on_overlap4)

def on_on_overlap5(sprite7, otherSprite5):
    otherSprite5.destroy()
    music.buzzer.play()
    if Math.percent_chance(25):
        statusbar.value += 15
sprites.on_overlap(SpriteKind.projectile, SpriteKind.badguy001, on_on_overlap5)

def on_on_overlap6(sprite8, otherSprite6):
    otherSprite6.destroy()
    info.change_score_by(40)
    info.change_life_by(1)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player,
    SpriteKind.Supergoldenshard,
    on_on_overlap6)

def on_a_pressed():
    global projectile
    controller.combos.set_trigger_type(TriggerType.CONTINUOUS)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
            rapid spiral not animated
        """),
        Hyper_the_dragon,
        1000,
        0)
    animation.run_image_animation(projectile,
        assets.animation("""
            rapid spiral animated
        """),
        100,
        True)
    projectile.set_velocity(1000000, 0)
    music.beam_up.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap7(sprite9, otherSprite7):
    for index4 in range(1):
        music.ba_ding.play()
        otherSprite7.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup8, on_on_overlap7)

def on_overlap_tile3(sprite10, location3):
    Hyper_the_dragon.set_position(20, 199)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile7
    """),
    on_overlap_tile3)

def on_on_overlap8(sprite11, otherSprite8):
    for index5 in range(1):
        music.ba_ding.play()
        otherSprite8.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup21, on_on_overlap8)

def on_on_overlap9(sprite12, otherSprite9):
    for index6 in range(1):
        music.ba_ding.play()
        otherSprite9.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup5, on_on_overlap9)

def on_left_pressed():
    global lastdirection
    animation.run_image_animation(Hyper_the_dragon,
        assets.animation("""
            hyper moving left
        """),
        70,
        True)
    lastdirection = 3
    music.thump.play()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap10(sprite13, otherSprite10):
    for index7 in range(1):
        music.ba_ding.play()
        otherSprite10.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup18, on_on_overlap10)

def on_on_overlap11(sprite14, otherSprite11):
    otherSprite11.destroy()
    info.change_score_by(15)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.goldenshardSP, on_on_overlap11)

def on_overlap_tile4(sprite15, location4):
    game.over(True)
    effects.star_field.end_screen_effect()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile39
    """),
    on_overlap_tile4)

def on_on_overlap12(sprite16, otherSprite12):
    for index8 in range(1):
        music.ba_ding.play()
        otherSprite12.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup19, on_on_overlap12)

def on_on_overlap13(sprite17, otherSprite13):
    for index9 in range(1):
        otherSprite13.destroy()
        music.play_melody("C5 C F C B D F F ", 500)
        music.set_tempo(120)
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup15, on_on_overlap13)

def on_on_overlap14(sprite18, otherSprite14):
    for index10 in range(1):
        music.ba_ding.play()
        otherSprite14.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup2, on_on_overlap14)

def on_on_overlap15(sprite19, otherSprite15):
    inferno_ruby.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup25, on_on_overlap15)

def on_on_overlap16(sprite20, otherSprite16):
    for index11 in range(1):
        otherSprite16.destroy()
        music.play_melody("C5 C F C B D F F ", 500)
        music.set_tempo(120)
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup13, on_on_overlap16)

def on_on_zero(status):
    info.change_life_by(-1)
    Hyper_the_dragon.set_position(20, 200)
    statusbar.value += 120
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_overlap_tile5(sprite21, location5):
    game.over(True)
    effects.star_field.end_screen_effect()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile40
    """),
    on_overlap_tile5)

def on_right_pressed():
    global lastdirection
    animation.run_image_animation(Hyper_the_dragon,
        assets.animation("""
            hyper moving right
        """),
        70,
        True)
    lastdirection = 1
    music.thump.play()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile6(sprite22, location6):
    Hyper_the_dragon.set_position(20, 199)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile84
    """),
    on_overlap_tile6)

def on_on_overlap17(sprite23, otherSprite17):
    statusbar.value += -30
    otherSprite17.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.badguy001, on_on_overlap17)

def on_on_overlap18(sprite24, otherSprite18):
    for index12 in range(1):
        music.ba_ding.play()
        otherSprite18.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup20, on_on_overlap18)

def on_on_overlap19(sprite25, otherSprite19):
    otherSprite19.destroy()
    info.change_life_by(1)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup1, on_on_overlap19)

def on_life_zero():
    game.over(False, effects.blizzard)
    music.play_melody("C5 A B E C F - E ", 500)
    music.play_melody("D F E D E F E D ", 600)
info.on_life_zero(on_life_zero)

def on_on_overlap20(sprite26, otherSprite20):
    for index13 in range(1):
        music.ba_ding.play()
        otherSprite20.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup6, on_on_overlap20)

def on_on_overlap21(sprite27, otherSprite21):
    for index14 in range(1):
        music.ba_ding.play()
        otherSprite21.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup23, on_on_overlap21)

def on_on_overlap22(sprite28, otherSprite22):
    for index15 in range(1):
        music.ba_ding.play()
        otherSprite22.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup7, on_on_overlap22)

def on_on_overlap23(sprite29, otherSprite23):
    for index16 in range(1):
        music.ba_ding.play()
        otherSprite23.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup24, on_on_overlap23)

def on_on_overlap24(sprite30, otherSprite24):
    for index17 in range(1):
        otherSprite24.destroy()
        music.play_melody("C5 C F C B D F F ", 500)
        music.set_tempo(120)
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup16, on_on_overlap24)

def on_on_overlap25(sprite31, otherSprite25):
    for index18 in range(1):
        otherSprite25.destroy()
        music.play_melody("C5 C F C B D F F ", 500)
        music.set_tempo(120)
sprites.on_overlap(SpriteKind.player, SpriteKind.Pickup4, on_on_overlap25)

def on_overlap_tile7(sprite32, location7):
    global Current_Level
    Current_Level += 1
    Change_level(Current_Level)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        transparency16
    """),
    on_overlap_tile7)

def on_on_overlap26(sprite33, otherSprite26):
    otherSprite26.destroy()
    info.change_score_by(5)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.goldenshardRE, on_on_overlap26)

def on_on_overlap27(sprite34, otherSprite27):
    for index19 in range(1):
        otherSprite27.destroy()
        music.play_melody("C5 C F C B D F F ", 500)
        music.set_tempo(120)
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup14, on_on_overlap27)

def on_on_overlap28(sprite35, otherSprite28):
    for index20 in range(1):
        music.ba_ding.play()
        otherSprite28.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.pickup22, on_on_overlap28)

moving = False
projectile: Sprite = None
welcome_to_crystal_tundra: Sprite = None
Plasma_gloves: Sprite = None
Robot_mini_001: Sprite = None
SP_demeral_5: Sprite = None
SP_demeral_4: Sprite = None
SP_demeral_3: Sprite = None
SP_demeral_2: Sprite = None
SP_demeral_1: Sprite = None
Plasma_topaz_5: Sprite = None
Plasma_topaz_4: Sprite = None
Plasma_topaz_3: Sprite = None
Plasma_topaz_2: Sprite = None
Plasma_topaz_1: Sprite = None
Blizzard_sapphire_5: Sprite = None
Blizzard_sapphire_4: Sprite = None
Blizzard_sapphire_3: Sprite = None
Blizzard_sapphire_2: Sprite = None
Blizzard_sapphire_1: Sprite = None
Blaze_ruby_5: Sprite = None
Blaze_ruby_4: Sprite = None
Blaze_ruby_3: Sprite = None
Blaze_ruby_2: Sprite = None
Blaze_ruby_1: Sprite = None
inferno_ruby: Sprite = None
The_super_ball: Sprite = None
The_SUPER_gold_shard: Sprite = None
The_Gold_Shard_3: Sprite = None
The_Gold_Shard_2: Sprite = None
The_GoldShard_1: Sprite = None
statusbar: StatusBarSprite = None
lastdirection = 0
Hyper_the_dragon: Sprite = None
Current_Level = 0
scene.set_background_image(assets.image("""
    The title screen
"""))
game.show_long_text("press a to start", DialogLayout.BOTTOM)
Current_Level = 0
Change_level(1)
Hyper_the_dragon = sprites.create(assets.image("""
        hyper the dragon
    """),
    SpriteKind.player)
characterAnimations.loop_frames(Hyper_the_dragon,
    assets.animation("""
        hyper blinking right
    """),
    100,
    characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT))
characterAnimations.loop_frames(Hyper_the_dragon,
    assets.animation("""
        hyper blinking left
    """),
    70,
    characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
if lastdirection == 1:
    animation.run_image_animation(Hyper_the_dragon,
        assets.animation("""
            hyper moving right
        """),
        70,
        True)
if lastdirection == 3:
    animation.run_image_animation(Hyper_the_dragon,
        assets.animation("""
            hyper moving left
        """),
        70,
        True)
if lastdirection == 1:
    characterAnimations.loop_frames(Hyper_the_dragon,
        assets.animation("""
            hyper jumping right
        """),
        70,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_RIGHT))
    characterAnimations.loop_frames(Hyper_the_dragon,
        assets.animation("""
            hyper jumping left
        """),
        70,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_LEFT))
    animation.run_image_animation(Hyper_the_dragon,
        assets.animation("""
            hyper just jumping
        """),
        70,
        True)
scaling.scale_to_pixels(Hyper_the_dragon,
    40,
    ScaleDirection.VERTICALLY,
    ScaleAnchor.TOP_RIGHT)
controller.move_sprite(Hyper_the_dragon, 200, 0)
Hyper_the_dragon.set_flag(SpriteFlag.BOUNCE_ON_WALL, False)
statusbar = statusbars.create(4, 70, StatusBarKind.health)
statusbar.set_color(7, 2)
statusbar.position_direction(CollisionDirection.LEFT)
statusbar.value = 125
Hyper_the_dragon.set_position(20, 199)
Hyper_the_dragon.ay = 180
info.set_life(3)
scene.camera_follow_sprite(Hyper_the_dragon)
music.footstep.play()
for value in tiles.get_tiles_by_type(assets.tile("""
    radient shard0
""")):
    The_GoldShard_1 = sprites.create(assets.image("""
        gold shard
    """), SpriteKind.goldenshard)
    tiles.place_on_tile(The_GoldShard_1, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
for value2 in tiles.get_tiles_by_type(assets.tile("""
    radient shard5
""")):
    The_Gold_Shard_2 = sprites.create(assets.image("""
            gold shard rare
        """),
        SpriteKind.goldenshardRE)
    tiles.place_on_tile(The_Gold_Shard_2, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))
for value3 in tiles.get_tiles_by_type(assets.tile("""
    radient shard6
""")):
    The_Gold_Shard_3 = sprites.create(assets.image("""
            gold shard special
        """),
        SpriteKind.goldenshardSP)
    tiles.place_on_tile(The_Gold_Shard_3, value3)
    tiles.set_tile_at(value3, assets.tile("""
        transparency16
    """))
for value4 in tiles.get_tiles_by_type(assets.tile("""
    myTile79
""")):
    The_SUPER_gold_shard = sprites.create(assets.image("""
            the super gold shard
        """),
        SpriteKind.Supergoldenshard)
    tiles.place_on_tile(The_SUPER_gold_shard, value4)
    tiles.set_tile_at(value4, assets.tile("""
        transparency16
    """))
for value5 in tiles.get_tiles_by_type(assets.tile("""
    myTile35
""")):
    The_super_ball = sprites.create(assets.image("""
            the fire ball life
        """),
        SpriteKind.pickup1)
    tiles.place_on_tile(The_super_ball, value5)
    tiles.set_tile_at(value5, assets.tile("""
        transparency16
    """))
for value6 in tiles.get_tiles_by_type(assets.tile("""
    myTile64
""")):
    inferno_ruby = sprites.create(assets.image("""
            the inferno ruby
        """),
        SpriteKind.pickup25)
    tiles.place_on_tile(inferno_ruby, value6)
    tiles.set_tile_at(value6, assets.tile("""
        transparency16
    """))
for value7 in tiles.get_tiles_by_type(assets.tile("""
    myTile23
""")):
    Blaze_ruby_1 = sprites.create(assets.image("""
            blaze ruby red
        """),
        SpriteKind.Pickup20)
    tiles.place_on_tile(Blaze_ruby_1, value7)
    tiles.set_tile_at(value7, assets.tile("""
        transparency16
    """))
for value8 in tiles.get_tiles_by_type(assets.tile("""
    myTile24
""")):
    Blaze_ruby_2 = sprites.create(assets.image("""
            blaze ruby orange
        """),
        SpriteKind.pickup21)
    tiles.place_on_tile(Blaze_ruby_2, value8)
    tiles.set_tile_at(value8, assets.tile("""
        transparency16
    """))
for value9 in tiles.get_tiles_by_type(assets.tile("""
    myTile25
""")):
    Blaze_ruby_3 = sprites.create(assets.image("""
            blaze ruby yellow
        """),
        SpriteKind.pickup22)
    tiles.place_on_tile(Blaze_ruby_3, value9)
    tiles.set_tile_at(value9, assets.tile("""
        transparency16
    """))
for value10 in tiles.get_tiles_by_type(assets.tile("""
    myTile26
""")):
    Blaze_ruby_4 = sprites.create(assets.image("""
            blaze ruby pink
        """),
        SpriteKind.Pickup23)
    tiles.place_on_tile(Blaze_ruby_4, value10)
    tiles.set_tile_at(value10, assets.tile("""
        transparency16
    """))
for value11 in tiles.get_tiles_by_type(assets.tile("""
    myTile27
""")):
    Blaze_ruby_5 = sprites.create(assets.image("""
            blaze ruby grey
        """),
        SpriteKind.pickup24)
    tiles.place_on_tile(Blaze_ruby_5, value11)
    tiles.set_tile_at(value11, assets.tile("""
        transparency16
    """))
for value12 in tiles.get_tiles_by_type(assets.tile("""
    myTile28
""")):
    Blizzard_sapphire_1 = sprites.create(assets.image("""
            Blizzard sapphire 1
        """),
        SpriteKind.Pickup)
    tiles.place_on_tile(Blizzard_sapphire_1, value12)
    tiles.set_tile_at(value12, assets.tile("""
        transparency16
    """))
for value13 in tiles.get_tiles_by_type(assets.tile("""
    myTile29
""")):
    Blizzard_sapphire_2 = sprites.create(assets.image("""
            blizzard sapphire 2
        """),
        SpriteKind.pickup2)
    tiles.place_on_tile(Blizzard_sapphire_2, value13)
    tiles.set_tile_at(value13, assets.tile("""
        transparency16
    """))
for value14 in tiles.get_tiles_by_type(assets.tile("""
    myTile30
""")):
    Blizzard_sapphire_3 = sprites.create(assets.image("""
            blizzard sapphire 3
        """),
        SpriteKind.Pickup17)
    tiles.place_on_tile(Blizzard_sapphire_3, value14)
    tiles.set_tile_at(value14, assets.tile("""
        transparency16
    """))
for value15 in tiles.get_tiles_by_type(assets.tile("""
    myTile31
""")):
    Blizzard_sapphire_4 = sprites.create(assets.image("""
            blizzard sapphire 4
        """),
        SpriteKind.Pickup18)
    tiles.place_on_tile(Blizzard_sapphire_4, value15)
    tiles.set_tile_at(value15, assets.tile("""
        transparency16
    """))
for value16 in tiles.get_tiles_by_type(assets.tile("""
    myTile32
""")):
    Blizzard_sapphire_5 = sprites.create(assets.image("""
            blizzard sapphire 5
        """),
        SpriteKind.Pickup19)
    tiles.place_on_tile(Blizzard_sapphire_5, value16)
    tiles.set_tile_at(value16, assets.tile("""
        transparency16
    """))
for value17 in tiles.get_tiles_by_type(assets.tile("""
    myTile18
""")):
    Plasma_topaz_1 = sprites.create(assets.image("""
        plasma topaz 1
    """), SpriteKind.Pickup3)
    tiles.place_on_tile(Plasma_topaz_1, value17)
    tiles.set_tile_at(value17, assets.tile("""
        transparency16
    """))
for value18 in tiles.get_tiles_by_type(assets.tile("""
    myTile19
""")):
    Plasma_topaz_2 = sprites.create(assets.image("""
            plasma topaz 2
        """),
        SpriteKind.pickup13)
    tiles.place_on_tile(Plasma_topaz_2, value18)
    tiles.set_tile_at(value18, assets.tile("""
        transparency16
    """))
for value19 in tiles.get_tiles_by_type(assets.tile("""
    myTile20
""")):
    Plasma_topaz_3 = sprites.create(assets.image("""
            plasma topaz 3
        """),
        SpriteKind.pickup14)
    tiles.place_on_tile(Plasma_topaz_3, value19)
for value20 in tiles.get_tiles_by_type(assets.tile("""
    myTile21
""")):
    Plasma_topaz_4 = sprites.create(assets.image("""
            plasma topaz 4
        """),
        SpriteKind.Pickup15)
    tiles.place_on_tile(Plasma_topaz_4, value20)
for value21 in tiles.get_tiles_by_type(assets.tile("""
    myTile22
""")):
    Plasma_topaz_5 = sprites.create(assets.image("""
            plasma topaz 5
        """),
        SpriteKind.pickup16)
    tiles.place_on_tile(Plasma_topaz_5, value21)
for value22 in tiles.get_tiles_by_type(assets.tile("""
    radient shard1
""")):
    SP_demeral_1 = sprites.create(assets.image("""
        SP demeral 1
    """), SpriteKind.Pickup4)
    tiles.place_on_tile(SP_demeral_1, value22)
    tiles.set_tile_at(value22, assets.tile("""
        transparency16
    """))
for value23 in tiles.get_tiles_by_type(assets.tile("""
    radient shard
""")):
    SP_demeral_2 = sprites.create(assets.image("""
        SP demeral 2
    """), SpriteKind.Pickup5)
    tiles.place_on_tile(SP_demeral_2, value23)
    tiles.set_tile_at(value23, assets.tile("""
        transparency16
    """))
for value24 in tiles.get_tiles_by_type(assets.tile("""
    radient shard3
""")):
    SP_demeral_3 = sprites.create(assets.image("""
        SP demeral 3
    """), SpriteKind.Pickup6)
    tiles.place_on_tile(SP_demeral_3, value24)
    tiles.set_tile_at(value24, assets.tile("""
        transparency16
    """))
for value25 in tiles.get_tiles_by_type(assets.tile("""
    radient shard2
""")):
    SP_demeral_4 = sprites.create(assets.image("""
        SP demeral 4
    """), SpriteKind.Pickup7)
    tiles.place_on_tile(SP_demeral_4, value25)
    tiles.set_tile_at(value25, assets.tile("""
        transparency16
    """))
for value26 in tiles.get_tiles_by_type(assets.tile("""
    radient shard4
""")):
    SP_demeral_5 = sprites.create(assets.image("""
        SP demeral 5
    """), SpriteKind.Pickup8)
    tiles.place_on_tile(SP_demeral_5, value26)
    tiles.set_tile_at(value26, assets.tile("""
        transparency16
    """))
for value27 in tiles.get_tiles_by_type(assets.tile("""
    myTile34
""")):
    Robot_mini_001 = sprites.create(assets.image("""
            robot mini 001
        """),
        SpriteKind.badguy001)
    tiles.place_on_tile(Robot_mini_001, value27)
    tiles.set_tile_at(value27, assets.tile("""
        transparency16
    """))
for value28 in tiles.get_tiles_by_type(assets.tile("""
    myTile87
""")):
    Plasma_gloves = sprites.create(assets.image("""
        plasma gloves
    """), SpriteKind.Pickup26)
    tiles.place_on_tile(Plasma_gloves, value28)
    tiles.set_tile_at(value28, assets.tile("""
        transparency16
    """))

def on_on_update():
    if Hyper_the_dragon.overlaps_with(Blaze_ruby_1) or (Hyper_the_dragon.overlaps_with(Blaze_ruby_2) or (Hyper_the_dragon.overlaps_with(Blaze_ruby_3) or (Hyper_the_dragon.overlaps_with(Blaze_ruby_4) or Hyper_the_dragon.overlaps_with(Blaze_ruby_5)))):
        characterAnimations.loop_frames(Hyper_the_dragon,
            assets.animation("""
                burning blazer
            """),
            70,
            characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.MOVING))
        characterAnimations.loop_frames(Hyper_the_dragon,
            assets.animation("""
                burning blazer0
            """),
            70,
            characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.MOVING))
        Hyper_the_dragon.start_effect(effects.fire)
        statusbar.set_color(2, 4)
        if Hyper_the_dragon.overlaps_with(Robot_mini_001):
            Robot_mini_001.destroy()
game.on_update(on_on_update)

def on_on_update2():
    global moving
    moving = controller.right.is_pressed() or controller.left.is_pressed()
    if not (moving):
        animation.stop_animation(animation.AnimationTypes.ALL, Hyper_the_dragon)
game.on_update(on_on_update2)

def on_on_update3():
    if Hyper_the_dragon.is_hitting_tile(CollisionDirection.RIGHT) and Hyper_the_dragon.vy >= 0:
        Hyper_the_dragon.vy = 0
        Hyper_the_dragon.ay = 0
        Hyper_the_dragon.set_image(assets.image("""
            hes on a wall 1
        """))
    else:
        Hyper_the_dragon.ay = 350
    if Hyper_the_dragon.is_hitting_tile(CollisionDirection.LEFT) and Hyper_the_dragon.vy >= 0:
        Hyper_the_dragon.vy = 0
        Hyper_the_dragon.ay = 0
        Hyper_the_dragon.set_image(assets.image("""
            hes on a wall 2
        """))
    else:
        Hyper_the_dragon.ay = 350
game.on_update(on_on_update3)

def on_forever():
    for index21 in range(4):
        music.play_tone(330, music.beat(BeatFraction.HALF))
        music.play_tone(494, music.beat(BeatFraction.HALF))
        music.play_tone(523, music.beat(BeatFraction.HALF))
        music.play_tone(440, music.beat(BeatFraction.HALF))
        music.play_tone(494, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.play_tone(440, music.beat(BeatFraction.HALF))
        music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.DOUBLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.DOUBLE))
    music.play_tone(262, music.beat(BeatFraction.BREVE))
forever(on_forever)
