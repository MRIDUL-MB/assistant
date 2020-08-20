import os
import pyttsx3
import speech_recognition as sr
import pyaudio


def command(choose):
            if (('run' in choose) or ('open' in choose)) and (('facebook' in choose) or ('Facebook' in choose)):
                pyttsx3.speak('opening....')
                os.system("chrome facebook.com")
                
                
            elif (('run' in choose) or ('open' in choose)) and (('LinkedIn' in choose) or ('linkedIn' in choose) or ('linkedin' in choose)):
                pyttsx3.speak('opening....')
                os.system("chrome linkedin.com")
                
                
            elif (('run' in choose) or ('open' in choose)) and (('YouTube' in choose) or ('youtube' in choose)):
                pyttsx3.speak('opening....')
                os.system("chrome youtube.com")
                
                
                
            elif (('run' in choose) or ('open' in choose)) and (('Notepad' in choose) or ('notepad' in choose)):
                pyttsx3.speak('opening....')
                os.system("notepad")
                
                
            elif (('run' in choose) or ('open' in choose)) and (('Window Media Player' in choose) or ('window media player' in choose) or ('media player' in choose)):
                pyttsx3.speak('opening....')
                os.system("wmplayer")
                
                
            elif (('run' in choose) or ('open' in choose)) and (('chrome' in choose) or ('Chrome' in choose)):
                pyttsx3.speak('opening....')
                os.system("chrome")
                
            elif (('run' in choose) or ('open' in choose)) and (('camera' in choose) or ('Camera' in choose)):
                pyttsx3.speak('opening....')
                os.system("start microsoft.windows.camera:")
                
                
            elif ('clear' in choose) and (('screen' in choose) or ('terminal' in choose)):
                pyttsx3.speak('clearing....')
                os.system("cls")
                
            elif ('thank you' in choose) or ('Thanks' in choose):
                pyttsx3.speak('Your Welcome')
                
            else:
                print("Try Again with correct keywords")
                input("\nEnter to Continue...")

srr = sr.Recognizer()
def voice_input():
    while True:
        try:
            with sr.Microphone() as source:
                srr.adjust_for_ambient_noise(source,duration=0.5)
                audio = srr.listen(source)
                text=srr.recognize_google(audio)
                text=text.lower()
                return text
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("Could not request results {0}".format(e))


    
def start():
    pyttsx3.speak("Welcome To Assistant") 
    print('''
                    __        __   _
                    \ \      / /__| | ___ ___  _ __ ___   ___
                     \ \ /\ / / _ \ |/ __/ _ \|  _ ` _ \ / _ 
                      \ V  V /  __/ | (_| (_) | | | | | |  __/
                       \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
          ''')

#pyttsx3.speak('What is your name')
#name = input('What is your name: ')

#pyttsx3.speak(f'Hello {name}')
#print(f'Hello, {name}')
pyttsx3.speak('How do you chat with us')
option = input('How do you chat with us (text/speak): ')

start()
#input('Enter to continue....')
if option == 'text':
    while True:
        #os.system('cls')
        bool = input("do you want to continue (y/n): ")
        if bool == 'y':
            choose = input('\nWhat do want to run: ')  
            command(choose)
        elif bool == 'n':
            pyttsx3.speak('Thank you') 
            print('Thank you!')
            break  
            
            
elif option == 'speak':
    while True:
        bool = input("do you want to continue (y/n): ")
        if bool == 'y':
            pyttsx3.speak("What do you want to run")
            print('\nWhat do want to run?')
            print('Recognizing....')
        
            choose = voice_input()
            print(f'{choose}') 
            command(choose)
        elif bool == 'n':
            pyttsx3.speak('Thank you') 
            print('Thank you!')
            break 
            
            
        
    
            
        
    
        