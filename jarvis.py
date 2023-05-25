import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import random
import requests
import pyautogui
from pynput.keyboard import Controller

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
keyboard = Controller()


emails = {
    ' sohan': 'senapati.sohan31@gmail.com',
    ' rohan': 'senapati.rohan23@gmail.com',
    ' roshan': 'p18roshan@iima.ac.in'
}

numbers = {
    'sohan': '+919078283132',
    'rohan': '+919100454825',
    'roshan': '+917531987282',
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("How May I Help You?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say That again please")
        speak("Say That again please")
        return "None"
    return query


def beginner():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say the command to activate....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing....")
        command = r.recognize_google(audio, language='en-in')
        print(f"User Said: {command}\n")

    except Exception as e:
        print(e)
        return "None"
    return command


email_id = 'senapati.rohan1234@gmail.com'
email_pswd = 'rohanrohan'

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_id, email_pswd)
    server.sendmail(email_id, to, content)
    server.close()


while True:
    command = beginner().lower()
    if "jarvis" in command:
        wishme()
        while True:
            query = takecommand().lower()

            if "search wikipedia for" in query:
                speak("Surfing through wikipedia...")
                query = query.replace("search wikipedia for", "")
                results = wikipedia.summary(query, sentences=2)
                speak("I found that")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("www.google.com")

            elif 'open whatsapp' in query:
                webbrowser.open("https://web.whatsapp.com/")

            elif 'open stack overflow' in query:
                webbrowser.open("www.stackoverflow.com")

            elif 'open github' in query:
                webbrowser.open("www.github.com")

            elif 'open facebook' in query:
                webbrowser.open("www.facebook.com")

            elif 'open snapchat' in query:
                webbrowser.open("www.snapchat.com")

            elif 'open instagram' in query:
                webbrowser.open("www.instagram.com")

            elif 'play music' in query:
                music_dir = 'C:\Rohan\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, random.choice(songs)))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Sir the time is {strTime}")

            elif "the date" in query:
                day = int(datetime.datetime.now().day)
                month = int(datetime.datetime.now().month)
                year = int(datetime.datetime.now().year)
                print(f"{day}/{month}/{year}")
                speak(f"sir the date is {day} {month} {year}")

        

            elif 'open chrome' in query:
                codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)

            elif 'open firefox' in query:
                codePath = "C:\Program Files\Mozilla Firefox\firefox.exe"
                os.startfile(codePath)

            elif 'send an email' in query:
                try:
                    query = query.replace("send an email to", "")
                    speak("what should i send")
                    content = takecommand()
                    to = emails[query]
                    sendemail(to, content)
                    speak("Email has been sucessfully sent")
                except Exception as e:
                    print(e)
                    speak("Sorry Boss! i am not able to send the email")

            elif 'send whatsapp message' in query:
                speak("whom should i send the message to ?")
                contact_name = takecommand().lower()
                speak("what should i send")
                message = takecommand()
                pywhatkit.sendwhatmsg_instantly(numbers[contact_name], message)
                pyautogui.press("enter", 1, 5)

            elif 'web search' in query:
                speak("From google i found that")
                query = query.replace("web search", "")
                pywhatkit.search(query)

            elif "shut down my laptop" in query:
                pywhatkit.shutdown()

            elif "cancel shutdown" in query:
                pywhatkit.cancelShutdown()

            elif "close jarvis" in query:
                speak("Have a Good Day sir")
                exit()

            elif "show the weather" in query:
                speak("which city's weather do you want to know about sir?")
                user_api = "1318a0fc30fc99cc8c183a4bfed36423"
                weather_city = takecommand()
                api_link_complete = "http://api.openweathermap.org/data/2.5/weather?q="+weather_city+"&appid="+user_api
                api_link = requests.get(api_link_complete)
                api_data = api_link.json()
                #api_data for the city is below#
                temp_city = ((api_data['main']['temp']) - 273.15)
                feel_temp = ((api_data['main']['feels_like']) - 273.15)
                weather_desc = api_data['weather'][0]['description']
                hmdt = api_data['main']['humidity']
                wind_spd = api_data['wind']['speed']
                print("---------------------------------------------------------------")
                print(f"weather stats for {weather_city} is")
                print("---------------------------------------------------------------")
                speak(f"weather stats for {weather_city} is")
                print(f"The Temperature is {temp_city:.2f} degree celcius.You will feel the temperature to be {feel_temp:.2f} degree celcius.The Humidity is {hmdt}.Weather can be described as {weather_desc}.Wind is blowing at a speed of {wind_spd} Km/h")
                speak(f"The Temperature is {temp_city:.2f} degree celcius . You will feel the temperature to be {feel_temp:.2f} degree celcius . The Humidity is {hmdt} . Weather can be described as {weather_desc} . Wind is blowing at a speed of {wind_spd} kilometer per hour")

            elif "who are you" in query:
                name = "Jarvis"
                created_on = datetime.date(2020, 5, 28)
                present_date = datetime.datetime.now().day
                present_month = datetime.datetime.now().month
                present_year = datetime.datetime.now().year
                created_date = 4
                created_month = 4
                created_year = 2023
                day_from_birth = abs(int(present_date) - int(created_date))
                year_from_birth = abs(int(present_year) - int(created_year))
                month_from_birth = abs(int(present_month) - int(created_month))

                speak(f"Sir i am An Programme made to make Your work easier my name is {name} . I was created on {created_on} . i am {day_from_birth} days {month_from_birth} months {year_from_birth} years old . I am still Devloping")



            elif "play a song" in query:
                speak("which song do you want to listen ? ")
                song_name = takecommand()
                pywhatkit.playonyt(song_name)

                
                
            elif "volume up" in query:
                pyautogui.press("volumeup", 3)

            elif "volume down" in query:
                pyautogui.press("volumedown", 3)

            elif "volume mute" in query:
                pyautogui.press("volumemute")

            
 

 
    else:
        speak("Jarvis did not activate")