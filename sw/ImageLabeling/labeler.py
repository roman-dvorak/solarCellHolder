import os, sys

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

print(sys.argv)
print("Usage 'labeler.py <folder> <cell_name> <shutter>'")

infolder = '/home/roman/cell/cell6_09_32x'
infolder = sys.argv[1]
outfolder = infolder+'/labeled'

for filename in os.listdir(infolder):
    if os.path.isfile(os.path.join(infolder, filename))  and 'label' not in filename:
        print(filename)
        img = Image.open(os.path.join(infolder, filename))
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("PTC55F.ttf", 30)
        # draw.text((x, y),"Sample Text",(r,g,b))

        draw.text((300, 50), "Cell: "+sys.argv[2] ,(255,255,255), font = font)
        draw.text((300, 90), "Current: "+filename.replace('.png', ' mA') ,(255,255,255), font = font)
        draw.text((300, 120), "Shutter: "+sys.argv[3]+"x" ,(255,255,255), font = font)
        img.save(os.path.join(infolder, 'label_'+filename))


##
##
## 224049 - CSEM
## 222609 - CSEM
##
## 222584 - PVLab
## 222588 - PVLab