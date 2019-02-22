from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '{}'.format(os.environ['ACCOUNT_SID'])
auth_token = '{}'.format(os.environ['AUTH_TOKEN'])
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Your BLANK Repository has an Open PR',
         from_='+{}'.format(os.environ['FROM']),
         to='+{}'.format(os.environ['TO'])
     )

print(message.sid)