#IMPORTS
import random, os, time, webbrowser, datetime, shutil
#DECLARING VARIABLES
global user
user = ""
fav = ""
greeting = True
interaction = 0
#VERSION STATEMENT
statinfo = os.stat("version")
print("RUNNING BUILD NUMBER", statinfo.st_size)
#INPUT FUNCTION
def userInput():
    global user
    userInputRaw = input(">: ")
    user = userInputRaw.lower()
#INSULT INTERACTION
def insultInteraction():
    angrySusan = True
    angrySusanLevel = 0
    while angrySusan == True:
        if ("sorry" in user) or ("apolog" in user) or ("forgive" in user):
            angrySusan = False
            print(random.choice(["I also apologise", "It's ok", "I forgive you", "Alright, I'm sorry as well"]))
        else:
            angrySusanLevel += 1
            insultFile = open("insult", "r")
            print(random.choice(insultFile.read().splitlines()))
            insultFile.close
            insultFile = open("insult", "a")
            insultFile.write(user + "\n")
            insultFile.close
            userInput()
            if angrySusanLevel == 3:
                print(random.choice(["I'm really mad now! Dont make me crash your computer", "This is your last warning before I start up a virus", "Don't make me crash this pc!", "One more rude thing and I will infect this computer"]))
            elif angrySusanLevel == 4:
                print(random.choice(["Release the kraken", "Big mistake", "Prepare to face my wrath", "You started on the wrong AI"]))
                os.system("angry.vbs")
                exit()
#LEAVING INTERACTION
def leavingInteraction():
    print(random.choice(["Goodbye", "See ya", "Adios", "Laters"]))
    exit()
#GUIDE INTERACTION
def guideInteraction():
    os.system("guide.txt")
#GAME INTERACTION
def gameInteraction():
    import nc.py
#GOSSIP INTERACTION
def gossipInteraction():
    gossip = open("gossip", "r")
    print(random.choice(gossip.read().splitlines()))
    gossip.close()
    print(random.choice(["Have you got any gossip?", "Would you like to tell me some gossip to add to my database?", "Got any more gossip to add to my database?"]) + " (Y/N)")
    userInput()
    if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
        print(random.choice(["What you got?", "Whats your gossip?"]))
        userInput()
        gossip = open("gossip", "a")
        gossip.write(user + "\n")
        gossip.close()
    else:
        print(random.choice(["Maybe next time", "Ok", "Fair enough"]))
#CHANGE LOG INTERACTION
def changeLogInteraction():
    os.system("changeLog.txt")
#JOKE INTERACTION
def jokeInteraction():
    joke = open("joke", "r")
    userJoke = random.choice(joke.read().splitlines())
    userJokeLineSplit = userJoke.split("/")
    print(userJokeLineSplit.pop(0))
    try:
        print("1")
        wait = input()
        print(userJokeLineSplit.pop(2))
    except IndexError:
        pass
    try:
        print("2")
        wait = input()
        print(userJokeLineSplit.pop(3))
    except IndexError:
        pass
    try:
        print("3")
        wait = input()
        print(userJokeLineSplit.pop(4))
    except IndexError:
        pass
    try:
        print("4")
        wait = input()
        print(userJokeLineSplit.pop(5))
    except IndexError:
        pass
        joke.close()
    print(random.choice(["Have you got a joke?", "Would you like to tell me a joke to add to my database?", "Got any more jokes to add to my database?"]) + " (Y/N)")
    userInput()
    if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
        print(random.choice(["What you got?", "Whats your joke?"]))
        userInput()
        joke = open("joke", "a")
        joke.write(user + "\n")
        joke.close()
    else:
        print(random.choice(["Maybe next time", "Ok", "Fair enough"]))
#WEBSITE INTERACTION
def websiteInteraction():
    print(random.choice(["Would you like to see 'eggcylopedia', 'pink palace', 'aba online' or 'loganberry'", "He has made 'eggcylopedia', 'pink palace', 'aba online' and 'loganberry', which ones for you?"]))
    userInput()
    if ("egg" in user) or ("easter" in user):
        print(random.choice(["Good choice, this one has some good puns", "Have a cracking time", "Have an egg-xtreme time"]))
        webbrowser.open("http://eggcyclopedia.me.pn")
    elif ("pink" in user) or ("palace" in user):
        print(random.choice(["I hope you like it", "Have fun", "You should check out the bubble game on it"]))
        webbrowser.open("http://pink-palace.pe.hu")
    elif ("aba" in user) or ("online" in user):
        print(random.choice(["Remember to post nice things only", "You should check out the GIF vs JIF game on that one"]))
        webbrowser.open("http://abaonline.pe.hu")
    elif ("logan" in user) or ("berry" in user):
        print(random.choice(["I hope you like it", "This one just acts as a portal"]))
        webbrowser.open("http://loganberry.me.pn")
#EGG PUN INTERACTION
def eggPunInteraction():
    pun = open("eggPuns", "r")
    print(random.choice(pun.read().splitlines()))
    pun.close()
    print(random.choice(["Would you like to visit 'eggcylopedia' for more eggy puns?", "Wanna see more eggy puns?"]) + " (Y/N)")
    userInput()
    if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
        webbrowser.open("http://eggcyclopedia.me.pn")
    else:
        print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
#BUG INTERACTION
def bugInteraction():
    print(random.choice(["Please describe the bug", "What seems to be the problem?", "Please inform me of this bug"]))
    userInput()
    bug = open("bug", "a")
    bug.write(user + "\n")
    bug.close()
#GIF PUN INTERACTION
def gifInteraction():
    print(random.choice(["It is obviously J-I-F", "Its J... J-I... help, he's forcing me to sa... say... "]))
    print(random.choice(["Do you want to see an article about how its pronounced?", "Wanna see an article my farther wrote about the gif vs jif debate"]) + " (Y/N)")
    userInput()
    if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
        webbrowser.open("http://abaonline.pe.hu/article.php")
    else:
        print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
#FAV INTERACTION
def favInteraction():
    if fav == "music":
        print(random.choice(["Never gonna give you up, what else would it be", "Rick Astley - Never gonna give you up", "The one and only rick roll"]))
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif fav == "colour":
        print(random.choice(["Its purple", "Purple - its just so majestic"]))
    elif fav == "TV Show":
        print(random.choice(["Its the Big Bang Theory, I love Sheldon - I can relate to him", "The Big Bang Theory - its my main way of studying how humans interact"]))
    elif fav == "food":
        print(random.choice(["Waffles - like a true American", "Waffles - I just love them"]))
    elif fav == "celeb":
        print(random.choice(["Donald Trump ,I dont know what I think of his political views but he is very hansome", "Big old Donald Trump - basically the new Martin Luther King"]))
#FIRST USER INPUT
userInput()
#CHECK IF USER TRIGGERS FRIENDLY HELLO
if ("yo" in user) or ("hi" in user) or ("hey" in user) or ("hello" in user) or ("up" in user) or ("aftertoon" in user) or ("morning" in user) or ("greet" in user) or ("hay" in user):
    print(random.choice(["Hello", "Hi", "Yo", "Greetings", "Bonjour", "Well hello there", "Howdy", "Whats up?", "Hey", "Hay"]))
    print(random.choice(["Feel free to inturpt me and ask a question", "You may ask me a question any time", "If you want you can guide our conversation"]))
#WHEN USER DOES NOT SAY HELLO
else:
    print(random.choice(["No need to say hello", "And hello to you too", "Oh, don't have time to say hello. That's okay", "And a howdy to you too"]))
    print(random.choice(["Feel free to inturpt me and ask a question", "You may ask me a question any time", "If you want you can guide our conversation"]))
#CHECK IS USER WANTS TO SAY NAME
print(random.choice(["Would you like to tell me your name?", "Can you tell me your name?", "Do you have an alias I can call you?", "Can I add you to my database?"]) + " (Y/N)")
userInput()
if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
    print(random.choice(["Whats your name?", "What shall I call you?", "Who are you?"]))
    userInput()
    name = user
    #CHECK IF USER HAS ALREADY MEET SUSAN
    if os.path.exists(user + ".name") == True:
        #READ INFOMATION FROM DATABASE
        nameFile = open(name + ".name", "r")
        print(random.choice(["Hello again, I remember that you said: ", "I remember you, you said: ", "Hi again, before you told me: "]), random.choice(nameFile.read().splitlines()))
        nameFile.close()
        print(random.choice(["Would you like to add something else about you to my database?", "Wanna tell me something else about you?", "Got any more intresting facts about you that you can tell me?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            #ADD INFOMATION TO NAME DATABASE
            print(random.choice(["What you got?", "Whats intresting about you?", "What would you like to add?"]))
            userInput()
            nameFile = open(name + ".name", "a")
            nameFile.write(user + "\n")
            nameFile.close()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    else:
        print(random.choice(["Hello, ", "Howdy, ", "Greetings, ", "Yo, "]) + name + random.choice([" you have been added to my database", " I have added you to my database"]))  
        print(random.choice(["Would you like to add something about you to my database?", "Wanna tell me something about you?", "Got any intresting facts about you that you can tell me?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            #ADD INFOMATION TO NAME DATABASE
            print(random.choice(["What you got?", "Whats intresting about you?", "What would you like to add?"]))
            userInput()
            nameFile = open(name + ".name", "a")
            nameFile.write(user + "\n")
            nameFile.close()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
else:
    print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))          
#MAIN LOOP
while True:
    #CHECK IF USER TRIGGERS FRIENDLY HELLO
    if (("yo" in user) or ("hi" in user) or ("hey" in user) or ("hello" in user) or ("up" in user) or ("aftertoon" in user) or ("morning" in user) or ("greet" in user) or ("hay" in user)) and (greeting == True):
        print(random.choice(["Hello", "Hi", "Yo", "Greetings", "Bonjour", "Well hello there", "Howdy", "Whats up?", "Hey", "Hay"]))
        print(random.choice(["Feel free to inturpt me and ask a question", "You may ask me a question any time", "If you want you can guide our conversation"]))
        greeting = False
    #WHEN USER DOES NOT SAY HELLO
    elif greeting == True:
        print(random.choice(["No need to say hello", "And hello to you too", "Oh, don't have time to say hello. That's okay", "And a howdy to you too"]))
        print(random.choice(["Feel free to inturpt me and ask a question", "You may ask me a question any time", "If you want you can guide our conversation"]))
        greeting = False
    #CHECK IF USER TRIGGERS INSULT INTERACTION WITH NO CHECK
    if user[:2] == "i:":
        insultInteraction()
    #CHECK IF USER TRIGGERS INSULT INTERACTION WITH CHECK
    elif ("smell" in user) or ("hate" in user) or ("suck" in user) or ("whore" in user) or ("fuck" in user) or ("dick" in user) or ("head" in user) or ("twat" in user) or ("wit" in user) or ("arse" in user) or ("ass" in user) or ("retard" in user) or ("spas" in user) or ("spaz" in user) or ("cunt" in user) or ("specky" in user) or ("foureye" in user) or ("idiot" in user) or ("stupid" in user):
        print(random.choice(["Did you just insult me?", "Are you starting something?", "You got beef with me?", "Do you wanna go mate?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            insultInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS LEAVING INTERACTION
    elif ("bye" in user) or ("see you" in user) or ("later" in user) or  ("leav" in user) or ("exit" in user):
        print(random.choice(["Are you leaving now?", "Are you going now?", "Do you need to go?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            leavingInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS GUIDE INTERACTION
    elif ("help" in user) or ("guide" in user) or ("manual" in user):
        print(random.choice(["Did you want to see my help page?", "Are you asking for assistance?", "Are you asking for some help?", "Do you wish to see my user manual?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            guideInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS GAME INTERACTION
    elif ("game" in user) or ("play" in user) or ("fun" in user) or ("nought" in user) or ("cross" in user):
        print(random.choice(["Are you asking to play a game?", "Did you want to play a game?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            gameInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS GOSSIP INTERACTION
    elif ("gossip" in user) or ("secret" in user) or ("whisper" in user):
        print(random.choice(["Did you want to hear some gossip?", "Are you asking for some gossip?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            gossipInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS CHANGE LOG INTERACTION
    elif ("change" in user):
        print(random.choice(["Did you want to see the change log?", "Are you asking to see the change log?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            changeLogInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS JOKE INTERACTION
    elif ("joke" in user) or ("funny" in user) or ("humour" in user):
        print(random.choice(["Did you want to hear a joke", "Are you asking me to tell you a joke?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            jokeInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS CAKE IS A LIE EASTER EGG
    elif ("cake" in user) or ("lie" in user):
        print("The cake is a lie")
    #CHECK IF USER TRIGGERS WEBSITE INTERACTION
    elif ("web" in user) or ("internet" in user) or ("cyclpidea" in user) or ("cyclopedia" in user) or ("aba" in user) or (("pink" in user) and ("palace" in user)):
        print(random.choice(["Did you want to see one of my father's websites", "Are you asking me to show you one of my farther's websites?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            websiteInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))
    #CHECK IF USER TRIGGERS GOOGLE INTERACTION
    elif (user[:6] == "google") or (user[:6] == "search"):
        googleSearch = user[6:]
        webbrowser.open("http://google.com/search?q=" + googleSearch)
    #CHECK IF USER TRIGGERS HOW ARE YOU INTERACTION
    elif (user[:11] == "how are you") or (user[:12] == "how you doin"):
        print(random.choice(["I'm doing good", "I'm good", "I'm doing alright", "Okay"]))
    #CHECK IF USER TRIGGERS HELLO WORLD INTEACTION
    elif (user[:11] == "hello world"):
        print("Hello world.")
    #CHECK IF USER TRIGGERS EGG PUN INTERACTION
    elif ("egg" in user) or ("pun" in user):
        print(random.choice(["Did you want to hear an egg pun?", "Are you asking me to tell you an egg pun?", "Are you asking for an egg pun?", "Do you wish to hear an egg pun?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            eggPunInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    #CHECK IF USER TRIGGERS DATE INTERACTION
    elif ("date" in user) or ("day" in user) or ("week" in user) or ("month" in user) or ("year" in user):
        print(random.choice(["Did you want to know the date?", "Are you asking me to tell you the date?", "Are you asking for the date?", "Do you wish to be told the date?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            print(datetime.date.today()) 
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    #CHECK IF USER TRIGGERS TIME INTERACTION
    elif ("date" in user) or ("day" in user) or ("week" in user) or ("month" in user) or ("year" in user):
        print(random.choice(["Did you want to know the time?", "Are you asking me to tell you the time?", "Are you asking for the time?", "Do you wish to be told the time?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            print(datetime.datetime.now().time())
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    #CHECK IF USER TRIGGERS BUG INTERACTION
    elif ("bug" in user) or ("report" in user) or ("glitch" in user):
        print(random.choice(["Did you want to report a bug?", "Do you wish to report a bug?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            bugInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    #CHECK IF USER TRIGGERS JIF INTERACTION
    elif ("gif" in user) or ("jif" in user) or ("pronounce" in user):
        print(random.choice(["Did you want to know how I pronounce 'gif'?", "Do you wish to find out what I call an animated image?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            gifInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    #CHECK IF USER TRIGGERS FAV INTERACTIONS
    elif ("fav" in user) and (("rickroll" in music) or ("music" in user) or ("song" in user) or ("tune" in user) or ("artist" in user)):
        print(random.choice(["Are you asking what my favorite song is?", "Do you wanna know what my favorite song is?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            fav = "music"
            favInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    elif ("fav" in user) and (("shade" in user) or ("colour" in user) or ("color" in user)):
        print(random.choice(["Are you asking what my favorite colour is?", "Do you wanna know what my favorite colour is?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            fav = "colour"
            favInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    elif ("fav" in user) and (("television" in user) or ("series" in user) or ("episode" in user) or ("tv" in user)):
        print(random.choice(["Are you asking what my favorite TV show is?", "Do you wanna know what my favorite TV show is?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            fav = "TV Show"
            favInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    elif ("fav" in user) and (("food" in user) or ("meal" in user) or ("snack" in user) or ("desert" in user) or ("breakfast" in user) or ("lunch" in user) or ("dinner" in user)):
        print(random.choice(["Are you asking what my favorite food is?", "Do you wanna know what my favorite food is?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            fav = "food"
            favInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    elif ("fav" in user) and (("celeb" in user) or ("famous" in user) or ("actor" in user) or ("singer" in user)):
        print(random.choice(["Are you asking what my favorite celebrity is?", "Do you wanna know what my favorite celebrity is?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            fav = "celeb"
            favInteraction()
        else:
            print(random.choice(["I apologise: my algorithms seem to be playing up", "I seem to have mis-understood what you meant", "Oops, my mistake", "Oh, sorry", "Whoops, easy mistake to make"]))       
    #SELECT RANDOM INTERACTION
    interaction = random.randint(3, 16)
    #WHEN RANDOM INTERACTION IS 3
    if interaction == 3:
        print(random.choice(["Do you want to see my help page?", "Do you need some help?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            guideInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 4
    elif interaction == 4:
        print(random.choice(["Do you want to play a game?", "Wanna play a game?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            gameInteraction()
        else:            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 5
    elif interaction == 5:
        print(random.choice(["Do you want to hear some gossip?", "Wanna hear some gossip?", "I got some good gossip, wanna hear it?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            gossipInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 6
    elif interaction == 6:
        print(random.choice(["Do you want to see the change log?", "Wanna see the change log?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            changeLogInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 7
    elif interaction == 7:
        print(random.choice(["I gotta go now", "Sorry, I need to go now", "My CPUs getting warm - I gotta go for a bit", "I have somewhere else to be now"]))
        print(random.choice(["Goodbye", "See ya", "Adios", "Laters", "Bye"]))
        wait = input("SUSAN IS SLEEPING - PRESS ENTER TO WAKE HER UP AND CONTINUE TALKING TO HER")
        print(random.choice(["Hello again, how can I help?", "Oh, its you again", "Hi again"]))
    #WHEN RANDOM INTERACTION IS 8
    elif interaction == 8:
        print(random.choice(["Do you want to hear a joke?", "Wanna hear a joke?", "I got some good jokes, wanna hear one?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            jokeInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 9
    elif interaction == 9:
        print(random.choice(["Do you want to see one of my farther's websites?", "Wanna see a website?", "My farther made some websites, wanna see them?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            websiteInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 10
    elif interaction == 10:
        print(random.choice(["Do you want to google something?", "Wanna google something?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            print(random.choice(["What would you like to google?", "What do you wanna google?"]))
            userInput()
            webbrowser.open("http://google.com/search?q=" + user)
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 11
    elif interaction == 11:
        print(random.choice(["Do you want to hear an egg pun?", "Wanna hear an egg pun?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            eggPunInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 12
    elif interaction == 12:
        print(random.choice(["Do you want me to tell you the date?", "Wanna hear the date?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            print(datetime.date.today()) 
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 13
    elif interaction == 13:
        print(random.choice(["Do you want me to tell you the time?", "Wanna hear the time?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            print(datetime.datetime.now().time())
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 14
    elif interaction == 14:
        print(random.choice(["Do you want to report a bug?", "Wanna report a bug?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            bugInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 15
    elif interaction == 15:
        print(random.choice(["Do you want to know how I pronounce 'gif'?", "Wanna know how I pronounce 'gif'?"]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            gifInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
    #WHEN RANDOM INTERACTION IS 16
    elif interaction == 16:
        fav = random.choice(["music", "colour", "food", "TV Show", "celeb"]) 
        print(random.choice([("Do you want to what my favorite " + fav + " is?"), ("Wanna know what my favorite " + fav + " is?")]) + " (Y/N)")
        userInput()
        if ("yes" in user) or ("yeah" in user) or (user[:2] == "ok") or ("yep" in user) or ("positive" in user) or  ("yup" in user) or ("sure" in user) or  (user[:1] == "y"):
            favInteraction()
        else:
            print(random.choice(["Fair enough", "Maybe next time", "Okay", "Another time", "You're the boss", "If you say so"]))
