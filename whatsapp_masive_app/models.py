import pywhatkit
import base64
from PIL import Image
from io import BytesIO
import time
import os


def send_whatsapp_request(message, phones, image, imageName,ipUser):
    imageRoute = save_image(ipUser,image,imageName) if (image != '' and imageName != '') else ''
    for phone in phones:
        if imageRoute != '' and message != '':
            send_images(imageRoute,phone)
            send_message(message, phone)
        elif imageRoute == '' and message != '':
            send_message(message, phone)
        elif imageRoute != '' and message == '':
            send_images(imageRoute,phone)
    delete_image(imageRoute)

def send_message(message, phone):
    pywhatkit.sendwhatmsg_instantly(
        phone_no= phone,
        message=message,
        tab_close=True
    )

def send_images(imageRoute, phone):
    pywhatkit.sendwhats_image(
        receiver=phone,
        img_path= imageRoute,
        tab_close=True
    )

def save_image(ipUser, imageUser,imageName):
    fileName = f'whatsapp_masive_app/images/{ipUser}_{imageName}'
    Image.open(BytesIO(base64.b64decode(imageUser.split(';base64')[1]))).save(fileName)
    return fileName

def delete_image(imagePath):
    if os.path.exists(imagePath):
        os.remove(imagePath)