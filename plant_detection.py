import cv2
import numpy as np

#img=cv2.imread(r"E:\core python\opencv\50.jpeg")
img=cv2.imread(r"C:\Users\hp\Downloads\plant1.jpeg")
img=cv2.resize(img,(500,500))

# find region of interest(ROI)
x,y,w,h=50,120,310,430
roi_img=img[y:y+h,x:x+w]
print(roi_img.shape)  #(415, 255, 3)
#cv2.imshow("roi",roi_img)

# converted to grayscale form
gry=cv2.cvtColor(roi_img,cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise
blurred = cv2.GaussianBlur(gry, (5,5), 0)

edge=cv2.Canny(blurred,130,150,apertureSize=3) 

# converted into binary form
_,thr=cv2.threshold(edge,50,255,cv2.THRESH_BINARY)
# cv2.imshow("thr",thr)


c,h=cv2.findContours(thr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
new_img=cv2.drawContours(roi_img,c,-1,(255,0,0),2)

# new_img = np.zeros_like(roi_img) # to create a blank image for drawing contours
# cv2.drawContours(new_img, c, -1, (255, 0, 0), 2)

# Assuming you have calculated these values
roi_width_pixels = 255  # Example width of ROI in pixels
roi_height_pixels = 415  # Example height of ROI in pixels
pixel_to_cm = 0.1  # Example conversion factor (0.1 cm per pixel)

# Convert pixel dimensions to cm
roi_width_cm = roi_width_pixels * pixel_to_cm
roi_height_cm = roi_height_pixels * pixel_to_cm

print(f"ROI width: {roi_width_cm:.2f} cm")
print(f"ROI height: {roi_height_cm:.2f} cm")


cv2.imshow("original",img)
cv2.imshow("contour",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

