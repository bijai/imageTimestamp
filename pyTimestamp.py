from PIL import Image, ImageFont, ImageDraw 
import datetime
from os import path



def writeTimeStamp(imagePath,timeStamp,outputFolderName=""):
    bundle_dir = path.abspath(path.dirname(__file__))
    fileName = path.basename(imagePath)
    my_image = Image.open(imagePath)

    font_size = round(my_image.size[1]*0.05)

    title_font = ImageFont.truetype(path.join(bundle_dir,'Lato-Regular.ttf'), font_size)
    title_text = timeStamp.strftime("%b %d, %Y %I:%M%p")
    image_editable = ImageDraw.Draw(my_image)
    text_length = (image_editable.textsize(title_text, font=title_font))[0]
    padding_x = round(my_image.size[0]*0.01)
    padding_y = round(my_image.size[1]*0.01)
    (x,y) = (my_image.size[0]-text_length-padding_x,padding_y)
    image_editable.text((x+6,y+6), title_text, (54, 54, 54), font=title_font)
    image_editable.text((x,y), title_text, (255, 255, 255), font=title_font)
    my_image.save(path.join(outputFolderName,fileName))
    

if __name__=="__main__":
    writeTimeStamp("DSCN8805.JPG",datetime.datetime.now())

