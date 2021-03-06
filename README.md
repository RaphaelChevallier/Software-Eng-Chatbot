# Software-Eng-Chatbot
## 310 Assignment 3: CHAT BOT
## USER GUIDE
Author: Raphael Chevallier

## Introduction
For this assignment, I build a chat bot to mimic basic bartending needs. Built with basic functionality that can accept a text entry and respond with a logical statement. My bot uses a trained NLP engine to provide language understanding as well as spell checking, sentiment analysis, synonym recognition, and entity recognition to help create the best response to the user. The app is accessible through Facebook and can be easily interacted with through the messenger. I decided to use Facebook Messenger for the wide use of Messenger letting many people reach my chatbot with ease

## Infrastructure
The bartender chatbot uses facebook as a front-end.  Communication with facebook is done through a nodeJS webhook that passes the message data to a python service (flask) which processes the user's message and responds accordingly. In order to readily communicate with facebook, the chatbot is currently installed and running on a dedicated linux server. The flask chatbot bartenderChatbot.py can run as a stand-alone chatbot service and hook into any kind of front end interface with minimal changes. The flask chatbot uses LUIS to understand the incoming text as best it can. Chat flow when user messages the bot follows the steps below.
* User messages chatbot on facebook
* Facebook API
* Nginx Forward proxy (for SSL termination) 
* Node JS
* Flask chatbot receives message and uses NLP engine to respond

## Libraries/Tools
* NLTK/TextBlob - Python framework used for natural language processing
* LUIS.ai - NLP engine from Microsoft that can be trained by user
* Express.js - A javascript Node.js library that facilitates REST API creation
* Flask - Python web framework used to communicate with POST requests

## Gain Permission to Access Chatbot
As facebook requires for any app on their services to be reviewed, my chatbot app is not accessible to the public. Awaiting facebook to review an app may take a while so for the meantime I need to authorize test users to access the chatbot through messenger. If you wish to test our app please contact raphaelchevallier@hotmail.com and pass your facebook ID or username. Once approved we will send back an invite to that facebook id/username and you will need to direct yourself to https://developers.facebook.com/ and accept the invite to be a tester. Once accepted, travel to https://www.facebook.com/Bartender-Chatbot-310-594256287663533/
and message the page. The chatbot will respond back to you and will be fully functional to you.

## Potential Improvements
Potential improvements to the system would be to implement a sort of memory system. It would be good to have the chatbot "remember" what it talks about to more smoothly follow a conversation

# Install Chatbot to own server
## Prerequisites
* NodeJS - NPM
* Python 3
* Flask

## Installing
Example commands for installing the Chatbot on an Ubuntu or Debian server. Flask can be installed using pip. It would be good practice to use a python virtualenv if installing on a shared computer.
```console
user@server:~$ apt install nodejs 
user@server:~$ apt install npm
user@server:~$ apt install python3-pip
user@server:~$ pip3 install flask
user@server:~$ apt install git
user@server:~$ git clone https://github.com/RaphaelChevallier/Software-Eng-Chatbot-G7.git
user@server:~$ cd Software-Eng-Chatbot-G7/
user@server:~$ npm install
```
## Running
Once installed, run flask and node as background processes.
```console
user@server:~$ nodemon webhook.js &
user@server:~$ python3 bartenderChatbot.py &
```
# Level 0 DFD
1. User types into messenger page
2. Chatbot system understands and produces a response
3. Repeat

# Level 1 DFD
1. User goes to messenger and types intent
2. Node.js file takes input and gives clean json to python file
3. Python file calls NLP engine LUIS and understands intent
4. Python file formulates response based off understanding
5. Sends response to user through clean Node.js file again

# Demo Output
![demo output](/demoImages/demo.png)

Limitations:
* Can't remember previous conversations so can't string very well certain sentences
* The sentiment analysis I get is very basic of positive, negative, or neutral
* Spell check isn't perfect

# Features that can be extracted as an API
* The analysis of sentiment can be used as an API for other bots
* Entity recognition can also be used for other bartender chatbots
* The spell check can
* The NLP engine can be used for training
* The weather topic can be used and shared to get weather in sourroundings

# Features Provided by chatbot
### 1.Great GUI - with the use of Facebook Messenger. Allows for a wide range of users and comfortability. Everyone knows how to use Messenger and is reliable.
![Facebook Messenger Logo](/demoImages/facebookLogo.png)
### 2.Adding extra topics to the bot - A bartender is meant to be able to provide small talk which is what I do and add. I add a weather topic, ordering topic, tips of places around town topic, and asking how the bot is doing.
![extra topic picture](/demoImages/extraTopic.png)
### 3.I have 5+ phrases for when the bot doesn't completely understand what the user wants to provide a smoothness. It is random so it was hard for me to get more of 5 different ones in a row so heres 4 in the image.
![5+ phrases for errors of misunderstanding](/demoImages/findingErrors.png)
### 4.My bot can do spell checking and still understand what the user intent is. With LUIS I can train it to surpass spelling mistakes as long as they are not too unrecognizable.
![spell check](/demoImages/spellCheck.png)
### 5.My chatbot recognizes synonyms as the same entity such as drink, booze, alcohol.
![synonyms](/demoImages/synonyms.png)
### 6.My bot can detect the entities of the sentences the user utters to the bot. This does not display in the chat however but rather the console of the server.
![sentiment and entity](/demoImages/findingEntity&Sentiment.png)
### 7.Lastly my chatbot can recognize sentiments as well from users. This is also only on the server console. This is basic however as it can only detect "positive", "negative", or "neutral" as well as provide a score of confidence on its decision.
![sentiment and entity](/demoImages/findingEntity&Sentiment.png)
