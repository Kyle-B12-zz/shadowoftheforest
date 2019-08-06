from sys import exit


name = input("Hello traveler, and who might you be?")

print ("Oh, "+name+" we've been waiting for you.")

def north():
    print ("What an interesting choice "+name+".")
    print ("                                                                                 ")
    print ("You start to walk north and walk for miles and for what seems like days, then you see it in the distance another post.")
    print ("                                                                                 ")
    print ("You start to run towards the post and it says North, South, East, West. This is the same post from before.")
    print ("                                                                                 ")
    print ("So you keep going north over and over again seeing the same post until you are starving and dehydrated, you fall to your knees and start to crawl")
    print ("                                                                                 ")
    print ("Just before you die you can see it in the distance another post")
    print ("                                                                                 ")
    print ("One single post that says North, South, East, West.")
    dead()

def west():
    print ("You start to walk west hoping you can get out of this nightmarish realm, you end up finding another tree with another hum that seems like the way out.")
    print ("Do you investigate?")

    choice_ten = input("> ")

    if "yes" in choice_ten or "YES" in choice_ten or "Y" in choice_ten or "y" in choice_ten or "Yes" in choice_ten:
        tree()

    if "no" in choice_ten or "NO" in choice_ten or "N" in choice_ten or "n" in choice_ten or "No" in choice_ten:
        print ("You walk away from the tree and trip over a rock falling down a deep and dark hole.")
        dead()

    if "Help" in choice_ten or "HELP" in choice_ten or "help" in choice_ten:
        print ("These are your choices,")
        print ("no, yes, help, exit")

    if "EXIT" in choice_ten or "Exit" in choice_ten or "exit" in choice_ten:
        exit(1)


def south():
    print ("""\
                ~         ~~
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '
              """)
    print ("You head south, and walk for a good while, until you see a city in the distance. After reaching the city you notice that there is no signs of life anywhere, just buildings and rubble.")
    print ("                                                                                 ")
    print ("Even the orange grass stopped growing, you look around for any signs of life just hoping you aren't alone.")
    print ("                                                                                 ")
    print ("You come to an intersection. Left or right?")

    one_choice = input("> ")

    if "left" in one_choice or "Left" in one_choice or "LEFT" in one_choice or "y" in one_choice or "Y" in one_choice:
        city()

    if "right" in one_choice or "RIGHT" in one_choice or "Right" in one_choice or "R" in one_choice or "r" in one_choice:
        print ("Walking towards the right you see in the distance a figure that seems humanlike.")
        print ("                                                                                 ")
        print ("You start to pick up your pace until you're in full sprint towards the figure, and as you get closer you start to see it more clear.")
        print ("                                                                                 ")
        print ("It is a human but it's holding a gun, you slow down trying not to spook the figure.")
        print ("                                                                                 ")
        print ("As you walk closer you hear a loud BANG, you look down at yourself revealing that you have been shot, bleeding out you think back to your life at home.")
        dead()

    if "exit" in one_choice or "Exit" in one_choice or "EXIT" in one_choice or "e" in one_choice or "E" in one_choice:
        exit(1)

    if "help" in one_choice or "Help" in one_choice or "H" in one_choice or "e" in one_choice:
        print ("These are your choices")
        print ("left, exit, help, right")
        south()


def city():
    print ("You choose to walk left. After walking a short distance, you hear a scraping noise coming from an alley on your left. Do you go investigate? Yes or No.")

    oh_nice = input("> ")

    if "yes" in oh_nice or "Yes" in oh_nice or "YES" in oh_nice or "Y" in oh_nice or "y" in oh_nice:
        print ("You cautiously walk towards the alley. As you get closer, the scraping stops. You enter and notice a figure hunched over something fleshy at the back of the alley.")
        print ("                                                                                 ")
        print ("You try to turn away from the figure, but as you step down, you break a shard of glass beneath your feet.")
        print ("                                                                                 ")
        print ("The figure hears and turns around, seeing you, you get a closer look at both it and its meal.")
        print ("                                                                                 ")
        print ("The creature is long, human-like, white as snow, and has skin thin enough to see all of its bones and innards. Its face is blank, save for a splash of red liquid on it, possibly blood, and a single thin line that currently has something that looks like a slice of meat hanging out of it.")
        print ("                                                                                 ")
        print ("Its meal, what looks like a human. But it's hard to exactly determine what it is as the creature ate the majority of it. The creature then starts sprinting towards you. You try to run but it quickly grabs you. The last thing you see is its mouth slowly open like a zipper, before it fully opens and engulfs your head. You die. Game Over.")
        dead()

    if "exit" in oh_nice or "Exit" in oh_nice:
        exit(1)

    if "help" in oh_nice or "HELP" in oh_nice or "Help" in oh_nice:
        print ("These are your chocies,")
        print ("yes, exit, no")

    if "no" in oh_nice or "No" in oh_nice or "NO" in oh_nice or "N" in oh_nice or "n" in oh_nice:
        print ("You slowly walk past the alley. As you do, the scraping stops. You then hear shuffling, and then you see some creature on top of the building behind you.")
        print ("                                                                                 ")
        print ("The creautre is long, human-like, white as snow, and has skin thin enough to where you can see all of its bones and innards.")
        print ("                                                                                 ")
        print ("Its face is blank, save for a splash of red liquid on it, possibly blood, and a single thin line that you assume is supposed to be a mouth.")
        print ("                                                                                 ")
        print ("The creature turns its head in your direction, and suddenly disappears.")
        print ("                                                                                 ")
        print ("Startled, you begin to run in the opposite direction, and in the distance, you see a manhole with the cover slightly ajar.")
        print ("                                                                                 ")
        print ("You get closer and you realize you could possibly jump into it if you moved the cover.")
        print ("                                                                                 ")
        print ("A screeching can be heard from behind you, and you realize the creature is getting closer, but you can't exactly see. Do you try to enter the manhole,")
        print ("                                                                                 ")
        print ("or do you continue to run and hope for other shelter?")
        hole()

def hole():

    choice_two = input("> ")

    if "manhole" in choice_two or "Manhole" in choice_two or "enter" in choice_two or "Enter" in choice_two or "enter the manhole" in choice_two or "Enter the Manhole" in choice_two or "open" in choice_two or "Open" in choice_two or "open manhole" in choice_two or "Open Manhole" in choice_two or "Open manhole" in choice_two:
        manhole()

    if "exit" in choice_two or "EXIT" in choice_two or "Exit" in choice_two:
        exit(1)

    if "help" in choice_two or "HELP" in choice_two or "Help" in choice_two:
        print ("These are your choices,")
        print ("enter, manhole, enter the manhole, run, exit, help")

    if "continue to run" in choice_two or "run" in choice_two or "Run" in choice_two or "Continue to Run" in choice_two or "RUN" in choice_two:
        print ("You decide that it will take too long to try and open the manhole, so you continue to run. You run and run, searching for shelter but you can't find any.")
        print ("                                                                                 ")
        print ("Eventually, the creature catches up and quickly grabs you. The last thing you see is its mouth slowly open like a zipper, before it fully opens and engulfs your head. You Die. Game Over.")
        dead()

def manhole():

    print ("You decide to try and open the manhole and crawl inside, just barely being able to shut it before you hear the creature bang on it.")
    print ("                                                                                 ")
    print ("After your adrenaline rush dies down, you quickly realize that you are now in a sewer.")
    print ("                                                                                 ")
    print ("As you suppress the urge to vomit, you realize that it is almost completely dark in the sewer save for a light in the distance.")
    print ("                                                                                 ")
    print ("Not seeing any alternatives, you start to walk towards the light, you see that the people are actually all skeletons. However, one seems to be clutching a peice of paper, and a gun.")
    print ("                                                                                 ")
    print ("Do you take them?")

    choice_four = input("> ")

    if "EXIT" in choice_four or "Exit" in choice_four or "exit" in choice_four:
        exit(1)

    if "HELP" in choice_four or "Help" in choice_four or "help" in choice_four:
        print ("These are your chocies,")
        print ("yes, no, exit, help")

    if "yes" in choice_four or "Yes" in choice_four or "affermative" in choice_four or "YES" in choice_four or "Y" in choice_four or "y" in choice_four:
        print ("You grab the piece of paper and notice that is is almost completely unintelligible, what you do make out is as follows.")
        print ("                                                                                 ")
        print ("...chamelon...find us...kill... Us find..."+name+"... find... spawn... kill...Free..""at the bottom of the papper you see a sequence of arrows.")
        print ("                                                                                 ")
        print ("The sequence goes left, ?, right, ?, ?, left, right, ?. The rest you can't make out")
        print ("                                                                                 ")
        print ("Shocked, you drop the paper. How could they know your name, these skeletons have been in here for what looks like years, since there isn't a single piece of skin or anything but bone.")
        print ("                                                                                 ")
        print ("Eventually, you snap out of your stupor and grab the gun, it's a type of pistol, but badly corroded. It looks like it is only capable of firing a single shot.")
        print ("                                                                                 ")
        print ("You take the light, which turns out to be a lantern, and sart walking. You walk for what feels like an eternity, before the light goes out.")
        print ("                                                                                 ")
        print ("You get unnerved, before you decide that you can't stay here so you keep walking forward, until you walk into a wall. You fall backwards, rubbing your face.")
        print ("                                                                                 ")
        print ("Eventually, you get up and wonder which way to go. You notice that the water seems to flow faster towards your right. Do you go Left or Right?")
        water()

    if "no" in choice_four or "No" in choice_four or "not" in choice_four or "Not" in choice_four or "NO" in choice_four or "N" in choice_four or "n" in choice_four:
        print ("You choose not to, deciding that you should just the leave the body alone. You take the light, which turns out to be a latern, and start walking. You walk a few feet")
        print ("                                                                                 ")
        print ("before the light unexpectedly goes out. Alone and in the dark, you have no idea what to do.")
        print ("                                                                                 ")
        print ("Eventually you keep waling forward, pressing your hand against the wall so you have a general sense of where you're headed. You keep going forward, until suddenly the wall")
        print ("                                                                                 ")
        print ("disappears and you fall to your right.")
        print ("                                                                                 ")
        print ("As you fall, you try to catch yourself but it's too late. You smack your head agasint the floor and get knocked out, your face fully submerged in the sticky warm liquids of the sewer.")
        print ("                                                                                 ")
        print ("You eventually drown. Game Over.")
        dead()

def water():

    choice_five = input("> ")

    if "right" in choice_five or "Right" in choice_five or "RIGHT" in choice_five or "R" in choice_five:
        print ("You turn to your right and start walking forward. You walk forward, and forward, the water below getting faster and faster.")
        print ("                                                                                 ")
        print ("Eventually, you get swept off your feet before you can turn around, and you get trapped in the flow of water. It drops, and after falling for a couple of seconds, you slam hard into something solid")
        print ("                                                                                 ")
        print ("The force of the impact kills you almost immediately. You die. Game Over.")
        dead()

    if "exit" in choice_five or "EXIT" in choice_five or "Exit" in choice_five:
        exit(1)

    if "help" in choice_five or "HELP" in choice_five or "Help" in choice_five:
        print ("These are your choices,")
        print ("right, left, help, exit")

    if "left" in choice_five or "Left" in choice_five or "LEFT" in choice_five or "L" in choice_five:
        print ("You turn to your left and head forward. You Keep walking forward until you walk right into another wall.")
        print ("Which way do you go, Right or Left?")

    choice_six = input("> ")

    if "Left" in choice_six or "L" in choice_six or "LEFT" in choice_six or "l" in choice_six or "left" in choice_six:
        print ("You turn left and walk a total of 2 feet before you walk into a wall. Maybe you should walk with your hand in front of you from now on.")
        print ("You turn around and and head forward")
        right()

    if "right" in choice_six or "RIGHT" in choice_six or "R" in choice_six or "r" in choice_six or "Right" in choice_six:
        right()

    if "EXIT" in choice_six or "Exit" in choice_six or "exit" in choice_six:
        exit(1)

    if "Help" in choice_six or "HELP" in choice_six or "help" in choice_six:
        print ("These are your choices,")
        print ("left, right, exit, help")

def right():
    print ("You turn right and start walking forward. You walk and walk for a couple of minutes, until you make out a wall in front of you, your eyes finally adjust to the dark.")
    print ("                                                                                 ")
    print ("It's still a bit difficult to see, but you can see that the wall leads to the left, and only the left. Before you run into the wall again, you turn left and continue straight.")
    print ("                                                                                 ")
    print ("You go forward until you start to see a light in the distance. You start to speed up and run untill you see that the light is shining on a wall and coming from the right.")
    print ("                                                                                 ")
    print ("You turn right and run and run and run... into a grate. You let out a curse and try to figure how to open it.")
    print ("                                                                                 ")
    print ("What do you do?")

    choice_seven = input("> ")

    if "Inspect" in choice_seven or "inspect" in choice_seven:
        print ("You see that a certain part of the grate is a bit weak. Maybe it could be broken if it's hit by something hard enough, maybe a rock or a brick.")
        brick()

    if "Look Around" in choice_seven or "look around" in choice_seven or "Look around" in choice_seven or "look Around" in choice_seven:
        print ("You look around for something to break the grate, and spot a brick.")
        brick()

    if "Hit" in choice_seven or "hit" in choice_seven or "Hit the Grate" in choice_seven or "HIT THE GRATE" in choice_seven or "hit the grate" in choice_seven:
        brick()

    if "Help" in choice_seven or "HELP" in choice_seven or "help" in choice_seven:
        print ("These are your choices,")
        print ("inspect, look around, help, hit grate, hit the grate, exit")

    if "EXIT" in choice_seven or "Exit" in choice_seven or "exit" in choice_seven:
        exit(1)

def brick():
    print ("You hit the grte with the brick, causing the part of the grate to fall off. The brick also breaks.")
    print ("                                                                                 ")
    print ("You climb out of the opening and in the distance you see a run-down building, possibly a factory.")
    print ("                                                                                 ")
    print ("You decide to walk towards it. After an hour of walking, you reach the building.")
    print ("                                                                                 ")
    print ("What do you do?")

    choice_eight = input("> ")

    if "Inspect" in choice_eight or "inspect" in choice_eight or "INSPECT" in choice_eight:
        print ("As stated before, it's a giant building, possibly a factory.")

    if "EXIT" in choice_eight or "Exit" in choice_eight or "exit" in choice_eight:
        exit(1)

    if "Help" in choice_eight or "HELP" in choice_eight or "help" in choice_eight:
        print ("These are your choices,")
        print ("Inspect, exit, look around, help")

    if "Look Around" in choice_eight or "look around" in choice_eight or "LOOK AROUND" in choice_eight:
        print ("You look around for a way into the building, Which way do you look first? Right or Left?")

    choice_nine = input("> ")

    if "right" in choice_nine or "RIGHT" in choice_nine or "Right" in choice_nine or "R" in choice_nine or "r" in choice_nine:
        print ("You head to the right, towards the front of the building. When you get to the front, you see what remains of the name of the building, you assume it says 'Ch__e__o_ En__r_i__s,' and a door.")
        print ("What do you do?")
        door()

    if "Left" in choice_nine or "LEFT" in choice_nine or "left" in choice_nine or "L" in choice_nine or "l" in choice_nine:
        print ("You head to the left, towards the back of the building. When you get to the back, you see different bits of human skeletons.")
        print ("You see a vent that leads in, do you climb into it? Or do you want to go back to the front?")
        front()

    if "EXIT" in choice_nine or "Exit" in choice_nine or "exit" in choice_nine:
        exit(1)

    if "HELP" in choice_nine or "Help" in choice_nine or "help" in choice_nine:
        print ("These are your chocies,")
        print ("right, left, exit, help")

def front():
    choice_raw = input("> ")

    if "Climb" in choice_raw or "CLIMB" in choice_raw or "Climb in" in choice_raw or "climb" in choice_raw or "climb in" in choice_raw:
        print ("You decide to climb into the vent, and start heading forward. After crawling for a bit,  the vent suddenly gives way from underneath you, causing you to go flying towards the ground.")
        print ("                                                                                 ")
        print ("You writhe around on the floor in pain for a bit, and get up to study where you're at. You look to see you're surrounded by old conveyor belts and other factory mechanisms.")
        print ("                                                                                 ")
        print ("You see a door ahead of you, and one behind you. You also notice a distant whirring ahead of you, which door do you go into?")
        door2()
        
    if "don't climb in" in choice_raw or "Don't Climb in" in choice_raw or "dont climb" in choice_raw or "Don't" in choice_raw:
        print ("You decide to not climb in the vent.")
        front()

    if "go back" in choice_raw or "leave" in choice_raw or "Go Back" in choice_raw or "Back" in choice_raw or "back" in choice_raw:
        print ("You decide to go to the front of the building.")
        front()

    if "EXIT" in choice_raw or "exit" in choice_raw or "Exit" in choice_raw:
        exit(1)

    if "HELP" in choice_raw or "Help" in choice_raw or "help" in choice_raw:
        print ("These are your choices,")
        print ("climb, dont climb, go back, exit, help")


def door():
    choice_good = input("> ")

    if "Open Door" in choice_good or "open door" in choice_good or "open the door" in choice_good:
        print ("You try to open the door, but find it locked.")
        brick()

    if "EXIT" in choice_good or "Exit" in choice_good or "exit" in choice_good:
        exit(1)

    if "HELP" in choice_good or "Help" in choice_good or "help" in choice_good:
        print ("These are your choices,")
        print ("open door, help, exit")

def door2():
    choice_what = input("> ")

    if "behind" in choice_what or "Behind" in choice_what:
        print ("You enter the door behind you. and you get hit with and overwhelmingly foul stench. It's hard to see, but you can just barely make out figures in the darkness.")
        print ("                                                                                 ")
        print ("Thinking they are human, you go further into the room. You go to touch one of the figures, but it suddenly grabs your arm. Too late, you realize that the figure you saw were all creatures you saw back in the city.")
        print ("                                                                                 ")
        print ("Slowly, they all get up and walk towards you. The last thing you see, is the one holding your arm thrust its claws at your face. Game Over.")
        dead()

    if "ahead" in choice_what or "Ahead" in choice_what:
        print ("You go towards the door ahead of you and open it, slowly. You cautiously enter the room, and you noitice a light in the distance. You walk towards the light, the whirring sounds getting louder and louder the closer you get.")
        print ("                                                                                 ")
        print ("Eventually you can make out that there's a machine ahead of you, and it appears to be creating more of those creatures you saw in the city.")
        print ("                                                                                 ")
        print ("Structurally, it looks weak, like it'd fall apart if someone shot it with a gun. You take a step forward, but suddenly an alarm blares. Thankfully, the creatures in the room aren't reacting to the noise, but under the blaring alarm, you hear a faint screeching.")
        print ("                                                                               ")
        print ("Realizing it's coming from the room behing you, you wonder if you should barricade the room or not. Do you?")
        barricade()

    if "Help" in choice_what or "help" in choice_what:
        print ("These are your choices")
        print ("ahead, behind, exit")

    if "exit" in choice_what or "Exit" in choice_what:
        exit(1)

def barricade():
    choice_ip = input("> ")

    if "no" in choice_ip or "No" in choice_ip:
        print ("You decide not to barricade the room, and the creatures break into the room, the last thing you see is a claw swipping at your face")
        dead()

    if "help" in choice_ip or "Help" in choice_ip:
        print ("These are your choices")
        print ("yes, no, exit")

    if "exit" in choice_ip or "Exit" in choice_ip:
        exit(1)

    if "yes" in choice_ip or "Yes" in choice_ip:
        print ("You barricade the room as best you can in the limited time you have. You hear the creatures banging against the door to get in, and one's claw breaks through your rudimentary blockage.")
        print ("                                                                                 ")
        print ("You turn back to the machine, you notice an opening in the wall to the right of it. This is your chance. Do you end this nightmare, or do you keep running like a coward?") 

    choice_lo = input("> ")

    if "run" in choice_lo or "Run" in choice_lo:
        print ("You decide to run, and as you exit through the wall, just narrowly avoiding the creatures, you notice a sign in the distance. You run towards it.")
        print ("                                                                                 ")
        print ("It says, within the deep, you shall find what was once the pinnicale of technology. Take it, and you shall defeet the machine. However, due to you being here "+name+", you failed.")
        print ("                                                                                 ")
        print ("And failure does not go unpunished. Keppt heading east. you shall return to where you started.")
        tree()

    if "help" in choice_lo or "Help" in chocie_lo:
        print("These are your chocies")
        print("run,shoot,exit")

    if "exit" in choice_lo or "Exit" in choice_lo:
        exit(1)

    if "shoot" in choice_lo or "Shoot" in choice_lo or "Shoot the machine" in choice_lo:
        print ("Clutching the grip of the pistol, you take aim.")
        print ("                                                                                 ")
        print ("You fire.")
        print ("                                                                                 ")
        print("You hit the machine and try to fire again and it hits the machine for a second time, casuing it to explode and send shrapnel everywhere.")
        print ("                                                                                 ")
        print ("You fall to the ground in pain, as you look up at the machine you see a portal where it once was. The creatures finally get into the room.")
        print ("                                                                                 ")
        print ("What do you do?")

    choice_ol = input("> ")

    if "run" in choice_ol or "Run" in chocie_ol:
        print ("Summoning what little strength you have left you run to the portal. Just as you pass into it, you see a creature reach towards you.")
        print ("                                                                                 ")
        print ("Suddenly, nothing. You blink and wind up back in front of the tree, everything as it was before. You stumble back home.")
        win()
        
        
def win():
    print ("Congratulations "+name+", you have won the game, we hope you enjoyed playing!! Big thank you from the developers!")
    exit(1)

def secret():
    print ("""\
                                               |>>>
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       \,/
                                             ||: , |            /`\
                                             ||:   |
                                             ||: . |
              __                            _||_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~
""")
    print ("I see you you have found a secret path "+name+", I wonder where it leads?")

    choice_is = input("> ")

    if "lore" in choice_is or "I don't know" in choice_is or "oof" in choice_is or "Kyle" in choice_is or "kyle" in choice_is or "yes" in choice_is or "YES" in choice_is or "Yes" in choice_is:
        print ("This tree you have found is of that of an odd sort")

    if "EXIT" in choice_is or "exit" in choice_is or "Exit" in choice_is:
        exit(1)

    if "HELP" in choice_is or "Help" in choice_is or "help" in choice_is:
        print ("These are your choices,")
        print ("lore, exit, help")


def dead():
    print ("""\
   _____                         ____
  / ____|                       / __ \
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|
   """)
    begin()

def begin():
    print ("Would you like to start over?")

    good_choice = input("> ")

    if "yes" in good_choice or "Yes" in good_choice or "y" in good_choice or "Y" in good_choice or "YES" in good_choice:
        start()

    if "no" in good_choice or "No" in good_choice or "N" in good_choice or "n" in good_choice or "NO" in good_choice:
        exit(1)

    if "HELP" in good_choice or "help" in good_choice or "Help" in good_choice:
        print ("These are your choices,")
        print ("yes, no, help")

def start():
    print("""\
                                     ######
                                  # #### ####
                                ### \/#|### |/####
                               ##\/#/ \||/##/_/##/_#
                             ###  \/###|/ \/ # ###
                           ##_\_#\_\## | #/###_/_####
                          ## #### # \ #| /  #### ##/##
                           __#_--###`  |{,###---###-~
                                     \ }{
                                      }}{
                                      }}{
                                      {{}
                                , -=-~{ .-^- _
                                       """)
    print ("You've been walking through an enchanted forest with gigantic trees as tall as mountains and as thick as large lakes.")
    print ("                                                                                 ")
    print ("You stumble upon a tree that seems to be glowing and emitting a certain sound, soft like a whisper.")
    print ("                                                                                 ")
    print ("You're drawn to the tree and have a weird feeling in your stomach, so "+name+" should you touch the tree or walk away?")
    print ("                                                                                 ")

    small_choice = input("> ")

    if "tree" in small_choice or "Yes" in small_choice or "yes" in small_choice or "Tree" in small_choice or "enter" in small_choice or "Enter" in small_choice or "touch" in small_choice or "Touch" in small_choice or "touch the tree" in small_choice or "Touch the Tree" in small_choice or "go" in small_choice or "Go" in small_choice:
        tree()

    if "walk" in small_choice or "Walk" in small_choice or "leave" in small_choice or "Leave" in small_choice or "walk away" in small_choice or "Walk Away" in small_choice or "no" in small_choice or "No" in small_choice:
        dead()

    if "exit" in small_choice or "Exit" in small_choice:
        exit(1)

    if "help" in small_choice or "Help" in small_choice or "HELP" in small_choice:
        print ("These are your choices,")
        print ("tree, enter, touch, touch the tree, go,")
        print ("walk, leave, walk away, no,")
        print ("Exit")

        start()
    else:
         print ("I have no idea what you're saying. Lets try that again.")
         start()


def tree():
    print ("""\
                    .    _    +     .  ______   .          .
                 (      /|\      .    |      \      .   +
                     . |||||     _    | |   | | ||         .
                .      |||||    | |  _| | | | |_||    .
                   /\  ||||| .  | | |   | |      |       .
                __||||_|||||____| |_|_____________\__________
                . |||| |||||  /\   _____      _____  .   .
                  |||| ||||| ||||   .   .  .         ________
                 . \|`-'|||| ||||    __________       .    .
                    \__ |||| ||||      .          .     .
                 __    ||||`-'|||  .       .    __________
                .    . |||| ___/  ___________             .
                   . _ ||||| . _               .   _________
                _   ___|||||__  _ \\--//    .          _
                     _ `---'    .)=\oo|=(.   _   .   .    .
                _  ^      .  -    . \.|
""")
    print ("You get sucked through a portal and you find yourself thrown upon a sandy ground.")
    print ("                                                                                 ")
    print ("The ground is of an orange coloration and the sky is of bright red.")
    print ("                                                                                 ")
    print ("You see skeletons all over the ground some seeming to be crawling away from the post and others towards. There are dead trees everywhere dry and broken.")
    print ("                                                                                 ")
    print ("You walk over to the post and it reads four directions North, South, East, and West.")
    print ("                                                                                 ")
    print ("Which way do you choose to go "+name+"?")

    do_what = input("> ")

    while True:
        if "north" in do_what or "North" in do_what or "n" in do_what or "N" in do_what:
            north()

        if "south" in do_what or "South" in do_what or "s" in do_what or "N" in do_what:
            south()

        if "east" in do_what or "East" in do_what or "e" in do_what or "E" in do_what:
            dead()

        if "west" in do_what or "Wast" in do_what or "w" in do_what or "E" in do_what:
            west()

        if "exit" in do_what or "Exit" in do_what or "e" in do_what or "E" in do_what:
            exit(1)

        if "help" in do_what or "Help" in do_what or "HELP" in do_what or "h" in do_what or "H" in do_what:
            print ("These are your choices")
            print ("North, South, East, West, Exit")
            tree()

        if "nowhere" in do_what or "Nowhere" in do_what or "n" in do_what or "N" in do_what:
            secret()

        else:
            print ("I got no idea what you're saying. Which way was it again?")
            tree()

start()
