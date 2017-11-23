from sys import exit

items = ['1. matchbook', '2. compass', '3. rope', '4. steel-platformed-boots']

print "This is a text game. You play by entering the numbers corresponding to the move you want to make. If you ever wish to do nothing, simply enter \'0\'. Good luck!"
def dark_room():
    print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
    stickybelly = False
    slobber_cover = False
    have_key = False

    while True:
        door = raw_input("> ")

        if door == "1":
            print "There's a giant bear wearing a key around his neck, eating a cheese cake. What do you do?"
            print "1. Take the cake."
            print "2. Pet the bear."

            bear = raw_input("> ")

            if bear == "1":
                take_cake()

            elif bear == "2":
                pet_the_bear()

        elif door == "2":
            print "I'm sorry, I haven't built anything to go behind that door yet."


def take_cake():
    print "\nThe bear licks your face. You are covered in bear slobber. Now what?"
    print "\n1. Find a towel and whipe the slobber off."
    print "2. Eat the cake."
    print "3. Go back through the door into the dark room."
    slobber_cover = True

    while True:
        choice3a = raw_input("> ")

        if choice3a == "1":
            clean_slobber_off()

        elif choice3a == "2":
            eat_the_cake()

        elif choice3a == "3":
            print "Goodbye!"

def clean_slobber_off():
    print "\nYou find a white towel, whipe the slobber off with it, and once the towel",
    print "gets wet, a message appears on it, saying \'look up\'. What do you do?"
    wipe_slobber_off()

def clean_sticky_belly():
    print "\nYou find a white towel, whipe the sticky stuff off with it, and once the towel",
    print "gets wet, a message appears on it, saying \'look up\'. What do you do?"
    wipe_slobber_off()

def wipe_slobber_off():
    print "\n1. Look up"
    print "\n2. Look down"
    print "\n3. Put the towel down and leave."

    towel = raw_input("> ")

    if towel == "1":
        look_up()

    elif towel == "2":
        look_down()

    elif towel == "3":
        print "Fine, I didn't want to play anyway."
        exit(0)


def look_up():
    print "\nYou see a ladder hanging down from the roof of the cave. You might be able",
    print "to reach it if you jump. What do you do?"
    print "\n1. Jump and climb"
    print "2. Eat the cake"
    print "3. Pet the bear"

    ladder = raw_input("> ")

    if ladder == "1":
        jump_and_climb()

    elif ladder == "2":
        eat_the_cake()

    elif ladder == "3":
        pet_the_bear()

def look_up_after_down():
    print "\nYou see a ladder hanging down from the roof of the cave. You might be able",
    print "to reach it if you jump. What do you do?"
    print "\n1. Jump and climb"
    print "2. Ask bear for key"

    ladder = raw_input("> ")

    if ladder == "1":
        jump_and_climb()

    elif ladder == "2":
        locked_trapdoor_choice()


def jump_and_climb():
    print "\nYou climb up and reach the very top, which leads you out of the cave",
    print "out into a sunny, grassy field. "
    print "Which direction do you go?"
    print "\n 1 = N \n2 = W \n3 = S \n4 = E"

    direction = raw_input("> ")

    if direction == "1":
        direction_north()

    elif direction == "2":
        print "\nYou go west until you find yourself at the beach.\n Yay beach!\n\n\n"
        exit(0)
    elif direction == "3":
        southbound()

    elif direction == "4":
        eastbound()

def direction_north():
    print "As you continue that way, the grass fades and you start to hear a hum."
    print "Keep going or turn around?"

    north = raw_input("> ")

    if north == "9" or "keep going" or "1":
        keep_going_north()

    elif north >= "10" or "turn around" or "3":
        go_back_from_highway()

def keep_going_north():
    print "\nYou come to a highway. Hitch-hike or go back?"

    highway = raw_input("> ")

    if highway >= "10":
        Hitch_hike()

    elif highway <= "10":
        go_back_from_highway()

def Hitch_hike():
    print "\nAn attractive young woman in a convertible with the top down stops and offers you a ride."
    print "\nDo you take it?"

    convertible = raw_input("> ")

    if convertible == "yes":
    #    print "She says, \"So, where to?\""

        print "\nShe responds, \"Well, %r sounds nice, but I'm going to a party and I think you'll have more fun there.\"" % raw_input ("Where to?")

            #print "\nShe responds, \"Well, %r sounds nice, but I'm going to a party and I think you'll have more fun there.\"" % destination
        print "You two drive off into the sunset."
        exit(0)
    elif convertible == "no" or "0":
        turn_down_first_ride()

def turn_down_first_ride():
    print "\nShe drives off and about ten minutes later, a young man in a pickup truck pulls over. There's a golden retriever in the passenger seat, and",
    print "you'd have to sit in the truck bed. \nDo you get in?"

    pickup_truck = raw_input("> ")

    if pickup_truck == "yes":
        print "\nYou hop in the back and enjoy the scenic route, which goes along the coast",
        print "and then up into the mountains. You're going through a redwood forest, up and up,",
        print "until finally you arrive at a cabin at the very top, overlooking the ocean."
        print "There's a big party with a bondfire and people playing music."
        print "You dance the night away!"
        exit(0)
    elif pickup_truck == "no":
        print "You wait a bit longer, and it turns out third time IS the charm. Santa comes and takes you away in his sleigh."
        print "Merry Christmas!"
        exit(0)
def go_back_from_highway():
    print "\nYou walk half a mile back the way you came, but a thick fog descends and soon you can't tell where you are."
    print "You hear a voice call out \"MARCO!\""
    print "\n Do you \n1. call back \n2. follow the voice\n\t or\n 3.run away\n "

    voice = raw_input("> ")

    if voice == "1":
        call_back()

    elif voice == "2":
        print "\nOut of the fog, you see a large, fluffy white figure come towards you,",
        print "and before you know it, you are enjoying the warm embrace of the Easter Bunny!"
        print "\n"
        exit(0)
    elif voice == "3":
        print "You run straight into a wall and get knocked unconscious."

    elif voice == "0":
        print "\nYou spend the rest of the day meditating in the fog."
        exit(0)
def call_back():
    print "\nThe voice starts getting closer, continuing to call out \"MARCO!\""
    print "\nYou hear foot steps approaching."
    print "\n\"MARCO!!!\""
    print "\nDo you continue responding?"
    marco_response()

def marco_response():
    while True:
        marco = raw_input("> ")

        if marco == "3":
            print "\nYou feel big furry arms wrap around your torso from behind."
            print "\nYou turn around..."
            print "\nand..."
            print "\n it's the Easter Bunny! You eat waffles and live happily ever after."
            exit(0)
        elif marco == "2":
            print "\nThe voice starts giggling and the giggles fade away."
            print "\nThe fog grows denser and denser, but in the distance you see a glow."

            glow = raw_input("> ")

            if glow >= "1":
                print "\nYou arrive at the source of the glow: a giant lava lamp!"
            elif glow == "0":
                print "\nYou spend the rest of the day meditating in the fog."
                exit(0)
        elif marco == "1":
            print "Try \"Yes\" or \"No.\""


def southbound():
    print "You go south until you find yourself at a river. To your left is a bridge, and to your right, a rope swing."
    print "You can \n1. try to wade or swim across the river \n2. cross the bridge \n3. use the rope swing"

    river = raw_input("> ")

    if river == "1":
        print "You get swept away by the current, go down a small waterfall, and find yourself in a lagoon with mermaids."
        print "\nYou spend the day with them swimming, singing, and braiding each other's hair.\n\n\n"
        exit(0)

    elif river == "2":
        cross_bridge()

    elif river == "3":
        print "The rope swing gets you safely to the other side, but a giant bird comes and takes you away.\n\n\n"
        exit(0)
def cross_bridge():
    print "You step on the bridge and it catapults you into a net."
    print "\nDo you climb out?"

    net = raw_input("> ")

    if net == "3":
        climb_out()

    elif net == "2":
        print "You land on a horse, who carries you off into the sunset. \n\n\n"
        exit(0)
def climb_out():
    print "You can climb out onto a tree or jump onto the ground. Tree or ground?"

    climb = raw_input("> ")

    if climb == "4":
        print "You climb up the tree until you reach a tree house. \n 1.Go in \n. or \n2.jump down?"

        treehouse = raw_input("> ")

        if treehouse == "0":
            print "You are now Tarzan.\nGoodbye!\n\n\n"
            exit(0)
        elif treehouse == "1":
            print "There are a bunch of monkeys having a tea party. You are the guest of honor!\n\n\n"
            exit(0)
        elif treehouse == "2":
            print "You land on a horse, who carries you off into the sunset. \n\n\n"
            exit(0)
        elif climb == "6":
            print "You land on a horse, who carries you off into the sunset. \n\n\n"
            exit(0)
def eastbound():
    print "You head east until you see, in the distance, a stand-alone building in the middle of a field.",
    print "As you get closer, you see it is a biker bar: a shack with a wrap-around porch, on which people are",
    print "smoking and drinking and one person wearing a mask is playing a banjo.\n 1 = GO INSIDE\n2 = START TALKING TO BANJO PLAYER",
    print "3 = PICK UP NEARBY FIDDLE AND PLAY ALONG"

    bar = raw_input("> ")

    if bar == "0":
        bar_no_response()

    elif bar == "1":
        print "You go inside and find yourself in an 18th century parlor hall. You look very out of place, but manage to make friends anyway."
        exit(0)

    elif bar == "2":
        talk_to_player()

    elif bar == "3":
        play_fiddle()

def bar_no_response():
    print "The people hanging out at the bar call at your from a distance and eventually toss a bottle your way."
    print "1 = CATCH"

    bottle = raw_input("> ")

    if bottle == "0":
        print "The bottle falls to the ground, shatters, and releases a thousand deafening shrieks."
        print "You decide to go in and have a drink after all, and have a great time.\n\n\n"
        exit(0)
    elif bottle == "1":
        print "The bottle lights up as you catch it, and starts growing bigger and bigger, until you have to drop it.",
        print "Eventually a unicorn forms inside the bottle and bursts through.\n\n\n"
        exit(0)
def talk_to_player():
    print "The banjo player responds to you in verse, but you can't understand, or even identify, the language they are speaking."
    print "You can, however, catch up on to the melody they are singing and kind of hum along."
    print "\n 1 = GO INSIDE \n2 = PICK UP NEARBY FIDDLE AND PLAY ALONG"

    porch = raw_input("> ")

    if porch == "0":
        porch_sing()

    elif porch == "1":
        print "You go inside and find yourself in an 18th century parlor hall. You look very out of place, but manage to make friends anyway."
        exit(0)
    elif porch == "2":
        play_fiddle()

def porch_sing():
    print "You sing your heart out with the banjo player until you are too tired to continue."
    print "Do you fall asleep there, or go home?"
    print "\n 1 = FALL ASLEEP THERE \n 2 = GO HOME"

    sleep = raw_input("> ")

    if sleep == "1":
        print "The other patrons roll out a bed for you. \n GOODNIGHT\n\n\n"
        exit(0)
    elif sleep == "2":
        print "You return home and realize you were at that bar for a week!\n\n\n"
        exit(0)
def play_fiddle():
    print "You start playing and everyone on the porch falls asleep immediately."
    print "\n 1 = GO INSIDE \n2 = LEAVE"

    fiddle = raw_input("< ")

    if fiddle == "1":
        print "There is nothing inside - just white empty space."
        exit(0)

    elif fiddle == "2":
        print "Goodbye!"
        exit(0)
def eat_the_cake():
    print "You bite into the cake, and feel something hard in your mouth. You spit it out",
    print "and watch a marble roll across the ground. Now what?"
    print "\n 1 = FOLLOW THE MARBLE"
    print "\n 2 = FINISH EATING CAKE"

    marble = raw_input("> ")

    if marble == "1":
        follow_the_marble()

    elif marble == "2":
        print "Turns out the cake had sedatives in it. Sweet dreams!"
        exit(0)
    else:
        print "You get a call from your mom and wants you to come home. Goodye!"
        exit(0)
def follow_the_marble():
    print "\n The marble leads you to a narrow passageway in the wall,",
    print " just big enough to crawl through. You hear music coming through the passageway.The passageway is blocked by a metal grate",
    print "What do you do?"
    passage_puzzle()

def passage_puzzle():
    print "\n1 = CRAWL THROUGH"
    print "\n2 = \"OPEN SESAME\""
    print "\n3 = SEARCH FOR KEY"
    grate_open = False
    hold_ruby = False
    while True:
        passageway = raw_input("> ")

        if passageway == "1" and not grate_open:
            print "It is locked. you can't do that."
            passage_puzzle()

        elif passageway == "2" and not hold_ruby:
            print "The grate shakes, but does not open."

        elif passageway == "3" and not grate_open:
            print "You search around the dark room and see a ruby glowing in the corner. you pick it up."
            hold_ruby = True

        elif passageway == "2" and hold_ruby:
            print "The grate opens while you are holding the ruby"
            grate_open = True

        elif passageway == "1" and grate_open:
            crawl_through()

        else:
            exit(0)

def crawl_through():
    print "You crawl down the small passageway about 30ft and come to a fork in the passageway."
    print "To the left you smell something sweet baking, to the right you hear music. Which way do you go?"

    fork = raw_input("> ")

    if fork == "4":
        print "\n \tThe passageway gets taller, and you're able to stand up. You continue down a hallway,",
        print "until, around a bend, it opens up into a kitchen. You walk into a kitchen full of bears",
        print "baking cakes. They are shocked to see you!"
        print "You all eat cake together and live happily ever after."
        exit(0)
    elif fork >= "5":
        print "\n \tYou call further down the passageway. It becomes smaller and darker, but you persist, because",
        print "you can hear the music getting louder as you get closer. Finally you arrive at a small door",
        print "reverberating with the beat of the music. You open the door and... \n"

        print "find yourself in...\n"



        print "\nthe Burghain."
        print "You party all night and day."
        exit(0)
    else:
        print "It turns out the bear has more marbles, and you guys play several games before you leave and go home."
        exit(0)

def look_down():
    print "There is a trap door beneath your feet."
    print "\n1. OPEN DOOR \nor\n 2. LOOK UP"
    have_key = False
    while True:
        trapdoor = raw_input("> ")

        if trapdoor == "1":
            print "It is locked!"
            print "1 = LOOK UP"
            print "2 = ASK BEAR FOR KEY"
            print "3 = OPEN DOOR"
            locked_trapdoor_choice()

        elif trapdoor == "2":
            look_up_after_down()

def trapdoor_puzzle():
    print "It is locked!"
    print "1 = LOOK UP"
    print "2 = ASK BEAR FOR KEY"
    print "3 = OPEN DOOR"
    locked_trapdoor_choice()


def locked_trapdoor_choice():
    have_key = False
    while True:
        locked_trapdoor_choice = raw_input("> ")

        if locked_trapdoor_choice == "1":
            look_up_after_down()

        elif locked_trapdoor_choice == "2":
            print "The bear gives you the key."
            have_key = True

        elif locked_trapdoor_choice == "3" and not have_key:
            trapdoor_puzzle()

        elif locked_trapdoor_choice == "3" and have_key:
            open_trap_door()


def open_trap_door():
    print "You see a spiraling staircase descending downward."
    print "1. LOOK UP \nor\n 2. TAKE STAIRCASE"

    staircase = raw_input("> ")

    if staircase == "1":
        look_up()

    elif staircase == "2":
        take_the_staircase()

    elif trapdoor == "2":
        look_up()

def take_the_staircase():
    print "You go further and further down until you step into a library. There is a tiny old man reading a very large book."
    print "1. TALK TO LIBRARIAN or \n 2.GO BACK THE WAY YOU CAME"
    while True:
        library = raw_input("> ")

        if library == "1":
            print "The librarian asks, \"What kind of books do you like?\""

            books = raw_input("> ")

            if books > "0":
                likes_books()

            else:
                print "Hmm, not familiar."

        elif library =="2":
            look_down()

        else:
            take_the_staircase()


def likes_books():
    print "\"Very good. You should enjoy that unmarked white book on the second shelf over there.\""
    print "\n You walk over to the book he incicated. It is between an unmarked black book and an unmarked red book."
    print "\nWhich book do you pick up?"
    print "\n 1 = WHITE \n 2 = RED \n3 = BLACK"
    second_book_choice = False
    while True:
        book_choice = raw_input("> ")

        if book_choice == "1" and not second_book_choice:
            white_book()

        elif book_choice == "2" and not second_book_choice:
            red_book()

        elif book_choice == "3" and not second_book_choice:
            black_book()


def second_book_is_red():
    print "The book turns out to be a box with a knife in it."
    print "Do you \n0 = LEAVE WITH NOTHING \nor\n 1 = TAKE THE KNIFE"

    second_knife_choice = raw_input("> ")

    if second_knife_choice == "0":
        print "You leave with nothing."
        after_book()

    elif second_knife_choice == "1":
        print "Now you have a knife."
        items.extend(['5. knife'])
        after_book()

def second_book_is_white():
    print "The book turns out to be a box with a flute."
    print "\nTake this, or nothing. \n 0= TAKE NOTHING \n1 = TAKE FLUTE"

    second_flute_choice = raw_input ("> ")

    if second_flute_choice == "0":
        after_book()

    elif second_flute_choice =="1":
        items.extend(['5. knife'])
        after_book()

def white_book():
    print "The book turns out to be a box with a flute."
    print "\n1 = TAKE FLUTE \n but if you don't want the flute, you can choose from"
    print "\n 2 = RED BOOK \n or\n 3 = BLACK BOOK"


    flute_choice = raw_input ("> ")

    if flute_choice == "1":
        print "Good choice."
        items.extend(['5. flute'])
        after_book()

    elif flute_choice == "2":
        second_book_is_red()

    elif flute_choice == "3":
        second_book_is_black()

    elif flute_choice == "0":
        print "You leave with nothing."
        after_book()


def red_book():
    print "The book turns out to be a box with a knife in it."
    print "Do you \n1. TAKE THE KNIFE \nor\n2. CHOOSE WHITE BOOK"
    print "\n3. CHOOSE BLACK BOOK"

    red_book_choice = raw_input("> ")

    if red_book_choice == "1":
        print "Now you have a knife."
        items.extend(['5. knife'])
        after_book()

    elif red_book_choice == "2":
        print "Last chance."
        second_book_is_white()

    elif red_book_choice == "3":
        print "Last chance."
        second_book_is_black()

    else:
        print "You leave with nothing."
        after_book()



def black_book():
    print "The book turns out to be a box with a lamp inside."
    print "\n1 = TAKE LAMP \n2 = CHOOSE WHITE BOOK \n 3 = CHOOSE RED BOOK"

    black_book_choice = raw_input("> ")

    if black_book_choice == "1":
        print "Now you have a lamp."
        items.extend(['5. lamp'])
        after_book()

    elif black_book_choice == "2":
        print "Last chance."
        second_book_is_white()

    elif black_book_choice == "3":
        print "Last chance."

def second_book_is_black():
    print "The book turns out to be a box with a lamp inside."
    print "\n0 = LEAVE WITH NOTHING \n1 = TAKE LAMP"

    lamp_choice = raw_input("> ")

    if lamp_choice == "0":
        print "You leave with nothing."
        after_book()

    elif lamp_choice == "1":
        print "Now you have a lamp."
        items.extend(['5. lamp'])
        after_book()



def after_book():
    print "You return to the librarian. He asks, \'Did you find something you like?\'"
    response = raw_input()
    print "\"Good. I'm afraid the staircase you came down is no longer in use. You will have to exit towards the back.\""
    print "The librarian gestures towards the very back of the library, where you see a small dark passageway."
    print "\"If you want to take what you found, you have to put it in here and take this with you.\" The librarian hands you a small backpack."
    print "Do you take it?"
    backpack_choice_function()

def backpack_choice_function():
    said_no_once = False
    while True:
        backpack_choice = raw_input("> ")

        if backpack_choice == "no" and not said_no_once:
            print "You won't get very far without it."
            said_no_once = True


        if backpack_choice == "yes" and said_no_once:
             print "Okay. You proceed to the passageway with nothing."
             print "Once you enter, a large wooden door slams down behind you, and you can't go back the way you came."
             print "It is very dark. How can you find your way out?"
             print "\n0 = stumble around in dark \n 1 = check backpack"
             library_passageway_no_backpack()

        elif backpack_choice == "yes" or "take backpack" and not said_no_once:
            print "You take the backpack with you into the dark passagway."
            library_passageway()

        elif backpack_choice == "take backpack" and said_no_once:
            print "You take the backpack with you into the dark passagway."
            library_passageway()

def library_passageway():
    print "Once you enter, a large wooden door slams down behind you, and you can't go back the way you came."
    print "It is very dark. How can you find your way out?"
    print "\n0 = stumble around in dark \n 1 = check backpack"
    while True:
        stumble_or_backpack = raw_input("> ")

        if stumble_or_backpack == "0":
            print "You trip and fall into oblivion."
            exit(0)

        elif stumble_or_backpack == "1":
            print "\nIn the backpack, you find: %r" % items
            print "\nWhich item do you use? You can only use each once, and only one at a time. Then you must throw them away."
            print "Use 1-5 to indicate which item you want to use."
            itemchoice()

def library_passageway_no_backpack():

    stumble_or_backpack = raw_input("> ")

    if stumble_or_backpack == "0":
        print "You trip and fall into oblivion."
        exit(0)
    elif stumble_or_backpack == "1":
            print "Sorry, you left the backpack behind, remember?"
            library_passageway_no_backpack()

def itemchoice():
    print items
    choseflute = False
    choseboots = False
    choserope = False
    choseknife = False
    tangled = False
    while True:
        backpackchoice1 = raw_input("> ")

        if backpackchoice1 == "1":
            first_choice_matchbook()

        elif backpackchoice1 == "2" and '2. compass' in items:
            first_choice_compass()

        elif backpackchoice1 == "2" and '2. compass' not in items:
            print "You already used that, remember? Pick something else."

        elif backpackchoice1 == "3" and not choserope:
            print "Are you sure? That won't be helpful right now."
            choserope = True

        elif backpackchoice1 == "3" and choserope:
            print "You get yourself tangled in a rope. Good job."
            items.pop(2)
            tangled = True

        elif backpackchoice1 == "4" and not choseboots:
            print "Maybe not what you need most right now."
            choseboots = True

        elif backpackchoice1 == "4" and choseboots:
            print "You walk around in your steel-platformed-boots, and feel sharp things crunching beneath your feet."
            print "You bump into something, trip, fall, and are too injured to continue."
            exit(0)

        elif backpackchoice1 == "5" and '5. lamp' in items:
            first_choice_lamp()

        elif backpackchoice1 == "5" and not tangled and '5. knife' in items:
            print "Really? What are you going to use that for?"
            choseknife = True

        elif backpackchoice1 == "5" and choseknife and not tangled:
            print "You walk with the knife, trip, and fall on it."
            exit(0)

        elif backpackchoice1 == "5" and tangled and choseknife:
            print "You cut yourself free from the rope, but now you're down a rope and a knife."
            items.pop()

        elif backpackchoice1 == "5" and '5. flute' in items and not choseflute:
            print "Feeling musical?"
            choseflute = True

        elif backpackchoice1 == "yes" and choseflute:
            first_choice_flute()

        else:
            print "Try something you actually have."

def first_choice_flute():
        print items.pop()
        print items.extend(['5. fireflies'])
        print "You play a tune on the flute, the cave slowly become lit by many fireflies as they fly towards you. A couple even fly",
        print "into your backpack. They are all coming from the same direction."
        print "You see that much of the ground is covered in sharp blades and stalagmites. What do you do?"
        print "1 = WALK OVER ANYWAY \n 2 = USE ITEM FROM BACKPACK"


        dangerouscaveground = raw_input(" ")

        if dangerouscaveground == "1":
            print "You seriously injur yourself and are unable to proceed."
            exit(0)

        elif dangerouscaveground == "2":
            seconditemchoice()

def first_choice_lamp():
        print items.pop()
        print "You use the lamp to light up the cave, which is massive and seems to span out in every direction."
        print "You notice a beautiful crystal near your feet. Pick it up?"

        crystal = raw_input(" ")

        if crystal == "yes":
            items.extend(['5. crystal'])
            print "You add it to your collection in your backpack."
            first_choice_lamp_part_2()

        elif crystal == "no":
            print "You proceed without it."
            first_choice_lamp_part_2()

def first_choice_lamp_part_2():
    print "Much of the ground is covered in sharp blades and stalagmites. You notice one stalagmite a few feet away from you that has",
    print "something written on it, but you can't walk over to it without cutting your feet. What do you do?"
    print "1 = WALK OVER ANYWAY \n 2 = USE ITEM FROM BACKPACK"


    dangerouscaveground = raw_input(" ")

    if dangerouscaveground == "1":
        print "You seriously injur yourself and are unable to proceed."
        exit(0)

    elif dangerouscaveground == "2":
        seconditemchoice()

def first_choice_compass():
    item_grab = items.pop(1)
    print "You chose %r" % item_grab
    print "\nFortunately, the face of the compass does give off a soft glow,",
    print "but it is only enough to illuminate the area immediately around you. You can't see much of the cave."
    print "Do you \n 1. choose a different item,\n or 2. Walk around and use the compass to navigate"

    compassfirst = raw_input("> ")

    if compassfirst == "1":
        itemchoice()

    elif compassfirst == "2":
        compasswalk()

def compasswalk():
        print "As you start walking, you feel something sharp cut through your shoe."
        print "You aim the face of the compass downward and see the ground is covered in sharp blades."
        print "Do you \n 1. continue walking \nor \n 2. put on the boots"

        walkorboots = raw_input("> ")

        if walkorboots == "1":
            print "You soon injur your feet too badly to continue."
            print "\n\n\nGOODBYE\n\n\n"
            exit(0)

        elif walkorboots == "2":
            items.pop(2)
            print "You are now able to safely walk about."
            getcompass()

def first_choice_matchbook():
    print items.pop(0)
    print "You use the matchbook to light up the cave, which is massive and seems to span out in every direction."
    print "Much of the ground is covered in sharp blades. You notice a stalagmite a few feet away from you that has",
    print "something written on it, but you can't walk over to it without cutting your feet. What do you do?"
    print "1 = WALK OVER ANYWAY \n 2 = USE ITEM FROM BACKPACK"


    dangerouscaveground = raw_input(" ")

    if dangerouscaveground == "1":
        print "You seriously injur yourself and are unable to proceed."
        exit(0)

    elif dangerouscaveground == "2":
        seconditemchoice()

def seconditemchoice():
    print "\nRemaining in your backpack, you have: %r" % items
    print "Which do you choose?"
    print "Use numbers 1 - 5 to indicate which you would like to use."
    print "\n\n!!!REMEMBER!!! You can only use one item at a time, and once you've used it, it's gone."
    print "Each time you grab a new item, you throw out the one you just used (with one exception, hehehe)"
    tangled = False
    tried_rope = False
    triedmatchbook = False
    while True:
        next_choice = raw_input(" ")

        if next_choice == "1" and '1. matchbook' in items and '5. fireflies' not in items:
            print "That's probably not the best choice for this scenario."
            triedmatchbook = True

        elif next_choice == "1" and '1. matchbook' in items and triedmatchbook:
            print items.pop(0)
            print "You have your matchbook out now, but it isn't going to help you walk around the sharp ground."

        elif next_choice == "1" and '1. matchbook' not in items:
            print "Sorry, you've already used that."

        elif next_choice == "1" and '1.matchbook' in items and '5. fireflies' in items and '4. steel-platformed-boots' not in items:
            print items.pop(0)
            print "You can see better now, but without the tune of the flute, the fireflies dissipate."
            print "Striking a match, you notice a stalagmite with writing on it a few feet away from you.",
            print "You walk over and see written on it,\n \"EXIT NORTH\""

        elif next_choice == "2" and '2. compass' in items:
            print "That isn't very useful right now. Try something else."

        elif next_choice == "2" and '2. compass' not in items:
            print "Sorry, you've already used that."


        elif next_choice == "3" and tried_rope:
            print "You get yourself all tangled up in a rope."
            print items.pop(1)
            tangled = True

        elif next_choice == "3" and tried_rope and '5. fireflies' in items:
            print "That can't really help you right now."

        elif next_choice == "3" and '3. rope' in items and fireflies not in items:
            print "That can't really help you now."
            tried_rope = True


        elif next_choice == "4" and '1. matchbook' not in items:
            print items.pop(2)
            print "You are able to walk on the sharp blades over to the stalagmite with writing."
            print "On it, you see written:"
            print "\"EXIT NORTH\""
            print "What do you do?"
            print "1 = GUESS WHICH WAY IS NORTH, WALK THERE"
            print "2 = USE COMPASS"
            stalagmiteclue()

        elif next_choice == "4" and '1. matchbook' in items and '2. compass' in items:
            print items.pop(3)
            print "You are able to walk on the sharp blades over to the stalagmite with writing."
            print "On it, you see written:"
            print "\"EXIT NORTH\""
            print "What do you do?"
            print "1 = GUESS WHICH WAY IS NORTH, WALK THERE"
            print "2 = USE COMPASS"
            stalagmiteclue()


        elif next_choice == "4" and '2. compass' not in items:
            items.pop(2)
            compassthenboots()

        elif next_choice == "4" and '5. fireflies' in items:
            items.pop(3)
            flutethenboots()

        elif next_choice == "5" and '5. knife' in items and not tangled:
            print "Not exactly useful right now."

        elif next_choice == "5" and '5. knife' in items and tangled:
            items.pop()
            print "You cut yourself free with the knife, but now you've used your rope AND your knife."

        elif next_choice == "5" and '5. lamp' in items and not choselamp:
            print "This isn't the most useful tool for this situation."
            choselamp = True

        elif next_choice == "5" and '5. lamp' in items and choselamp:
            items.pop()
            print "Using your lamp, you can see things more clearly, but you still can't walk over rocks."


        elif next_choice == "5" and '5. flute' in items and not choseflute:
            print "This won't help you right now."
            choseflute = True

        elif next_choice == "5" and '5. flute' in items and choseflute:
            print "You play the flute, dance, and terribly injur your feet on the sharp blades."
            print "You are too injured to continue."
            exit(0)

        elif next_choice == "5" and '5. crystal' in items:
            print "Not useful right now. Try something else."

        else:
            print "You must choose something you have."

def flutethenboots():
    items.pop(3)
    print "\nNow that you can walk about safely, where do you go? (by the way, the boots are the only things",
    print "from your backpack that you can continue using as you select other objects, so you can still use",
    print "the flute for now)."
    print "1 = GET NEW OBJECT \n2 = GO TO WHERE THE FIREFLIES ARE COMING FROM \n 3 = KEEP PLAYING FLUTE"
    playingflute = False

    while True:

        flutedandbootedchoice = raw_input("> ")

        if flutedandbootedchoice == "1":
            itemchoice()

        elif flutedandbootedchoice == "2" and playingflute:
            print "You follow the fireflies through the stalagmites for about a mile, and eventually come to a passageway with a",
            print "small girl sitting in front of it. The fireflies are flying over head, and she is in your way."
            girlguard()

        elif flutedandbootedchoice =="2" and not playingflute:
            print "Unless you continue playing the flute, the fireflies dissipate and you can't follow them to ",
            print "where they're coming from."

        elif flutedandbootedchoice == "3":
            print "The fireflies love the music and keep flying in. You can see clearly where they're coming from."
            playingflute = True

def girlguard():
    print "You ask the girl to please move, and she says, \"I will only move if you give me something first.\""
    print "1 = GET ITEM OUT OF BACKPACK 2 = PUSH GIRL OUT OF THE WAY 3 = TRY TO STEP OVER GIRL"
    while True:
        girlchoice = raw_input(" ")

        if girlchoice == "1":
            girlgift()

        elif girlchoice == "2":
            print "The girl slaps you and you are knocked unconscious."
            exit(0)

        elif girlchoice == "3":
            print "The girl raises her hand and pushes you away with her pinky finger. You nearly fall over and injur yourself."

def girlgift():
    print "The items you have left are:"
    print items
    print "\nWhat do you get out of your backpack?\nUse 1 - 5 to choose"
    triedmatchbook = False
    tried_rope = False
    while True:

        girlgiftchoice = raw_input(" ")

        if girlgiftchoice == "1" and '1. matchbook' in items and not triedmatchbook:
            print "The girl says,\n \"This doesn't interest me.\""
            triedmatchbook = True

        elif girlgiftchoice == "1" and triedmatchbook:
            print "The girl takes the matches, strikes one, and lights your clothes on fire."
            print items.pop(0)
            print "Stop, drop, roll and try something else."

        elif girlgiftchoice == "2" and '2. compass' in items and '1. matchbook' in items:
            print "\"This will do. You may pass.\"\n The girl moves out of your way and lets you proceed."
            print items.pop(1)
            aftergirl()

        elif girlgiftchoice == "2" and '2. compass' in items and '1. matchbook' not in items:
            print "\"This will do. You may pass.\"\n The girl moves out of your way and lets you proceed."
            print items.pop(0)
            aftergirl()

        elif girlgiftchoice == "3" and '3. rope' in items and not tried_rope:
            print "\"This is boring. I do not want this.\""
            tried_rope = True

        elif girlgiftchoice == "3" and tried_rope:
            print "The girl takes the rope from you, ties you up, drags you deep into the cave, and leaves you there."
            exit(0)

        elif girlgiftchoice == "5" and '5. lamp' in items:
            print "\n\"Thank you, I like this.\"\n The girl gets up and lets you pass."
            print items.pop()
            aftergirl()

        elif girlgiftchoice == "5" and '5. knife' in items:
            print "\n\"Thank you. This seems useful.\"\n The girls steps aside so you may pass."
            print items.pop()
            aftergirl()

        elif girlgiftchoice == "5" and '5. fireflies' in items:
            print "The fireflies fly away, and the girl stares at you blankly."
            items.pop()

        elif girlgiftchoice == "5" and '5. flute' in items:
            print "\"This is acceptable, if you play me a song first.\""
            girlasksforflute()

        elif girlgiftchoice == "5" and '5. crystal' in items:
            print "Oooo pretty! Thank you!"
            print items.pop()
            aftergirl()

def girlasksforflute():
    print "Do you \n1. play her a song \nor\n2. choose a different item"
    playsongchoice = raw_input(" ")

    if playsongchoice == "1":
        print "\"Thank you. That was beautiful. I will take your flute and let you pass.\""
        items.pop()
        aftergirl()

    elif playsongchoice =="2":
        girlgift()

def aftergirl():
    print "You go past the girl, and walk down a narrow pass about a quarter mile. Eventually",
    print "it ends, and you see light coming down from above. You look up and see a hook near the top that",
    print "is securely planted in the cave wall. The items you have left are:"
    print items
    print "You need to throw a rope over the hook and pull yourself up to get out."
    print "1 = USE ROPE"
    print "2 = GO BACK"
    while True:

        caveescape = raw_input("> ")

        if caveescape == "1" and '3. rope' in items:
            print "You kick your boots off, throw the rope over the hook, and successfully pull yourself up and out of the cave."
            jump_and_climb()

        elif caveescape == "1" and '3. rope' not in items:
            print "You don't have that anymore."

        elif caveescape == "2":
            caveeastbound()








def compassthenboots():
    items.pop(3)
    print "With the boots on, you are safely able to traverse over the ground, but now you can't see. Now what?"
    print "1 = WALK OFF IN RANDOM DIRECTION"
    print "2 = GET SOMETHING OUT OF BACKPACK"

    canwalknotsee = raw_input("> ")

    if canwalknotsee == "1":
        print "You trip over a stalagmite and injur yourself too badly to continue."
        print "\n\n\nGOODBYE\n\n\n"
        exit(0)

    if canwalknotsee == "2":
        itemchoicecb()

def itemchoicecb():
    print "The items you have left are:"
    print items
    print "Which one do you choose now?"
    tangled = False
    while True:
        itemchoiceb = raw_input

        if itemchoicecb == "1" and '1. matchbook' in items:
            items.pop(0)
            "You use the matchbook to light up the cave, which is massive and seems to span out in every direction."
            caveilluminated()

        elif itemchoicecb == "3" and '3. rope' in items and '5. knife' not in items:
            items.pop(2)
            print "Okay, you're rope is out now. Doesn't really help you see..."

        elif itemchoicecb == "3" and '3. rope' in items and '5. knife' in items:
            items.pop(2)
            print "Great, now you're all tangled up AND you can't see."
            tangled = True

        elif itemchoicecb == "5" and '5. knife' in items and not tangled:
            items.pop()
            print "This doesn't really help wih the whole not-being-able-to-see thing."

        elif itemchoicecb == "5" and '5. knife' in items and tangled:
            items.pop()
            print "You use the knife to cut yourself free - but now you're down a knife and a rope and you STILL can't see anything."

        elif itemchoicecb == "5" and '5. lamp' in items:
            items.pop()
            caveilluminated()

        elif itemchoiceb == "5" and '5. flute' in items:
            first_choice_flute()

def caveilluminated():
    print "You notice a stalagmite a few feet away from you that has something written on it. You walk over and read that it says,",
    print "\"EXIT NORTH\""
    print "What do you do?"
    print "\n1 = GUESS WHICH WAY IS NORHT"
    print "\n2 = GET ITEM FROM BACKPACK"

    while True:
        caveilluminatedchoice = raw_input(" ")

        if caveilluminatedchoice == "1":
            print "You wander around for hours, until you find yourself back at this same point. You went in a giant circle."

        elif caveilluminatedchoice == "2":
            print items
            print "Which one do you choose?"
            itemchoicecbi()

def itemchoicecbi():
    while True:
        itemchoicecchoice = raw_input

        if itemchoicecchoice == "1" and '1. matchbook' in items:
            print "That isn't helpful right now."

        elif itemchoicecchoice == "2" and '2. compass' in items:
            getcompass()

        elif itemchoicecchoice == "3" and '3. rope' in items and '5. knife' not in items:
            print "That isn't helpful right now."

        elif itemchoicecchoice == "3" and '3. rope' in items and '5. knife' in items:
            items.pop(2)
            print "Great, now you're all tangled up and you still don't know where you're going."
            tangled = True

        elif itemchoicecchoice == "5" and '5. knife' in items and not tangled:
            items.pop()
            print "This doesn't help you navigate."

        elif itemchoicecchoice == "5" and '5. knife' in items and tangled:
            items.pop()
            print "You use the knife to cut yourself free - but now you're down a knife and a rope and you still don't know which way you're going."

        elif itemchoicecchoice == "5" and '5. lamp' in items:
            print "Not the most helpful item right now."

        elif itemchoicecchoice == "5" and '5. flute' in items:
            first_choice_flute()

def second_choice_matchbook():
    print "You use the matchbook to light up the cave, which is massive and seems to span out in every direction."
    print "Much of the ground is covered in sharp blades. You notice a stalagmite a few feet away from you that has",
    print "something written on it, but you can't walk over to it without cutting your feet. What do you do?"
    print "1 = WALK OVER ANYWAY \n 2 = USE ITEM FROM BACKPACK"

    dangerouscaveground = raw_input(" ")

    if dangerouscaveground == "1":
        print "You seriously injur yourself and are unable to proceed."
        exit(0)

    elif dangerouscaveground == "2":
        thirditemchoice()


def stalagmiteclue():
    while True:
        stalagmitecluechoice = raw_input("> ")

        if stalagmitecluechoice == "1":
            print "You wander around for hours, until you find yourself back at this same point. You went in a giant circle."


        elif stalagmitecluechoice == "2" and '1. matchbook' not in items:
            print items.pop(0)
            print "You throwout the matchbook, but fortunately the face of the compass gives off a",
            print "soft glow, so you can see around you just a little bit."
            getcompass()

        elif stalagmitecluechoice == "2" and '1. matchbook' in items:
            print items.pop(1)
            print "You have to put the lamp down, but fortunately the face of the compass gives off a soft glow."
            getcompass()

def getcompass():
    print "In which diretion do you proceed?"
    print "\n1 = NORTH \n2 = WEST \n3 = SOUTH \n4 = EAST"

    while True:
        directionchoice = raw_input(" ")

        if directionchoice == "1":
                print "You travel north for about a mile, while the cave gets narrower and narrower, until it is almost like a hallway."
                print "Eventually you come to a passageway that might be a way out of the cave, and there is a small girl sitting in front of",
                print "the passageway entrance."
                girlguard()

        elif directionchoice == "2":
            print "You head west, and a giant stalagmite falls on you and crushes you."
            print "\n\n\n GOODBYE \n\n\n"

        elif directionchoice == "3":
            print "To the south is the library, which you can't get back into."

        elif directionchoice == "4":
            caveeastbound()

def caveeastbound():
    print "You head east several hundred yards, and the cave smaller and smaller,",
    print " until you arrive at a passage large enough only to crawl through."
    print "\n\n1 = ENTER \n\n2 = TURN AROUND AND GO BACK THE WAY YOU CAME\n\n"

    hotcavepassage = raw_input(" ")

    if hotcavepassage == "1":
        print "You crawl into the passageway and fall into a pit of lava."
        print "\n\n\nGOODBYE!\n\n\n"
        exit(0)

    elif hotcavepassage == "2":
        print "You make your way back to the stalagmite with writing on it."
        getcompass()



















def pet_the_bear():
    print "The bear's belly is covered in something sticky."
    print "1. Continue petting \nor\n 2. Find a towel to clean your hands."
    stickybelly = True
    stickyfur = raw_input ("> ")

    while True:
        if stickyfur == "1":
            continue_petting()
        elif stickyfur == "2":
            clean_sticky_belly()

def continue_petting():
    print "The bear doesn't seem to like the feeling of you pulling at his sticky fur. He growls."
    print "0 = KEEP PETTING \n 1 = STOP PETTING"

    petting = raw_input ("> ")

    if petting == "0":
        print "The bear slaps you away and you fly across the room, knocked unconscious."
        exit(0)

    elif petting == "1":
        escape_from_bear()

def escape_from_bear():
    print "The bear starts chasing you. He is blocking the door you came through, but you notice a trapdoor in the floor",
    print "and a ladder hanging from the roof of the cave."
    print "1 = FIGHT BEAR"
    print "2 = JUMP AND CLIMB"

    escape = raw_input("> ")

    if escape == "1":
        print "You don't win."
        exit(0)
    elif escape == "2":
        print "Good idea."
        jump_and_climb()


dark_room()
