import random
import pyttsx4

'''
 1 for rock
 -1 for paper
 0 for scissor 
'''
engine = pyttsx4.init()

voices = engine.getProperty('voices')
for voice in voices:
    # Check for gender property (not always available) or a name that suggests a female voice
    if voice.gender == 'female' or 'zira' in voice.name.lower() or 'helen' in voice.name.lower():
        female_voice_id = voice.id
        break
if female_voice_id:
    engine.setProperty('voice', female_voice_id)
else:
    pass

engine.setProperty("rate", 150)

computer = random.choice([1 , -1, 0])

# engine.say("Enter your choice (r for Rock, p for Paper, s for Scissor): ")
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissor): ")
youdict = {"p" : 1, "r" : -1, "s" : 0 }
reversedict = {1 : "Paper", -1 : " Rock", 0 : "Scissor"}

you = youdict[youstr]

print(f"Computer chose {reversedict[computer]}. \nYou chose {reversedict[you]}.")
engine.say(f"Computer chose {reversedict[computer]}. \nYou chose {reversedict[you]}.")


# now we have 2 numbers, one from computer and one from user
if ( computer == you) :  
    print("This game is draw!!") 
    engine.say("This game is draw!!")
else :
    if (computer == 1 and you == -1) : 
        print("You Lost the game!")
        engine.say("You Lose the Game!")
    elif (computer == 1 and you == 0) : 
        print("You Won the Game!")
        engine.say("You Won the Game!")
    elif (computer == -1 and you == 1) : 
        print("You Won the Game!")
        engine.say("You Won the Game!")
    elif (computer == -1 and you == 0) : 
        print("You Lose the Game!")
        engine.say("You Lose the Game!")
    elif (computer == 0 and you == 1) : 
        print("You Lose the Game!")
        engine.say("You Lose the Game!")
    elif (computer == 0 and you == -1) : 
        print("You Won the Game!")
        engine.say("You Won the Game!")
    else :
        print("Something went wrong!! \n TRY AGAIN !")
        engine.say("Something went wrong!! \n TRY AGAIN !")

engine.runAndWait()   