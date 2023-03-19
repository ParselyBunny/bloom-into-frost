# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(None, color="#ffffff", window_background="gui/textbox.png")
define foxglove = Character("Me", color="#ffffff", window_background="gui/fxgtextbox.png")
define plumeria = Character("Plumeria", color="#ffffff", window_background="gui/plutextbox.png")
define grandma = Character("Grandmother", color="#ffffff", window_background="gui/textbox.png")
define announcer = Character("Announcer", color="#ffffff", window_background="gui/textbox.png")
define foxglove_and_plumeria = Character("Foxglove and Plumeria", color="#ffffff", window_background="gui/textbox.png")
define fennel = Character("Fennel", color="#ffffff", window_background="gui/textbox.png")
define radio = Character("Radio", color="#ffffff", window_background="gui/textbox.png")
define spirit = Character("Spirit", color="#ffffff", window_background="gui/textbox.png")

# Declare images
image black = "#000"
image foxglove:
    "character/foxglove.png"
    zoom .33
image plumeria:
    "character/plumeria.png"
    zoom .38


# The game starts here.

label start:

    narrator "When I was twenty-one, I visited my grandmother for the first time."
    
    #play music "audio/illurock.ogg" fadeout 1.0 fadein 1.0
    # TODO: train chug sfx
    
    scene bg train night
    with fade
    
    show foxglove at left
    with fade

    narrator "The rattle of the train is constant and soothing. It’s creeping into winter, and flakes of snow dance microsecond ballets in the lights from the train windows."

    narrator "I’d cracked the window by my seat open. The air flowing in is cool and damp, like the memory of a river."

    narrator "I’ve always preferred the cold. Heat has a tendency to leave me listless and sluggish."

    narrator "The dim lights in the train are too dark to read by. Next to me, Plumeria dozes fitfully."
    
    show plumeria at right
    with fade

    narrator "She is a tall, curvy woman, with elegant upwards horns and mossy green hair, a student in the university back home."

    narrator "My roommate? Friend? Either way, she had come along with me, for reasons I wasn’t entirely certain of. They’d just sort of tagged along."

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

    # "The mountains with a dead god are seen."
    scene bg train dead god night

    narrator "Yeah. It was an impressive sight."

    narrator "Godigsfel nestles at the base of the mountains, tucked into the valley like a baby chick. The corpse of – which one was it again?"

    narrator "Well, whichever – one of the gods lies sprawled across the mountains, glistening and never rotting. I stare at the giant body, distant and gloomy in the dusk."

    narrator "The voice of the train conductor comes over the speakers, thick and crackly to near incoherence."

    # TODO: play audio of announcement

    announcer "Approaching Godigsfel station."

    # TODO: Back to train. Background shows mountains.
    
    scene bg train night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "Besides me, Plumeria stirs back to groggy wakefulness."

    plumeria "Hmm? Ah... are we...?"

    narrator "She scrubs at her face with a sleeve. Her eyes, a startling malachite green, blink repeatedly at me before she turns to peer out the window."

    narrator "Seeing the crystalline corpse of what’s-their-name, she lets out a little gasp."

    plumeria "Ahh! You should have woken me!"

    narrator "I shrug."

    foxglove "Why? We’re going to be here for a couple of weeks. You’ll have plenty of time to see it, and in a better light, too."

    narrator "She gives an exaggerated sigh, then grins at me as she nudges me with an elbow. How is it so pointy? My gods, her horns would be blunter."

    plumeria "You’ve got no poetry in your soul."

    foxglove "Nope."

    narrator "She gives a huff of amused exasperation."
    
    # TODO: train brakes SFX
    
    scene bg train station night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "The station wasn’t that much brighter than the train. The lights are dim and flicker fitfully, fluffy wintermoths clustering around them in frantic swirls."

    narrator "The snow has stopped for the moment. The air is clear and sharp as glass. Compared to the sea air back home, the absence of salt is startlingly present. I take a moment to breathe it in"

    narrator "Plumeria is staring up at the lights and their attendant clouds of cottonball shaped moths, each bug fruitlessly clacking its head on the glass."

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

    narrator "I give her an annoyed look. She merely laughs in reply."

    plumeria "I guess look around and bother old ladies until you find the right one."

    narrator "In the stained illumination of the platform lights, I throw my glances over the other figures about, shrunk in on themselves against the bite of the air."

    narrator "Never minding bothering the right old lady, there doesn’t seem to be one to bother at all.The cavernous station is almost empty."

    narrator "An old man dribbles smoke from a cigarette, ungloved fingers stained yellow with age and tobacco. He’s the right sort of age group, wrong everything else. Especially since he’s holding a train ticket."

    narrator "Leaning against a pillar is a sarran in a suit. He looks tired and impatient."

    narrator "Guess he must be taking one of the night trains, probably all the way south to Sarrand. You don’t see many sarrans back home; the scars the occupied areas earned during the war never healed well."

    narrator "It’s a little weird how they don’t have horns. Their scriptures say the gods gave tellarns horns so we could never hide our wicked natures."

    narrator "From the little I remember, ours say the gods took theirs for the same reasons. What a stupid thing to hate each other for. I turn my gaze away before I can be considered staring."

    narrator "The only other person about is a  cute-looking girl, about my age. If this is my grandmother, she’s sure aged well. I wonder if she’s a local? Her horns have that downwards curve common in the north."

    plumeria "Checking out girls already? You sure move fast, huh."

    foxglove "Wha- no! I was just looking around!"

    plumeria "Uh-huh."

    narrator "She snickers at my expense, then shivers."

    plumeria "Well, lovergirl, hurry up and find your granny before I freeze solid."

    narrator "Plumeria shivers as she stands still. She’s hunched in on herself, trying to bury her face into her collar against the early touch of Sister Winter. I smile, seeing a chance to get my own back."

    foxglove "Is it a bit nippy out tonight?"

    narrator "I speak with excessive casualness and am immediately rewarded with a fearsome glare."

    plumeria "I wonder what gave you the slightest hint of a notion of an idea of the concept it might be a little cold, yeah."

    plumeria "I swear to the gods, if my toes drop off from frostbite I’m going to make you eat every last one of them while they’re frosted and crunchy."

    foxglove "You have a twisted imagination, miss Feld."

    plumeria "And you have no sense of proper temperature."

    narrator "It’s a little too small on her to actually wear it, so my coat becomes a cape instead. Without it, even I find it a little cold."

    narrator "It’s a little too small on her to actually wear it, so my coat becomes a cape instead. Without it, even I find it a little cold."

    foxglove "Here, your majesty, so you don’t perish in the cold and I don’t have to eat your disgusting frozen toes."

    plumeria "Oh! You sure?"

    narrator "I simply nod. If nothing else, it’ll be encouragement to find my grandmother quicker."

    plumeria "Thanks. Maybe I won’t have to feed you frozen body parts after all."

    # "[Character models should change: protag loses coat, plu gains an extra layer.]"

    narrator "I frown. It was pretty clear that my grandmother was either invisible or absent."

    # "[grandmother sprite appears midsentence]"
    show grandma at center

    grandma "Who isn’t?"

    foxglove_and_plumeria "Gyaghhh!"

    narrator "I clutch at my chest, heart hammering, as I take in the little old woman that’s appeared behind us."

    narrator "She’s well dressed against the cold, with sharp features and a hard intelligence undimmed by age behind her eyes. One of her horns is severed in half, capped off with brass or bronze."

    grandma "So you’re the daughter of that foolish girl, hmmm?"

    foxglove "Um-"

    narrator "Without asking, she reaches up and grabs hold of my horns. She angles my head until I’m staring down into purple eyes; the same kind of eyes I have, that my mother has."

    narrator "The old woman observes my face without speaking. It’s like a staring contest with a scalpel."

    foxglove "Can, can you, um, le-"

    grandma "Hold still, girl!"

    narrator "It is perhaps one of the most awkward moments of my life. I look sideways, beseeching Plumeria for help, trying to signal SOS by the inclination of my eyebrows."

    narrator "She gives me two thumbs up. In my head, I swear eternal vengeance."

    grandma "Hmm."

    narrator "Abruptly she lets go and turns that sharp gaze upon Plumeria. My roommate gives a winning smile."

    grandma "And who are you, hmm?"

    plumeria "Plumeria Feld, your darling granddaughter’s roommate. Pleased to meet you, granny!"

    narrator "She offers a hand to shake, keeping up that roguish grin. The effect is only slightly spoiled by the way she has to fight to keep her teeth from chattering."

    narrator "Against this assault of charm, however, the frown on my grandmother’s face is a minefield."

    grandma "..."

    plumeria "...Mrs. Heath?"

    grandma "..."

    plumeria "...Ma’am?"

    narrator "The old woman gives a tiny nod, and Plume unconsciously gives a little sigh of relief."

    grandma "Hmmph. I only have one spare bed, so you’ll have to share, but you’re free to stay as well."

    plumeria "Hey, it’s better than the shed, right? And besides..."

    narrator "Foxglove whispers."

    narrator "Foxglove whispers."

    foxglove "I will end you."

    narrator "Smoothly she switches tracks."

    plumeria "...You don’t mind, right?"

    narrator "I roll my eyes."

    foxglove "I think I’ll get by."

    narrator "I startle as she drops her hand on my shoulder. Her expression is as solemn as the ironwork of the train station."

    plumeria "I should inform you now I plan to steal all of your body heat. I thought you should know."

    narrator "With just as graven an expression, I nod."

    foxglove "I will remember this betrayal."

    narrator "We both stare at each other before she giggles and I let out a huff, shaking my head as I feel a grin pull at my cheeks."

    narrator "The old woman I’d come here to meet merely watches this with her unblinking gaze. Finally, she too shakes her head at the folly of youth."

    grandma "Well, come along. Once it starts getting cold-"

    plumeria "Wait, this isn’t it getting cold?"

    narrator "Grandmother ignores the interruption with all the uncaring majesty of an iceberg."

    grandma "-Then it tends to make these old bones ache, so come along now, you two."

    narrator "She turns and begins striding off, her short legs deceptively eating up the distance. The few people still about clear her path like sparrows before an eagle."

    narrator "She doesn’t even pause as the station attendant wishes her a respectful good night, merely nodding."

    grandma "You two! Get!"

    narrator "Her voice cracks out like a whip."

    narrator "We get."
    
    scene bg streets night
    with fade
    
    show foxglove at left    
    show plumeria at right
    show grandma at center
    with fade

    narrator "Our path from the station soon takes us from the wide main roads to the tangles of terraced houses built for pilgrims in ages past."

    narrator "The streets fade from macadam to cobblestones, clacking beneath our shoes like a background track of finger snaps."

    narrator "The terraced buildings are tall and narrow, whitewashed, leaning like lines of drunks above the road. Their roofs are jagged with tiles, sharp and pointed, biting like teeth up towards the clouds."

    narrator "Stars peer demurely between gaps in the clouds, red, blue, white pinpricks in the night sky. The dead god is cast in slices of moonlight, quicksilver draped unmoving across the black-and-white pillars of the mountains."

    narrator "The blue lanterns strung out above doors give the whole thing an ethereal air, like an underwater tunnel. Sound, normally carried well by clear air, seems muted. The sounds of people - laughter, talking, dogs barking - is a susurrus of distant waves."

    narrator "For a moment, I feel weightless, my head fuzzing. I am adrift, in a deep, dark sea. I breathe in, trying to let the crisp cut of the air centre me."

    plumeria "-ve?"

    narrator "Abruptly I realise Plumeria is saying something. Now she’s leaning in, peering at my face. My grandmother is ahead, marching with a firm step that belies her age entirely."

    narrator "Her walking stick is held in one hand, entirely unneeded. Perhaps she just carries it about in case she needs to clobber someone."

    narrator "Ah, I’m getting distracted. My head is still a little foggy."

    foxglove "Hmm? Sorry, I missed what you were saying."

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

    grandma "Here we are."

    narrator "The house isn’t anything exceptional in this tangle of pilgrim housing. It’s still well-maintained, a thin spike of a house in cheval de frise terraces. We wait by the door as grandmother fumbles through her pockets for her keys, occasionally quietly grumbling."

    narrator "Like many of the others, a blue lantern burns above the door. I smell the smoke of it. Incense. Heavy and cloying, it slinks into my lungs with the flickering of the sapphire light. It’s a strange smell, and not entirely pleasant."

    foxglove "Um, Ma’am...?"

    narrator "At my hesitant tone, Grandmother looks up at me and I fight back the urge to twitch under that razor gaze. She stops searching through her pockets for a moment."

    grandma "Hmmph. Call me Grandmother. I’ll not need my own kin to bow and scrape."

    plumeria "How abou-"

    grandma "Plumeria looks dejected."

    grandma "Plumeria looks dejected."

    foxglove "Ah, well, Grandmother, I was wondering - why the blue lanterns?"

    narrator "Besides me, Plumeria is paying keen interest. The old woman pauses for a second, regarding me thoughtfully, but she suddenly snaps her fingers. I flinch at the unexpected sound, but she’s already rummaging through the chest pocket of her coat."

    grandma "Now I remember. That’s where I put the blasted things."

    narrator "Her keys jangle in discordant chimes as she slots them into the door. She shoves it open against its attempts to wedge itself still half shut, and steps back to gesture us inside."

    grandma "As for your question, girl - the lanterns are..."

    narrator "She trails off for a second, looking almost wistful."

    grandma "Just an old superstition now. Now get inside, if you would."
    
    scene bg home night
    with fade
    
    show foxglove at left    
    show plumeria at right
    show grandma at center
    with fade

    narrator "We aren’t provided much time to look around. Within a few minutes, we’re sheparded to the spare room and told we could talk and acquaint ourselves in the morning."

    scene bg bedroom night
    
    narrator "The room itself bears the faint signs it had once been a child’s room. The walls are covered in a rather antique floral wallpaper; one side is filled with a low desk and an empty cabinet."

    narrator "A vase of flowers over the fireplace had shrivelled with the change in seasons. Browning spurs of plant matter curled in on themselves like poisoned spiders."

    narrator "Next to them, a stuffed doll in a white old-fashioned looking uniform sits with golden glass eyes and a remarkably smug smile."

    plumeria "You know, I was joking earlier, but I really hope you don’t mind sharing this, because there really isn’t going to be much wiggle room."

    narrator "Yeah, that’s another way I can guess it used to be a child’s room. The bed is not large, in the same way I am not tall."

    foxglove "Alright. I’ll ask my grandmother if there’s a shed for you to sleep in."

    plumeria "Ha. Ha ha. Real funny."

    foxglove "Aren’t I just."

    narrator "She sighs and looks at the bed. We were going to be snug, certainly. Abruptly I yawn so wide my jaw cracks. Plume gives a small chuckle."

    plumeria "Well its not going to get any bigger."
    
    scene cg tucked into bed
    with fade

    #Scene fades to showing them tucked in bed. It’s crowded and they look uncomfortable. Horn caps on.

    foxglove "Hey, Plume."

    narrator "My voice is a quiet murmur."

    plumeria "Hmm?"

    foxglove "Why did you come with me?"

    narrator "She is silent for a long moment, breathing slow and steady, and I begin to wonder if she’d fallen asleep. Finally, without opening her eyes, she speaks, low enough I could barely hear."

    plumeria "I just felt like it, was all. Wanted to see the north."

    narrator "She doesn’t say anything more, and neither do I. I listen to our breathing until, like sinking into a still pond, I fall asleep."

    # Day 1
    scene bg bedroom day
    with fade

    narrator "The morning comes, as they tend to do, quicker than I expect. I’ve slept surprisingly well, even though I wake up with Plumeria’s elbow lodged in my ribs."

    scene bg home day
    
    show foxglove at left    
    show plumeria at right
    show grandma at center
    with fade

    narrator "All the same, I’ve never been a morning person, and I feel too sleepy for any awkwardness until we’re all sat at the table, having breakfast."

    narrator "The awkwardness returns in force once I start waking up, however. Plumeria is steadily working her way through toast painted gold with honey."

    narrator "My grandmother sits as stiff as an old sentinel, carefully holding a steaming porcelain cup. I, for my part, have a double helping of no ideas on how to talk to this person to go with my own, slightly chipped, mug of hot liquid."

    narrator "My grandmother sips at her tea carefully. I do the same. The tea burns my tongue a little; hot and slightly bitter."

    plumeria "So what’s the plan for today?"

    narrator "My roommate sounds far too cheery for a time so early. I take another sip of the tea, focusing on the floral tang of it to resist the urge to shut my eyes again."

    grandma "Hmm. Since you haven’t been to Godigsfel before, you should look about the town. Learn where things are; if you’re going to stay here, you can at least pick up my groceries."

    plumeria "Dunno about her, but that’s fine with me, granny-"

    narrator "The look Grandmother gave her was probably similar in deadly power to what had killed the god up on the mountain."

    plumeria "-Ma’am."

    grandma "Hmm."

    narrator "She takes a measured swallow from her cup and looks at me."

    grandma "While it’s not ideal, I do have business I need to take care of today, so I’ll leave you to your own devices. I trust you won’t make a mess."

    narrator "She gives a meaningful look between me and Plumeria. It takes a moment to sink in what she’s implying."

    foxglove "Ah - no, we’re not, not like that-"

    narrator "Plume nods sagely, then with deliberate tones adds a single word."

    plumeria "Yet."

    foxglove "Aaagh!"

    narrator "I cover my face with my hands, feeling the burning of my cheeks against my fingers. Through my mask of hands, I hear my Grandmother sigh. The chair scrapes as the old woman rises to her feet."

    grandma "A key is in the biscuit tin on the side, there. Lock the door if you leave."

    narrator "I hear her sharp steps fade."

    plumeria "Your grandma is the most intense old lady I’ve ever met, gods above. I thought she was about to pull my soul right out of my body just then."

    narrator "In a single fierce motion I level a finger at my friend."

    foxglove "You!"

    plumeria "Me."

    foxglove "‘Yet’? ‘Yet’?! Oh my gods, Plume, that’s my grandmother you’re making innuendo in front of!"

    narrator "Rather than look apologetic, Plumeria gives me a look so self-satisfied you could call it a cat."

    plumeria "Made you wake up, didn’t it?"

    foxglove "You’re awful."

    narrator "Plume just laughs."

    plumeria "Come on. Get ready and let’s have a look around town."

    # "Scene: city streets during the day"
    scene bg streets day
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "We wander along cobbled streets. They’re pretty, in a slightly worn-down sort of way; back home the city is all just concrete after the rebuilding. It’s a nice change."

    narrator "The people we pass are well wrapped up against the upcoming chill of winter, almost all of them bearing the downwards curved horns of northern tellarn."

    narrator "They nod to us as they pass. Plumeria, shining social butterfly she is, nods back. I tuck my chin deeper into my coat."

    narrator "In the light of day, the aetherial nature of the town is replaced with something much more mundane."

    narrator "It’s pretty empty with the pilgrim season wound down; a lot of the shops, intended to cater to those who come god-seeking, have shuttered their doors for the time being."

    narrator "We take meandering examinations through those that remain; we poke through shelves crowded with knick-knacks and baubles, debate the necessity of tii-seed oilcloth coats against foul weather, and laugh at the supposed certificates of authenticity for crystalline fragments claimed to be part of the dead god above."

    scene bg streets night
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "Eventually, as the sun begins to creep back down towards the horizon, we purchase steaming cups of drink and a pail full of sticks of hot, greasy mystery meat."

    narrator "We settle to eat on a stone bench in a little square, a fountain half-heartedly puttering splurts of frigid water towards the heavens. I sit and listen to the pattering splashes of the falling droplets as they fail to reach the sky."

    plumeria "There sure are a lot of shops selling that incense."

    foxglove "I wish they didn’t. Stuff smells awful."

    narrator "Plume looks at me, mildly surprised."

    plumeria "Really? Seemed quite nice to me. Sort of floral."

    foxglove "Huh."

    plumeria "The people here must really love the stuff, at any rate. Nearly every house here has a lantern of the stuff outside their door."

    foxglove "I guess there’s no accounting for taste."

    narrator "Plume laughs, a velvety chuckle. She has a nice laugh, I’ve noticed over the years we’ve spent together as roommates; easy and gentle."

    plumeria "I do wonder about mine, sometimes."
    
    # Day 2
    scene bg home day
    with fade
    
    show foxglove at left    
    show plumeria at right
    show grandma at center
    with fade

    narrator "The next morning, I’m still groggy from sleep and rubbing a crick out my neck when Grandmother cuts to the chase."

    grandma "You want to know why that foolish girl no longer talks to her own mother, I suppose."

    narrator "Her face is carefully neutral. It had already become evident that Dahlia Heath was not a woman who ever minced words; she had a dialectic technique of going straight for the jugular."

    grandma "This family has long held a - tradition, of sorts. We have lived in this valley for a long time."

    narrator "She peers out the window, towards the looming mountains."

    grandma "Yes, a very long time indeed. An oath was made, long ago in the past, when ice spirits guided our ancestors, lost in a blizzard, safely back down."

    foxglove "Wait, ice spirits?"

    plumeria "Those still exist? I thought..."

    narrator "The old woman smiles thinly. Plumeria and I glance at each other."

    grandma "Few of such things remain since the time of the gods, indeed, but these ones still live. Our history is entwined with theirs."

    grandma "Every time one of our family was born, they would be taken up the mountain and shown to the spirits. This happened, unbroken, for a thousand years."

    foxglove "Is that why...?"

    grandma "Quite so. That foolish girl refused. She wanted you to have nothing to do with old spirits. Instead, she moved south, and took you with her, of course."

    narrator "She takes another long sip, closing her eyes briefly. The smell of it reaches my nose; hot and bitter. Grandmother opens her eyes, only to stare into her cup."

    grandma "To be more specific, she climbed the mountain to see the spirits around, oh, three months pregnant with you, not long after she’d told me. I had been furious. Didn’t even know the father, never mind that she had been in a relationship. I was..."

    narrator "Her brow furrows."

    grandma "Hmmph. A damned fool, I suppose. That girl had no one to support her but me. Mica had already passed away by that point."

    foxglove "I’m sorry - Mica?"

    grandma "Ah. Your grandfather. Mica Lepidoli. We used my surname after the marriage; sarran names weren’t very popular, as you might imagine."

    narrator "She pauses and sets down her tea with a hard skeleton clatter of porcelain."

    grandma "Well, anyway. She walked the pilgrim’s path up to the corpse of God. Spoke to the spirits, I imagine, and three weeks after you were born, left without a word."

    narrator "Plumeria had sat through all of this. I wonder what she’s thinking, hearing all this family drama. Interested? Awkward? Surprisingly for her, her expression is carefully neutral, hiding any thoughts."

    plumeria "Why would she climb a mountain while pregnant? I can’t imagine that being easy."

    narrator "The old woman gives a husky chuckle of laughter. It rustles like old paper, dry and brittle."

    grandma "Ha. I’ve always been as stubborn as a mule, and my daughter was no different. I imagine my granddaughter is the same as well."

    narrator "I can only blink back as she turns her gaze on me."

    grandma "If there is any answer to it, it is between that girl and the spirits."

    narrator "This is a bit much, isn’t it? I glance out the window, though the city blocks my view from where I’m sitting, in the direction of the mountain."

    foxglove "Then I’ll climb the mountain and talk to them myself."

    narrator "The words are out before I can think about them, but somehow I feel certain about it. Grandmother simply watches me, her face still and giving nothing away. Plumeria, for her part, is looking doubtful."

    plumeria "Not to throw water on your fire, here, but are you sure about that? You haven’t climbed any mountains before, right?"

    foxglove "If my mother managed while heavily pregnant, I’m sure I can. I’m not that unfit."

    plumeria "We went jogging once and you threw up. After you refused to ever do it with me again. Three months isn’t heavily pregnant, either."

    foxglove "Look, that was- that was then, right? This is now. I can build up to it."

    narrator "My grandmother interjects calmly."

    grandma "If you do, then you won’t have that long to do so. In a month or less, the winter will be deep upon us, and the mountain will be too dangerous to climb at all."

    foxglove "Well, call it three weeks to do it, then. I can manage."

    grandma "Hmm. Very well. But listen well, girl. If the weather changes and the winter storms begin, abandon your attempts."

    grandma "The mountains can be terribly dangerous. I will not meet my grandchild for the first time only to see her perish before the feet of God."

    narrator "Her gaze bores into me, skewering me like a bug on a hook. My words dry up in my throat. It’s all I can do to nod, and her expression softens a fraction from granite to merely sandstone."

    narrator "I take a second to recover, and my grandmother turns that terrible gaze upon Plumeria."

    grandma "You too, girl. I will hold you responsible for her safety. Ensure it."

    foxglove "I just get no respect, huh."

    narrator "I’m ignored. Plumeria, with the same expression of a bug facing the taxidermist’s spike, gives a wilted thumbs-up."

    plumeria "Can count on me, Ma’am."

    grandma "Good."
    
    scene bg pilgrims path day
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "The Pilgrim’s Path begins at the foot of the mountain."

    narrator "The flinty grey stone blocks, wide enough for a procession, were worn lumpy and sagging by a thousand years of footfalls; every step curved like a cross-section of a bowl towards the middle."

    narrator "All the same, they look steep and horrible, and this was just the least of it. Next to them, a large board depicts the journey of any would-be faith-seekers."

    plumeria "Oh, hey. So Mr. Dead up there was called Kalarlomoth. That was bugging me."

    # "A map of the Pilgrim’s Path is shown."
    scene cg pilgrims path map day

    foxglove "So the stairs last all the way up to the... Chapel of the Nail? It's not, like... A toenail of it, is it?"
    
    scene bg pilgrims path day
    show foxglove at left    
    show plumeria at right

    narrator "Plumeria had spurned the map to gaze upwards towards that distant funerary peak, her expression approaching resigned from the borders of reluctance. The stairs traitorously remain still and solid despite her disapproval."

    plumeria "I can't believe they don't have a cable car or something. All the priests I've ever seen have been old and fat. No way they'd climb a mountain of stairs like this."

    foxglove "I guess a cable car isn’t very holy."

    plumeria "Well, anyway. Up these, then it’s following a trail, right?"

    foxglove "Yeah. Up to... Orchid’s Point, up past that, there’s another temple, the Aumic Temple, and then you’re at the big guy himself."

    narrator "I look up at the mountainous slopes. The corpse of Kalarlomoth is visible, of course, strewn like a discarded diamond sculpture across the far peaks, but I can’t pick out any buildings."

    plumeria "Well, hopefully we’ll be able to stop off at the various points."

    narrator "She scratches her chin thoughtfully."

    plumeria "Is that symbol up by the big guy a chapel or something? It’s different from the others."

    foxglove "I think it’s a survival shelter, maybe? I guess climbing down during a storm would be a bit dangerous if you got caught at the top."

    plumeria "Well, no point in delaying, right?"

    narrator "The stairs rise above me like a scale-ridged leviathan."

    foxglove "Yep. Here we go."

    narrator "I take the first step and stop, feeling as though I should say something momentous and important to mark the beginning of my climb. Nothing comes to mind."

    plumeria "Tired already, huh?"

    foxglove "Wha- no! Tired of you being a butt, maybe."

    plumeria "Uh-huh."

    narrator "She gazes at me doubtfully."

    plumeria "We don't have to climb the mountain. We could just say we did and find a pub instead. That'll have ice and spirits, too."

    narrator "I sigh."

    foxglove "Ok, fine, let's climb this stupid rock. I was trying to think of something cool to say-"

    narrator "Plume snorts inelegantly in amusement."

    foxglove "What?"

    plumeria "No, no, nothing. Don't let me stop you. Lay upon me your inspirational words, oh most wordiest of wordsmiths."

    foxglove "I was trying to think of some, alright?"

    plumeria "It's ok. I'll wait."

    narrator "She stares at me expectantly. A tiny smile plays around her lips as she tries to force her face into mocking neutrality. The pressure builds. Come on, think of something - I have to say something at this point!"

    narrator "How about - about - ah, it's pointless. She's actively grinning now, enjoying my consternation."

    foxglove "Forget it! How about this: let's climb this before I kick your butt so hard Kalarlomoth comes back to life just to say 'damn, that's a kicked butt', huh?"

    narrator "She simply laughs and begins climbing the stairs, playfully nudging me with her shoulder as she goes past."

    # scene change
    scene bg pilgrims path day
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "We climb... and climb... and climb."

    narrator "An endless sea of stone rises ahead of us, winding upwards like a prayer. This was just the first stage. I couldn’t quit already."

    foxglove "This is... so many stairs..."

    narrator "My legs are burning. A strenuous feeling of regret stretches along my thighs and promises worse to come, aches chuckling their way down to my calves with every step."

    narrator "I want to quit already."

    narrator "While we talked at first, I soon abandoned any held conversation for the sake of conserving my breath."

    narrator "The stairs are steep and narrow, the centres sunken and smooth by generations of devout footsteps."

    plumeria "Do you want the good news or the bad news first?"

    narrator "I look up at her. She looks far less terrible than I feel, as if climbing all the stairs in the world was a brisk stroll rather than a bizarre torture I’ve inflicted upon myself. In fact, she looks downright chipper."

    foxglove "How... how are you... still not tired?"

    plumeria "Oh, didn’t you know? I’m part of the university triathlon back home. This is nothing, haha!"

    # "Foxglove is angry"

    foxglove "..."

    narrator "Plumeria just laughs, the clear notes of her merriment ringing in the crisp air."

    plumeria "Anyway, you said good news first, right? Good news: we’re pretty much here."

    narrator "Abruptly I realise the stairs level off only a little bit above into a charming little plaza surrounding a mosaic. A squat chapel is built into the mountain like a blister of stonework and stained glass."

    plumeria "Hey."

    narrator "Her voice is soft. She’s looking past me, back the way we came. I turn to look, and-"

    # "Splash screen of the town below"
    scene cg godigsfel overlook day
    with fade

    narrator "Godigsfel opens itself to my sight like a flower below, rows of pointy red roofs rising like spears unto heaven and crisscrossed by white-stoned streets. At the edges, it fades into green fields and then the brown prickly ocean of the forest."

    narrator "The blue of the sky above is a bold, endless canvas, painted with only the barest white brush-strokes of clouds.The view is pretty good, I have to admit. The noises of the town reach here only as a shimmer of noise, any distinction to it lost."

    plumeria "Imagine how it’ll look even higher up."

    narrator "I merely let out a groan as I sink down onto the top step, staring down at the town below."

    foxglove "You’ll have to just imagine for today. My legs are killing me already."

    narrator "Plume sits besides me, legs sprawling out across the steps below as she supports herself on her elbows. She’s smiling innocently. Too innocently."

    foxglove "...What?"

    plumeria "You know, I asked if you wanted to hear the good or the bad first."

    narrator "Her tone is sweet as poisoned honey."

    plumeria "This is the bad news: you still have to walk back down."

    narrator "The thought of heading down immediately is far too daunting, so after resting for a bit we take a look around the little church built into the mountainside."

    scene bg chapel of the nail
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "The Chapel of the Nail turns out to be bigger than I expected. Inside, the rough-carved stone of the walls extends back into the rock of the mountain itself."

    narrator "The arched ribs of the ceiling give the impression of standing in the chest of some half-buried primaeval skeleton."

    narrator "It’s lit only by the blue light of ghost lanterns with their faintly repellent incense; a hundred years of burnt offerings gives an indelible taste to the air."

    narrator "It’s warmer in here than outside, and combined with the incense it makes it vaguely cloying. We’re the only ones here; every sound echoes strangely."

    narrator "At the far end lies the namesake nail, and-"

    plumeria "Oh, that’s so gross."

    narrator "It’s a nail, but the toe is still attached. It sits like a hunk of crystal on a pedestal, the stone before it worn smooth with the imprint of a million kneeling pilgrims."

    narrator "I step closer to it. My footsteps ring in the empty cloisters of the chapel."

    narrator "Whatever chopped off the toe of the dead god above left a smooth cut, though the way it’s placed I can’t see if there’s bones and veins and stuff or if it’s just one smooth mass."

    foxglove "You think whatever killed him cut it off, or people did to bring it down here?"

    plumeria "Well, there used to be ways of shaping god-flesh, I think. But we can’t do it anymore. Even odds, really."

    narrator "She pulls an exaggerated expression of disgust."

    plumeria "You’d think they could have chosen a better bit to bring down to worship, though."

    foxglove "I guess the ancients were feet people."

    narrator "Plumeria, in a sort of horrified fascination, steps closer to it. She reaches out a hand and touches the deity’s severed digit, brushing her fingertips across dermis and cuticle."

    plumeria "Oh, that’s kind of weird."

    foxglove "Weird as touching dead god toe?"

    plumeria "Hush, you. Come try it."

    narrator "I give her a look, and she makes an impatient beckoning gesture."

    plumeria "It’s not gross, just kind of strange."

    ## Player choice 1; touch the toe or not
    
    menu:
    
        "Touch it.":
            jump do_touch
           
        "Don't touch it.":
            jump dont_touch

    # "[touch it]"
    label do_touch:

        narrator "I look at her for a moment longer, then give in and traipse over to touch the ancient artefact. Where a statue would have been worn smooth by the touch of a hundred thousand beseeching penitents, it has remained as whole and inviolate as the day it was cut."

        narrator "Gingerly, I reach out and press my hand against it. Even through my gloves, it feels cold and smooth, like marble, unyieldingly solid."

        narrator "I poke at the crystalline flesh surrounding the diamond plate of the nail itself and snatch back my hand, the spasmodic reflex of the fingertip in the flame."

        foxglove "It’s- warm, and-"

        plumeria "Weird, right? Like static."

        narrator "I look down at my glove, half-expecting to see the tips discoloured by contact with the divine."

        narrator "Same as always; the only evidence of contact is a faint tingle that remains in the furthest reaches of my hands, so faint I’m not sure it isn’t imagined. I shake my hand to rid it of the feeling, like shedding spider web."

        foxglove "You could have warned me."

        narrator "My grumble has no real heat in it, and Plumeria just grins."

        plumeria "Then you wouldn’t have touched it, would you? And now you can say you poked one of the gods themselves."

        foxglove "Lucky me."

        narrator "Something tickles the inside of my throat, and I cough abruptly."
        
        jump choice_1_end

    # "[Don’t touch it]"
    label dont_touch:

        narrator "I shake my head."

        foxglove "I’m good, thanks. There’s probably been a million grubby hands rubbing all over it for years."

        narrator "Plume makes a groan, amused and disappointed in equal measure."

        plumeria "Aw, too bad. It’s sort of tingly, you know? Warmer than you’d think, too."

        foxglove "Well, now I’m doubly glad I didn’t. That sounds even worse than I expected."

        narrator "Something occurs to me, and I pull an expression of distaste."

        foxglove "Aw, that’s why it’s warmer in here, isn’t it? The air is full of... toe heat."

        narrator "Something about that statement sends my friend cackling with ungraceful laughter. She deliberately rubs a hand on the toe again, and with an evil expression advances on me, contaminated hand held towards me like a weapon."

        foxglove "Oh my gods, you horrible woman, don’t you dare-"

        narrator "She lunges, and I dart backwards, definitely not making a squeaking sound of alarm. She gives an exaggeratedly evil cackle, but stops abruptly when coughing abruptly racks my chest and brings tears to my eyes."

        jump choice_1_end

    # End choice 1
    label choice_1_end:

    plumeria "You alright?"

    foxglove "Urgh, yeah. I think it’s the incense bothering my throat. I’ll be ok outside, I think."

    narrator "I head for the door, and Plumeria trots to catch up, her longer legs easily carrying her to my side."

    foxglove "Maybe I’m a little allergic to it or something."

    plumeria "Maybe you’re actually a ghost and we never realised."

    narrator "I waggle my fingers at her, making a sound like the most half-hearted spectre in existence."

    foxglove "Woooo~"

    plumeria "Consider me spooked."
    
    scene cg godigsfel overlook day
    with fade

    narrator "Outside the air feels deliciously crisp in comparison. Looking back down at the panorama of the town below, I spend a few minutes admiring the view. Eventually, though, I have to stop delaying."

    narrator "I look at the time-worn stairs and remember the aches along my calves."

    foxglove "Alright, well. Let’s get this over with."
    
    # Day 3
    scene bg home night
    with fade
    
    show foxglove at left    
    show plumeria at right
    show grandma at center
    with fade

    narrator "There’s no more fun going down them as there was going up. The next day I don’t do much walking. Perhaps in mercy to my aching leg muscles, it rains. Rather than snow, the sky slashes at the ground with fierce flurries of  heavy raindrops, frigid and fat."

    narrator "Obviously, to try to climb the mountain today would be suicide, never mind the fact it wouldn't be climbing so much as swimming. Simply stepping out of the alcove of the doorway is sufficient to saturate you to the skin."

    narrator "Instead we stay inside, raising our voices over the racket of watery teeth chattering on the window frames."

    narrator "Somehow, the conversation turns to war. My grandmother ponders for a moment, then rises and disappears into her room."

    # TODO: box latching sfx

    narrator "When she reemerges a few minutes later, she’s holding a small metal case. Placing it on the table carefully, she clicks the latches and flips it open."

    plumeria "Oh!"

    foxglove "That’s..."

    grandma "A gun, yes. My service pistol during the war. I kept hold of it."

    narrator "Indeed, inside the box was a blocky steel revolver. It gleamed softly in the light, without a hint of rust or corrosion."

    narrator "The only signs it had ever been taken out of the box were faint nicks and marks in the metal finish, the imprints of fingers rubbed into the cheap sandy wood panelling of the handle."

    narrator "Next to it, in little slotted frames, sat two rows of bullets with shiny brass casings. Ten stubby little brass fingers, tipped in lead, they sat with innocuous ease next to the gun."

    grandma "You may pick it up, if you like. It doesn’t have anything in it; all the same, don’t point it at someone."

    ## Player choice 2: Gun
    menu:
    
        "Pick it up.":
            jump pick_up
            
        "Don't pick it up.":
            jump dont_pick_up

    # "[Pick it up]"
    label pick_up:

        narrator "I look to Plumeria, and she shakes her head slightly. I reach into the box and pick it up, blinking at the weight of it. The grip is coarse against my palm, and fits neatly; all the same, I hold it awkwardly, unsure how to heft it properly."

        foxglove "It’s heavier than I expected."

        narrator "Grandmother let out a small laugh, absent of humour."

        grandma "A gun should always be the heaviest thing in the world to carry."

        narrator "She stares at the thing in my hand with a strange expression. Fondness and hate for it blended like a poison. Uncomfortable, I offer it to her, but she just gestures to the box. With some relief, I stick it back into its little prison."
        
        jump choice_2_end
        
    # "[Don’t pick it up]"
    label dont_pick_up:

        foxglove "I’d... rather not."

        narrator "At this my Grandmother simply gives me a glance."

        grandma "I suppose so. In these times of peace, and such."

        narrator "I can’t understand her tone - does she approve of my choice or not? Her face gives away nothing as she stares gravely down into the box, the revolver sitting innocently in the padding. Has it killed someone?"

        narrator "Has Grandmother?"

        narrator "I find myself unable to ask, and unsure if I even want to. "

        jump choice_2_end
        
    # End choice 2
    label choice_2_end:

    plumeria "If you don’t mind me asking, then - if you dislike them so much, why did you keep it?"

    grandma "Hmmph. I wonder. As a reminder, perhaps."
    
    # TODO: box latching sfx

    narrator "She shuts the box, the latches clack-clacking, but doesn't take it away. One hand beats a pattern on the top like it was recalling some distant marching drum."

    grandma "This gun is nothing more than a theft."

    narrator "I blink at this seeming non-sequitur. Plumeria gives me a tiny confused shrug."

    foxglove "You, er, stole it?"

    narrator "The old woman snorts with exasperated amusement."

    grandma "No, you foolish girl. No, we were allowed to keep them after we were sent home. What I mean is this - this gun and its necessity was a theft from all the people of Tellen."

    grandma "A clever mind designed it. With effort, ore was mined and smelted, the steel shaped. Same with each of the bullets - made, and shaped, and filled, and once fired, gone."

    narrator "She heaves a sigh."

    grandma "It could have been a machine that helped people. A ploughshare. Iron nails. Instead, it is something that can merely destroy other people. It grows nothing and creates only corpses."

    foxglove "Do- do you regret fighting in the war?"

    grandma "Regret? Hmm. I don’t regret fighting, no. It had to be done, after all. I suspect you’ve heard plenty about what was done in the occupied territories. Terrible things, really. Monstrous."

    narrator "She clicks open the case again, to look down at the weapon. One wizened finger brushed along the barrel - along the TELLEN STATE ARMOURY 1191 stamped along it."

    grandma "So I don’t regret fighting to stop them. I regret, however, how it was necessary. All the lives lost, and effort expended, and those terrible hard days... I had hoped that perhaps - we could teach our children well enough they would not have to suffer the same."

    grandma "That foolish girl suffered terribly as a result of her parentage. Having a sarran for a father certainly did her no favours. My generation, who fought and suffered in the war, all carried the pain of that war. I suppose I was lucky, in that sense."

    narrator "She reaches up and raps a nail on the shiny brass of the cap on her broken horn."

    grandma "My own wounds were slight, if permanent. Perhaps they even helped, to some extent. A visible sign that I’d sacrificed in the war."

    grandma "So many had wounds deeper within. They passed down that pain as a warning. But perhaps all we achieved in the end was to ensure our descendants will suffer the same, someday."

    narrator "I open my mouth to speak, and hesitate. My grandmother makes a huff, a short sharp exhalation, and stands."

    grandma "Another cup of tea?"

    foxglove "-sure. Please."

    plumeria "Ah, yeah, that’d be good."

    narrator "She sounds as off-balance as I am. My friend waits for my grandmother to have bustled over to the kettle before she speaks, letting the sounds of the gas stove hissing cover her quiet words."

    plumeria "Have I ever told you your granny is scarily intense?"

    foxglove "No kidding."

    narrator "When she returns with three cups of steaming, fragrant tea, the conversation moves on to other things. Plume spends a while trying to explain her field of study at the university, back home."

    narrator "The study of old miracles and magic, the reproduction of what little can still be done. Trying to relearn how to shape godsflesh for its otherwise impossible properties."

    narrator "Even back in Grandmother’s day, the magic was mostly gone from the world. It had died with the gods, all those hundreds of years ago, when they’d fought each other to the grave - or at least to utterly mortal wounds."

    narrator "The conversation leaves me weirdly melancholic."
    
    scene bg bedroom night
    with fade
    
    show foxglove at left
    with fade
    
    narrator "Eventually, I head off to sleep, and not long later, Plumeria pads in to join me."
    
    show plumeria at right
    with fade

    narrator "Within the bedroom I shared, the air tonight seems thick with heat. Unpleasantly so."

    narrator "Plume lay bundled in the covers, heedless of the warmth. Not sure if she’s awake or not, I whisper her name."

    narrator "She stirs, but her eyes remain solidly shut. Her mossy green hair is spread around her head like a meadow in gloom."

    foxglove "Plume?"

    plumeria "Mmm?"

    foxglove "It’s too warm. I’m gonna open the window, ok?"

    plumeria "Mmm."

    narrator "I wait a moment longer, but when no further answer is forthcoming I slip out and pad to the window. Outside, it’s still and dark. The storm has passed."

    narrator "A few souls had emerged from their homes to light their lamps at some point, and the blue wash of their ghost lanterns flickers fitfully along the streets in irregular blooms of colour.  Condensation studs the windowpane with a hundred tiny gems."

    narrator "The air creeping in was heavy with the scent of just-stopped rain. Bacterial blooms on tarmac. Slick stone. Wet soil. It creeps in without a sound, as if the deluge of the day had washed all the noise out of the universe. I drink it in like nectar."

    narrator "All I can hear is Plumeria besides me, the soft rise and fall of her breathing. Finally she mutters something unintelligible. Strong arms curl around me and pull me close."

    foxglove "Plume...?!"

    narrator "My voice is a strangled whisper. Plume mutters something again, shifts her weight, and is still."

    narrator "She was still asleep. She must have been cold with the window open, though her body felt like a furnace against mine."

    narrator "My heart beats strangely fast. Being grabbed must have startled me more than I thought."

    narrator "Trying to break her hold might wake her up, I reasoned. Best to lie still."
    
    # Day 6
    scene bg pilgrims path day
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "And so the days passed. Each day, we would climb the mountain for a while, seeking higher and higher heights."

    narrator "It was day six when we attempted the trail up to Orchid’s Point. Instead of stairs, it’s simply a rough trail following the slopes of the mountain, ground into the rock and soil with the passage of time."

    narrator "I’m a little surprised to find it easier than the stairs. The path is, like everything else on the mountain, long worn into the sides of it; only short, squishy moss grows along the trail here."

    narrator "No trees grow this high; only a few knobbly shrubs and clusters of whispering bracken. Their long strand-like fronds are studded with pellets of frost where dew has frozen into diamonds."

    narrator "They shudder in the cold wind. So does Plumeria, the breeze running ethereal fingers through her green hair."

    plumeria "Gah! That cuts right through you."

    narrator "She gives me a sideways glance and shakes her head."

    plumeria "I’ll never understand how you don’t feel chilly in moments like this."

    foxglove "Where there’s no sense there’s no feeling, I suppose."

    narrator "She snorts inelegantly as she steps around a mossy hillock. Rocks project from the moss and the ferns underfoot like jagged teeth as we follow a winding path."

    plumeria "Next time we go up I’m going to wear more underlayers. Gods, though, it’s cold enough. Perhaps your spirits can be nice and meet us halfway."

    foxglove "It’d sure save my thigh muscles if they did."

    plumeria "Actually, that’s a silver lining. A few weeks of this and you’ll have killer legs."

    narrator "She waggles her eyebrows at me lavisciously, and I find myself thankful the flush of exertion and brisk air hides any additional blood to my cheeks. Even after two years of her playful teasing, for some reason it never fails to fluster me a little."

    narrator "Maybe it’s because I never had much experience with romance growing up? Either way, I look away and speak my reply into the air."

    foxglove "Yeah, well, at the moment they’re more killed than killer."

    narrator "I hear her amusement, but she doesn’t say anything. For another long while we’re quiet. I find myself enjoying the crisp cleanness of the air and the soft crunch of frosty moss crushing underfoot."

    narrator "All this time, we’ve not seen a single other person along the trail. I’m glad Plumeria came along, even if I’m not sure why. The climb up the mountain would certainly be lonelier without her presence."

    narrator "Sooner than I expected, the trail levels out onto a small plateau."

    foxglove "Oh, wow."

    plumeria "They’re beautiful."

    narrator "Across the plateau, silvery-white flowers are in bloom, a shin-high sea of moon-shaded petals. They ripple in the winds like waves on a lunar ocean."

    narrator "At the centre a small trickle of water coming from higher up, rimmed in by ice, feeds a small pool of glass-clear water."

    plumeria "I guess these are the orchids of Orchid’s Point. Maybe they’re like snowdrops? Late-flowering?"

    narrator "I simply make a hum in response. Carefully, I step through the flower-field, desperate not to crush any of the blooms beneath my tread. Following some strange instinct, I kneel by the pond, briefly pulling off my glove to dip my fingers into it."

    narrator "The water was sharply cold, like a liquid knife. My hand pierces the surface with barely a ripple, reaching down to grasp something gleaming dully amid the pebbles at the bottom of the pool."

    narrator "Shaking off the droplets, I wipe it off on my coat. In my hand is a tiny metal disk, swirled with blooms of verdigris. Half-hidden by the tarnish is a little embossed figure, legs fading into points, face a blank mask."

    foxglove "Hmm."

    narrator "Plumeria watches this with bemusement."

    plumeria "What on earth are you doing?"

    foxglove "There’s a whole bunch of these things in there."

    narrator "She pads over. A small part of me is glad to see she, too, takes care not to trample the floral wilderness around us."

    plumeria "That’s an offering coin, isn’t it? Bet that’s old."

    foxglove "An offering coin?"

    plumeria "Yeah. It’s a sort of effigy. People would offer these in sacrifice to spirits and gods in the place of people."

    narrator "A prickle of unease runs through me."

    foxglove "Spirits took people as sacrifices?"

    narrator "Foxglove, perhaps seeing my expression, laughs."

    plumeria "Children, according to stories, anyway. Anthropologically speaking, probably a good excuse for leaving unwanted kids on the hillside when you couldn’t feed them."

    narrator "University student. Right. She grins, teasing."

    plumeria "What, did you mum never threaten that the spirits would snatch you away if you didn’t go to bed as a kid?"

    foxglove "Ah- no. She didn’t."

    narrator "I see her smile hitch. She scratches at the back of her head awkwardly, but I speak before she can say anything, and if my tone is a little louder and faster than necessary, she doesn’t comment on it."

    foxglove "Anyway, if they do want one, you’ll volunteer bravely, right?"

    narrator "I give my best taunting smile back, and she grins again, wide and relieved."

    plumeria "Please. My nice long legs? I’ll be half-way down the mountain by the time they’ve finished turning you into an icicle."

    narrator "I roll my eyes and toss the effigy coin back into the pool. It spins, once, twice, catching the light with a sharp glint, and sinks into the water with a plop. It settles back amongst the pebbles as if it had never been away."

    plumeria "Not keeping it?"

    foxglove "If we’re meeting them, probably best not to have robbed them beforehand."

    narrator "I look up the slope, towards the snowcap and the undecaying corpse strewn across the heights. Plumeria steps next to me, following my gaze towards the peaks."

    plumeria "Do you really think there’s still spirits up there?"

    narrator "My dearest friend smiles and bumps me with her hip."

    plumeria "Well, let’s not climb anymore today. We’ll have a drink and head back down."

    narrator "We perch ourselves on the rocks and share out a thermos of hot tea. I sip at it, holding the grassy taste of it on my tongue as I watch the susurration of the winter blooms."

    narrator "This high, the sounds from the town have faded into nothing; it’s as if Plumeria and I are alone in the world."

    foxglove "Hey, Plume."

    plumeria "Hmm?"

    narrator "I pause. The words had come out before the thought had finished. There’s a feeling in my chest, but I don’t have words for it."

    narrator "Instead, I just lean against her, my head propped against her shoulder. I hear her intake of breath, and then she rests her head against mine."

    narrator "Neither of us say anything for a while."

    scene bg bedroom night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "Despite my tiredness that night, I sleep poorly. I toss and turn, trying to get comfortable, until Plumeria grumbles discontentedly at the disturbance. Glancing out the window, the moon peeks in through the curtains, casting a slice of the room in silver."

    scene bg home night
    show foxglove at left
    with fade

    narrator "I slip out the covers and stand, padding through into the next room. I stand for a moment, letting my eyes adjust to the dim shapes coalescing into furniture."

    narrator "The ashes in the fireplace still give off a faint heat, the fire now just a few lonely embers amidst the ash."

    # "Grandmother appears suddenly."
    show grandma at right

    grandma "Can’t sleep?"

    foxglove "Gyaah!"

    narrator "My grandmother, seated in one of the plush armchairs close to the fireplace, watches impassively in the gloom as I try to calm my thundering heart."

    foxglove "How- how do you keep doing that?"

    narrator "The old woman huffs in amusement."

    grandma "In the war, I learned to avoid catching attention if I didn’t need to. Less likely to meet a bullet that way. I suppose I kept the habit."

    narrator "She pauses."

    grandma "Also, I’ve been sitting here since you went to bed. I find it easier to sleep in the chair, sometimes, when my bones ache too much."

    foxglove "Oh. Did I- did I wake you? Sorry."

    narrator "She waves a hand dismissively."

    grandma "We’re a family of light sleepers, it seems. Your mother found it terribly difficult to sleep when she was a child, too."

    foxglove "I’m twenty-three, Grandmother. I’m not a child."

    narrator "As soon as I say it, I’m aware of how childish my complaint sounds. The shadowed pool of my grandmother’s face moves in a way that might have been a smile. She chuckles, a desiccated rattle of a laugh."

    grandma "Compared to me, you will be a child for a long time yet, girl. Come, sit."

    narrator "Obediently, I perch on the edge of one of the chairs."

    foxglove "My mother grew up in this house, right?"

    grandma "That is so, yes. She lived here until the day she left Godigsfel and I far behind and went south, though towards the end we barely spoke except in anger."

    narrator "She sighed."

    grandma "I only learned when I got a call from her, telling me she was not returning. We haven’t spoken since, of course."

    plumeria "She kept your number, though. Maybe one day she planned to call."

    grandma "Hmm. Perhaps. I have her number, too. Maybe one day, I planned to as well."

    narrator "She laughs, sudden and startling. This time it is a bitter rasp, as if unwilling."

    grandma "Hmmph. So much for the wisdom of your elders, girl. Both of us, waiting for the other to call first."

    narrator "Her laughter subsides into a weary sigh."

    grandma "Your mother was always very determined. She found this town stifling, I think."

    grandma "There is not much here, beyond Kalarlomoth above, and there was little enough kindness for a child of the enemy. As if she could have had any responsibility for what was done in the war."

    narrator "She almost snarls the word."

    foxglove "Did people... did people treat you badly because your hus- because Grandfather was a sarran?"

    grandma "There were some who tried. But I’d earned a medal or two during the war, and Mica had spent most of it doing farm work on loan from a prison camp nearby, so it wasn’t as bad as it could have been. Also,"

    narrator "She gives a rasping chuckle."

    grandma "They learned that opening their mouth to me to be impolite tended to lead to those words being spoken through broken teeth."

    foxglove "Wow."

    narrator "I try to imagine her even more fearsome in her prime and can’t picture it. Somehow, I get the feeling she’d still wipe the floor with me if it came to a fight. My eyes, adjusted to the dark, can make out her smile this time."

    grandma "Now, it is late. Are you climbing the mountain again tomorrow?"

    foxglove "That was the plan, yeah. ...Sorry. I came all this way to visit you, and I’m spending most of it outside anyway."

    narrator "The old woman waves a wrinkled hand dismissively."

    grandma "It’s fine. Having you and your lively girl in here constantly would drive me to distraction, anyway. I have learned to appreciate the quiet, over the years."

    narrator "I offer a smile, though I suspect she can’t-"

    foxglove "She’s not- she’s not my girl, Grandmother! She’s just... flirty."

    narrator "There’s a moment of silence. I carefully don’t look at the questioning air the shadows have taken on around my elder’s face."

    grandma "...Hmm. Right. Anyway, it’s late. You should be back to bed. Do you want a nightcap?"

    foxglove "A nightcap?"

    grandma "A glass of brandy does wonders, I found."

    foxglove "I-I’ll pass, thanks."

    grandma "Your choice. Go on with you, now. Leave an old woman in peace."

    narrator "I stand, and hesitate for a moment. The words are odd on my tongue after a lifetime, but nice to say nonetheless."

    foxglove "...Goodnight, Grandmother."

    grandma "Goodnight, child."
    
    scene bg bedroom night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "I pad carefully back into the little bedroom I’m sharing with Plume. With my eyes adjusted to the dark, I can pick out the curves of her limbs amid the sheets, the mossy bloom of her hair on the pillow."

    narrator "A sliver of blue light from an outside ghost-lantern casts half her face in aquamarine, like a sculpture. I want to trace my fingers across it, to see if I feel soft skin or hard gemstone."

    narrator "Without warning, my Grandmother’s words come back to me."

    narrator "You and your lively girl."

    narrator "A heat rises in my cheeks and ears."

    narrator "Don’t be weird about this, me. We’re friends."

    narrator "I hover next to the bed, looking down at my sleeping companion. I’m paralysed by a feeling I can’t name."

    plumeria "Mmm... ‘vvve..."

    narrator "My guilty jolt sends me stumbling. I creep back forwards, embarrassment replacing my previous feelings."

    plumeria "Get in."

    narrator "Her voice is low and thick with sleep. Without an excuse, I obediently enter the pile of blankets. I squeak as she pulls me nearer without warning."

    narrator "I hope she’s not awake enough to remember that noise, at least."

    plumeria "‘s cold."

    narrator "She follows up on her complaint by burrowing her face in my shoulder. My heart thunders. I squirm, but her grip is as warm and unrelenting as molten iron."

    narrator "Surely she can hear my heart, punching a drumbeat percussion in my chest."

    narrator "If she does, she doesn’t say a word. Her breathing is slow and steady."

    narrator "She’s asleep."

    # Day 7
    scene bg pilgrims path day
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "The next day, climbing the mountain, my heart isn’t in it."
    
    narrator "I’m distracted, my mind drifting in odd directions."
    
    narrator "Plume picks up on it, of course, and I pretend not to see her questing looks."

    scene bg streets night
    show foxglove at left    
    show plumeria at right
    with fade
    
    narrator "The sun has already begun to go down as we begin heading back through the streets. Part way back, Plumeria hesitates."

    plumeria "Hey, how about a drink?"

    foxglove "Hmm?"

    narrator "She hooks a finger over her shoulder at a nearby building. It’s fronted with thick, frosted glass windows, ruddy light shining from within."

    narrator "I can hear the sounds of a drinking establishment emanating muddily from inside; glasses clinking, bursts of careless laughter, voices raised a touch louder than needed."

    narrator "In this quiet religious town, it makes sense the liveliest place would be the one with all the booze."

    foxglove "...Sure, why not. I could do with a drink."

    narrator "Plume gives a small whoop and punches the air in triumph."

    plumeria "Alright!"

    narrator "Cheerfully, she strides to the door and pushes it open, letting me go first with mock gallantry."

    # TODO: bar noise
    scene bg bar
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "I walk into a wave of solid noise. It crashes against my eardrums, and I rock back on my heels, momentarily stunned by the sheer assault of talking, laughing, clattering."

    narrator "The air is thick and warm, with definite undertones of sweat and spilled beer. The building is almost entirely one big room, filled with a motley assortment of tables, chairs and stools, barely any two the same."

    narrator "A large bartop fills a corner next to a cluster of booths. While it isn’t late, the place is crammed with locals."

    narrator "Plumeria’s mouth moves, but the background racket smears the words into illegibility."

    foxglove "What?"

    narrator "She grins and leans in closer. Her green hair brushes against my cheek, and I fight the urge to twitch at the ticklish sensation."

    plumeria "I guess they prefer gin to gods, huh? Prefer a booth?"

    narrator "I nod fervently, and I feel more than hear her laughter."

    plumeria "Alright! I’ll get us drinks, you get us a booth!"
    
    hide plumeria
    with fade

    narrator "She splits off from me as I shuffle towards the cluster of walled-off tables. Full, full, full..."

    narrator "Ah, none of them are free. I hover awkwardly, hoping one of them would free up, but all the groups sitting in the booths seem pretty entrenched. Oh wait, that one at the end seems empty."

    show fennel at center
    with fade

    narrator "One of them only has a single woman in it, who looks up as I wander up. She considers me for a second, then gestures to the seat opposite. I hesitate a moment, then take it."

    narrator "The woman is pretty cute. Obviously a northerner, with heavy, downwards-kinked horns and startling dark hair and eyes. A pale hand plays with half-empty beer glass. The pale gold fluid inside sloshes too and fro, leaving thin, foamy trails on the sides of it."

    fennel "Hey there! Come here alone?"

    foxglove "Oh! Um, no, I came with- my friend, she’s getting some drinks."

    fennel "Ah, too bad. I was meeting someone here, and I think I’ve been ditched."

    narrator "She gives a languid shrug."

    fennel "Too bad for them. Fennel!"

    foxglove "Eh?"

    narrator "She smiles, showing a thin sliver of white teeth."

    fennel "Names, cutie. Mine’s Fennel. And yours?"

    foxglove "Oh, right, yeah."

    narrator "I laugh, feeling the flush of embarrassment on my cheeks, and tell her my name. To my surprise, she looks thoughtful."

    fennel "You related to that old lady living on Armiger Street?"

    narrator "I have no idea what the actual address is, but saying so would really make me look like an idiot, so I just nod and hope it’s right."

    foxglove "Y-yes? I think so?"

    narrator "The girl nods, satisfied."

    fennel "Yeah, old Mrs. Heath. You’ve got the same eyes. Scary old bird. We all thought she was a witch, growing up. Didn’t know she had family."

    foxglove "Neither did we, until recently."

    fennel "So you came to visit? I knew you couldn’t be a local. I think I’d remember."
    
    show plumeria at right
    with fade

    narrator "She opens her mouth, perhaps to ask more, when Plume shows up at last. She slides into the seat next to me, placing down a pair of white-crowned pints."

    plumeria "Oh, you found a friend! Nice to meet you."

    foxglove "Uh, Fennel- this is my friend, Plumeria. Plume, this is Fennel."

    narrator "The two are looking at each other, taking the other in. Fennel raises her glass in a small salute."

    fennel "Charmed."

    narrator "There’s a moment of silence as we drink. The beer (or is it ale? I can never remember the difference-) is dark and heavy, and faintly warm. It smells earthy, bringing to mind pine trees, and I stare into the oil-black depths of it before I take a sip."

    narrator "My mouth fills with the tang of hops, thick and bitter, and I fight back the urge to wince at the overbearing flavour."

    narrator "Plume notices anyway, and raises a questioning eyebrow."

    plumeria "Not a fan?"

    foxglove "Honestly, it’s a little strong for my tastes."

    narrator "Our new companion looks between us, then pushes her half-drained glass in my direction. Waves dance on the amber liquid in its glass prison from the motion."

    fennel "You can have mine, if you want. Should be a bit more drinkable if you something milder."

    narrator "Perhaps she misinterprets my look of surprise, for she spreads her hands and smiles. She’s wearing a subtle lipstick; I only notice now, seeing the mark it’s left on the glass."

    fennel "I promise I haven’t spat in it, if that’s what you’re worried about."

    foxglove "Oh- no, that’s not it-"

    narrator "Plume cuts in."

    plumeria "I can just get you another. It’s not a big deal."

    narrator "The raven-haired girl merely cocks her head a little in my direction, waiting for my answer."

    ## Player choice 3: Drink with Fennel
    menu:
        
        "Accept the drink.":
            jump accept_drink
            
        "Refuse the drink.":
            jump refuse_drink

    # "[Accept the drink]"
    label accept_drink:

        foxglove "Um, well, cheers."

        narrator "The lighter ale (beer?) is lighter flavoured, less overwhelmingly bitter and into tolerable levels. In truth, I’d always preferred spirits, and the sweeter ones at that."

        foxglove "How about a swap, then, if I’ve got yours?"

        narrator "Fennel shrugs and claims the drink that was formerly mine, taking a swallow."

        fennel "This is the local speciality cask stuff, right? Yeah, they always flog it on visitors. Gods only know why, because it’s definitely an acquired taste, if you ask me."

        plumeria "Seems pretty nice to me. Honestly, compared to some of the things I’ve drank at university parties, this is nothing."

        fennel "You’re a university student?"

        narrator "Plume, perhaps sensing an opportunity, grins. She waves her glass in emphasis, narrowly avoiding painting the already-sticky tabletop with a fresh layer of awful."

        plumeria "Yup. Thaumaturgical History. That is to say- the study of magic back when it was strong and people had magic and miracles just squirting out of every orifice."

        foxglove "I’m consistently amazed at your ability to say the worst things ever. You’d think I’d get used to it, but it never seems to happen."

        plumeria "Please, call me amazing more."

        foxglove "Remind me why I didn’t leave you back home?"

        narrator "Fennel looks between the two of us as we banter, dark eyes flicking to and fro. I’m just taking a sip when she asks a question."

        fennel "So, you two dating, or what?"

        narrator "I choke. The pressure builds in my throat as I try to avoid hacking up a lung. Beer (or perhaps ale) merrily leaps up into my nasal cavity, stinging wildly. Fennel watches me, hand partly raised in the beginnings of assistance and an expression of amusement."

        fennel "That a no, then?"

        narrator "I clear my throat a couple of times, trying to find my voice. I wave off Plumeria’s concern as it becomes evident I’m not about to choke to death in a dingy pub in Godigsfel."

        foxglove "Ah, no, we’re not. We’re friends."

        narrator "The local hums thoughtfully, resting her chin on the back of one snow-skinned hand."

        fennel "Oh ho. Interesting."

        narrator "Before I can ask interesting how, she focuses on me."

        fennel "So she’s a university student. Are you one, too?"

        foxglove "I’m not, no. I wanted to, but, you know."

        narrator "I shrug helplessly. It’s a bitter taste in my mouth, even more so than the tarry black of the beer."

        foxglove "Couldn’t afford the fees."

        fennel "That’s tough. Not like there’s one in this town, to be fair, so I’m in the same boat. Thought about heading down the tracks to someplace else, but this little town is still home, you know?"

        narrator "She rolls the pint glass in her palms, back and forth, dark liquid inside rising and falling as steady as dusk. Foam hisses silently against the glass."

        plumeria "I’ve always felt it’s more the people than the place that makes a home. So even if you’d have left me at home, I’d still have come along."

        narrator "She grins at me. Fennel gives her a look, slightly exasperated, before she sighs."

        fennel "Guess I really do have no luck today. Alright, well."

        narrator "She drains the rest of her glass."

        fennel "Well, nice to meet you both, I guess. Now if you don’t mind, there’s a cutie at the bar looking lonely, so I’m going to try my luck."

        foxglove "Oh, um, bye."
        
        hide fennel
        with fade

        narrator "She winks and is gone, to try her game elsewhere."

        narrator "Good luck to her, I guess...?"

        narrator "I can’t help but feel a little relieved; she wasn’t bad to talk to, but I have no idea how to deal with people like that. Plume flirting with me for fun is bad enough. The aforementioned flirter watches Fennel go with an unreadable expression before she turns to me."

        plumeria "You sure meet different people in pubs, huh. You want to head off, or still up for staying?"

        foxglove "Well, we haven’t been here very long. I’m fine for staying a bit longer."

        narrator "And we do: slowly, we try whatever on the boards catches our attention with strange or interesting names."

        jump choice_3_end
        
    # "[Refuse the drink]"
    label refuse_drink:

        foxglove "Ah- thanks, but I wouldn’t want to deprive you or anything."

        fennel "Suit yourself, cutie."

        narrator "Fennel takes a sip, shrugging lightly."

        narrator "Plumeria nods and stands again."

        plumeria "Alright. Got any preferences?"

        foxglove "Something light, I guess? You can practically chew this one."

        narrator "She laughs and throws a mock salute."

        plumeria "Aye-aye, ma’am. Save my chair."

        narrator "After she’s departed to battle her way through the crowd at the bar, Fennel leans in towards me."

        fennel "So are you two, you know, together?"

        narrator "The question brings inadvertent heat to my cheeks. To cover, I take another sip of the thick black ale. Yeah, it still tastes grim. Bad move."

        foxglove "Ah, no, we’re not - she’s just- we’re just friends."

        fennel "Uh-huh."

        narrator "She gives a slim, satisfied smile."

        fennel "Lucky me."

        foxglove "-eh?"

        fennel "You know, I thought this night might be a bust, but you know..."

        narrator "There’s no mistaking that sort of tone, even for me. She traces a finger along mine, and I try not to jump out of my skin. She smiles at my blush, sharp and teasing, a predator finding prey."

        fennel "I always did like the shy ones."

        foxglove "Ah- um, I-"

        narrator "She leans forward. Her voice has lowered to a husky tone."

        fennel "So how about it, cutie?"

        narrator "A drink slams on the table with a thud. Golden liquid slops from the glass, adding fresh layers of stickiness to the tabletop."

        plumeria "How about what?"

        narrator "She’s frowning down at the local girl. Fennel scowls back, obviously displeased to be interrupted. I take a second to try to cool the flames off my cheeks."

        fennel "What’s your problem?"

        narrator "Plumeria thuds herself down in the seat, close enough to me our shoulders brush. She smiles at Fennel."

        plumeria "Nothing at all. How about what, now?"

        narrator "The two stare at each other for a long moment, the tension increasingly thick, before the local girl lets out a loud and irritated sigh."

        fennel "Ah, what the hell. This night really is a bust."

        narrator "She rises to her feet."

        fennel "At least fuck if you’re going to be possessive. Hey, cutie, let me know if you get bored with greenie here. See you around."

        hide fennel

        narrator "With a farewell flick of her fingers, Fennel stalks off into the crowds, heading towards the bar. Plume watches her go, frowning, then visibly shakes it off."

        plumeria "Friendly locals, huh?"

        narrator "She pauses for a second as I give her back a weak smile. We very carefully do not talk about Fennel’s parting shots."

        plumeria "Sorry I spilled some of your drink. Well, if you still want it. We could head out if you want."

        foxglove "Consider it part of the experience, I guess. Maybe if we’re lucky there’ll be a bar fight and you can knock out someone with a barstool."

        narrator "This forces a laugh out of her - an inelegant snort that widens her eyes in delighted surprise."

        plumeria "Well, you’ll have to back me up. Get ‘em in the kidneys with a broken bottle or something."

        foxglove "It’s a plan."

        narrator "We stay for a while afterwards, though we miss out on any bar fights. Lucky for them."

        narrator "They’re only averaging twice my weight and half a head taller, after all."
        
        jump choice_3_end

    ## End choice 3
    label choice_3_end:

    narrator "We sip at the beers, trying a new variety each glass, before we swap to a different local speciality; a smooth, mellow gin brewed with the little blue winterberries found up the mountain."

    narrator "Without the intense bitterness of the hops, I find it goes down easily from the thimble-sized glasses it comes in."

    narrator "It’s deceptively strong, and soon I find my limbs a touch clumsier than before; my voice comes easier and louder, and a pleasant, fuzzy heat has settled in my bones. Glasses of varying sizes form battlements between my friend and I."

    narrator "Plumeria, an adorable flush across her cheeks from the alcohol, grins at me. One of her hands reaches up to brush back a stray hair, and I’m struck by how pretty she is."

    narrator "Inside, my heart makes a complicated motion. I want to reach up and brush my hand through that green hair. I want to-"

    narrator "Before I can think it through, I start reaching up to do so, only to flinch as my arm knocks some of the glasses standing like soldiers between us. Seeing it, Plume laughs."

    plumeria "Alright, maybe we should make a move."

    narrator "Her words are fond, tone dripping with fake exasperation."

    plumeria "C’mon, you terrible lush."

    narrator "She overbalances when she tries to stand up, and has to lunge to grab the table edge or fall over. It sets me off giggling, and her defensive what only makes me giggle harder."

    narrator "I work my way up from my seat, and together we head for the door, the room wobbling discourteously when I’m trying to balance."

    scene bg streets night
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "The outside, cool and damp, is like stepping into another world after the stifling sweat and heavy heat of the pub. I breathe in deep, feeling it seep into the crannies of my lungs, my chest swelling with the sharpness of it like a breathed-in glacier."

    narrator "Next to me, Plumeria gives an abrupt, violent shiver, like a dog shaking itself off after a dip. I wrap her hand in mine, curling my fingers through hers, and her lips curl upwards."

    narrator "I don’t want her to get frostbite in her fingers, of course, which was the reason I did that."

    narrator "The streets, in contrast to the pub, are quiet and serene. The sun has long since set, of course, and the stars peer down out of a night sky slatted with clouds. The blue lights of the ghost lanterns paints the world in shades of cerulean and azure."

    foxglove "...’s pretty."

    narrator "Plume looks my way, amusement in her expression. The booze has given her a pretty flush across the cheeks, and she nudges against me for no real reason I can tell."

    plumeria "Yeah. I’m glad I came."

    foxglove "I’m glad, too."

    narrator "She hums in acknowledgement, and for the rest of the walk, we don’t talk."

    narrator "But she doesn’t let go of my hand."
    
    scene bg home night
    show foxglove at left    
    show plumeria at right
    with fade
    
    show grandma at center
    with fade

    narrator "We enter the house as quietly as possible, which is not very. Grandmother takes one look at us from her chair."

    grandma "Youths."

    narrator "She shakes her head and waves us off to bed."
    
    scene bg bedroom night
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "I lie tucked against Plume, the sheets heavy and piled high. I can still feel the fizz of the alcohol in my fingertips, in my head, like a distant cloud. I can only just see the ceiling of the room."

    narrator "It’s late, and I should be asleep, but something stops me from slipping off in slumber. Next to me, I can hear Plumeria’s breath, steady and gentle."

    narrator "Without a plan, I whisper."

    foxglove "Hey, Plume."

    narrator "Her breath stills. There’s a long moment of silence before she finally answers, voice husky and low, so quiet even next to her I have to strain to hear."

    plumeria "...Yeah?"

    narrator "I glance over her way. In the soft gloom, I can only just make out the soft curves of her face. Her eyes are still shut."

    foxglove "Why did you really follow me here?"

    narrator "Plume merely hums. I wait for a proper answer before she abruptly opens her eyes. She looks at me sideways, her eye a thin slice of emerald in the dark."

    plumeria "I think... it’s because you weren’t going to come back."

    foxglove "What? Of course I was going to come back."

    narrator "She hums again, a doubtful tone to it."

    plumeria "You’re not a very good liar, I don’t think. Even if you don’t realise you’re lying."

    foxglove "What do you mean by that?"

    narrator "In lieu of an answer, she reaches out and pulls me closer. After two weeks, the feeling of her closeness is comforting."

    narrator "The bed, once so cramped, feels large enough; we slot together like two puzzle pieces. I can feel the motion of her chest as she breathes, slow and measured like the tides of a soft ocean."

    plumeria "We’ve known each other for three years, right? I like to think I know you pretty well."

    narrator "I say nothing. Her heart beats beneath me, steady and strong."

    plumeria "I’m not actually saying you’re a liar, but... how to put this? You’re not very honest with yourself."

    foxglove "...Explain."

    narrator "I feel her grip tighten a little, keeping me pressed against her. Her heart beats against my back, thump-thump-thump, and so does mine in sequence. Plume’s voice is a soft murmur."

    plumeria "I think you’ve always wanted to leave that city behind. I get the feeling, right? Fresh place, fresh start. There’s been something I wanted to ask you about, but I felt like you’d, well, frighten, I guess, if I ever did. I didn’t want you to run away."

    foxglove "I wouldn’t run away."

    plumeria "Wouldn’t you? Wasn’t this? This is what I mean by not very honest to yourself. I think you would have come here, and you would just find reasons not to come back. And you wouldn’t- you wouldn’t be doing it deliberately, not really."

    narrator "I can’t find words to argue against her. Was she really wrong? Truly? Despite my hesitation, she presses on."

    plumeria "Alright, then. I’ll ask you this: what are we?"

    foxglove "Wh-what do you mean?"

    narrator "Her grip loosens. I wriggle free and turn to face her. She’s propped herself up on one elbow, the sheets falling from around her shoulders like a shroud."

    narrator "Her hair, almost black in the dim light, runs in rivulets down her face, but her expression is, for once, not smiling - her mouth is carved into a line, her brows furrowed in serious concentration."

    narrator "In the tight confines of the bed, I’m close enough to feel the ticklings of her breath on my face."

    plumeria "We’ve been close for years. You’re interested in women. You react when I flirt. We hold each other in bed every night. Are we friends? More? Less? What do you want?"

    narrator "My mouth works. I want to say a dozen things, half of them contradicting. They stick and stumble on my tongue, saying nothing. My mind is a hiss of white noise. We’re friends- more- we’re- we’re-"

    narrator "Plumeria smiles gently. Her eyes seem terribly distant. They’re windows into prehistoric forest, the green of leaves hiding what lies among the roots. Her voice is slow and calm, as if she didn’t want to spook an animal."

    plumeria "I didn’t want to scare you away, or push you into something you didn’t really want. But you were going to go away, and I couldn’t wait any longer to see if you were ever going to do something about it."

    foxglove "Oh, Plume."

    narrator "It’s about all I can say. There’s a horrible, yawing, wretched feeling inside, swallowing anything I want to speak. I slump forwards towards her, hiding my face against her chest.."

    foxglove "‘m sorry."

    narrator "The words come out muffled, but I hear as much as feel the intake of breath. A hand runs soothingly across my hair, tracing the root of one of my horns."

    plumeria "No, it’s ok. It’s not something you need to be sorry for."

    narrator "There’s a sort of resignation in her tone, and at it something hot and ugly jabs at my stomach. I push myself up until we’re face to face. There’s no distance at all between us. Our noses are practically rubbing. Her face fills the world."

    foxglove "I’m not- I’m not saying no to anything, ok? Give me - I’ll give you a proper answer. But let- let me think of what to say first, please."

    narrator "Her hand cups my cheek, tenderly. At first I think she’s moving in to kiss me, and I shut my eyes in preparation, but she just presses her forehead against mine."

    narrator "When I peek, her own eyes are shut, and some of the familiar amusement has come back to her features."

    plumeria "Never do today what you can do tomorrow, huh?"

    narrator "She grins at me with all the familiar cheekiness. I find myself smiling back."

    foxglove "That’s the plan."

    narrator "With exaggerated casualness, she stretches sinuously and yawns."

    plumeria "Alright. Well, it is late. Do you want me to go? I can sleep in one of the armchairs if you’d like."

    foxglove "Ah, no, no! Stay. Please."

    narrator "She simply smiles."

    plumeria "As you command. Now, come here - I still need to steal your body warmth."

    # day 8
    scene bg bedroom day
    show foxglove at left
    show plumeria at right
    show grandma at center
    with fade

    narrator "The radio mutters angrily. The voice of the spokesman is a hoarse, rumbling thing, seeming half-way to a snarl."

    radio "...forecast to arrive within the next few days. Heavy rain or snow, depending on location. Authorities have warned those in the path of the storm to prepare. Each household should stock at least a week’s worth of food and water..."

    narrator "I listen to the gruff voice of the spokesman with dismay."

    grandma "...Hmmph. Looks like you might not be able to climb it after all. A shame, but such is as it is."

    narrator "She’s seated in one of the armchairs in the main room, a cup of steaming tea gently releasing its vapours at her elbow. Her eyes are shut, listening to the radio, and she doesn’t look at us as she talks. Her tone is perfectly matter-of-fact, but I shake my head in denial."

    narrator "...Her eyes are shut. Plumeria snickers silently at me, and with a quick safety check Grandmother’s eyes are still shut, I make a rude gesture at her. She mimes an exaggerated expression of shock until I roll my eyes and she breaks out into a grin."

    narrator "Trying to stab Plume with my eyes alone, I give a verbal answer instead."

    foxglove "There’s still time. Arriving within the next few days, it said. So as long as we reach the top today, it’s not a problem. We’ll be up and down before any bad weather arrives."

    plumeria "I guess. We might have to stay overnight. There’s a little cabin at the top, if I remember correctly. Climb up, say hello to your icy friends, climb down in the morning. Should work."

    narrator "My grandmother frowns. Her eyes open, the crows-feet deep at the corners."

    grandma "The weather can change very quickly in this region of the world. That goes double for the mountain-tops."

    foxglove "I can do it, Grandmother. I know I can."

    narrator "When she still seems unconvinced, I click my fingers."

    foxglove "Look, we’ll stock up on emergency stuff, right? We’ll have flares and things, there’s a cabin right up there for difficulties. If the spirits are there, they’d want to help, right? They did for my ancestors."

    narrator "The old woman pins me in her gaze for a moment longer, before she sighs. For a moment, she looks tremendously old. Tired. Weathered, like the mountain itself - worn down by a thousand storms."

    grandma "Very well. You are both adults, I suppose, and can look after yourselves."

    narrator "She throws the battleaxe of her line-of-sight at Plumeria, who bravely doesn’t quail before the force of it."

    grandma "Do you remember what I said to you, Miss Feld?"

    plumeria "Ahaha. Ha. I sure do, Ma’am, don’t you worry."

    narrator "Her slightly nervous laughter ratchets itself like the mechanical splutters of a failing engine as I glance out the window. The sky aches with gloomy grey clouds, but the air itself is still and dry."

    foxglove "Well, if time is short, I don’t want to delay. We’ll head out in a minute, then?"

    narrator "Plume grabs the lifeline with unconcealed relief."

    plumeria "Yeah, sounds like a plan. I’ll just grab our kit from our room."

    narrator "Rapidly, she retreats from the room."

    grandma "Child. Are you sure?"

    narrator "I meet her gaze. Her eyes are the same violently purple as mine - undimmed by age, they glitter like amethysts in the crags of her face."

    foxglove "Yeah, I am."

    narrator "I’m almost surprised to find I mean it. But I’ve been clambering up and down that big dumb rock for the past week. Plumeria’s with me; I couldn’t ask for better company."

    narrator "Something pulls me onwards, like I was always meant to climb the mountain. I guess that’s the weight of family legacy, or something along those lines."

    grandma "Hmmph. Then go on, then. I’ll see you when you get back."

    narrator "She pauses, and then adds:"

    grandma "Be careful."

    foxglove "I will, Grandmother. ...Thanks."

    narrator "I open my mouth to say something more and hesitate, unsure of what I even wanted to say in the first place. I’m saved from my indecision by Plume coming out of our room, a couple of backpacks in hand and coats draped over her forearms."

    plumeria "Alright, let’s make a move."

    narrator "After a final goodbye, we let ourselves out."
    
    scene bg pilgrims path day
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "We set a hard pace. The cobbles of the roads fade to the weary worn surface of the steps. The faint burn in my thighs from climbing is nothing in comparison to the first attempt, now, and I stomp my way up with a steady tread."

    narrator "Plume and I don’t talk much. Perhaps she can sense my determination; perhaps she’s just saving her breath for the trail."

    narrator "I find myself casting constant glances at the sky. It’s almost entirely clear, with only a thin grey ache of clouds in the distance, but I’ve been told enough that the weather can change in a heartbeat up the heights."

    narrator "We pause for lunch at the little plateau among the orchids. Frost beads like jewelled spider webs across the leaves and fat-bodied petals. Looking at them now, I notice the fine hairs on every leaf. I guess even plants have fur if it’s cold enough."

    narrator "Perhaps regretting her own lack thereof, Plume is sitting with her hands curled around a cup. Steam dances from the top of it like winter ghosts."

    plumeria "Sure is cold today."

    narrator "Now we’ve stopped for a bit, I can tell she’s right. The sweat of the exertion of the rapid climb clings to me unpleasantly, sapping my heat like tiny icy ticks."

    narrator "I shudder, more at the imagery my brain conjures of that than the actual temperature, but Plume notices."

    plumeria "Wow. If you’re shivering, it really must be cold. If I freeze solid, I give you permission to market me as the world’s most beautiful ice sculpture."

    narrator "I roll my eyes and in retaliation inflict the image I’m picturing on her, and she pulls a disgusted face. She casts a wary gaze on the vegetation around us."

    foxglove "Relax. There’s no way bugs would live this high up, in this temperature."

    plumeria "Yeah, well, we thought that about orchids, too, and they don’t flower for no reason."

    narrator "She slops the dregs of her cup out onto the ground and rises to her feet, carefully brushing herself off."

    plumeria "Well, no point sitting about. We've still got a big rock to climb."

    narrator "And so we do."

    narrator "The path winds up and up, getting steeper and rockier, narrower and more twisted, until it’s little better than a trail."

    narrator "The snow on the ground becomes thicker, changing from winter precipitation to permafrost. It crunches under our steps, unmarked and unsullied before our boots."

    narrator "It’s perhaps mid-afternoon by the time we reach the Aumic Temple. The mountain here had a sort of slot carved out of it, long ago, by the final battles of the gods, and the Temple sits in like a wedge in the cleft in the stone."

    scene bg aumic temple day
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "Like the Chapel of the Nail, it’s half underground. We force open the heavy wooden door, staring into the cool dark inside."

    narrator "The walls are covered with carved frescoes, the roof supported with angular statues of the god above. Little side chambers lead to sleeping hollows for pilgrims."

    narrator "The roof is unpleasantly low. Rather than an ordinary building, it’s built like a tunnel, hewed out and repurposed, and I don’t like it much. It feels more like a crypt than a place to stay.."

    foxglove "Staying here tonight?"

    plumeria "It’s that or a tent, and I think these walls might be a bit better than canvas at blocking the wind."

    narrator "I unsling my bag and tuck it in one of the chambers. No sense dragging our sleeping gear up the mountain just to bring it back down a little bit later. Plume’s still got the essentials."

    narrator "With no divine toe to provide horrible but useful warmth, it’s just as cold inside as it is outside, and with time ticking, we don’t have much reason to stay. We can have a proper look at the frescoes and statues tomorrow."

    narrator "Decided, we move on."
    
    # TODO: wind noise should increase
    scene bg pilgrims path day
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "The last portion of the climb is viciously steep. We don’t walk but clamber awkwardly, scrambling over dyed-white stone."

    narrator "The air seems thinner, breaths shallower, but I don’t slow my pace. Something drives me on, on, until I’m panting, sweat slick around my spine prickling like needles."

    narrator "We pass the highest construction on the mountain - a squat little survival shack, so mountaineers caught in squalls might have a chance not to die from exposure and cost the town in getting them back down."

    narrator "It’s a little wooden construction, the walls low and angled against the wind."

    plumeria "Want a look?"

    foxglove "Nah. We’re almost there, anyway."

    plumeria "Think they’re about?"

    narrator "She doesn’t have to say who they are, of course. I’ve not seen any sign of them so far, but who knows?"

    narrator "I let Plumeria pull me up onto a crag and look. The ground here is flatter, a little plateau near the peak of the mountain."

    narrator "Draped across the terrain is a corpse. The corpse, perhaps. This close, the body has a sort of lumpenness to it - as if it was shaped out of clay a little less delicately, less detailed, than us."

    narrator "No spirits appear. It’s just us and Kalarlomoth."

    foxglove "Spirits?"

    narrator "I call, and immediately feel foolish. Only the breeze, sharp and astringent, moves the world around us. Plume waits a moment longer for ancient creatures of myth to spring out from behind a boulder, then shrugs."

    plumeria "We can check tomorrow morning before we head back down."

    foxglove "I guess. Maybe they’re not around any more."
    
    scene cg the dead god dusk
    with fade

    narrator "The giant body of the god lies dead and still before us. No snow settles on his crystalline flesh, melting away silently like a dream whenever flakes settle on the divine cadaver."

    narrator "I can see the terrible rift in it, where something I can’t imagine had sliced open the chest of him and cast him down. A great empty hollow sits exposed where the heart would be. Was this what killed the god, in the end?"

    narrator "There’s a feeling in the air - almost a sound, but not quite. I don’t hear it with my ears, but with my soul. It feels-"

    narrator "It feels-"

    narrator "Sad, perhaps. A deep and aching grief. An echo of a pain faded but never quite gone. A regret so potent it’s stained the very world and never washed away and never will."

    narrator "Kalarlomoth, a thousand years destroyed, still seeps his sorrow into the mountain. It seeps into me, caught in the air like stars in the distant heavens, like dust in an abandoned home breathed in now the air was stirred."

    narrator "My feet carry me around the colossal wreck. Finally I reach the head, the great smooth plane of the face. What I think might be eyes are closed. I don’t know if I should be glad or not for that."

    narrator "The mouth lies open slightly, revealing the peaks and troughs of sharp, triangular teeth, like a shark. Did the gods eat? I don’t remember."

    narrator "I pull off a glove and gently place my fingers on the face of the divine. It’s warm, but only just; the lingering heat of ashes in an extinguished fire."

    narrator "I hold my hand there for a moment longer, then let it drop. The mineral flesh shows no sign I’ve ever touched it at all."

    narrator "For a moment, I feel terribly, terribly sad."

    narrator "I turn away. Plumeria is there, studying the dead god with unbridled interest. She’s even gotten a little sketchbook out and is scribbling in it."

    narrator "Seeing me turn away, she looks up."

    plumeria "Hell of a sight, huh?"

    foxglove "Yeah. I guess so."

    narrator "Perhaps more emotion leaked into my tone than I intended, as she looked at me again before sticking the notebook back in her pocket."

    narrator "Despite whatever heat the god might be giving off, the temperature feels like it must have dropped. The wind is blowing stronger."

    plumeria "You alright?"
    
    scene cg godigsfel overlook night
    with fade

    narrator "Not trusting words, I simply nod. Looking out from the mountain, the sun is low in the sky. It paints the canvas of the sky in hues of purples and reds like a bruise."

    narrator "Shadows are painted across the land, dipping black paint across the fields and forests spread out below."

    narrator "In the matchbox city of Godigsfel below, already I can see the eerie blue light of the ghost lanterns."

    narrator "With the sun so low, so is the temperature. The wind is tossing our hair, hissing viciously in our ears. I shake my head."

    foxglove "Can you feel it?"

    plumeria "...Yeah."

    foxglove "It’s sad."

    plumeria "...Yeah."

    narrator "She pulls me into a hug, and I wrap my arms around her. We cling to each other at the top of the world."

    narrator "I pull away. The wind is screaming a low, choppy howl, catching the powdery snow around us and tossing it about. Plume shivers through her coat."

    foxglove "Well, no spirits. We should get back to the Temple before the weather gets worse."

    plumeria "No argument from me there. Damn, but it’s getting cold."
    
    scene bg pilgrims path night
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "I give the dead god a final look, examining the silent gasp of the expression one last time, looking for something- I don’t know. But whatever it is, I can't find it, and finally I turn away."

    # TODO: the wind becomes DEAFENING here sfx

    narrator "It’s not far back down the trail when the wind abruptly kicks up, hard enough I stagger against the sudden force. Plume cries out in surprise. Ice shrieks as it's pulled from the ground, whirling around us trapped in the eye of the storm."

    plumeria "What the h- when they say weather changed quick, I didn’t think they meant this quick!"

    narrator "Her voice trembles even as she tries to make a joke of it."

    foxglove "Plume! Look!"

    narrator "Shapes are moving in the bleak fog of the snowdrifts, and I jab at the motion with an outstretched finger. Plumeria looks at what emerges. For once, her words fail her."

    scene cg spirits night
    with fade

    narrator "All around us, figures seem to loom out of the snow. One, three, five- they surround us, still and silent, their frigid bodies shining like the bellies of glaciers."

    show foxglove at left    
    show plumeria at right
    with fade

    plumeria "Oh, my gods. Spirits- they actually exist-"

    narrator "Their voice - voices? - ring out about us, every syllable a violent crack of breaking ice. The sound of it is sharp, almost painful, and instinctively I shrink closer to Plumeria."

    foxglove "You know who I am?"

    narrator "The air is so frigid, now. The fog gets thicker, like the spirits have drank the world. We are surrounded by it, like a cocoon of cold."

    foxglove "What- what are you talking about? Why did my mother come here? Why did she leave?"
    
    # TODO: spirit hissing sfx

    narrator "The spirits around us hiss, a sibilant sound of snow sliding on snow. My heart pounds in my throat. Plumeria is staring out at the apparitions about us, her arm half-raised in front of me."

    plumeria "Are you going to answer her?"

    narrator "Her shout is attempting to be brave, but I can hear the slick undercurrent of fear in it. Her eyes are wide and flicking back and forth."

    narrator "The spirits hiss again."

    plumeria "D-don’t threaten-"

    foxglove "What- what bargain?! What are you talking-"

    narrator "The lead spirit levels an icicle-like finger at my chest. I feel it like a bullet. My blood is icy slush. My organs feel frozen. My heart hammers in a glistening cage."

    narrator "I slump to my knees in the snow. It’s doing something. In a frantic motion I tear off my gloves. The tips of my fingers are crystalline and clear, the nails a diamond fleck. Like ice. Like a spirit."

    foxglove "Ah- ahhh-"

    narrator "Plumeria crashes to her knees besides me. She grabs at my hands and looks up to scream at the wintery ghost-figures around us."

    plumeria "Stop it! Stop!"

    narrator "The icy transformation is creeping further up my fingers. My toes tingle ferociously then go numb."

    plumeria "She doesn’t belong to anyone!"

    narrator "She scrambles through her bag, spilling the contents into the snow; water bottles and snack bars, a coil of the blue incense, the four cylindrical emergency flares, absurdly candy-red against the snow."

    narrator "She snatches one up and cracks it. Abruptly the scene is cast in harsh red light. It hangs on the fog like a mist of blood and turns the spirits to ruby statues, sanguine and merciless."

    plumeria "Get back!"

    narrator "She thrusts it towards them, and they drift back a little where she jabs, floating closer where she doesn’t. She’s panting harshly, her eyes wide and terrified in the flare-light. She tugs at my shoulder."

    plumeria "Come on, get up! We’re going! Don’t try to stop us!"

    narrator "All around us, the inhuman creatures close in, the teeth in a tremendous set of jaws."

    narrator "One lunges from behind, a hissing, embodied avalanche, and Plumeria cries out as she whirls. The flare strikes it in the face and it staggers back, emitting an awful, cracking shriek, a breaking ice sheet, but the flare gutters and another spirit reaches forward."

    narrator "It doesn’t claw or rend Plumeria. It simply places a hand on her chest. The colour drops from her face. Blue spreads on her lips like a bruise. Without a word, she collapses backwards into the snow. The flare goes out. The contrast leaves me blinded."

    foxglove "Plu-Plume..."

    narrator "I force myself to move. My hand fumbles in the snow. It takes three tries for my fingers to close around the second flare. They’re crystal down to the palm, now, and gripping the flare I feel nothing at all from them."

    foxglove "Y-you... monsters..."

    narrator "Sight returns against the dimness of the fog. The spirits float soundlessly closer. They stare down at me, a wall of frozen bodies all around, close enough I could reach out and touch their angular forms."

    narrator "The air rasps daggerlike in my throat. Every breath seems to leave me more airless than before. I force my other hand to the cap of the flare."

    foxglove "N-no..."

    narrator "I grip the cap. It shifts, grates against the tip, ready to spark. The motion takes a thousand years. I am cold beyond cold. Plumeria is motionless. The shadows pool in her eyes and make a funeral mask of her face."

    narrator "Oh, dead and distant gods, let her live."
    
    # TODO: flare pop oneshot sfx
    # TODO: flare burning sfx

    narrator "The flare ignites beneath my twisting grip. The monsters around me recoil and begin the lunge, but the split second is enough."

    narrator "I stab the flare downwards like I’m trying to pierce the heart of God and plunge it into the incense. It ignites under the ferocious heat of the flare and I choke on the sudden rush of the fumes."

    narrator "I topple backwards, coughing. Where my fingers had crystallised, they sting furiously, acidic pinpricks everywhere the smoke touches, but the pain is sensation and life and I seize on it."

    # TODO: spirits scream sfx

    narrator "The spirits scream, a furious animal sound, wrenching themselves backwards in great jagged motions away from the incense, their immortal grace melting away."

    narrator "I force down coughs from the acrid smoke and scream back. Abruptly I am no longer scared - no, I am, but it’s buried beneath a great red fury, that these monsters would decide I belong to them, that they’d try and hurt my dearest and most important person."

    narrator "I snatch up the third flare and it comes into furious crimson life beneath my grip. I hurl it at the spirits and they flinch away from it, reflexive and phobic, a brand splitting the dark."

    foxglove "No, I’m not! I didn’t agree to anything! I’m not- I’m not my mother’s to give away!"

    narrator "The spirits howl, a mad, baleful chorus, and I light the last flare. The light tessellates through my frozen fingers."

    foxglove "So leave us alone!"

    narrator "I wind back my arm and throw the last flare. It flies straight and true and cracks against the leading spirit’s head, bursting in a shower of ruddy incandescent sparks. The spirit screeches and retreats, and the others follow, disappearing into the mist."

    # TODO: stop flare SFX
    scene bg pilgrims path night
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "I watch them go, panting, fighting the urge to pass out. When the fog begins to break apart, and I’m sure they’re not coming back, I drop to my knees."

    foxglove "Plume!"

    narrator "I snatch at her shoulders. Her eyes are shut, her expression a wax mask."

    foxglove "Oh, gods, please don’t be dead-"

    narrator "I press my head against her chest, feeling the crunch of ice where the spirit had touched her, but I can’t hear a heartbeat through her coat and my own blood pounding in my ears."

    foxglove "Come on come on-"

    narrator "I hold my head next to her face and I feel a faint tickle of breath on my cheek. The rush of relief I feel nearly makes me collapse forwards."

    narrator "I have to get her somewhere warmer."

    narrator "The little survival cabin not far below. That’d be out of the wind, at least. I grab the survival blanket, forcing it into a pocket, and hook my arms under Plumeria’s shoulders."

    foxglove "Hold on, Plume, I’ll- I’ll get you safe-"

    narrator "I drag her for a thousand years until the little hut looms up. I fumble one handed with the handle, and shoulder open the door, ignoring the bloom of pain from ramming the heavy door."

    # TODO: door slam oneshot sfx
    # TODO: windows rattling sfx
    # TODO: muffled, howling wind sfx
    scene bg cabin dark night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "A tiny bit of colour has returned to Plumeria’s lips as I slam the door and lay her down. That must be a good sign, right?"

    narrator "I don’t really know. I don’t really know what to do."

    # TODO: foil blanket crinkle oneshot sfx

    narrator "I pull out the survival blanket, unfolding the crinkling foil, and wrap Plumeria in it. I turn to the fireplace, scraping out the snow that had come down the chimney with my hand."

    narrator "The hewed logs from before are of course still there, and I pile them and kindling in before I strike a match. The first breaks, and the second, and I nearly scream with frustration before the third catches."

    # TODO: fire roar oneshot sfx
    # TODO: fire crackling sfx
    scene bg cabin lit night
    show foxglove at left    
    show plumeria at right

    narrator "I nurse it in the kindling, building the fire until it’s fiercely licking yellow tongues across the chunks of timber."

    narrator "I check back on Plume. My fingers are still changed, and I can’t feel heat or cold with them, so I press my forehead against hers. Still freezing cold."

    narrator "I remember what I see in films in this sort of situation, and I pray that it’s not just made up, that I won’t do more harm than good."

    narrator "There’s no room for embarrassment, and I mutter an apology as I strip us both and huddle under the blanket with her, cradling her between my arms in a reflection of the previous night."

    narrator "All I keep on is Plumeria’s gloves; I’ve left mine back up the mountain. I don’t know how cold my frozen fingers are to touch. I don’t want to make her worse."

    narrator "Something occurs to me, and I smile faintly. Something between a laugh and a sob bubbles up from my chest."

    foxglove "You said you’d steal my body heat. So here. Take it all."

    narrator "I bury my head against her shoulder. She feels desperately cold against me, and I will my heart to be a furnace, my bones an inferno, if just to keep her warm."

    foxglove "Just be okay..."

    narrator "I don’t know how long I huddle against her, my eyes screwed tightly shut against the world. Slowly, she stops feeling so cold. Finally she stirs. A low, slow groan creeps out her like the hinge on a coffin."

    plumeria "Wha...?"

    foxglove "!"

    plumeria "What’s...?"

    foxglove "Plume! Oh, thank- thank the gods-"

    narrator "She wriggles around in my grip. At the sight of her face, colour mostly returned, heavy bags under her eyes, I feel tears begin to well up in my eyes."

    foxglove "I thought- I thought-"

    narrator "Gently, if a tad unsteadily, she tugs at an arm until she has a hand free. She brushes a thumb across my cheeks, wiping away the tears on my cheeks. Her voice is hoarse, but tender."

    plumeria "Hey, hey, it’s okay. I mean, I feel terrible, but-"

    narrator "She blinks and looks around at the inside of the little cabin, then down at the slivers of bare flesh she can see beneath the blanket. Her eyebrows raise, but what she chooses to ask is:"

    plumeria "We got away?"

    foxglove "The- the incense. It drove them off, and I threw the other flares at them. And I dragged you back here, and you were so cold, and I didn’t know what to do, so I-"

    plumeria "Hey, it’s ok. You did good. Besides..."

    narrator "She grins up at me, unsteady but alive, alive, alive."

    plumeria "I had a dream not far off this the other night as well."

    narrator "For a long moment, I’m dumbstruck. I stare at her, and she looks back, already returning to her signature look of confident amusement. A laugh shudders its way out my mouth involuntarily, and I let my head fall forward to rest against her shoulder."

    plumeria "Oh, my gods. Now I really do know you’re feeling better."

    narrator "She laughs, then quiets. I feel her hand wrap around my back, pulling me closer."

    plumeria "I thought I’d die."

    narrator "Her voice is a tiny thing, terribly delicate. She whispers, because trying to say it louder would break it apart."

    plumeria "When that thing touched me, it was so cold I don’t have the words. It felt like- it felt like my heart stopped."

    foxglove "If you’d died, I would have- I don’t know. I’m just- I’m just so glad you’re not dead."

    narrator "I feel her chuckle rumble in her chest. Before, there was no time for embarrassment, but now, it seems, there’s space on the clock. She pulls back to look me in the eye. The firelight frames her face through gaps in the green hair hanging down like a curtain."

    plumeria "I’m pretty glad I’m not dead, too. Same for you, too. I’m happy to see you’re not a walking ice sculpture."

    foxglove "Well, not for the most part, anyway."

    narrator "I wiggle one of my hands up to my mouth and use my teeth to pull off a glove. She frowns down at my transfigured hand. I can see her refracted through the translucent digits, and she gently takes hold of them with her own."

    plumeria "How do they feel?"

    foxglove "Not much of anything, to be honest. I can barely tell you’re touching them. Are they... well, cold?"

    plumeria "Yeah. Not quite as cold as ice, I don’t think."

    narrator "She hesitates, and then, as delicately as if they might shatter in her grip, presses her lips to the crystal tips on my fingers. As if transferred, the heat blooms in my cheeks instead."

    narrator "No more delaying. I’ve survived a near-death experience. I’m already skin-to-skin. She’s been flirting with me for literally years. Come on."

    narrator "Plumeria’s breath hitches in just a little, and then she smiles."

    plumeria "I’m listening, miss Feld."

    ## Player choice 4: smooch
    
    menu:
    
        "Admit your feelings.":
            jump feelings
            
        "Just kiss her already, dumbass.":
            jump kiss

    # "[Admit your feelings.]"
    label feelings:

        narrator "I take a deep breath. In and out. My gaze is trapped by hers. They are a deep and verdant sea, and I gladly drown in them. I feel the warmth of her breath, her body."

        narrator "I begin, my words slow and careful."

        foxglove "You’re my very best friend, Plume. I really don’t know what I’d- what I’d do without you. You’re always so-"

        narrator "I break off. Plume watches me steadily, the corners of her mouth curved in a small, secret smile, for this moment, secret for just the two of us."

        foxglove "What I’m trying to say is- what I want to say is-"

        narrator "Come on. Say it, already."

        foxglove "I guess I love you, Plumeria."

        narrator "Plume smiles, wide and almost proud. She curls her hands around the back of my neck, cradling my head. Her voice is low, a husky whisper, and the sound of it lights fires inside I don’t have a name for."

        plumeria "Can I give my answer to that, now?"

        foxglove "Y-yea- mmfh!"

        narrator "She’s gently but firmly pulled my head forward. Her lips press against mine, muffling my words. They’re soft, and warm, and it sends prickles of weird heat radiating through me from the very core."

        narrator "She kisses me again, and again, and again, until I’m half-dazed with it. Finally, she pulls back a little. I pant softly as my lips are freed. Her own are red and kiss-swollen. She grins, pure Plumeria mischief written on it."

        plumeria "Left you breathless, huh?"

        foxglove "Oh my gods, you dork."

        narrator "She chuckles and steals another. She glances down, at our bare bodies beneath the crinkly aluminium blanket, deliberately dwelling at where we’re pressed together."

        narrator "I follow her gaze and flush. She grins wider at my embarrassment, and deliberately wriggles."

        plumeria "You know, we’re already naked."

        foxglove "Ye-yeah. We are."

        plumeria "Foxglove."

        narrator "Her saying my name sparks in my brain. I stare at her, wordlessly, hoping to push all my feelings for her through the strength of my gaze alone."

        foxglove "Plume..."

        plumeria "Can we?"

        narrator "There’s no doubt as to what she means. I give a tiny nod. Very gently, she leans in and kisses me again. I wrap my arms around her, pulling her closer, closer. Her hands trace across my shoulders, my back, and down."

        narrator "My dear Plumeria."

        narrator "And for a while, there aren’t any words at all."
        
        jump choice_4_end

    # "[Just kiss her already, dumbass.]"
    label kiss:

        narrator "For a moment I search for the words, but then I give a tiny shake of my head. My voice had always failed me before, so I tell her through another way."

        narrator "Gently, nervously, I free my hand from her grip. I run my crystalline fingers down the back of her head, letting the soft green hair trace between my fingers. Plume is very still. Only the soft press of her chest lets me know her heart is still beating."

        narrator "I listen to it, fast and excited. I guess maybe she’s nervous, too."

        narrator "I draw her head downwards, leaning up. Slowly our lips touch. I kiss her, once, and pull back to see her face, and her expression is so tender I almost want to cry."

        plumeria "That’s your answer, huh?"

        narrator "Her voice is a husky whisper, and something about it sends sparks right from my core to the very tips of my extremities. Even my changed fingers tingle with it. I have to swallow before I can answer."

        foxglove "If- if it’s unclear I can try again."

        narrator "She chuckles, low and delighted, at my clumsy flirt."

        plumeria "I think it might be a good idea, yeah. Clear any uncertainties."

        narrator "I lean up and kiss her again. She catches the back of my head and neck with her hands and kisses back. Again, and again, until I’m panting, kiss-drunk."

        narrator "Plume smiles down at me, face flushed, indescribably lovely. Our heated bodies nearly burn where they’re in contact, skin against skin."

        foxglove "Plume, can we..."

        narrator "I trail off, but the question is obvious. She presses another kiss to my lips, resting her forehead against mine."

        plumeria "You sure?"

        foxglove "Y-yeah. I want this."

        narrator "She pauses mischievously, grinning at me through her reddened cheeks and quickened breaths."

        plumeria "I should have suggested mountain climbing sooner if this was the outco-"

        narrator "With an exasperated giggle, I seal her lips with my own. I wrap my arms around her, pulling her closer, closer, and I feel her hands trace across my shoulders, my back, and down."

        narrator "My dear Plumeria."

        narrator "And for a while, there aren’t any more words at all."
        
        jump choice_4_end

    # End choice 4
    label choice_4_end:

    # Day 9
    scene bg cabin day
    with fade
    
    show foxglove at left    
    with fade

    narrator "Consciousness comes slowly, like meltwater dripping from ice. There’s aches in my arms and legs like I’ve run a marathon; other places, too, in ways that aren’t entirely unpleasant. My back clicks horribly as I stretch from where I’ve slept on the hard floor."

    narrator "The light in the little shelter is dim, mottled red-blue from the light peeking through the door slats and the little fire burning in the hearth. Cold air whispers around my shoulders, reminding me of my nakedness and-"

    foxglove "Plume?!"

    narrator "She’s not in the little building. Quickly, I fumble around for my clothes. They’ve been piled neatly by the fire, close enough to absorb the warmth, and I get them on as soon as possible."

    narrator "My transformed fingers catch the light, refracting the fire into prisms that dance around the room and some part of me notes that means they’re probably never changing back."

    narrator "I take quick steps towards the door when it starts to swing open, and I have to leap backwards to avoid a flattened nose."

    show plumeria at right
    with fade

    narrator "Plumeria sticks her head through and gives me a cheery grin. With her comes a blast of cold air, sending the fire dancing wildly in its little stone prison."

    plumeria "Oop, sorry, nearly got you there."

    foxglove "Plume! Gods, I woke up and you weren’t here-"

    narrator "Seeing my worry, her expression softens. She steps in and swings the door shut behind her, cutting out the wind."

    plumeria "Hey, hey, it’s fine. I just headed up and fetched your gloves. You were still sleeping, and I figured you needed it after, well, everything. Spirits and afterwards."

    narrator "She waggles her eyebrows lasciviously and I find myself blushing, but I step forward and hug her. My head thumps against her chest. She chuckles, and her arms encircle me."

    foxglove "I wasn’t the one who nearly died, dummy. What if they’d come back?"

    narrator "She frees up some space and pulls out a thermos flask."

    plumeria "Well, it wasn’t me they wanted - I figured they’d given up. Besides, I was prepared. I put a bit of incense in here, let it fill with the smoke. If they came at me, I’d unscrew the lid, let out the smoke, and bam. No more spirits."

    narrator "I frown at the flask."

    foxglove "What if it hadn’t worked?"

    narrator "My friend - girlfriend now, I suppose? - shrugs easily."

    plumeria "Then you’d have had to come and rescue me. It worked out pretty well for me last time, after all."

    narrator "I force down a laugh and bury my head in her chest again."

    foxglove "Oh my gods, you horndog, is that all you can think about now?"

    narrator "She laughs again, clear and ringing, like bells, then quietens. When she speaks again, her voice is low and serious."

    plumeria "Hey. Do you still want to go out? Last night was- well, emotions were high, right? I’m not going to hold it against you if you’ve changed your mind."

    narrator "I look up at her face. She’s not smiling, her green gaze steady. I match it for a long moment. She’s putting on a brave face, but I can see the tension in the set of her jaw, the slight furrow of her brow. I smile and then reach up and lightly flick her nose."

    plumeria "Wha- hey!"

    foxglove "My answer hasn’t changed. There’s no one- there’s no one more important to me than you, Plumeria Feld."

    narrator "I keep my gaze in hers, even as I feel my cheeks heat. In reply, she leans in and kisses me again. Wow, but her lips are soft, even though the cold air of the mountains has chapped them a little."

    narrator "She pulls away, smirking at my expression as she does."

    plumeria "Come on. Let’s have breakfast and start heading down. Your granny’s probably worried since we didn’t come back last night, and I’m starving for some proper food."

    plumeria "The weather seems to have cleared up a bit over night, but I wouldn’t wait around longer than we need to. There were some big clouds on the horizon."

    narrator "At her words, my stomach lets loose with an enormous growl. Abruptly, I realise; yeah, I’m absolutely ravenous, and we have a long way to walk back down."

    foxglove "Gods, yeah. What have we got?"

    plumeria "Nothing! When I checked out my bag, it turns out someone set it on fire with a flare. Absolutely ruined."

    narrator "At my expression, she barks out a laugh, loud and teasing."

    foxglove "It was- it was necessary!"

    plumeria "I know, I know. Luckily, this being a survival shelter, it should have something in here for us."

    narrator "She pokes through some of the little cupboards, putting aside firelighters and a couple of packaged survival blankets."

    narrator "...maybe I should have looked in there last night, but, well, I had other things on my mind."

    plumeria "Aha!"

    narrator "She flourishes a chunky block of foil."

    plumeria "Chocolate! Enough sugar to keep you fuelled against a billion ice spirits."

    narrator "My palm finds my face."

    foxglove "Oh my gods, Plume, don’t. Haven’t you ever heard of tempting fate?"

    narrator "She laughs, and I find myself chuckling along. Yeah, last night was scary. Well, more than that - terrifying, perhaps, and I’m sure the whole near-death-experience thing would come back later."

    narrator "But for now, in the light of day (or firelight, I guess, in here) the whole thing has an air of unreality."

    plumeria "This is survival chocolate, so, you know, it’s not going to be great, but I figure we could do with something sugary."

    foxglove "I guess there’s that."

    narrator "We spend a moment trying to break it to no avail. In the end, we soften it by the fire and shave off chunks with a pocket knife. I chew, thoughtfully, the still-solid mass cracking under my teeth."

    foxglove "Huh. This is..."

    plumeria "Absolutely awful."

    foxglove "Yeah. Oh my gods, is this chocolate or sawdust?"

    plumeria "Got to have something to stop people from nicking it to eat, I suppose."

    narrator "After suffering through as much of the horrible chocolate as I can stomach, I sit back for a moment to let Plume finish hers off. Finally, even she’s had as much as she can force, and she pockets the rest with a reluctant expression."

    foxglove "I guess we’ll need to work out who to tell to get it replaced, right? I hope it’s not too expensive."

    narrator "Plume doesn’t look too worried."

    plumeria "Eh, I don’t mind. It saved our butts, didn’t it? If I have to buy some more absolutely grim-tasting chocolate, I can deal."

    scene bg pilgrims path day
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "Under the cold light of day - so to speak - the events of yesterday seem like a dream. It doesn’t stop me from carefully looking around for any ambush."

    narrator "Nothing; it hasn’t even really snowed last night, and the groundcover is still lumpy and broken from our movements. In a sudden moment of irrational doubt, I pull back a glove and peek at my crystalline fingers, just to be sure that it did happen."

    narrator "As we retrace our steps back down the mountain, though, nothing appears. I look back up the mountain, over and over, and see no malignant ice-being sweeping down like an avalanche."

    narrator "It’s only once we’re far past it I remember my bag, still sitting in the Temple up above, but yeah - I think the spirits can keep it. When I raise this to Plume, she just laughs."

    narrator "The only time we stop is at Orchid’s Point. There, we take a moment among the frost-clad flowers, ever swaying in a gentle dance to the breeze."

    narrator "We don’t have any more hot drink, so we scoop a handful of snow each and let it melt in our mouths, then gnaw some more at the survival chocolate."

    plumeria "Not any better."

    narrator "I was inclined to agree."

    narrator "Just before we start off again, I pause and turn back to the pool and the tiny symbolic coins within. In a moment of spite, I plunge my hand in the icy water and pull out one of the tarnished metal disks."

    narrator "I stare back up the mountain, and for a moment, far up, I’m sure I see a glint of frost on an almost-humanoid figure - but then it turns and flits away, back up towards the long-dead deity above."

    narrator "I waver on telling Plume, but something keeps me quiet. To her questioning look, I merely shrug."

    foxglove "Call it compensation."

    narrator "When we head further down, I feel lighter, somehow."
    
    scene bg streets night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "We make it down without incident aside from my growing awareness of my aches and pains."

    narrator "Climbing up and down the mountain would have been enough on their own, but dragging Plume through the snow and then our... activity... afterwards had given my muscles work all of their own."

    narrator "It feels profoundly weird walking through the streets with life going on as normal. It feels like people should know, somehow - but to them, we’re probably just two tourists towards the end of the season, walking arm in arm."

    narrator "My Grandmother’s front door makes a welcome sight. I have to stop myself from rushing as I fumble for the latch and throw it open, stamping inside eagerly."
   
    scene bg home night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    foxglove "We’re back!"
    
    show grandma at center
    with fade

    grandma "Ah, good."

    narrator "She appears from the living room and stops. Her purple eyes scan us up and down, and her mouth hardens into a frown."

    grandma "What happened?"

    narrator "Before I can offer a word in explanation, we’re shepherded into the living room and made to sit. We wait in silence while she makes cups of strong, hot tea and brings them in. She looks between us, and then adds a measured shot of brandy to each."

    grandma "Now. Talk."

    narrator "We talk. I explain the trip up, the appearance of the spirits, what they said. I talked about driving them off with the flares and the incense."

    narrator "I talk about Plume and having to heat her up - though I leave off the precise details there, and desperately pray the tinge of my cheeks as I skip over it is blamed on the brandy."

    narrator "Grandmother listens to it all with a hard frown, interrupting rarely. She makes me take off my gloves and inspects my transmuted fingers, tapping at them with a fingernail and asking what I can feel before letting them go, seemingly satisfied they’re not about to immediately drop off."

    narrator "Finally, we finish. The room is silent, only the clock on the mantlepiece clicking and the low rustling of the fire."

    narrator "Grandmother is silent for a long time before she sighs. She levers herself to her feet and disappears into her bedroom for a moment."

    narrator "When she returns, it’s with the heavy revolver in her grip. In her wizened hands, it looks almost comically large, but she holds it with a familiar ease."

    grandma "You two get some more rest. There’s no more trains running, so you’ll have to head back tomorrow."

    foxglove "Wait, Grandmother - are you planning to just shoot them if they show up?"

    narrator "The old woman’s lips curl. Above them, in the shadows of her face, her eyes are as firm and unyielding as the mountain."

    grandma "I do not know what fool thing my daughter might have promised them. But I can promise this - they will not get either of you."

    narrator "It’s not a big boast. It’s simply a statement, a plain declaration that this old woman would, if necessary, face down the ancient magics of the spirits with a gun made for a war decades distant."

    plumeria "Well, I don’t know about you, but if it comes to a fight, my money’s on Granny."

    narrator "She starts and looks at Grandmother as if expecting a thunderbolt, but Dahlia simply raises an eyebrow."

    grandma "I’ll let you have that one."

    plumeria "Thanks, Gran."

    grandma "Don’t push your luck."

    plumeria "R-right."
    
    scene bg bedroom night
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "Together, we head into the bedroom. The window is shut securely; a tiny saucer of incense is set burning on the windowsill, the acrid trickles of it tickling my nose."

    narrator "Plume sits down on the bed heavily. I plomp down next to her, and she wraps an arm around my shoulders."

    plumeria "Your granny is still the scariest thing I’ve ever met. I’ll take the spirits over her when she’s angry, I'll tell you that."

    foxglove "Remember what I said about tempting fate?"

    narrator "Without warning, she falls back, dragging me with her. I bury my face against her chest, feeling it move with her breath, with her heart."

    plumeria "Come on, babe. Let’s get into bed."

    narrator "Neither of us move. The bed beneath us is comfortable,"

    foxglove "Babe? Really?"

    plumeria "Is Honey preferable?"

    narrator "I try to suppress my snort of laughter and fail. I can hear the smirk in her voice now."

    plumeria "Babycakes?"

    narrator "I lightly ball my fist and let it drop on her chest. Plume wraps her free hand around it, interlinking our fingers."

    plumeria "Nothing babe-derived, then. How about Darlinggg~?"

    narrator "She draws it out, affecting some ridiculous accent, and I can’t help but laugh. Finally I push myself up. She’s watching me, her deep, green eyes soft."

    foxglove "Alright, let’s get changed before you come up with something even worse sounding."

    narrator "We begin to change. I avert my eyes from the sounds of rustling cloth before I hear a chuckle."

    plumeria "We are dating, remember? You don’t have to look away."

    narrator "I glance back, seeing smooth, toned flesh, before I snap my head away again, my cheeks burning. Plume’s lovely laugh, low and husky, comes from out of sight."

    plumeria "Hey, now. You’ve more than looked at it, you know."

    foxglove "I know, I know. It’s just - different here, you know. It feels different."

    narrator "I look back. She sits back across the bed, but my eyes are drawn towards her chest. There, above her heart, is an uneven pale starburst on her skin. She follows my gaze and smiles wanly."

    plumeria "I guess we both have a mark from our mountain friends, huh? I’m kinda surprised you didn’t notice before, but then, I guess, you had other thoughts on your mind."

    narrator "She grins wickedly, but as she looks at my face, it becomes more tender. She opens her arms and I fall into them."

    narrator "A moment of awkward wriggling later and we’re ensconced under the covers. My body slots into the curves of hers, her warmth pressing against me."

    foxglove "I’m sorry."

    plumeria "Hmm?"

    foxglove "You nearly died. If I hadn’t come here..."

    plumeria "Hey, now. It’s not your fault."

    foxglove "If I hadn’t come here-!"

    narrator "My voice has started to raise, and she gently hushes me."

    plumeria "Not your fault. I chose to come, anyway. Besides, you were the one who saved us, anyway. So if you really insist, you’ve already balanced it out."

    narrator "She reaches out and clicks off the light. We’re plunged into the dark together."

    narrator "One of her hands wraps around me, seeking mine, and I grasp her fingers with my own; crystal against flesh."

    narrator "But she doesn’t seem to mind."
    
    # Day 10
    # TODO: train chug sfx
    scene bg train day
    with fade
    
    show foxglove at left    
    show plumeria at right
    with fade

    narrator "Slowly, the train pulls away from the station. My grandmother stands, watching, straight-backed and solemn."

    narrator "Almost as soon as we’d awoken, she’d escorted us to the train station, not a hint of nerves or worry on her face."

    narrator "Her hand comes up in a wave, and I return it, keeping her in sight until the last moment."

    narrator "I slump back into my seat. Next to me, Plumeria wraps my hand in hers. Even through the gloves we wear, I can feel the warmth."

    narrator "The rattle of the train is constant and soothing. It’s crept into winter, the sun heatless but golden, and flakes of snow dance microsecond ballets in the morning light."

    narrator "The morning sun pours in through the windows, like a promise of better days. Plumeria wriggles in closer, our shoulders brushing."

    foxglove "Didn’t you want to see Kalarlomoth from the train?"

    plumeria "Ah! You’re right!"
    
    scene cg train dead god day

    narrator "She cranes her head round. The dead god lies, still and crystalline, across the mountain top, a petrified giant of glass."

    narrator "Beneath, the town reaches skyward with roofs and spires, half-asleep until the spring thaw. Smoke spirals into the sky from the chimneys like an exorcism."

    plumeria "...Sure was a trip and a half, huh."

    narrator "Her gaze is fixed on the ever-more-distant god as the train carries us further away. Mine is on her."

    foxglove "It really was."

    plumeria "I guess we won’t be back. Best not to push our luck with those spooky icicles, right?"

    narrator "The sheer irreverence forces a chuckle out my mouth."

    foxglove "Yeah. All the same, I think I’ll see Grandmother again. Maybe once spring comes."

    narrator "The first wiry trunks of the forest rise into view and disappear past just as quickly. We’re approaching the bend that will take Godigsfel out of sight."

    narrator "Above, the god catches the light, gleaming gold one last time-"
    
    scene bg black
    with fade

    narrator "-and is gone."

    return
    
    # TODO: credits sequence?
