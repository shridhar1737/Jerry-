import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import time
import pywhatkit
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id
engine.setProperty('voice', voices[1].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

speak('HELLO')
print("HELLO")


def wishme():
   Hour = int(datetime.datetime.now().hour)
   if 0 <= Hour < 12:
       speak('Good Morning sir')
       print("Good Morning sir")

   elif 12 <= Hour < 18:
       speak('Good Afternoon sir')
       print("Good afternoon sir")

   else:
       speak('Good Evening sir')
       print("Good Evening sir")

   speak('I am Jerry , How can i help you sir ?.')
   print('I am Jerry , How can I help You sir ?.')


def takeCommand():
   """It takes microphone input from the user and returns string output"""
   r = sr.Recognizer()
   with sr.Microphone() as sourse:
       print('Listening.....')
       r.pause_threshold = 0.8
       audio = r.listen(sourse)

   # noinspection PyBroadException
   try:
       print('Recognizing...')
       command = r.recognize_google(audio, language='en-in')
       print(f'User said:{command}\n')  # [\n] shows new a line

   except Exception:
       # print(e)
       speak("Sorry sir i can't understand ,please can you Say that again...")
       print("Sorry sir i can't understand ,please can you Say that again...")
       return 'None'

   return command


def sendEmail(to, content):
   server = smtplib.SMTP(smtp.gmail.com, 587)
   server.ehlo()
   server.starttls()
   server.login(' piyush@gamil.com', 'piyush@123')
   server.sendmail('piyush@gmail.com', to, content)
   server.close()


if __name__ == "__main__":
   wishme()
   while True:
       command = takeCommand().lower()
       '''Logic for executing tasks based on command'''
       if 'date' in command:
           localtime = time.asctime(time.localtime(time.time()))
           print(localtime)
           speak(localtime)

       elif 'the time' in command:
           #    format of time: strTime = datetime.datetime.now().strftime('%H;%M;%S')
           #                    localtime = time.asctime(time.localtime(time.time()))
           now = datetime.datetime.now()
           hour = '{:02d}'.format(now.hour)
           minute = '{:02d}'.format(now.minute)
           print(f'The time is {hour}hours and {minute}minutes')
           speak(f'The time is {hour}hours and {minute}minutes')

       elif 'open google' in command:
           webbrowser.open('google.com')

       elif 'open another tab' in command:
           webbrowser.open_new_tab('google.com')

       elif 'open youtube' in command:
           webbrowser.open('youtube.com')

       elif 'search info' in command:
           print('What should I searh..')
           speak('What should I searh..')
           cn = takeCommand().lower()
           webbrowser.open(f'{cn}')

       elif 'wikipedia' in command:
           print('Searching Wikipedia...')
           speak('Searching Wikipedia...')
           command = command.replace('wikipedia', '')
           results = wikipedia.summary(command, sentences=2)
           print('According to Wikipedia')
           speak('According to Wikipedia')
           print(results)
           speak(results)

       elif 'play video on youtube' in command:
           print('Please tell me which video to play..')
           speak('Please tell me which video to play..')
           yt = takeCommand().lower()
           pywhatkit.playonyt(f'{yt}')

       elif 'live score of ipl' in command:
           print("Score of today's match is....")
           speak("Score of today's match is....")
           webbrowser.open("https://www.google.com/search?q=live+ipl+scoere&rlz=1C1CHBF_enIN918IN918&oq=live+ipl+scoere&aqs=chrome..69i57j0i13l9.3822j1j7&sourceid=chrome&ie=UTF-8#sie=lg;/g/11fqtnjjg0;5;/m/03b_lm1;mt;fp;1;;")

       elif "today's weather " in command:
           print('Weather is...')
           speak('Weather is...')
           webbrowser.open("https://www.google.com/search?q=weather+today%27s+weather+in+parbhani&ei=54t6YKvFMbCc4-EPr5GxsAo&oq=weather+today+weather+in+parbhani&gs_lcp=Cgdnd3Mtd2l6EAMYADIICCEQFhAdEB46BwgAEEcQsAM6BwgAELADEEM6AggAOggIABCxAxCDAToFCAAQyQM6BggAEBYQHjoJCAAQyQMQFhAeUKt2WOnOAmCz2AJoA3ACeACAAYkIiAHtHpIBCTAuOS42LjctMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz")


       elif 'send message' in command:
           print('to whom do you want to send the message?')
           speak('to whom do you want to send the message?')
           saakshi = '+919518366522'
           shreya = '+919730836615'
           unnati = '+919822433200'
           shree = '+919322154505'
           shreyas = '+919730836615'
           Maam = '+917058595567'
           n = takeCommand().lower()
           if n=='saakshi':
               a=saakshi

           elif n=='shreya':
               a=shreya

           elif n=='unnati':
               a=unnati

           elif n=="Maam":
               a=Maam

           elif n=="shree":
               a=shree

           elif n=="shreyas":
               a=shreyas

           else:
               a=shree

           print('What message do you want to send?')
           speak('What message do you want to send?')

           messege = takeCommand().lower()
           now = datetime.datetime.now()
           hour = '{:02d}'.format(now.hour)
           minute = '{:02d}'.format(now.minute)
           pywhatkit.sendwhatmsg('+', f'{messege}', int(hour), int(minute) + 2)


       elif 'send mail to shree' in command:
           try:
               speak("what you like to send sir?")
               print("what you like to send sir?")

               content = takeCommand()
               to = "shripatil1737@gmail.com"
               sendEmail(to, content)
               speak("Email has been send!!")
               print("Email has been send!!")
           except Exception as e:
               print(e)
               speak("sorry sir. I am not able to send the email")
               print("sorry sir. I am not able to send the email")

       elif 'open office' in command:
           wordPath = "C:\\Users\\user\\Desktop\\Office.lnk"
           os.startfile(wordPath)

       elif 'open vscode' in command:
           powerpointPath = "C:\\Users\\user\\Desktop\Visual Studio Code.lnk"
           os.startfile(powerpointPath)

       elif 'play music' in command:
           music_dir = '"D:\\music\\y2mate.com - Pink Sweat  At My Worst Lyrics.mp3"'
           songs = os.listdir(music_dir)
           # random_no = random.randint(0, 8)
           # print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))

       elif 'Jerry, i am getting bore' in command:
           speak('I Have some thing for you !!')
           print('I Have some thing for you !!')
           speak(pyjokes.get_joke('en', 'all'))
           print(pyjokes.get_joke('en', 'all'))

       elif "what is today's Home work" in command:
           speak('sorry SIR ,Now I have a headache i want small break')
           print('sorry SIR ,Now I have a headache i want small break')


       elif 'ok bye Jerry' in command:
           speak("Ok Bye sir, Have a nice day I will take a small break")
           print("Ok Bye sir, Have a nice day I will take a small break")
           break

