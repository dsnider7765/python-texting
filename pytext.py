# pytext.py
# David Snider
# November 14,2016

'''an attempt at using python to send texts'''
from twilio.rest import TwilioRestClient
accountSID = 'AC1ce4d981192db20123f84bd6cf6035bc'
authToken = '643726e40cc3def605b4e72c46c6ae5f'

twilioCli = TwilioRestClient(accountSID,authToken)
twilioNumber = '+13146268235'
myNumber = '+16362321563'
zach = '+16362848811'

#testing
twilioCli.messages.create(body='testing testing \
1234 1234', from_=twilioNumber, to=myNumber)
