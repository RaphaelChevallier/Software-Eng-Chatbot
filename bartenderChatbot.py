from flask import Flask
from flask import request
import random
import json
import os
import requests

os.environ['NLTK_DATA'] = '~/nltk_data'
GREETING_RESPONSES = ["What can I get you?", "Hello stranger, what can I serve up for you?", "Need a drink?", "Hi, hope you're thirsty. What can I get you?"]
GOODBYE_RESPONSES = ["Have a good night", "Drive safe!", "Until next time"]
DRINK_RESPONSES = ["Sure coming right up", "Here you go. Here's your drink", "Your drink is coming right up"]
FOOD_RESPONSES = ["Sure coming right up", "Here you go. Here's your food", "Your food is coming right up"]
STATUS_RESPONSES = ["I'm doing pretty good. It's a busy night tonight though. Are you going to order?", "Great! I'm doing fantastic", "Just trying to pay the bills man", "You going to have to tip for me to talk to ya"]
WEATHER_RESPONSES = ["It's sunny today. Maybe you should go outside", "Pouring rain and freezing cold. Maybe you should stay in and get more drinks?", "It's hot. Sticky 85 degrees."]
TRAVEL_RESPONSES = ["Go downtown. It's a great place to chill and get ice cream", "The lake is amazing. Great for the hot weather and swimming", "Big white is nearby. You should check that out."]
HEDGE_RESPONSES = ["I have no idea what you're asking", "I'm not sure", "Can you re-phrase that?", "Pardon?", "Sorry I can't do that", "I'm confused"]
chat_log = {}

  #Call on LUIS app here
def LUIS_Call(message):
	headers = {
		# Request headers
		'Ocp-Apim-Subscription-Key': 'b0a33f5fa946453ca4aa2a6ef8703568',
	}

	params = {
		'q': message,
		'verbose': 'true'
	}
	try:
		#c35e79c6427144fc9695a914ce1874c6
		r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/79b9c6d3-8740-4b03-97fe-93a83779505b?spellCheck=true&bing-spell-check-subscription-key=%7Bc35e79c6427144fc9695a914ce1874c6',headers=headers, params=params)
		return r.json()

	except Exception as e:
		# pylint: disable=no-member
		print("[Errno {0}] {1}".format(e.errno, e.strerror))

def createMessage(input):
	'''Takes json facebook input and creates the message to return to facebook'''
	input_msg = input['text']
	senderId = input['sid']
	data = buildMessage(input_msg, senderId)
	return str(data)  #this will return the wanted message back out to messenger


def buildMessage(input_msg, senderId):
	'''Core Logic to build the message.
	If unsure how to reply, will respond with a hedge'''

	# Clears the user session to start over new
	if input_msg.lower() == 'clear':
		clearSession(senderId)
		return "Session cleared"

	times_con = howManyMessages(senderId)
	luis = LUIS_Call(input_msg)
	intent = luis['topScoringIntent']['intent']
	sentiment = luis['sentimentAnalysis']
	print(sentiment)
	if intent == 'getDrink' or intent == 'getFood':
		print(luis['entities'])


	# If the user is greeting, respond with a greeting
	if intent == 'greeting':
		return random.choice(GREETING_RESPONSES)

	if intent == 'goodbye':
		# They're leaving, so clear the session
		clearSession(senderId)
		return random.choice(GOODBYE_RESPONSES)

	if intent == 'getStatus':
		return random.choice(STATUS_RESPONSES)

	if intent == 'getWeather':
		return random.choice(WEATHER_RESPONSES)

	if intent == 'getTravel':
		return random.choice(TRAVEL_RESPONSES)

	if intent == 'getDrink':
		num_drinks = chat_log[senderId]['drinks_served']
		if num_drinks > 3:
			return "Sorry you've had too many drinks. You're drunk rn"
		else :
			return random.choice(DRINK_RESPONSES)

	if intent == 'getFood':
		return random.choice(FOOD_RESPONSES)

	return random.choice(HEDGE_RESPONSES)

def createChatLog(senderId):
	'''Keeps track of each session ID in a dictionary'''
	log = {'times_contacted': 1, 'context': None, 'drinks_served': 0}
	chat_log[senderId] = log


def howManyMessages(senderId):
	'''Check the chat log for number of messages and increment accordinly.'''
	if senderId not in chat_log:
		createChatLog(senderId)
		#return value is number of messages received
		return 1
	else:
		times_con = chat_log[senderId]['times_contacted'] + 1
		chat_log[senderId]['times_contacted'] = times_con
		return times_con


def clearSession(senderId):
	'''Delete any data from the user session log'''
	chat_log[senderId]['times_contacted'] = 0
	chat_log[senderId]['drinks_served'] = 0


#all code above this created API
app = Flask(__name__) #create the app server to recieve json

@app.route('/givenMessage', methods = ['POST'])
def postJsonHandler():
	'''Receives POST request from webhook and returns POST data'''
	#print (request.is_json)
	content = request.get_json()
	#print (content)
	message = createMessage(content)
	return message

app.run(host = '0.0.0.0', port = 8090)
