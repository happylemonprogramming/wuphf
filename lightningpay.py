import requests
import json
import uuid
from datetime import datetime
import os
import qrcode

strikeapikey = os.environ.get('strikeapikey')

def generate_invoice_id():
    """
    Generates a unique invoice ID using the current date/time and a unique identifier
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")  # format current date/time
    uid = str(uuid.uuid4().hex.upper()[0:6])  # generate unique identifier
    invoice_id = f"{now}-{uid}"  # combine date/time and identifier
    return invoice_id

def lightning_invoice():
  # Create a new invoice
  url = "https://api.strike.me/v1/invoices"

  payload = json.dumps({
    "correlationId": generate_invoice_id(),#</= 40 characters
    "description": 'Samule.io Basic Plan Monthly', #</= 200 characters
    "amount": {
      "currency": "USD",
      "amount": '0.01' #for testing purposes
    }
  })
  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {strikeapikey}' #TODO: make this an environment variable
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  # print(response.json())
  invid = response.json()['invoiceId']
  return invid

# Function to generate lightning address
def lightning_quote():
  invid = lightning_invoice()
  # insert invoice id here
  url = "https://api.strike.me/v1/invoices/"+invid+"/quote" 

  payload={}
  headers = {
    'Accept': 'application/json',
    'Content-Length': '0',
    'Authorization': f'Bearer {strikeapikey}' #TODO: make this an environment variable
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  lninv = response.json()['lnInvoice']
  conv_rate = response.json()['conversionRate']['amount']
  return lninv, conv_rate, invid


def invoice_status(invoiceId):

  url = f"https://api.strike.me/v1/invoices/{invoiceId}"
  payload={}
  headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {strikeapikey}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  status = response.json()['state']
  return status


# print(lightning_quote())

# def lightning_QRCode():
#   # Generate QR Code
#   # from PIL import Image
#   lninv = lightning_quote()[0]
#   conv_rate = lightning_quote()[1]
#   img = qrcode.make(lninv)
#   imgpath = "Strike.png"
#   img.save(imgpath)

#   # Read the image file as binary data
#   with open(imgpath, 'rb') as f:
#       image_data = f.read()
#   return image_data

# # print(lightning_QRCode())