import os, sys
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import matplotlib.pyplot as plt

print(sys.argv)
print("Usage 'labeler.py <folder> <cell_name>'")

infolder = sys.argv[1]

values = []
current = []

for filename in sorted(os.listdir(infolder)):
    if os.path.isfile(os.path.join(infolder, filename))  and 'label' not in filename:
        print(filename)
        img = Image.open(os.path.join(infolder, filename))
        array = np.array(img) 
        values += [np.sum(array)]
        current += [float(filename.replace('.png', ''))]

print(values)
plt.plot(current, values)
#plt.ylabel('some numbers')
path = os.path.join(infolder, '..', sys.argv[2]+'.png')
print(path)
print(infolder)
plt.savefig(path, bbox_inches='tight')
plt.show()

##
##
## 224049 - CSEM
## 222609 - CSEM
##
## 222584 - PVLab
## 222588 - PVLab