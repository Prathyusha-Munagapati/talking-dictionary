# Import the modules required
import json
from difflib import get_close_matches
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
# rate = engine.getProperty("rate")
engine.setProperty("rate", 130)
# Loading data from json file
# in python dictionary
data = json.load(open(r"C:\Users\LENOVO L440\Desktop\dict.json"))


def translate(word):
    # converts to lower case
    word = word.lower()

    if word in data:
        return data[word]
    # for getting close matches of word
    elif len(get_close_matches(word, data.keys())) > 0:
        engine.say("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        engine.runAndWait()
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


# Driver code
response = 1
while(response == 1):
    engine.say("Enter the word you want to search for")
    engine.runAndWait()
    word = input("Enter here: ")
    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
            engine.say(item)
            engine.runAndWait()
    else:
        print(output)
        engine.say(output)
        engine.runAndWait()
    try:
        response = int(input("Enter 1 to search again or 0 to exit"))
    except:
        print("Enter proper input")
        engine.say("Enter proper input")
        # engine.runAndWait()
        engine.say("It should be either 0 or 1")
        engine.runAndWait()

        response = int(input("It should be either 0 or 1"))

