import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (80,60),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 2,
            color =(0,0,255))
cv2.putText(img,
            "Mercury",
            (120,250),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color =(0,255,0))
cv2.putText(img,
            "Venus",
            (200,260),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color =(0,255,0))
cv2.putText(img,
            "Earth",
            (295,270),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color =(0,255,0))
cv2.putText(img,
            "Mars",
            (390,260),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color =(0,255,0))
cv2.putText(img,
            "Jupiter",
            (550,380),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.8,
            color =(0,255,0))
cv2.putText(img,
            "Saturn",
            (760,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.6,
            color =(0,255,0))

cv2.putText(img,
            "Uranus",
            (970,290),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.6,
            color =(0,255,0))

cv2.putText(img,
            "Neptune",
            (1123,290),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.6,
            color =(0,255,0))


cv2.imshow ("Output",img)
cv2.waitKey(0)
