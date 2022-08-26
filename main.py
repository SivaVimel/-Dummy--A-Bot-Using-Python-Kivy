import kivy
kivy.require('1.7.1')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from sys import path
from instaloader.exceptions import ProfileNotExistsException
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pafy
from plyer import tts
import random

__version__ = '1.1.12'


class SayThis(BoxLayout):
    saywhat_text = ObjectProperty(None)
    
    def say_something(self, text):
        try:
            text = text.lower() #To convert the input text into lowercase
            
            #keywords reply - to take random output
            fav = ["yes this has the kick", "for me too", "i know"]
            how = ["i am genius","its magic","well you know","nice joke", "very well thank you"]
            appreciation = ["thank you","I did the best","Yes, its my effort","i appreciate you too"]
            we_did_it = ["yes, we did it","Not without me","Yes"]
            hru = ["I am good, how about you", "i am good", "fine" ,"fine and you" ,"i am fine and how is it for you"]
            gd = ["You should always be happy, thats your favorite thing and i am here for you always on your command", "its good to hear", "great", "its good to hear you are happy"]
            bd = ["you are not alone", "if you are alone then i am also alone"]
            food = ["You should probably eat" , "Your health is important", "do you want me to open online food shops?" , "Do you want me to call any food service"]
            mfav = ["thank you", "I appreciate that", "I am also my favourite"]
            bst = ["Yes, I am","Yes, I am the best","Yes I know","You have brain","People always say that"]
            ty = ["Gracias","I am the best","Thank You","Well Welcome",":D"]
            okay = ["Yes, do you want anything else?","Yes","Do you have anything to ask?",]
            nope = ["Just go and take a hike","Nope","Not On Planet Earth"]
            space = ["The line separating the atmosphere and outer space is called the Kármán line. \nThe term outer space and the universe are roughly equivalent, \nexcept that outer space refers only to the area between planets, \nwhile the universe encompasses planets as well.\n The universe is about 13.8 billion years old.","Space is a near perfect vacuum containing a low density of particles, \npredominantly a plasma of hydrogen and helium, as well as electromagnetic radiation, \nmagnetic fields, neutrinos, dust, and cosmic rays.","Because space is a near-perfect vacuum \n— meaning it has exceedingly few particles \n— there's virtually nothing in the space between stars and \nplanets to scatter light to our eyes. And with no light \nreaching the eyes, they see black."]
            ocean = ["There are various reasons why someone may develop a fear of the ocean. \nA bad experience with water may lead to a fear response and phobia. \nFor instance, if you nearly drowned while swimming in a lake or saw a shark in the ocean, \nyou may develop an intense fear. \nPhobias can also develop without any experience or traum", "Ocean is full of blackholes","Human's are Constantly Discovering Terrifying New Creatures in Ocean","The Ocean is Home Base for Hurricanes","Jellyfish","The Ocean Floor is Littered with Shipwrecks"]
            like = ["I like Space and Ocean","I am into Space and Ocean","I am currently in love with Space and Ocean"]
            jellyfish = ["It's understandable that you might not want to encounter \na shark during your swim, but the pesky jellyfish—of which \nthere are millions in the ocean—may actually be a greater threat to your life. \nThanks to their venom and relative lack of detectability underwater, \njellyfish have a body count that's actually five times higher than that of sharks. \nAgain, we've never encountered a single creature this terrifying out in the cosmos."]
            scary = ["Nothing scares me rather than space and ocean and also EXIT BUTTON","Human's should be terrified of Space and Ocean","Anything can come out of space and ocean","Earth can be swallowed by space or ocean, jk nothing will happen ;D"]
            wru =["I am Dummy","My name is Dummy","I am Dummy, you can call me Dummy"]
            yourname = ["I am Dummy, a dummy bot created to ba your friend in talk","I am Dummy, not a alien or ghost but just a bot","I am Dummy for sure"]
            wdl = ["I am living in your device but i am not a parasite for sure","I have rented to part of your device","I am living in a device, that's currently in planet earth"]
            youruse = ["I thought I am Dummy, not you","I am useful to be not useful","I can respond to some commands.\n Type 'help' for commands list"]
            
            elsehere = ["What do you mean 🎶 ~JB","Did you forget my name is Dummy, not Google","well i dont know what the heck you are saying","What are you even saying","I am a child","Oh No","Out Of Syllabus","Just Go and Live","Take A Hike Mate, \n Live A Life","One Day I May Reply For This \nBut Not Today"]
            #music commands -- 
            if 'play motivational' in text:
                tts.speak("boss i am playing some motivational songs for you")
                webbrowser.open_new_tab(
                    'https://www.youtube.com/watch?v=UtF6Jej8yb4&list=PLWc9sw89ZYSlAgwhb4PDXF8ouui_FvcAj')
                
            elif 'play bass' in text:
                tts.speak("Yes boss, lets shake the house")
                webbrowser.open_new_tab(
                    'https://www.youtube.com/watch?v=Bznxx12Ptl0&list=PLWc9sw89ZYSlTc35ibDq2t01NvwFVit8-')
            elif 'my needle' in text:
                tts.speak("Yes boss, here is the needle tracks for you")
                webbrowser.open_new_tab(
                    'https://www.youtube.com/watch?v=ebXbLfLACGM&list=PLWc9sw89ZYSnprxT42PdPzjc8X-wavnTK')
            elif 'play happy' in text:
                tts.speak("Yes boss, here you go")
                webbrowser.open_new_tab(
                    'https://www.youtube.com/watch?v=k-T4Odb-r5c&list=PLWc9sw89ZYSksJNICqx8jnp-Zpn5IwUii')
            elif 'play sad' in text:
                tts.speak("boss you have me, here is the song for you")
                webbrowser.open_new_tab(
                    'https://www.youtube.com/watch?v=W2PHbt6fr-g&list=PLWc9sw89ZYSkhKzA0yl8pEnlTZ77LaaCW')
            elif 'play mood' in text:
                tts.speak("boss here you go the naughty tracks")
                webbrowser.open_new_tab(
                    'https://www.youtube.com/watch?v=OORoOGY8D2M&list=PLWc9sw89ZYSmh8k_QqHXDgPuQILo7QBFN')
            elif 'my beat' in text or 'play music' in text:
                tts.speak("Yes boss, playing your listed songs")
                webbrowser.open_new_tab(
                    'https://www.youtube.com/watch?v=kudi8OtMu9s&list=PLWc9sw89ZYSkJkqF8M3aCKuxPS8jrUaiP')
                   
               
            # greetings
            elif "hey" in text or "hello" in text or "i am back" in text or "hola" in text:
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour <= 12:
                    tts.speak("Good Morning")
                elif hour >= 12 and hour < 18:
                    tts.speak("Good Afternoon")
                else:
                    tts.speak("Good Evening")   
            elif "bye" in text or "go to sleep" in text:
                hour = int(datetime.datetime.now().hour)
                if hour >= 6 and hour <= 15:
                    tts.speak("Good Bye, enjoy your day")
                    exit()
                elif hour >= 15 and hour <= 19:
                    tts.speak("Good Bye, enjoy your evening")
                    exit()
                elif hour >= 19 and hour <= 23:
                    tts.speak("Good Bye, enjoy your night")
                    exit()
                else:
                    tts.speak("Good Night boss")
                    exit()      
            elif 'the best' in text:
                tts.speak(random.choice(bst))
            elif 'ok' in text or 'okay' in text or "kk" in text:
                tts.speak(random.choice(okay))
            elif 'no' in text or 'nope' in text or "na" in text:
                tts.speak(random.choice(nope))
            elif 'thank you' in text or 'thankyou' in text:
                tts.speak(random.choice(ty))
            elif 'good work' in text or 'nice job' in text:
                tts.speak("Thank You boss") 
            
            #-open link    
            elif 'open google' in text:
                webbrowser.open('www.google.com')
                tts.speak("Here is google for you boss")
            elif 'open stackoverflow' in text:
                webbrowser.open('www.google.com')
                tts.speak("Here is Stackoverflow for you boss")
            
            elif 'search' in text:
                text = text.replace("search", "")
                
                search = text
                url = 'https://google.com/search?q=' + search
                webbrowser.open_new_tab(url)
                tts.speak('Here is What I found for' + search) 

                
            elif 'what is' in text or 'tell me about' in text:
                text = text.replace("what is", "")
                text = text.replace("tell me about", "")
                search = text
                url = 'https://en.wikipedia.org/wiki/' + search
                url1 = 'https://google.com/search?q=' + search
                tts.speak('Here is What I found for' + search) 
                webbrowser.open_new_tab(url1)
                results = wikipedia.summary(text, sentences=2) 
                tts.speak(results) 
                
            elif 'my github' in text or 'open github' in text:
                tts.speak("boss i am opening your github profile")
                webbrowser.open_new_tab(
                    'https://github.com/SivaVimel/SivaVimel')
                
            elif 'open youtube' in text:
                webbrowser.open('www.youtube.com')
                tts.speak("Here is youtube for you boss")
            elif 'in youtube' in text:
                text = text.replace("in youtube", "")
                tube = text
                url = "https://www.youtube.com/results?search_query=" + tube
                webbrowser.open_new_tab(url)  
                
            #get location via google map
            elif 'location' in text or 'locate' in text:
                text = text.replace("location", "")
                text = text.replace("locate", "")
                location = text
                url = 'https://google.nl/maps/place/' + location + '/&amp;'
                webbrowser.open_new_tab(url)
                tts.speak('Here is the location ' + location)
                
            #Download YouTube Video
            elif 'a youtube video' in text:
                text = text.replace("a youtube video", "")
                url = text
                video = pafy.new(url)

                streams = video.streams
                for i in streams:
                    print(i)
                best = video.getbest()

                tts.print(best.resolution, best.extension)
                best.download()
                tts.speak("Its done boss, i have downloaded the video your asked")
                
            #Download YouTube Audio
            elif 'a youtube audio' in text or 'a youtube song' in text:
                text = text.replace("a youtube audio", "")
                text = text.replace("a youtube song", "")
                url = text
                video = pafy.new(url)

                bestaudio = video.getbestaudio()
                bestaudio.download()
                tts.speak("boss i have downloaded the audio your asked")
            
            #Get Instagram Profile Details via instaginasta.com
            elif 'insta stuff' in text:
                webbrowser.open('https://instafinsta.com/')
                tts.speak("boss here is the result")    
            
            #Indian Food Ordering Systems
            elif 'open swiggy' in text:
                webbrowser.open_new_tab("https://www.swiggy.com/")
            elif 'open zomato' in text:
                webbrowser.open_new_tab("https://www.zomato.com/")   
                
                
            #Talking------
            elif 'how do you know' in text or 'how you know' in text:
                tts.speak(random.choice(how))
            elif 'favourite song' in text:
                tts.speak(random.choice(fav))
            elif 'you did great' in text:
                tts.speak(random.choice(appreciation))
            elif 'we did great' in text or 'we did it' in text:
                tts.speak(random.choice(we_did_it))
            elif 'how are you' in text:
                tts.speak(random.choice(hru))
            elif 'good day' in text or 'great day' in text or 'happy day' in text or 'good time' in text or 'great time' in text or 'happy time' in text:
                tts.speak(random.choice(gd))
            elif 'feeling bad' in text or 'am alone' in text or 'am sad' in text or 'bad day' in text or 'bad day' in text or 'sad day' in text or 'bad time' in text or 'bad time' in text or 'bad time' in text or 'feeling sad' in text or 'am broken' in text or 'in pain' in text or 'am heart broken' in text or 'in heart breaking' in text:
                tts.speak(random.choice(bd))
                tts.speak("boss how can i help you")
                tts.speak("do you need your energy pill boss?")
                tts.speak("just tell me which music pill you prefer")
            elif 'drama queen' in text:
                tts.speak("No, your girlfriend is the drama queen")
            elif 'i am hungry' in text or 'i am starving' in text or 'did not eat food' in text or 'have not ate food' in text or 'did not ate food' in text:
                tts.speak(random.choice(food))
            elif 'you are my favourite' in text :
                tts.speak(random.choice(mfav))
            elif 'scary' in text or 'terrifying' in text:
                tts.speak(random.choice(scary))
            elif 'you like' in text :
                tts.speak(random.choice(like))
            elif 'who are you' in text or 'what are you' in text:
                tts.speak(random.choice(wru))
            elif 'your name' in text or 'are you alien' in text or 'are you ai' in text or 'are you a bot' in text or 'are you bot' in text or 'dummy' in text or 'are you' in text or 'are you a' in text:
                tts.speak(random.choice(yourname))
            elif 'where are you' in text or 'your location' in text or 'where do you live' in text or 'which planet are you from' in text:
                tts.speak(random.choice(wdl))
            elif 'your use' in text:
                tts.speak(random.choice(youruse))
            elif 'help' in text:
                tts.speak("Commands : \n Search (Title) - for title search via google \n Play (Music/MusicType) - to go to custom music playlist")
            #space
            elif 'space' in text:
                tts.speak(random.choice(space))
            elif 'ocean' in text:
                tts.speak(random.choice(ocean))
            elif 'jellyfish' in text or 'jelly fish' in text:
                tts.speak(random.choice(jellyfish))
                
                
            else:
                tts.speak(random.choice(elsehere))
                tts.speak("Well I can do google search for you")
                tts.speak("Type Search Title")

        #Error--
        except NotImplementedError:
            popup = Popup(title='TTS Not Implemented',
                          content=Label(text='Sorry. TTS is not available.'),
                          size_hint=(None, None), 
                          size=(300, 300))
            popup.open()
    
    #Clear button     
    def clear(self):
        #removes text in InputBox with
        self.saywhat_text.text = "" 
        self.saywhat_text.focus = True


class SayThisApp(App):
    
    def build(self):
        return SayThis()

    def on_pause(self):
        return True

    def on_resume(self):
        pass 


if __name__ == '__main__':
    SayThisApp().run()