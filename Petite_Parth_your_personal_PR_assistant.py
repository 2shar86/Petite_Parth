import sys
import time
from PIL import Image
from IPython.display import display, Audio, Image as IPyImage

def type_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def main():
    petitometer = 0

    
    type_print(" SYSTEM: Welcome to the Petite Parth simulator! He is your very own 'PR' assistant. \n \n Trigger Parth's Petite fantasies by saying " \
               "what turns him on the most! And await the juiciest " \
               "ending to your interactions. \n\n" \
               "But be aware, Petite Parth is not your usual kind of assistant, he has a special way of getting turned on," \
               " your job is to find the best way to turn him on!\n")

    type_print(" PETITE PARTH: Halo guyz, I am ur frendly assistant, but " \
               "please dont take mind to my language, I am on the dickslexic side. " \
               "\nI just finished preparing for war for mother India, now I am all yours ...." \
               "to help!" \
               "\n \n" \
               " SYSTEM: Incite Parth with one of the following spicy cat calls\n" \
               "1. Parth you look handsome today\n" \
               "2. Parth you look extra petite today\n" \
               "3. Parth you look as midget as usual\n\n")
    first_ans = input()
    if first_ans == "Parth you look handsome today":
        type_print("PETITE PARTH: Hmm either daal mein kuch kaala hai ya fir aap kaale ho sir"
                   "\n SYSTEM: Looks like Parth does not like conventional compliments, he's playing"
                   " hard to get, try something blunt\n\n")
        petitometer += 1
    elif first_ans == "Parth you look extra petite today":
        type_print("PETITE PARTH: haan mein petis khaata huin" \
                   " Goodu's Pasteries se mil jaata hai \n" \
                   "SYSTEM: Looks like Parth is also mildly autistic. Please do not use" \
                   " complex vocabulary to communicate with him.\n\n")
        petitometer += 2
    elif first_ans == "Parth you look as midget as usual":
        type_print("PETITE PARTH: abbe oh randi ke bacche, systum faad dunga," \
                   "shaant ho ja, yahan tereko levels nhi pata levels\n" \
                   "SYSTEM: OH WOW! Quite the reaction! Looks like Petite Parth is starting to get" \
                   " moist. Keep it going.\n\n")
        petitometer += 3
    else:
        type_print("PETITE PARTH: kya bbol rha hai bsdk muh se supari nikaal ke bol bc\n" \
                   "SYSTEM: Please give a valid response next time, you are making Petite Parth impatient" \
                   " and you might miss out on turning him on!\n\n")

    type_print("SYSTEM: Keep saying things that turn Petite Parth on:\n"
               "1. Parth you are a nigger\n"
               "2. Parth what is your type\n"
               "3. Parth you said you are my PR assistant, but what 'PR' do you do for me\n")
    second_ans = input()
    if second_ans == "Parth you are a nigger":
        type_print("PETITE PARTH: Haan isliye teri maa ne uss raat mereko aate hue nahi dekha andhere mein\n"
                   "aur tu paida hogya\n"
                   "SYSTEM: WTF! Amazing! Petite Parth is now emotionally attracted to you and your mother!\n " 
                   "Keep it going Soldier.\n\n")
        petitometer += 3
    elif second_ans == "Parth what is your type":
        type_print("PETITE PARTH: I love tall woman with big knockers!\n"
                   "SYSTEM: Looks like parth's fantasy is to be a full time" \
                   " shortking sucking on goth-mew-two-build-mommy tits.\n But this is not" \
                   " enough to incite him.\n\n")
        petitometer += 1
    elif second_ans == "Parth you said you are my PR assistant, but what 'PR' do you do for me":
        type_print("PETITE PARTH: I personally ride dick just for you my friend\n"
                   "SYSTEM: Looks like Parth's illiteracy level has elevated his fanatastical desires!\n\n")
        petitometer += 2
    else:
        if petitometer < 2:
            type_print("PETITE PARTH: kya bbol rha hai bsdk muh se supari nikaal ke bol bc, mein chala gn\n"
                       "SYSTEM: You did not provide a valid response and it seems like Parth is turned off. GG," 
                       " better luck next time\n\n")
            return main()
        else:
            type_print("PETITE PARTH: kya bbol rha hai bsdk muh se supari nikaal ke bol bc\n"
                       "SYSTEM: Please give a valid response next time, you are making Petite Parth impatient" \
                       " and you might miss out on turning him on!\n\n")

    type_print("SYSTEM: OK this is the FINAL attempt to make Petite Parth Bust with"
               "how much your words have turned him on, make sure this one counts!\n"
               "1. Parth will you be mine\n"
               "2. Parth be my personal Bennett Bunny\n" 
               "3. Parth I love blue balling you whenever you call me to play games with you\n")
    third_ans = input()
    if third_ans == "Parth will you be mine":
        type_print("PETITE PARTH: I have always been yours baby\n"
                   "SYSTEM: Turns out Parth is gay himself, but this isnt enough" \
                   "to turn him on\n\n")
        petitometer += 2
    elif third_ans == "Parth be my personal Bennett Bunny":
        type_print("PETITE PARTH: Hatt madarchod, teri maa ke paas hoga bunny pussy\n"
                   "SYSTEM: Yes, Yes, YES! This might do it, this might turn petite parth's\n" 
                   "petite fantasies on full throtle and give you a sweet surprise!\n\n")
        petitometer += 6
    elif third_ans == "Parth I love blue balling you whenever you call me to play games with you":
        type_print("PETITE PARTH: Pheli baat teri khaandan randi, tu randi, teri shakal bhi randi\n"
                   "SYSTEM: This looks promising, parth is overwhelmed with emotions\n\n")
        petitometer += 4
    else:
        type_print("SYSTEM: for god's sake learn to type and give a valid response, Start again!")
        return main()

    type_print("SYSTEM: ALRIGHT enough chatting and let's see if Petite Parth's Petite Pussy is wet emough! \n"
               "5              4              3           2              1!\n\n")
    if petitometer < 10:
        type_print("PETITE PARTH: I don't feel horny enough with you! I am done being ur assistant!\n"
                   "SYSTEM: Unfortunetly it seems like you could not meet Parth's Petite expectations. Try again next time!\n")
        return main()
    else:
        type_print("PETITE PARTH: Ohhhh, NOooOooooooOOOooo La Polizia\n"
                   "I             \n"
                   "am          \n"
                   "about     \n"
                   "to.  .   .  .   .     \n"
                   "CUMMM\n")
        try:
            display(IPyImage("cockroach.png"))
            display(Audio("hawyeah.mp3", autoplay=True))
        except FileNotFoundError as e:
            type_print(f"Error: '{e.filename}' not found.")
        except Exception as e:
            type_print(f"Error displaying media: {e}")

if __name__ == "__main__":
    main()