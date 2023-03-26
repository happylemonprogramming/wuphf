import qrcode

def QR_Code(data):
  # Generate QR Code
  img = qrcode.make(data)
  imgpath = "qrcode.png"
  img.save(imgpath)

  # Read the image file as binary data
  with open(imgpath, 'rb') as f:
      image_data = f.read()
  return image_data