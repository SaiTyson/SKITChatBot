# Readme info:

Version: 1.0.0 <br/>
Authors: SKIT CSE DEPARTMENT <br/>
Date: 30th March 2018 <br/>

# Introduction


SKITCollegeChatBot is an AI bot specially tailored for College institution purpose. This bot is designed to both have a good core knowledge about SKIT College as well as JNTUA. It Consists of Regulation syllabus, lecture notes, previous question papers for all branches with accurate links. This project is based on AIML 1.0, 1.0.1, 2.0 and uses Program Y and PyAIML for using the AIML interpreter in python. 

Our chatbot runs on two variety of clients 

*Console
*Web Chat

This chatbot is fully cross plaform, running on 

* Mac OSX
* Linux
* Windows

Note: Some required dependencies has to be manually installed on windows which sometime may lead to errors.

See the individual files of unix and windows scripts required to run a bot.


# Short Intro on Program Y

Program Y is an AIML interpretor written in Python. It includes an entire Python 3 framework for building you own chat bots using
Artificial Intelligence Markup Language, or AIML for short. 

Programy-Y is fully 100% Support for all AIML 2.0 Tags plus all Pandora bot ones they never documented

* Full support for al AIML 2.0 Tags
* RDF Support through addtriple, deletetriple, select, uniq and uniq
* List processing with First and Rest
* Advanced learn support including resetlearn and resetlearnf
* Full Out Of Band Support
* Full embedded XML/HTML Support
* Dynamic Sets, Maps and Variables

Full documentation is available on [Program Y Wiki](https://github.com/keiffster/program-y/wiki)

# System Requirements

Program Y is built using Python 3.x and has dependencies upon the following Python libraries

requests==2.18.1
Flask==0.12.2
python-dateutil==2.6.1
beautifulsoup4==4.6.0
lxml==3.8.0
wikipedia==1.4.0
PyYAML==3.12
redis==2.10.6
aiml
SpeechRecognition
pyalsaaudio
pyttsx
gTTS

You can run `pip install -r requirements.txt` to install them all.

- ### AIML (For Pattern Recognition)
    `pip install aiml`

- ### Speech Recognition
    `pip install SpeechRecognition`

- ### PyAudio is required for microphone input
    `pip install pyaudio`

- ### alsaaudio: (For Volume Control)
    `pip install pyalsaaudio`

- ### ttsx: (Offline Text to Speech Service)
    `pip install pyttsx`
- ### Optional for Google Text to Speech:
   + #### gTTS: (Google Text to Speech service)
      `pip install gTTS

## Installation and Execution:

Clone this repository. Change directories to go to that directory. Run the script "script.py" **from the directory containing it**.
Run script as:

skcb.sh -- A shell file to execute the project and to debug the errors in terminal

skcb-web.sh -- A shell file to execute and run the project in http mode

skcb-web.cmd -- A batch command file to execute and run the project in http mode (Windows)

python script.py voice` : for voice mode of input or while in web page mode type "talk skitcb"

Voice mode may give a series of warnings for numerous reasons, but still might fuction properly.

## Contribution:

A lot can be done with this project. More python scripts can be associated. Pull requests for any such changes are accepted. Feel free to fork this project and make your own changes too.


#Learn AIML 2.0

Once you have got the system installed and have run our bot, head over to the [Tutorial](https://github.com/keiffster/program-y/wiki/AIML-Tutorial) on the Wiki for a full run down of everything possible in AIML





