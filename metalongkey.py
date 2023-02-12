import requests

app_id = '554211022979973'
# Need to store as environment variable
app_secret = 'f7cabaab119d7bd8dcafb3bec28c5cc3'
temp_access_token = 'EAAH4DU8nw4UBAA1e5v0mBDf59y0kGqUZCtEWRg7jWSzl5cSiKUvia63vGUK2hh3DftoWqELWj3QlNJ4GODn8GzVyxeQ6ijgSBiO9lVqyUWmyrH9uAALBlLTA3ApJXFufYiSRcAoe3YzdtT1QBBBAH2oLWxN2cezqk1BE1nHMoxNUOYdNXBXF69lZB73nU8NKRgOdup9Kc1NZAEm1x7v'

# curl -i -X GET "https://graph.facebook.com/{graph-api-version}/oauth/access_token?  
#     grant_type=fb_exchange_token&          
#     client_id={app-id}&
#     client_secret={app-secret}&
#     fb_exchange_token={your-access-token}" 

# # Get Pages ID
key_url = "https://graph.facebook.com/v16.0/oauth/access_token"
id_data = {
    "grant_type":"fb_exchange_token",
    "client_id": app_id,
    "client_secret": app_secret,
    "fb_exchange_token": temp_access_token}
response = requests.get(key_url, params=id_data)
long_key = response.json()
print(long_key)