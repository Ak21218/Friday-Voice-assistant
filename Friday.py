import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    instruction = " "  # Initialize instruction here
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction= instruction.lower()
            if "Friday" in instruction:
                instruction = instruction.replace('Friday', " ")
                print(instruction)
            
    except:
        pass
    return instruction

def play_Friday():
    instruction = input_instruction()  # Call the function to get the instruction
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('current time ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date " + date)

    elif 'how are you' in instruction:
        talk('I am fine, how are you')

    elif 'What is your name' in instruction:
        talk('I am Friday, What can I do for you?')

    elif 'Who is' in instruction:
        human = instruction.replace('who is'," ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else:
        talk('Please repeat')

play_Friday()