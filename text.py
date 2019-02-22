from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '{}'.format(os.environ['ACCOUNT_SID'])
auth_token = '{}'.format(os.environ['AUTH_TOKEN'])
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="GitHub Repo: {}\nMessage: A New PR has been Created by {}".format(os.environ['GITHUB_REPOSITORY'], os.environ['GITHUB_ACTOR']),
         from_='+{}'.format(os.environ['FROM']),
         to='+{}'.format(os.environ['TO'])
     )

print(message.sid)