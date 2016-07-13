from PIL import Image, ImageDraw, ImageFont

def addNum2Image(img,num):
    width,height = img.size
    fontsize = int(width*0.2)
    fnt = ImageFont.truetype('Arial.ttf',fontsize)
    
    draw = ImageDraw.Draw(img)
    draw.text((width - fontsize-10,0),str(num),font=fnt,fill=(0,255,0))
    img.save('numImage.jpg','JPEG')
    return 0
    
if __name__ == '__main__':
    image = Image.open('0455.jpg')
    addNum2Image(image,99)

