# import matplotlib.pyplot as plt
# import cv2
# import easyocr
# from IPython.display import Image

# Image("plates/scaned_img_0.jpg")

# reader = easyocr.Reader(['en'])

# output = reader.readtext('plates/scaned_img_0.jpg')
# output 

import easyocr

# plt.imshow(cv2.imread("plates/scaned_img_0.jpg"))
# plt.show()

reader = easyocr.Reader(['en'])

output = reader.readtext('plates/scanned_img_20240907_185722.jpg')
# print(output)
for box, text, confidence in output:
    print(text)
    print(confidence)