# plant_height_width_measure
To measure the real height and width of an object using OpenCV in Python, 
We follow several steps;
1)Convert the image to grayscale and apply Gaussian Blur to reduce noise.
2)Use the Canny edge detector to find edges in the image./Optionally, apply thresholding to get a binary image if needed.
3)Find contours in the edge-detected image.
4)Calculate the real dimensions of the object based on a known reference object's dimensions in the real world.
