# The script of the game goes in this file.


init python:
    import random
    import math

    # Define "ambience" sound channel, mixed w/music slider, loops by default
    
    renpy.music.register_channel("ambience", "music", True)
    renpy.music.register_channel("ambience2", "music", True)
    renpy.music.register_channel("typewriter", "sound", True)
    
    # Define typewriter FX
    def fox_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/deepclick.mp3", channel="typewriter", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="typewriter")

    def plumeria_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/buttonclick.mp3", channel="typewriter", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="typewriter")
    
    def grandma_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/click.mp3", channel="typewriter", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="typewriter")
    
    # fennel
    def fennel_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/twangclick.mp3", channel="typewriter", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="typewriter")
    
    # radio
    def radio_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/radioclick.mp3", channel="typewriter", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="typewriter")
    
    # spirit
    def spirit_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/iceclick.mp3", channel="typewriter", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="typewriter")
    
    # Source: https://www.reddit.com/r/RenPy/comments/17o8vaf/made_a_firefly_effect/
    # This one updates the fly position everyframe
    fly = None
    def firefly_update(st):
        for i in fireflies_sprites:
            fly = i[0]
            fly.y = fly.y - 5 * i[4]

            # fly_xposition = start_position + (sin(fly.yposition / 180 * oscillate_intensity) * direction)
            if fly.y < -100:
                fly.y = 1200 + renpy.random.uniform(0,600)
            if i[5] == 2:
                sine = math.sin(fly.y / 180.0 * i[3]) * -1
            else:
                sine = math.sin(fly.y / 180.0 * i[3])
            if sine == 0:
                sine = 0.1
            sined = 250 * i[2] * sine
            fly.x = i[1] + sined
        return 0.01

    # To summon the fireflies
    random.seed()
    fireflies = SpriteManager(update=firefly_update)
    fireflies_sprites = [ ]
    fireflies_pos = None

    # Since there isn't any way to change the size, I had to make multiple images of fireflies with different size LMAO
    fireflyimages = [Image("/images/blue-small-42.png"), Image("/images/blue-small-67.png"), Image("/images/blue-small-100.png")]
    for i in range(100):
        imagerand = renpy.random.randint(0,len(fireflyimages) - 1)
        newfly = fireflies.create(fireflyimages[imagerand])
        # 0 = the fly
        # 1 = the xpos
        # 2 = sinetensity
        # 3 = sinspeed
        fireflies_sprites.append([newfly,renpy.random.randint(-200, 1900),renpy.random.uniform(0.3,1.0),renpy.random.uniform(0.5,1.0),renpy.random.uniform(0.4,1.0),renpy.random.randint(1,2)])

    n = 0
    for i in fireflies_sprites:
        i[0].y = 1200 + n
        n = n + renpy.random.uniform(0,600)

    del fly
    del newfly
    del i

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator  = Character(None, color="#ffffff", window_background="gui/textbox.png")
define foxglove  = Character("Me", color="#ffffff", window_background="gui/fxgtextbox.png", callback=fox_beep )
define plumeria  = Character("Plumeria", color="#ffffff", window_background="gui/plutextbox.png", callback=plumeria_beep)
define dahlia    = Character("Grandmother", color="#ffffff", window_background="gui/gdmtextbox.png", callback=grandma_beep)
define announcer = Character("Announcer", color="#ffffff", window_background="gui/textbox.png")
define fennel    = Character("Fennel", color="#ffffff", window_background="gui/fnltextbox.png", callback=fennel_beep)
define radio     = Character("Radio", color="#ffffff", window_background="gui/textbox.png", callback=radio_beep)
define spirit    = Character("Spirit", color="#ffffff", window_background="gui/textbox.png", callback=spirit_beep)

# Define images
image black = "#000"

layeredimage foxglove:
    always "character/foxglove/foxglove neutral.png"
    zoom .33
    ypos 0.175
    
    group breath:
        pos(1200,750) # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 1.7      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage foxglove neutral:
    always "character/foxglove/foxglove neutral.png"
    zoom .33
    ypos 0.175
    
    group breath:
        pos(1200,750) # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 1.7      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage foxglove annoyed:
    always "character/foxglove/foxglove annoyed.png"
    zoom .33
    ypos 0.175
    
    group breath:
        pos(1200,750)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 1.7      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage foxglove flustered:
    always "character/foxglove/foxglove flustered.png"
    zoom .33
    ypos 0.175
    
    group breath:
        pos(1200,750)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 1.7      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage foxglove not smiling:
    always "character/foxglove/foxglove not smiling.png"
    zoom .33
    ypos 0.175
    
    group breath:
        pos(1200,750)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 1.7      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage foxglove sarcastic:
    always "character/foxglove/foxglove sarcastic.png"
    zoom .33
    ypos 0.175
    
    group breath:
        pos(1200,750)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 1.7      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage foxglove terror:
    always "character/foxglove/foxglove terror.png"
    zoom .33
    ypos 0.175
    
    group breath:
        pos(1200,750)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 1.7      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
            
layeredimage plumeria:
    always "character/plumeria/plumeria neutral.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage plumeria neutral:
    always "character/plumeria/plumeria neutral.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage plumeria annoyed:
    always "character/plumeria/plumeria annoyed.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage plumeria flirt:
    always "character/plumeria/plumeria flirt.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage plumeria grin:
    always "character/plumeria/plumeria grin.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage plumeria guffaw:
    always "character/plumeria/plumeria guffaw.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage plumeria serious:
    always "character/plumeria/plumeria serious.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage plumeria surprised:
    always "character/plumeria/plumeria surprised.png"
    zoom .36
    ypos 0.03
    
    group breath:
        pos(1140,660)  # Line up with mouth.
        xzoom -1      # Flip horizontally.
        zoom 2.1     # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
    
layeredimage dahlia:
    always "character/dahlia/dahlia neutral.png"
    zoom .45
    ypos 0.05
    
    group breath:
        pos(640,760)  # Line up with mouth.
        zoom 1.1      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage dahlia neutral:
    always "character/dahlia/dahlia neutral.png"
    zoom .45
    ypos 0.05
    
    group breath:
        pos(640,760)  # Line up with mouth.
        zoom 1.1      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
layeredimage dahlia commanding:
    always "character/dahlia/dahlia commanding.png"
    zoom .45
    ypos 0.05
    
    group breath:
        pos(640,760)  # Line up with mouth.
        zoom 1.1      # Resize
        alpha 0.7     # More transparent.
        attribute breath:
            "frost_breath"
    
layeredimage fennel:
    always "character/fennel/fennel neutral.png"
    zoom .36
    ypos 0.1
    
image snow_100 = SnowBlossom("snow_100.png", count=500, xspeed=50, yspeed=220, start=10)
image snow_59  = SnowBlossom("snow_59.png",  count=500, xspeed=50, yspeed=175, start=10)
image snow_25  = SnowBlossom("snow_25.png",  count=500, xspeed=50, yspeed=100, start=10)

image frost_particles = Composite(
    (200,200),
    (0,0), At("frost_breath/p2.png", frost_particles(0.0)),
    (0,0), At("frost_breath/p3.png", frost_particles(0.1)),
    (0,0), At("frost_breath/p4.png", frost_particles(0.2)),
    (0,0), At("frost_breath/p1.png", frost_particles(0.3)),
    (0,0), At("frost_breath/p5.png", frost_particles(0.4)))
image frost_breath:
    "frost_particles"
    choice:
        pause 6.0
    choice:
        pause 7.0
    choice:
        pause 8.0
    repeat
    
# Define transforms
transform left:
    xalign 0.05

transform center:
    xalign 0.5

transform right:
    xalign 1.05
    
transform right_sitting:
    xalign 1.025
    ypos 0.25
    
transform left_sitting:
    xalign 0.05
    ypos 0.3
    
transform frost_particles(delay):

    zoom 2.0 alpha 0.0 yoffset 0 xoffset 0 rotate 0

    pause delay

    parallel:
        linear 2.0 alpha 0.5
        linear 2.0 alpha 0.0

    parallel:
        easein 4.0 xoffset -150

    parallel:
        choice:
            easein 4.0 yoffset 10
        choice:
            easein 4.0 yoffset 0
        choice:
            easein 4.0 yoffset -10

    parallel:
        choice:
            easein 4.0 rotate 5
        choice:
            easein 4.0 rotate 0
        choice:
            easein 4.0 rotate -5


# The game starts here.

label start:
    scene black
    with fade
    
    stop music fadeout 5.0

    show snow_100
    show snow_59
    show snow_25
    show black onlayer screens
    
    hide black onlayer screens with Fade(0.0, 6.5, 5.0)

    play music "audio/music/Terminal.mp3" noloop volume 6.0

    narrator "When I was twenty-one, I visited my grandmother for the first time."

    play ambience "audio/ambience/chugga chugga.mp3" fadein 5.0 loop volume 2.0

    narrator "The rattle of the train is constant and soothing. It’s creeping into winter, and flakes of snow dance microsecond ballets in the lights from the train windows."

    narrator "I’d cracked the window by my seat open. The air flowing in is cool and damp, like the memory of a river."

    narrator "I’ve always preferred the cold. Heat has a tendency to leave me listless and sluggish."

    narrator "There’s nothing to do but dwell on my thoughts. The rocking of the train swirls them in my brain, thick and oily."

    narrator "I have to admit, I’m a little nervous to meet the old woman. I’ve never seen her before, of course."

    narrator "I didn’t know the specifics – I knew that my mother and her had quarrelled, and the disagreement has sat sharp and sour between them for years, only ever growing more bitter with time."

    narrator "My mother is an easy person to argue with. Her temper was always flinty and sharp, quick to find faults and slow to praise. Oh, there’d been fights aplenty in my childhood."

    narrator "Thinking back now, I wonder how much of that was down to the coldness she’d been treated with through much of her life."

    narrator "People were never kind to half-horns, or to single mothers – and my mother had been both."

    narrator "People had never forgiven our historical enemies, the hornless sarran, and the half-horns beget between our two peoples received hatred in their stead."

    narrator "I was fortunate, in that sense – my horns were large enough that I escaped that particular form of judgement. I was simply bullied for being the child of a half-horn."

    narrator "Children are cruel."

    narrator "I knew my grandfather had died years ago. When my mother had refused to tell me anything about my grandmother, I had decided to take matters into my own hands."

    narrator "Using what was perhaps excessive caution, I sneaked a peek in my mother’s phonebook."

    narrator "There, in her tiny, crabby handwriting, was written the word mother next to a phone number, crossed out with a single sharp line. The prefix was for the northern region."

    narrator "It had taken me some time to gather the courage to call that number. In truth, I hadn’t known if my grandmother was still alive, if her number had changed, or even if she’d want to talk."

    narrator "A muttering among the other passengers catches my attention. We've come round a bend in the tracks, leaving behind the forest that had swallowed us until now."

    narrator "It reaches spindly fingers after us, most of the leaves shed already, but even those are quickly left behind."

    narrator "The sightlines to our destination are clear. The Feallan Mountains had come into view."

    stop ambience fadeout 1.0

    scene cg train dead god night
    with fade

    narrator "Yeah. It was an impressive sight."

    narrator "Godigsfel nestles at the base of the mountains, tucked into the valley like a baby chick. The corpse of – which one was it again?"

    narrator "Well, whichever – one of the gods lies sprawled across the mountains, glistening and never rotting. I stare at the giant body, distant and gloomy in the dusk."

    narrator "The voice of the train conductor comes over the speakers, thick and crackly to near incoherence."

    play sound ["<silence 0.2>", "audio/oneshot/pa scary.mp3"] volume 1.0

    announcer "Approaching Godigsfel station."

    play ambience "audio/ambience/chugga chugga.mp3" fadein 5.0 volume 2.0
    
    scene bg train night
    with fade
    
    show foxglove at left_sitting    
    with dissolve

    narrator "In the dim light I can see that Plumeria stirs back to groggy wakefulness."

    show plumeria serious at right_sitting
    with dissolve

    plumeria "Hmm? Ah... are we...?"

    narrator "She is a tall, curvy woman, with elegant upwards horns and mossy green hair, a student in the university back home."

    narrator "My roommate? Friend? Either way, she had come along with me, for reasons I wasn’t entirely certain of. She'd just sort of tagged along."

    narrator "She scrubs at her face with a sleeve. Her eyes, a startling malachite green, blink repeatedly at me before she turns to peer out the window."

    narrator "Seeing the crystalline corpse of what’s-their-name, she lets out a little gasp."

    show plumeria surprised
    with dissolve

    plumeria "Ahh! You should've woken me!"

    narrator "I shrug."

    foxglove "Why? We’re going to be here for a couple of weeks. You’ll have plenty of time to see it, and in a better light, too."

    show plumeria flirt
    with dissolve

    narrator "She gives an exaggerated sigh, then grins at me as she nudges me with an elbow. How is it so pointy? My gods, her horns would be blunter."

    plumeria "You’ve got no poetry in your soul."

    show foxglove sarcastic
    with dissolve

    foxglove "Nope."
    
    show plumeria grin
    with dissolve

    narrator "She gives a huff of amused exasperation."
    
    stop ambience fadeout 6.0
    scene bg train station
    with fade
    play ambience "audio/ambience/train station.mp3" fadein 5.0 volume 0.6
    
    show foxglove breath at left    
    show plumeria breath at right
    with dissolve

    narrator "The station wasn’t that much brighter than the train. The lights are dim and flicker fitfully, fluffy wintermoths clustering around them in frantic swirls."

    narrator "The snow has stopped for the moment. The air is clear and sharp as glass. Compared to the sea air back home, the absence of salt is startlingly present. I take a moment to breathe it in."

    narrator "Plumeria is staring up at the lights and their attendant clouds of cottonball shaped moths, each bug fruitlessly clacking its head on the glass."

    play sound [ "<silence 2.5>", "audio/oneshot/pa informative.mp3" ] volume 0.85

    narrator "Her breaths expand into great misty clouds that dissolve into the air."

    plumeria "Gaslights."

    foxglove "What?"

    plumeria "This place still uses gaslights. See the flickering?"

    narrator "I glare into the lights and are rewarded with a bunch of bright spots in my vision. Feeling like an idiot, I scrub at my eyes until I’m less blind."

    foxglove "I’ll take your word for it. Why’s that?"

    narrator "She gives a languid shrug as she turns away. She cups her hands and breathes into them, rubbing them together like she’s trying to make sparks through the friction."

    plumeria "No money to upgrade, probably. Not much money in pilgrim towns any more."

    foxglove "The things you know."

    plumeria "The things I know. Go on, find your grandmother, would you? We’re meeting at the station, right?"

    foxglove "That’s what she said on the phone."

    plumeria "You do know what she looks like, right?"
    
    show foxglove annoyed
    with dissolve
    
    show plumeria grin
    with dissolve

    narrator "I give her an annoyed look. She merely laughs in reply."

    plumeria "I guess look around and bother old ladies until you find the right one."
    
    show foxglove neutral
    with dissolve
    
    show plumeria neutral
    with dissolve

    narrator "In the stained illumination of the platform lights, I throw my glances over the other figures about, shrunk in on themselves against the bite of the air."

    narrator "Never minding bothering the right old lady, there doesn’t seem to be one to bother at all. The cavernous station is almost empty."

    narrator "An old man dribbles smoke from a cigarette, ungloved fingers stained yellow with age and tobacco. He’s the right sort of age group, wrong everything else. Especially since he’s holding a train ticket."

    narrator "Leaning against a pillar is a sarran in a suit. He looks tired and impatient."

    narrator "Guess he must be taking one of the night trains, probably all the way south to Sarrand. You don’t see many sarrans back home; the scars the occupied areas earned during the war never healed well."

    narrator "It’s a little weird how they don’t have horns. Their scriptures say the gods gave tellarns horns so we could never hide our wicked natures."

    narrator "From the little I remember, ours say the gods took theirs for the same reasons. What a stupid thing to hate each other for. I turn my gaze away before I can be considered staring."

    narrator "The only other person about is a cute-looking girl, about my age. If this is my grandmother, she’s sure aged well. I wonder if she’s a local? Her horns have that downwards curve common in the north."

    show plumeria flirt
    with dissolve
    
    plumeria "Checking out girls already? You sure move fast, huh."

    show foxglove flustered
    with dissolve
    
    foxglove "Wha- no! I was just looking around!"
    
    show plumeria guffaw
    with dissolve

    plumeria "Uh-huh."

    narrator "She snickers at my expense, then shivers."
    
    show plumeria neutral
    with dissolve

    plumeria "Well, lovergirl, hurry up and find your granny before I freeze solid."

    narrator "Plumeria shivers as she stands still. She’s hunched in on herself, trying to bury her face into her collar against the early touch of Sister Winter. I smile, seeing a chance to get my own back."

    show foxglove sarcastic
    with dissolve
    
    foxglove "Is it a bit nippy out tonight?"
    
    show plumeria annoyed
    with dissolve

    narrator "I speak with excessive casualness and am immediately rewarded with a fearsome glare."

    plumeria "I wonder what gave you the slightest hint of a notion of an idea of the concept it might be a little cold, yeah."

    plumeria "I swear to the gods, if my toes drop off from frostbite I’m going to make you eat every last one of them while they’re frosted and crunchy."

    foxglove "You have a twisted imagination, miss Feld."

    plumeria "And you have no sense of proper temperature."
    
    show foxglove neutral
    with dissolve
    
    show plumeria neutral
    with dissolve

    narrator "I consider for a second, before I slide my coat off and drape it round her shoulders. "

    narrator "It’s a little too small on her to actually wear it, so my coat becomes a cape instead. Without it, even I find it a little cold."

    show foxglove sarcastic
    with dissolve
    
    foxglove "Here, your majesty, so you don’t perish in the cold and I don’t have to eat your disgusting frozen toes."
    
    show plumeria surprised
    with dissolve

    plumeria "Oh! You sure?"
    
    show foxglove neutral
    with dissolve
    
    narrator "I simply nod. If nothing else, it’ll be encouragement to find my grandmother quicker."

    show plumeria grin
    with dissolve

    plumeria "Thanks. Maybe I won’t have to feed you frozen body parts after all."

    narrator "And isn’t that what friendship is all about."

    # "[Character models should change: protag loses coat, plu gains an extra layer.]"
    
    show plumeria neutral
    with dissolve

    narrator "I frown. It was pretty clear that my grandmother was either invisible or absent."

    foxglove "Hey, Plume, I don’t think she’s here. Maybe she’s waiting outside the st-"

    stop ambience fadeout 1.5
    play music [ "<silence 1.75>", "audio/music/Harlequin.mp3" ] volume 0.5
    show dahlia breath at center
    with dissolve

    dahlia "Who isn’t?"
    
    show foxglove terror
    with dissolve
    
    show plumeria surprised
    with dissolve

    foxglove "Waaaghhh!"
    
    plumeria "Gyaghhh!"

    narrator "I clutch at my chest, heart hammering, as I take in the little old woman that’s appeared behind us."

    show plumeria neutral
    with dissolve
    
    show foxglove neutral
    with dissolve

    narrator "She’s well dressed against the cold, with sharp features and a hard intelligence undimmed by age behind her eyes. One of her horns is severed in half, capped off with brass or bronze."

    dahlia "So you’re the daughter of that foolish girl, hmmm?"

    foxglove "Um-"

    narrator "Without asking, she reaches up and grabs hold of my horns. She angles my head until I’m staring up into purple eyes; the same kind of eyes I have, that my mother has."

    narrator "The old woman observes my face without speaking. It’s like a staring contest with a scalpel."
    
    # TODO: show foxglove nervous

    # TODO: shaking FX
    foxglove "Can, can you, um, le-"

    show dahlia commanding
    with dissolve
    
    dahlia "Hold still, girl!"

    narrator "It is perhaps one of the most awkward moments of my life. I look sideways, beseeching Plumeria for help, trying to signal SOS by the inclination of my eyebrows."

    show plumeria grin
    with dissolve
    
    narrator "She gives me two thumbs up. In my head, I swear eternal vengeance."

    show dahlia neutral
    with dissolve
    
    dahlia "Hmm."
    
    show foxglove neutral
    with dissolve

    narrator "Abruptly she lets go and turns that sharp gaze upon Plumeria. My roommate gives a winning smile."

    dahlia "And who are you, hmm?"
    
    show plumeria grin
    with dissolve

    plumeria "Plumeria Feld, your darling granddaughter’s roommate. Pleased to meet you, granny!"

    narrator "She offers a hand to shake, keeping up that roguish grin. The effect is only slightly spoiled by the way she has to fight to keep her teeth from chattering."

    narrator "Against this assault of charm, however, the frown on my grandmother’s face is a minefield."

    dahlia "..."
    
    show plumeria serious
    with dissolve

    plumeria "...Mrs. Heath?"

    dahlia "..."

    plumeria "...Ma’am?"
    
    show plumeria neutral
    with dissolve

    narrator "The old woman gives a tiny nod, and Plume unconsciously gives a little sigh of relief."

    dahlia "Hmmph. I only have one spare bed, so you’ll have to share, but you’re free to stay as well."

    show plumeria flirt
    with dissolve

    plumeria "Hey, it’s better than the shed, right? And besides..."

    narrator "She nudges me with the boniest elbow in the world. I can tell that shit-eating expression."
    
    narrator "She’s about to say something terrible and flirtatious, like she always does when she wants to fluster me, and that will make my first impression with my grandmother."

    show foxglove annoyed
    with dissolve

    foxglove "I will end you."

    narrator "Smoothly she switches tracks."
    
    show plumeria neutral
    with dissolve
    
    show foxglove neutral
    with dissolve

    plumeria "...You don’t mind, right?"

    narrator "I roll my eyes."
    
    show foxglove sarcastic
    with dissolve

    foxglove "I think I’ll get by."
    
    show foxglove neutral
    with dissolve
    
    show plumeria serious
    with dissolve

    narrator "I startle as she drops her hand on my shoulder. Her expression is as solemn as the ironwork of the train station."

    plumeria "I should inform you now I plan to steal all of your body heat. I thought you should know."

    narrator "With just as graven an expression, I nod."

    show foxglove sarcastic
    with dissolve

    foxglove "I will remember this betrayal."
    
    narrator "..."
    
    show foxglove not smiling
    with dissolve
    
    show plumeria guffaw
    with dissolve

    narrator "We both stare at each other before she giggles and I let out a huff, shaking my head as I feel a grin pull at my cheeks."

    narrator "The old woman I’d come here to meet merely watches this with her unblinking gaze. Finally, she too shakes her head at the folly of youth."

    show plumeria neutral
    with dissolve
    
    show foxglove neutral
    with dissolve

    dahlia "Well, come along. Once it starts getting cold-"

    plumeria "Wait, this isn’t it getting cold?"

    narrator "Grandmother ignores the interruption with all the uncaring majesty of an iceberg."

    dahlia "-Then it tends to make these old bones ache, so come along now, you two."

    narrator "She turns and begins striding off, her short legs deceptively eating up the distance. The few people still about clear her path like sparrows before an eagle."

    narrator "She doesn’t even pause as the station attendant wishes her a respectful good night, merely nodding."

    show dahlia commanding
    with dissolve
    
    dahlia "You two! Get!"

    narrator "Her voice cracks out like a whip."

    narrator "We get."
    
    stop music fadeout 1.0
    scene bg streets night
    with fade
    play music "audio/music/Trio for Piano, Cello, and Clarinet.mp3" fadein 5.0 loop
    show expression fireflies as fireflies

    narrator "Our path from the station soon takes us from the wide main roads to the tangles of terraced houses built for pilgrims in ages past."

    narrator "The streets fade from macadam to cobblestones, clacking beneath our shoes like a background track of finger snaps."

    narrator "The terraced buildings are tall and narrow, whitewashed, leaning like lines of drunks above the road. Their roofs are jagged with tiles, sharp and pointed, biting like teeth up towards the clouds."

    narrator "Stars peer demurely between gaps in the clouds, red, blue, white pinpricks in the night sky."

    narrator "The dead god is cast in slices of moonlight, quicksilver draped unmoving across the black-and-white pillars of the mountains."

    narrator "The blue lanterns strung out above doors give the whole thing an ethereal air, like an underwater tunnel."

    narrator "Sound, normally carried well by clear air, seems muted. The sounds of people - laughter, talking, dogs barking - is a susurrus of distant waves."

    narrator "For a moment, I feel weightless, my head fuzzing. I am adrift, in a deep, dark sea. I breathe in, trying to let the crisp cut of the air centre me."

    plumeria "-ve?"
    
    show foxglove breath at left
    with dissolve    
    show plumeria surprised breath at right
    with dissolve

    narrator "Abruptly I realise Plumeria is saying something. Now she’s leaning in, peering at my face. My grandmother is ahead, marching with a firm step that belies her age entirely."

    narrator "Her walking stick is held in one hand, entirely unneeded. Perhaps she just carries it about in case she needs to clobber someone."

    narrator "Ah, I’m getting distracted. My head is still a little foggy."

    foxglove "Hmm? Sorry, I missed what you were saying."
    
    show plumeria neutral
    with dissolve

    narrator "Plume searches my expression for a moment, before they give a small smile."

    plumeria "In a world of your own, huh?"

    foxglove "Yeah, sorry. I guess I’m a little tired."

    plumeria "Makes sense. You didn’t sleep on the train."

    narrator "She lightly bumps against my shoulder."

    plumeria "We can’t be that far off. This town isn’t that big."

    foxglove "Mmm."

    narrator "For a while more we walk in silence, but it’s a comfortable one. The blue light frames her graceful form in aquamarine."

    narrator "It strikes me how tall she is - half a head again taller than me, curvy, features finely made with an easy smile. My opposite, in that sense."

    narrator "I must be tired. My thoughts are going all over the place."

    narrator "Plume catches me in my impromptu study, and raises an eyebrow questioningly. I’m saved from having to think of an answer when my grandmother ahead comes to a stop."

    show dahlia breath at center
    with dissolve

    dahlia "Here we are."

    narrator "The house isn’t anything exceptional in this tangle of pilgrim housing. It’s still well-maintained, a thin spike of a house in cheval de frise terraces."

    narrator "We wait by the door as grandmother fumbles through her pockets for her keys, occasionally quietly grumbling."

    narrator "Like many of the others, a blue lantern burns above the door. I smell the smoke of it. Incense."

    narrator "Heavy and cloying, it slinks into my lungs with the flickering of the sapphire light. It’s a strange smell, and not entirely pleasant."

    foxglove "Um, Ma’am...?"

    narrator "At my hesitant tone, Grandmother looks up at me and I fight back the urge to twitch under that razor gaze. She stops searching through her pockets for a moment."

    dahlia "Hmmph. Call me Grandmother. I’ll not need my own kin to bow and scrape."

    show plumeria grin

    plumeria "How abou-"

    dahlia "No."
    
    show plumeria serious

    narrator "Plumeria looks dejected."

    show plumeria neutral
    with dissolve

    foxglove "Ah, well, Grandmother, I was wondering - why the blue lanterns?"

    narrator "Besides me, Plumeria is paying keen interest. The old woman pauses for a second, regarding me thoughtfully, but she suddenly snaps her fingers."

    narrator "I flinch at the unexpected sound, but she’s already rummaging through the chest pocket of her coat."

    dahlia "Now I remember. That’s where I put the blasted things."

    narrator "Her keys jangle in discordant chimes as she slots them into the door. She shoves it open against its attempts to wedge itself still half shut, and steps back to gesture us inside."

    dahlia "As for your question, girl - the lanterns are..."

    narrator "She trails off for a second, looking almost wistful."

    dahlia "Just an old superstition now. Now get inside, if you would."
    
    hide fireflies
    scene black
    with fade
    stop music fadeout 1.0
    pause 1.5
    
    play sound ["<silence 0.2>", "audio/oneshot/door shut.mp3"] volume 5.0
    
    pause 2.0
    
    narrator "We aren’t provided much time to look around. Within a few minutes, we’re sheparded to the spare room and told we could talk and acquaint ourselves in the morning."

    pause 1.0
    
    scene bg bedroom night
    with fade
    play music "audio/music/Danse Morialta.mp3" loop fadein 3.0
    
    show foxglove at left
    with dissolve
    
    show plumeria at right
    with dissolve
    
    narrator "The room itself bears the faint signs it had once been a child’s room. The walls are covered in a rather antique floral wallpaper; one side is filled with a low desk and an empty cabinet."

    narrator "A vase of flowers over the wood stove had shrivelled with the change in seasons. Browning spurs of plant matter curled in on themselves like poisoned spiders."

    narrator "Next to them, a stuffed doll in a white old-fashioned looking uniform sits with golden glass eyes and a remarkably smug smile."

    plumeria "You know, I was joking earlier, but I really hope you don’t mind sharing this, because there really isn’t going to be much wiggle room."

    narrator "Yeah, that’s another way I can guess it used to be a child’s room. The bed is not large, in the same way I am not tall."

    show foxglove sarcastic
    with dissolve

    foxglove "Alright. I’ll ask my grandmother if there’s a shed for you to sleep in."

    show plumeria grin
    with dissolve

    plumeria "Ha. Ha ha. Real funny."

    foxglove "Aren’t I just."
    
    show plumeria neutral
    with dissolve
    
    show foxglove neutral
    with dissolve

    narrator "She sighs and looks at the bed. We were going to be snug, certainly. Abruptly I yawn so wide my jaw cracks. Plume gives a small chuckle."

    show plumeria grin
    with dissolve
    
    plumeria "Well, it's not going to get any bigger."
    
    play sound ["<silence 0.2>", "audio/oneshot/cloth rustle.mp3"] volume 5.0
    
    hide plumeria
    with dissolve
    
    hide foxglove
    with dissolve
    
    pause 1.0
    
    scene cg tucked into bed 1
    with dissolve

    foxglove "Hey, Plume."

    narrator "My voice is a quiet murmur."
    
    scene cg tucked into bed 2

    plumeria "Hmm?"
    
    stop music fadeout 5.0

    foxglove "Why did you come with me?"

    narrator "She is silent for a long moment, breathing slow and steady, and I begin to wonder if she’d 
        fallen asleep. Finally, she speaks, low enough I could barely hear."

    plumeria "I just felt like it, was all. Wanted to see the north."
    
    scene cg tucked into bed 3

    narrator "She doesn’t say anything more, and neither do I. I listen to our breathing until, like sinking into 
        a still pond, I fall asleep."
        
    scene black
    with fade
    
    pause 3.0
    
    narrator "Thanks for playing our demo of Bloom Into Frost."
    narrator "Please look forward to the full release and the conclusion of the story later this year."

    scene black with fade
    pause 3.0

    ### END OF DEMO ###
