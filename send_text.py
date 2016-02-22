from twilio.rest import TwilioRestClient
import datetime
import random

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "" #input your account sid
auth_token  = "" #in your auth token
#Instantiate class TwilioRestClient with your credentials
client = TwilioRestClient(account_sid, auth_token)

#set current date and time into variable
d = datetime.datetime.now() 

#List that holds the messages that are texted
text = ['Hello Hilary. This is your reminder to drink water. Thank you.',
		'Bernardo wants to know if you\'re drinking water. Hugs!',
		'*computer voice* Drink water please!',
		'May I recommend this site: http://greatist.com/health/health-benefits-water',
		'I\'m thirsty. Are you thirsty? Let\'s go grab a water!',
		'It\'s Water O\'Clock somewhere, am I right?',
		'Hey kid, wanna try some water? All the cool kids are drinking it.',
		'Gimme a H. Gimme a 2. Gimme an O. What\'s that spell? Water!',
		'Don\'t you love letting out a big \'Aaaahhh\' after a nice gulp of water?',
		'Kick back, put your feet up, grab a drink of water and enjoy this https://www.youtube.com/watch?v=oHg5SJYRHA0',
		'Waiter, what\'s the water de jour? It\'s the water of the day. Thank you, I\'ll have that.']


if d.isoweekday() in range(1, 6): #checks for Monday - Friday
	if d.hour in range(10, 18): #checks for 10am - 5pm
		message = client.messages.create( 
    		body=random.choice(text), #randomly select a message from the text list
    		to="",   # Replace with your phone number starting with +1
    		from_="") # Replace with your Twilio number starting with +1
		print message.sid
	else:
		print 'Not in time range'
else:
	print 'Not weekday'


