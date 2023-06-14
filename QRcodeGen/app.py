#in this app we will convert a text or a link into a QR code
#we will use libraries but we have to install the first
#create a fuction that collects the text and converts it to a QR code 
#then save the QR code as an image

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color ="black", back_color ="white")
    img.save("qrimg1.png")

user = input("Enter your word to be converted into a QRcode: ")
generate_qrcode(user)
