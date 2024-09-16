import cv2
import numpy as np

# Load and resize the image
img=cv2.imread(r"C:\Users\hp\Downloads\plant1.jpeg")
img=cv2.resize(img,(500,500))

# Define region of interest(ROI)
x,y,w,h=50,120,310,430
roi_img=img[y:y+h,x:x+w]
print(roi_img.shape)  #(415, 255, 3)

# Convert ROI to grayscale
gry=cv2.cvtColor(roi_img,cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise
blurred = cv2.GaussianBlur(gry, (5,5), 0)

# Detect edges using Canny edge detection
edge=cv2.Canny(blurred,130,150,apertureSize=3) 

# converted into binary form
_,thr=cv2.threshold(edge,50,255,cv2.THRESH_BINARY)
# cv2.imshow("thr",thr)


c,h=cv2.findContours(thr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
new_img = cv2.drawContours(roi_img.copy(), c, -1, (255, 0, 0), 2)


# Assuming these values are correct for your setup
roi_width_pixels = roi_img.shape[1]  # Width of ROI in pixels
roi_height_pixels = roi_img.shape[0]  # Height of ROI in pixels
pixel_to_cm = 0.1  # Example conversion factor (0.1 cm per pixel)

# Convert pixel dimensions to cm
roi_width_cm = roi_width_pixels * pixel_to_cm
roi_height_cm = roi_height_pixels * pixel_to_cm

print(f"ROI width: {roi_width_cm:.2f} cm")
print(f"ROI height: {roi_height_cm:.2f} cm")

# Display images
cv2.imshow("original",img)
cv2.imshow("contour",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

