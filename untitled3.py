# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WXnTkhVeVPilOhWybmYoxX5q250_weza
"""

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread( "a12 — копия.jpg")
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread( "a27.jpg")
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread( "a64 — копия.jpg")
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)