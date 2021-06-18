import pyttsx3 as audio
import speech_recognition as sr

choice=-1

isTrue=True

mick=sr.Recognizer()

def speakOnly():
    global isTrue
    while isTrue:
        try:
            with sr.Microphone() as source1:
                mick.adjust_for_ambient_noise(source1,duration=1)
                audio.speak("Start Speaking")
                print("Listening...........")
                command=mick.listen(source1)
                print("Processing..........")
                print("--------------------------------------")
                text=mick.recognize_google(command)
                audio.speak(text)
                print(f"Did You said:- {text}")
                predection=str(input("Y/N:- "))
                print("--------------------------------------")
                predection=predection.lower()
                if(predection == "y"):
                    isTrue=False
                    return text
                elif(predection == "n"):
                    isTrue=True
                else:
                    print("Inavlid Input")
        except sr.RequestError as e:
            print(e)
        except sr.UnknownValueError as e:
            print(e)

def speakWrite():
    global isTrue
    isTrue=True
    write=speakOnly()
    with open ("Speech_To_Text.txt","a") as f:
            f.write(f"{write}\n")
            print("Success \U0001F44D")

while choice != 0:
    print("-----------------MENU-----------------")
    print("1). Speak only")
    print("2). Speak and Write To File")
    print("3). Exit")
    print("--------------------------------------")
    choice=int(input("Enter Your Choice:- "))
    if choice == 1:
        speakOnly()
    elif choice == 2:
        speakWrite()
    elif choice == 3:
        print("--------------------------------------")
        audio.speak("Thanks For Using")
        exit()
    else:
        print("--------------------------------------")
        audio.speak("Enter A Valid Choice.")