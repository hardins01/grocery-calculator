# this config file will support the creation of the venmo access token
from venmo_api import Client

access_token = Client.get_access_token(username='xxxxxxxxxxxx@xxxxx.com', password='xxxxxxxxxx')
print("My token:", access_token)
client = Client(access_token=access_token)
client.log_out(access_token)
