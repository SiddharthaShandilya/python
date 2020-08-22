import os
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate


#"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

pyttsx3.speak("Hello addy")
print()
print("WELCOME TO MY INTELLIGENCE WORLD".center(125))                    
engine.runAndWait()
pyttsx3.speak("I am your virtual assistant laila")
pyttsx3.speak("How can i help you...?")
while True:
  print()
  p = input("\t \t \t Hey user what you want to run: ")





  if ("date" in p): 
    pyttsx3.speak("showing todays date")
    os.system("date")
  elif ("time" in p): 
    pyttsx3.speak("showing current time")
    os.system("time")
  elif ("chrome" in p): 
    pyttsx3.speak("opening chrome")
    os.system("chrome")
  elif ("spotify" in p): 
    pyttsx3.speak("opening spotify")
    os.system("chrome www.spotify.com")
  elif ("Hello" in p) or ("hy" in p) or ("hey" in p):
    pyttsx3.speak("Hello addy")
  elif ("tell" in p) or ("about" in p) or ("yourself" in p):
    pyttsx3.speak("My name is laila , I am your virtual assistant , i am very intelligent and i am always there to help you")
  elif ("azure" in p) or ("ms cloud" in p):
    pyttsx3.speak("opening azure cloud")
    os.system("chrome azure.microsoft.com")
  elif ("google" in p) or ("gcp" in p):
    pyttsx3.speak("opening google cloud")
    os.system("chrome cloud.google.com")
  elif ("aws" in p) or ("aws cloud services" in p):
    pyttsx3.speak("opening amazon web services")
    os.system("chrome aws.amazon.com")
  elif ("gmail" in p):
    pyttsx3.speak("opening G mail")
    os.system("chrome www.gmail.com")
  elif ("yahoomail" in p) or ("yahoo mail" in p):
    pyttsx3.speak("opening yahoo mail")
    os.system("chrome www.yahoomail.com")
  elif ("youtube" in p):
    pyttsx3.speak("opening youtube")
    os.system("chrome www.youtube.com")
  elif ("twitter" in p):
    pyttsx3.speak("opening twitter")
    os.system("chrome www.twitter.com")
  elif ("whatsapp" in p):
    pyttsx3.speak("opening whatsapp")
    os.system("chrome web.whatsapp.com")
  elif ("facebook" in p):
    pyttsx3.speak("opening facebook")
    os.system("chrome www.facebook.com")
  elif ("linkedin" in p):
    pyttsx3.speak("opening linkedin")
    os.system("chrome www.linkedin.com")
  elif ("amazon" in p):
    pyttsx3.speak("opening amazon")
    os.system("chrome www.amazon.in")  
  elif ("flipkart" in p):
    pyttsx3.speak("opening flipkart")
    os.system("chrome www.flipkart.com")
  elif ("editor" in p): 
    pyttsx3.speak("opening notepad")
    os.system("notepad")
  elif ("puttygen" in p): 
    pyttsx3.speak("opening putty")
    os.system("puttygen")
  elif ("putty" in p): 
    pyttsx3.speak("opening putty")
    os.system("putty")
  elif ("virtualbox" in p) or ("virtual box" in p) or ("VM" in p) or ("vbox" in p) or ("vm" in p): 
    pyttsx3.speak("opening Vbox")
    os.system("virtualbox")
  elif ("discord" in p): 
    pyttsx3.speak("opening discord")
    os.system("discord")
  elif ("slack" in p): 
    pyttsx3.speak("opening slack")
    os.system("slack")
  elif ("steam" in p): 
    pyttsx3.speak("opening steam")
    os.system("steam")
  elif ("anydesk" in p): 
    pyttsx3.speak("opening anydesk")
    os.system("anydesk")
  elif ("teamviewer" in p): 
    pyttsx3.speak("opening team viewer")
    os.system("teamviewer")
  elif ("How" in p) or ("laila" in p):
    pyttsx3.speak("i can help you in following ways")
    print()
    print("!! I can help you in following ways !!".center(126))
    pyttsx3.speak("such as window based commands")
    print()
    print(" * Window Based Commands".center(126))
    pyttsx3.speak("Entertainment")
    print()
    print(" * Entertainment".center(126))
    pyttsx3.speak("Public clouds")
    print()
    print(" * Public Clouds".center(126))
    pyttsx3.speak("emails")
    print()
    print(" * Emails".center(126))
    pyttsx3.speak("Social media")
    print()
    print(" * Social Media".center(126))
    pyttsx3.speak("Shopping")
    print()
    print(" * Shopping".center(126))
    pyttsx3.speak("Workflows")
    print()
    print(" * WorkFlows".center(126))
    pyttsx3.speak("Remote login")
    print()
    print(" * Remote Login".center(126))
    pyttsx3.speak("Virtualization")
    print()
    print(" * Virtualization".center(126))
    pyttsx3.speak("Steam Gaming")
    print()
    print(" * SteamEngine Gaming".center(126))
  
  elif ("exit" in p) or ("quit" in p) or ("bye" in p):
    pyttsx3.speak("see you soon,, have a nice day...!!!")
    break
  else: 
    print("\t \t \t \t don't support")

  



