# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gui.choice_button_text_idle_color = '#9b2215'

image bard happy = im.Crop("BARD HAPPY.png", (300, 200, 1100, 1800))
image bard happy = im.Scale("BARD HAPPY.png", 500, 750)

image piz idle = im.Crop("PIZ IDLE.png", (300, 200, 1100, 1800))
image piz idle = im.Scale("PIZ IDLE.png", 500, 750)

image piz think = im.Crop("PIZ THINK.png", (300, 200, 1100, 1800))
image piz think = im.Scale("PIZ THINK.png", 500, 750)

image piz horror = im.Crop("PIZ HORROR.png", (300, 200, 1100, 1800))
image piz horror = im.Scale("PIZ HORROR.png", 500, 750)

image piz speak = im.Crop("PIZ SPEAK.png", (300, 200, 1100, 1800))
image piz speak = im.Scale("PIZ SPEAK.png", 500, 750)

image bob idle = im.Crop("BOB IDLE.png", (300, 200, 1100, 1800))
image bob idle = im.Scale("BOB IDLE.png", 500, 750)

image bob happy = im.Crop("BOB HAPPY.png", (300, 200, 1100, 1800))
image bob happy = im.Scale("BOB HAPPY.png", 500, 750)
           
image bob think = im.Crop("BOB THINK.png", (300, 200, 1100, 1800))
image bob think = im.Scale("BOB THINK.png", 500, 750)
               
image bob horror = im.Crop("BOB HORROR.png", (300, 200, 1100, 1800))
image bob horror = im.Scale("BOB HORROR.png", 500, 750)
                
image bob speak = im.Crop("BOB SPEAK.png", (300, 200, 1100, 1800))
image bob speak = im.Scale("BOB SPEAK.png", 500, 750)

image bard happy = im.Crop("BARD HAPPY.png", (300, 200, 1100, 1800))
image bard happy = im.Scale("BARD HAPPY.png", 475, 725)

image owlbear mad = im.Crop("OWLBEAR MAD.png", (300, 200, 1100, 1800))
image owlbear mad = im.Scale("OWLBEAR MAD.png", 500, 750)

image stress bar = im.Scale("stress_bar.png", 350, 35)
image stress bar:
    "stress_bar.png"
    xalign 0.95
    yalign 0.1

define piz = Character("Piz", color="#0055FF")
define bob = Character("Bob", color="#89CC4B")

default stress_level = 0
default focus_level = 0

default did_food_activity = False
default did_music_activity = False
default did_buy = False
default did_scope_activity = False
default did_warmup_activity = False

default showup_bob = False
default showup_piz = False
default showup_none = False
default showup_both = False
default showup_one = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg welcome
    play music "audio/theme.mp3"
    play audio 'audio/Crowd in Fair.mp3' volume 0.15 loop
    "Welcome to Townia Fair!"   

    label piz:
        scene bg fair

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        show piz idle
        show screen bar_stress_level
        show stress bar
        # These display lines of dialogue.
        voice "audio/piz_happy3.mp3"
        piz "I made it to the fair right on schedule! This fair has attracted such a large crowd. Hopefully, I can accomplish my tasks in the correct order."
        show piz think
        voice "audio/piz_think1.mp3"
        piz  "First, I need to find my missing topping. Second is the cheese filling booth for my crust. Then, I need to get a decoration for the final touch. From there to the competition."
    
    #1.2
    menu:
        "Find missing topping":
            jump piz_choice1_toppings
        "Wander in":    
            jump piz_choice1_wander

    label piz_choice1_toppings:
        jump piz_choice4_toppings

    label piz_choice1_wander:  
        $ stress_level += 15
        show piz idle
        "Looking around, there seems to be great excitement at the fair with many people walking to-and-fro. "
        "The toppings stall, which is at top of Piz’s list, appears to be at the far end of the fair."
        stop music fadeout 1.0
        play music "audio/Musician - First Half (Slow).mp3"
        "Whereas, the cheese crust filling stall is nearby. There is the sound of someone playing the lute close by as well."

    show piz think

    #2.2
    menu:
        "Reach the toppings stall":
            jump piz_choice2_toppings
        "Approach the cheese crust filling stall":    
            jump piz_choice2_crust
        "Follow the music":
            jump piz_choice2_music    

    label piz_choice2_toppings:
        stop music
        play music "audio/theme.mp3"
        jump piz_choice4_toppings

    label piz_choice2_crust:
        $ stress_level += 15
        stop music
        play music "audio/theme.mp3"
        jump piz_crust_out_of_order

    label piz_choice2_music:
        $ stress_level += 20
        stop music
        play music "audio/Musician - Second Half (Fast).mp3"
        show piz horror
        show bard happy at left
        voice "audio/piz_horror3.mp3"
        piz "The music is nice, but this definitely isn’t where I’m supposed to be."   
        "Looking around: the toppings stall, which is at the top of Piz’s list, appears to be at the far end of the fair, whereas the cheese crust filling stall is nearby."

    #3.2
    menu:
        "Reach the toppings stall":
            jump piz_choice3_toppings
        "Approach the cheese crust filling stall":    
            jump piz_choice3_crust
        "Listen to the music for a while longer":
            jump piz_choice3_music    

    label piz_choice3_toppings:
        stop music
        play music "audio/theme.mp3"
        jump piz_choice4_toppings

    label piz_choice3_crust:
        $ stress_level += 15
        stop music
        play music "audio/theme.mp3"
        jump piz_crust_out_of_order

    label piz_choice3_music:
        $ stress_level += 25
        show piz horror
        show bard happy at left
        voice "audio/piz_horror1.mp3"
        piz "I really shouldn’t be wasting my time on this. I still have a list of errands to accomplish before the competition."
        "Looking around: the toppings stall, which is at the top of Piz’s list, appears to be at the far end of the fair, whereas the cheese crust filling stall is nearby." 
        stop music
        play music "audio/theme.mp3"

    #4.2
    menu:
        "Reach the toppings stall":
            jump piz_choice4_toppings
        "Approach the cheese crust filling stall":    
            jump piz_choice4_crust
    
    #5
    label piz_choice4_crust:
    label piz_crust_out_of_order:
        $ stress_level += 15
        play sound "audio/Trade - Cheese Filling.mp3"
        show piz horror
        voice "audio/piz_horror2.mp3"
        "There seemed to be a big crowd between Piz and the topping stall. Therefore, Piz decided to approach the nearby stall and have his crust filled with cheese."
        "Having done that, Piz made his way through the crowd to reach the toppings stall."  
        jump piz_topping_out_of_order

    #6.1
    label piz_choice4_toppings:
        play sound "audio/Trade - Cast Iron.mp3"
        show piz idle
        "Piz cleared a path through the crowd to the stall and picked out his missing topping, now satisfied that he completed the first item on his list."
        show piz speak   
        voice "audio/piz_happy2.mp3"
        piz "This is exactly what I needed!"
        show piz idle
        "Next on his list is the cheese crust filling, and then to find the perfect decoration for the final touch up."

    #6.2
        show piz think
    menu:
        "Approach cheese crust filling stall":
            jump piz_choice5_crust
        "Find the perfect final decoration":    
            jump piz_choice5_decor

    #7.1
    label piz_choice5_crust:
        play audio "audio/Trade - Cheese Filling.mp3"
        "Piz made his way back to where the stall was. Completing items on the list in order helps focus him on his task." 
        show piz idle
        "Therefore, he managed to get his crust filled with quality cheese."
        show piz speak  
        voice "audio/piz_happy1.mp3"
        piz "This cheese holds up really well!"
        piz "The final touch up would be to find the final decoration to add before signing up."
        jump choice_6

    label piz_choice5_decor:
        $ stress_level += 15
        jump piz_decor_out_of_order

    #7.2
    label choice_6:
        show piz think
    menu:    
        "Sign up to the competition":
            jump piz_choice6_signup
        "Find the perfect final decoration":    
            jump piz_choice6_decor

    label piz_choice6_signup:
        $ stress_level += 15
        jump piz_final         

    label piz_choice6_decor:
        jump piz_decor_in_order   

    #8.1
    label piz_topping_out_of_order:
        play sound "audio/Trade - Cast Iron.mp3"
        show piz idle
        "Piz approached the stall and picked out his missing topping, finally completing the first item on his list. Completing tasks out of order stresses him out."
        "Now, all that is left on the list is to find the perfect decoration for the final touch up before signing up to the competition."
    #8.2
        show piz think
    menu:    
        "Sign up to the competition":
            jump piz_choice7_signup
        "Find the perfect final decoration":    
            jump piz_choice7_decor

    label piz_choice7_signup:
        $ stress_level += 15
        jump piz_final

    label piz_choice7_decor:
        jump piz_decor_in_order    

    #9
    label piz_decor_out_of_order:
        play sound "audio/Trade - Sparkle.mp3"
        show piz horror
        "Sifting through a nearby stall, Piz found an adequate final decoration to set on himself for the competition."
        voice "audio/piz_horror3.mp3"
        piz "I wasn’t supposed to do this now, but I suppose that this should do."       
        "From there, he moved on to the cheese crust filling stall and arranged that as well."   
        jump piz_decor_after

    #10
    label piz_decor_in_order:
        play sound "audio/Trade - Decoration Sparkle.mp3"
        show piz idle
        "The last item on the list is to find the final perfect decoration, and Piz definitely found it. The magnificent piece adornes his body perfectly."
        show piz speak
        voice "audio/piz_happy4.mp3"
        piz "This is perfect!"
        jump piz_decor_after

    #11
    label piz_decor_after:
        play sound "audio/Trade - Ding.mp3"
        show piz speak
        voice "audio/piz_happy2.mp3"
        piz "Finally, all errands are complete and I can go sign up to the competition!"
        jump piz_competition

    #12
    label piz_final:
        show piz horror
        voice "audio/piz_horror1.mp3"
        piz "I didn’t get a chance to complete all my errands. I hope I’m ready for the competition. Regardless, there is no turning back"
        jump piz_competition   

    label piz_competition:
        jump bob



    label bob:
        scene bg welcome
        hide screen bar_stress_level
        "Meanwhile…"

        scene bg fair
        show screen bar_focus_level
        show bob happy
        voice "audio/bob_happy1.mp3"
        bob "Hello Townia fair!"
        bob "Let’s see, I have to find the sign up booth to test my strength swinging that hammer."
        voice "audio/bob_happy3.mp3"
        stop music
        play music "audio/Musician - First Half (Slow).mp3"
        bob "But look at this place! There are so many things to try out, food to eat, goods to peruse, and the sound of music being played. What shall I do first?"

    #2.2
    menu:
        "Look for competition sign up":
            jump bob_choice1_signup
        "Approach the first stall":
            jump bob_choice1_stall
        "Follow the music":
            jump bob_choice1_music

    label bob_choice1_signup:
        $ focus_level += 35
        stop music
        play music "audio/theme.mp3"
        jump bob_choice5_signup
    label bob_choice1_stall:
        stop music
        play music "audio/theme.mp3"
        jump bob_choice3_stall

    #3.1
    label bob_choice1_music:
        show bob happy
        show bard happy at left
        voice "audio/bob_happy4.mp3"
        bob "This music sounds really nice! Just what I need to get into the mood of the competition!"
        show bob think

    #3.2
    menu:
        "Look for competition sign up":
            jump bob_choice2_signup
        "Listen to the music":
            jump bob_choice2_music

    label bob_choice2_signup:
        if (not did_food_activity and not did_music_activity):
            $ focus_level += 25
        else:
            $ focus_level += 15
        stop music
        play music "audio/theme.mp3"
        hide bard happy # won't go away on its own
        jump bob_choice5_signup

    #4.1
    label bob_choice2_music:
        $ did_music_activity = True
        stop music
        show bard happy at left
        play music "audio/Musician - Second Half (Fast).mp3"
        show bob idle
        "Bob made it to the musician who was playing for quite the crowd. All seemed happy and pleased to just stand by and listen."
        "A few even tossed coins into the hat placed nearby on the floor."
        show bob happy
        bob "This was great and I enjoyed that a immensely! What should I do next?"
        voice "audio/bob_think1.mp3"
        bob "I need to sign up to the competition, but there is still so much to explore at this amazing fair."
        stop music
        play music "audio/theme.mp3"

        if not did_food_activity:
            #4.2
            show bob think
            menu:
                "Look for competition sign up":
                    $ focus_level += 25
                    jump bob_choice3_signup
                "Approach the first food stall":
                    jump bob_choice3_stall
        #4.3
        else:
            $ focus_level += 15
            jump bob_choice3_signup


    label bob_choice3_signup:
        hide bard happy # won't go away on its own
        jump bob_choice5_signup

    #5.1
    label bob_choice3_stall:
        hide bard happy # won't go away on its own
        $ did_food_activity = True
        play sound "audio/Trade - Food Sizzle.mp3"
        show bob happy
        voice "audio/bob_happy2.mp3"
        bob "Oh wow, look at all of this amazing food! Maybe I have time to try a tiny bite…"
        # bard image is showing up, not sure why

    #5.2
    menu:
        "Buy food and eat it":
            jump bob_choice4_food
        "Look for sign up competition":
            jump bob_choice4_signup

    label bob_choice4_signup:
        if (not did_food_activity and not did_music_activity):
            $ focus_level += 25
        else:
            $ focus_level += 15
        jump bob_choice5_signup

    #6.1
    label bob_choice4_food:
        $ did_food_activity = True
        play sound "audio/Trade - Eat Food.mp3"
        show bob idle
        bob "Om nom nom"
        voice "audio/bob_think2.mp3"
        bob "This tasted so good. What should I do now?"

    if not did_music_activity:
        #6.2
        show bob think
        menu:
            "Follow the music":
                jump bob_choice1_music
            "Look for competition sign up":
                $ focus_level += 25
                jump bob_choice5_signup
    else:
        $ focus_level += 15
        jump bob_choice5_signup

    #7.1
    label bob_choice5_signup:
        show bob think
        voice "audio/bob_think1.mp3"
        "The sign up stall is straight ahead, right next to a stall with a lot of shiny materials and elements on display."

    #7.2
    show bob idle
    menu:
        "Sign up":
            jump bob_choice6_signup

        "Examine shiny stall":
            jump bob_choice6_shiny

    label bob_choice6_signup:
        $ focus_level += 20
        jump bob_signup

    #8.1
    label bob_choice6_shiny:
        $ did_buy = True
        play sound "audio/Trade - Whetstone.mp3"
        show bob happy
        "Before signing up to the competition, Bob decided to examine the nearby stall. The items at the stall are mesmerizing in their appearance and function."
        voice "audio/bob_happy4.mp3"
        bob "I’ll buy this shiny whetstone, which will definitely upgrade the sharpness of my mighty axe."
        "Following the purchase, Bob signed up to the competition, and realized there is still time before it starts. He could try to do something useful to focus himself or just wait and let the excitement take over."
    #8.2
    show bob idle
    menu:
        "Do warm up sessions":
            jump bob_choice7_warmnup
        "Scope out competitors":
            jump bob_choice7_scope
        "Wait for start of competition":
            jump bob_choice7_competition

    label bob_choice7_warmnup:
        $ focus_level += 15
        jump bob_choice8_warmnup

    label bob_choice7_scope:
        $ focus_level += 15
        jump bob_scope

    label bob_choice7_competition:
        if did_buy:
            $ focus_level -= 10
            jump bob_buy_competition
        else:
            jump bob_not_buy_competition

    #9.1
    label bob_signup:
        show bob think
        voice "audio/bob_think1.mp3"
        "Bob signed up to the competition, and realized there is still time before it starts. He could try to do something useful to focus himself or just wait and let the excitement take over."

    #9.2
    menu:
        "Do warm up sessions":
            jump bob_choice8_warmnup
        "Scope out competitors":
            jump bob_choice8_scope
        "Wait for start of competition":
            jump bob_choice8_competition

    label bob_choice8_scope:
        $ focus_level += 15
        jump bob_scope


    #10.1
    label bob_choice8_warmnup:
        $ focus_level += 15
        $ did_warmup_activity = True
        if not did_scope_activity:
            show bob think
            "This competition is important and therefore, it is important to make sure one is prepared for when it is time to land the decisive strike."
            voice "audio/bob_happy3.mp3"
            bob "These really helped me focus! Should I check out who my competitors are or just wait by myself for the competition to start?"
            #10.2
            menu:
                "Scope out competitors":
                    jump bob_choice9_scope
                "Wait for the start of the competition":
                    jump bob_choice9_competition

            label bob_choice9_scope:
                $ focus_level += 25
                jump bob_scope_did_warmup

            label bob_choice9_competition:
                if did_buy:
                    $ focus_level -= 10
                    jump bob_buy_competition
                else:
                    jump bob_not_buy_competition

        #10.3
        else:
            label bob_warmup_did_scope:
                show bob think
                "This competition is important and therefore, it is important to make sure one is prepared for when it is time to land the decisive strike. All that is left is to wait for the competition to start."
                if did_buy:
                    $ focus_level -= 10
                    jump bob_buy_competition
                else:
                    jump bob_not_buy_competition

    #11.1
    label bob_scope:
        $ did_scope_activity = True
        if not did_warmup_activity:
            show bob think
            voice "audio/bob_horror1.mp3"
            "The competition looks fierce and Bob examines each of the seven carefully: three are human, one a half-orc, two dwarves and a rather burly elf."
            "He gains the confidence that he truly has a chance to beat them for the winning title. He can just wait for the competition to start or do some warm sessions beforehand."

            #11.2
            menu:
                "Do warm up sessions":
                    jump bob_choice10_warmnup
                "Wait for start of competition":
                    jump bob_choice10_competition

            label bob_choice10_warmnup:
                $ focus_level += 25
                jump bob_warmup_did_scope

            label bob_choice10_competition:
                if did_buy:
                    $ focus_level -= 10
                    jump bob_buy_competition
                else:
                    jump bob_not_buy_competition
        #11.3
        else:
            label bob_scope_did_warmup:
                show bob think
                voice "audio/bob_horror1.mp3"
                "The competition looks fierce and Bob examines each of the seven carefully, three are human, one a half-orc, two dwarves and a rather burly elf."
                voice "audio/bob_happy2.mp3"
                "He believes that he stands a good chance against them. All that is left is to wait for the competition to start."


        label bob_choice8_competition:
        if did_buy:
            jump bob_buy_competition

        else:
            jump bob_not_buy_competition

    #13
    label bob_buy_competition:
        $ focus_level -= 10
        play sound "audio/Trade - Ding.mp3"
        show bob happy
        "While Bob waits for the competition to start, he pulls out the whetstone he just bought and works on sharpening his mighty axe."
        "He is full of excitement as he waits for the competition to start. It should be soon."
        voice "audio/bob_happy2.mp3"
        bob "I will show everyone what a gelatinous octopus such as myself is capable of. I can do this!"
        jump ending_seq

    #12
    label bob_not_buy_competition:
        show bob happy
        "Bob is full of excitement as he waits for the competition to start. It should be soon."
        voice "audio/bob_happy2.mp3"
        bob "I will show everyone what a gelatinous octopus such as myself is capable of."
        jump ending_seq



    #1
    label ending_seq:
        hide screen bar_focus_level
        hide bob happy # won't go away on its own
        show bg welcome
        stop music
        play music "audio/Fight Theme.mp3"
        "As people are enjoying the town fair, it’s music, food and various activities, the sound of something big starts to be heard over the excitement."
        show owlbear mad
        voice "audio/owlbeart_angry.mp3"
        "As it grows closer, it appears that a great owlbear decided to crash the festivities."

        if (focus_level <= 80):
            $ showup_bob = True
        if (stress_level <= 80):
            $ showup_piz = True
        if (not showup_bob and showup_piz) or (showup_bob and not showup_piz):
            $ showup_one = True
        elif showup_bob and showup_piz:
            $ showup_both = True
        else:
            $ showup_none = True

        # Caused issues - needs fixing --->  if showup_both or showup_one:
            #sound and background


        if showup_both:
            jump showup_both_finale
        if showup_one:
            jump showup_one_finale
        if showup_none:
            jump showup_none_finale

    label showup_both_finale:
        play sound "audio/Full Saved- Crowd Screaming Only.mp3"
        "The monster’s intentions are clear, he aims to destroy the fair and anyone who stands in its way!"
        "Is there anybody that would stop it before it is too late?"

        show piz think at left
        show bob speak at right
        "Piz and Bob are prepared to make a stand against the horrible creature."
        play sound "audio/piz_bob_battle.mp3"
        "The battle is hard as the monster slashes at them, while they both defend against the attacks. Piz fires a spell to stun the creature as Bob drives his mighty axe to finally strike down the beast."

        hide owlbear mad
        hide piz think
        hide bob speak
        show piz speak at left
        show bob happy at right
        play sound "audio/Full Saved- Cheering.mp3"
        "Piz and Bob are heroes who stood up against the massive owlbear and defeated it. Townia’s fair was saved and that evening there was a big celebration in their honor."
        jump game_ending

    label showup_one_finale:
        play sound "audio/Half Saved- Crowd Screaming + Slight Destruction.mp3"
        "The monster’s intentions are clear, he aims to destroy the fair and anyone who stands in its way!"
        "Is there anybody that would stop it before it is too late?"
        if (showup_piz):
            show piz think at left
            play sound "audio/piz_think1.mp3"
            "Piz is prepared to make a stand against the horrible creature."
            play sound "audio/piz_battle.mp3"
            "But the monster is big and its slashes cut deep into Piz’s crust. Piz manages to conjure a few crucial spells that hit the monster hard and finally, it is defeated."

            hide owlbear mad
            show piz idle
            "When all seemed lost as a horror swept into the fair, there was only one who stood against it. Piz fought hard and managed eventually to halt the monster’s progress."
            show piz speak
            play audio "audio/Half Saved- Cheering.mp3"
            "However, it was not without its toll of destruction. There was a tame celebration in Piz’s honor before the crowd shuffled to start work on clearing up the mess left behind."
            jump game_ending

        if (showup_bob):
            show bob speak at right
            play sound "audio/bob_walk.mp3"
            "Bob is prepared to make a stand against the horrible creature."
            play sound "audio/bob_battle.mp3"
            "But the monster is big and its slashes cut deep into Bob’s gelatinous form. Despite this, Bob doesn’t waver and continues to hold fast."

            "Finally, he finds the monster’s weak spot and strikes true with his giant axe, as the monster crumples down, defeated."

            hide owlbear mad
            show bob idle
            "When all seemed lost as a horror swept into the fair, there was only one who stood against it. Bob fought hard and managed eventually to halt the monster’s progress."
            show bob happy
            play audio "audio/Half Saved- Cheering.mp3"
            "However, it was not without its toll of destruction. There was a tame celebration in Bob’s honor before the crowd shuffled to start work on clearing up the mess left behind."
            jump game_ending

    label showup_none_finale:
        play sound "audio/Destroyed- Screaming + Destruction.mp3"
        "The monster’s intentions are clear, he aims to destroy the fair and anyone who stands in its way!"
        "Is there anybody that would stop it before it is too late?"
        "As the monster roared and bared its sharp claws, there was no one to stand against it. It easily menaced its way through the fair grounds, destroying anything and anyone in its wake."
        "..."
        hide owlbear mad
        # maybe should add a black screen as a background
        play sound "audio/Destroyed- Sad Crowd + Fire.mp3"
        "When it finally left, the entire place was in shambles and many were injured or killed. This isn’t a day that the people of Townia will soon forget…"
        jump game_ending


        




    # This ends the game.
label game_ending:
    return
