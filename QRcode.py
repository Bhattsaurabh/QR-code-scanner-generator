import pyqrcode     # for qr generate
import pyzbar       # for qr scanner
from pyzbar.pyzbar import decode
from PIL import Image
content="https://bhattsaurabh.github.io/saurabhportfolio.github.io/"
qr_code=pyqrcode.create(content)
qr_code.png('myportfolio.png', scale=5)
print("QR CODE GENERATED SUCCESSFULLY")


#SCANNER

img = Image.open("myportfolio.png")
cont =  decode(img)
print(cont[0].data.decode())
