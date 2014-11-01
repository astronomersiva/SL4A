import android
import time
import urllib2
import json
import re
import random

droid = android.Android()

def speedDet():
   droid.ttsSpeak("Please wait till I fetch your location. ")
   droid.startLocating(30)
   droid.eventWaitFor("location")
   l=droid.readLocation().result
   try:
      movSpeed=l['network']['speed']
      if movSpeed>40:
         droid.ttsSpeak("You are over speeding at %s! You are going to kill yourself" %str(int(movSpeed)))
      elif movSpeed<3 and movSpeed>=0:
         droid.ttsSpeak("Don't you know that speed is distance by time. You should move first of all!")
      else:
         droid.ttsSpeak("You are driving fine at %s!" %str(int(movSpeed)))
   except:
      pass

def makeCall(): 
   try:
      contactIndex = (userInput.split(" ")).index("call") + 2
      number = userInput.split(" ")[contactIndex]
      droid.phoneCallNumber(contacts[number])
   except:
      try:
         contactIndex = (userInput.split(" ")).index("call") + 1
         number = userInput.split(" ")[contactIndex]
         droid.phoneCallNumber(contacts[number])
      except:
         droid.ttsSpeak("I am facing some problem Siva. Try later!")

def sendMessage():
   try:
      contactIndex = (userInput.split(" ")).index("message") + 2
      messageIndex = contactIndex + 2
      messageText = userInput.split(" ")[messageIndex:]
      messageText = " ".join(messageText)
      number = contacts[userInput.split(" ")[contactIndex]] 
      droid.smsSend(number, messageText)
   except:
      try:
         contactIndex = (userInput.split(" ")).index("message") + 1
         messageIndex = contactIndex + 2
         messageText = userInput.split(" ")[messageIndex:]
         messageText = " ".join(messageText)
         number = contacts[userInput.split(" ")[contactIndex]] 
         droid.smsSend(number, messageText)
      except:
         droid.ttsSpeak("I am facing some problem Siva. Try later!")

def sendMessage1():
   try:
      contactIndex = (userInput.split(" ")).index("text") + 2
      messageIndex = contactIndex + 2
      messageText = userInput.split(" ")[messageIndex:]
      messageText = " ".join(messageText)
      number = contacts[userInput.split(" ")[contactIndex]] 
      droid.smsSend(number, messageText)
   except:
      try:
         contactIndex = (userInput.split(" ")).index("text") + 1
         messageIndex = contactIndex + 2
         messageText = userInput.split(" ")[messageIndex:]
         messageText = " ".join(messageText)
         number = contacts[userInput.split(" ")[contactIndex]] 
         droid.smsSend(number, messageText)
      except:
         droid.ttsSpeak("I am facing some problem Siva. Try later!")

def takePhoto():
   droid.ttsSpeak("Aye aye sir! Smile please!")
   time.sleep(1)
   droid.cameraCapturePicture('/sdcard/testrun/001.jpg', False)
   
def sayTime():
   droid.ttsSpeak(time.strftime("%_I %M %p"))

def sayDate():
   droid.ttsSpeak(time.strftime("%A, %B %_e, %Y "))   


def google():
   googleIndex = (userInput.split(" ")).index("search") + 2
   searchText = userInput.split(" ")[googleIndex:]
   searchText = " ".join(searchText)
   msg = "http://www.google.com/search?q=" + searchText.replace(' ','+')+'&btnI=745'
   droid.startActivity('android.intent.action.VIEW', msg)

def toggleMode():
   toggleIndex = (userInput.split(" ")).index("toggle") + 1
   toggler[userInput.split(" ")[toggleIndex]]()

def launcher():
   launchIndex = (userInput.split(" ")).index("open") + 1
   droid.launch(apps[userInput.split(" ")[launchIndex]])


def showMap():
   mapIndex = (userInput.split(" ")).index("map") 
   placeIndex = mapIndex + 2
   placeName = userInput.split(" ")[placeIndex:]
   placeName = " ".join(placeName)
   droid.viewMap(placeName)

def getLoc():
   droid.startLocating(30)
   droid.eventWaitFor("location")
   l=droid.readLocation().result
   lat=l['network']['latitude']
   lon=l['network']['longitude']
   url = "http://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(lon)+"&sensor=false"
   print url
   s = urllib2.urlopen(url).read()
   c = json.loads(s)
   x = c['results'][0]['formatted_address']
   droid.ttsSpeak (x)
   droid.viewMap(x)
   droid.stopLocating()

def distress():
   droid.startLocating(30)
   droid.eventWaitFor("location")
   l=droid.readLocation().result
   lat=l['network']['latitude']
   lon=l['network']['longitude']
   url = "http://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(lon)+"&sensor=false"
   s = urllib2.urlopen(url).read()
   c = json.loads(s)
   x = c['results'][0]['formatted_address']
   droid.smsSend('9444440690','Urgent: I am in distress. Location ' + x)


def morals():
   moral = "I follow the Zen of Python. They are : Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.\
            Complex is better than complicated.Flat is better than nested. Sparse is better than dense.\
            Readability counts.Special cases aren't special enough to break the rules.\
            Although practicality beats purity.Errors should never pass silently.\
            Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.\
            There should be one, and preferably only one - obvious way to do it.Although that way may not be obvious at first unless you're Dutch.\
            Now is better than never.Although never is often better than *right* now.\
            If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.\
            Namespaces are one honking great idea - let's do more of those!"
   droid.ttsSpeak(moral)

def barcode():
   print droid.scanBarcode().result

def calculate():
   print userInput
   match = re.findall(r'\d+',userInput)
   if 'into' in userInput:
      a = int(match[0]) * int(match[1])
      print a
      droid.ttsSpeak(str(a))
   elif 'by' in userInput:
      a = int(match[0]) / int(match[1])
      droid.ttsSpeak(str(a))
   elif '+' in userInput:
      a = int(match[0]) + int(match[1])
      print a
      droid.ttsSpeak(str(a))
   elif '-' in userInput:
      a = int(match[0]) - int(match[1])
      droid.ttsSpeak(str(a))
   elif 'power' in userInput:
      a = int(match[0]) ** int(match[1])
      droid.ttsSpeak(str(a))
   else:
      droid.ttsSpeak("My creator has not given me that much functionality!")

def waiter():
   time.sleep(15)

def chat():
   droid.ttsSpeak("Sure thing sir. What are doing right now?")
   userInput = droid.recognizeSpeech().result
   droid.ttsSpeak("Wow! That's great. Should I do anything?")
   command = droid.recognizeSpeech().result
   if list(set(command.split(" ")).intersection(contacts.keys())) is not None:
      contactNumber = contacts[list(set(command.split(" ")).intersection(contacts.keys()))[0]]
      droid.smsSend(contactNumber, userInput)


def weatherReport():
   droid.startLocating(30)
   droid.eventWaitFor("location")
   l=droid.readLocation().result
   lat=l['network']['latitude']
   lon=l['network']['longitude']
   droid.webViewShow('http://www.wunderground.com/cgi-bin/findweather/getForecast?query='+str(lat)+','+str(lon)+'&MR=1')
   droid.stopLocating()

def portfolio():
   droid.ttsSpeak("Warm greetings everyone. I am a voice command system developed by the students of RMK Engineering College.\
                             I am based on the Scripting Layer For Android, popularly known as SL4A. My core functionality comes from a few\
                             hundred lines of Python code. Feel free to explore some of my features.")

def tellName():
   droid.ttsSpeak("my creator is too lazy to give me a name")
def tellFather():
   droid.ttsSpeak("Siva is my father.")
def tellMother():
   droid.ttsSpeak("i am a piece of computer code. i don't need a mother")
def tellMarry():
   droid.ttsSpeak("sorry, interspecies marriages are not allowed in my universe")
def tellEat():
   droid.ttsSpeak("i eat electricity")
def tellKill():
   droid.ttsSpeak("please don't forget to charge me before you commit suicide.")
def tellKill1():
   droid.ttsSpeak("I am going to call the police to murderer!")

contacts={'home':'04425530214', 'mother':'9444440690', 'father':'9444111615', 'vishwas':'9677055570'}

apps = {'settings':'com.android.settings.Settings', 'whatsApp':'com.whatsapp.Main',
      'clock':'com.sec.android.app.clockpackage.ClockPackage',
      'music':'com.sec.android.app.music.MusicActionTabActivity','chrome':'com.google.android.apps.chrome.Main',
      'calculator':'com.sec.android.app.popupcalculator.Calculator'}

choices={'calculate':calculate,'map':showMap,'speed':speedDet,'call':makeCall,'message':sendMessage,'camera':takePhoto,'toggle':toggleMode,'time':sayTime,
         'date':sayDate,'location': getLoc, 'search':google,'open':launcher,'philosophy':morals,'barcode':barcode, 'photo':takePhoto, "emergency": distress,
          "wait": waiter, 'text':sendMessage1, 'weather':weatherReport, 'about': portfolio, 'name':tellName, 'father':tellFather,'mother':tellMother,
          'marry':tellMarry,'eat':tellEat, 'kill':tellKill1, 'suicide':tellKill, 'chat': chat}

toggler={'wifi':droid.toggleWifiState,'bluetooth':droid.toggleBluetoothState,'airplane':droid.toggleAirplaneMode,'silent':droid.toggleRingerSilentMode,
   'vibrate':droid.toggleVibrateMode}

exitTerms = ["goodbye", "good bye", "bye","see you","exit","catch you later"]
greetings = ["hello","hi", "hey","good morning","good afternoon","good evening","greetings"]
thankTerms = ["thank you", "thanks", "thank you so much"]
greetingsReplies = ["hello","hi","greetings"]
locationTerms = ["where am i", "what is my location", "track me"]
userInput = ""
droid.makeToast("Initialising..please wait")
droid.ttsSpeak("Hello..")
droid.dialogCreateAlert("I am Miss Xi")
droid.dialogSetItems(["Listen", "Wait", "Exit"])
droid.dialogShow()
choice=droid.dialogGetResponse().result
if choice["item"] == 1:
   droid.ttsSpeak("Okay sir. ")
   time.sleep(10)
   choice["item"] = 0
while choice["item"]==0 and userInput not in exitTerms:
   userInput=droid.recognizeSpeech().result
   print userInput
   try:
      userInput=userInput.lower()
      #works
      if userInput in greetings:
         droid.ttsSpeak(random.choice(greetingsReplies))
      elif userInput in locationTerms:
         getLoc()
      elif userInput in exitTerms:
         break
      elif userInput in thankTerms:
         droid.ttsSpeak("you are welcome sir")
      elif list(set(userInput.split(" ")).intersection(choices.keys())) is not None:
         reqdFunction = list(set(userInput.split(" ")).intersection(choices.keys()))[0]
         choices[reqdFunction]()
      droid.dialogCreateAlert("I am Miss Xi")
      droid.dialogSetItems(["Listen","Wait","Exit"])
      droid.dialogShow()
      choice=droid.dialogGetResponse().result
      if choice["item"] == 1:
         droid.ttsSpeak("Okay sir. I will come back after some time.")
         time.sleep(10)
         choice["item"] = 0
   except:
         droid.ttsSpeak("I am sorry, I couldn't understand that. Can you repeat your command.")
         droid.dialogCreateAlert("I am Miss Xi")
         droid.dialogSetItems(["Listen", "Wait", "Exit"])
         droid.dialogShow()
         choice=droid.dialogGetResponse().result
         if choice["item"] == 1:
            droid.ttsSpeak("Okay sir.")
            time.sleep(10)
            choice["item"] = 0
