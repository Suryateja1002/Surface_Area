# Surface Area Calculation for Detected Objects

### Overview
This script calculates the surface area of detected objects in an image using OpenCV. It preprocesses the image, detects contours, calculates the area of each detected contour, and annotates the image with the calculated areas.

### Approach

1.**Image Loading :** The image is loaded using cv2.imread().

2.**Grayscale Conversion :** The image is converted to grayscale to simplify processing.

3.**Gaussian Blurring :** Gaussian blur is applied to reduce noise in the image.

4.**Adaptive Thresholding :** Adaptive thresholding is used to handle varying lighting conditions and to better separate the objects from the background.

5.**Contour Detection :** Contours are detected in the thresholded image using cv2.findContours().

6.**Contour Filtering and Area Calculation :** Small contours (e.g., noise) are filtered out, and the area of each significant contour is calculated using cv2.contourArea().

7.**Drawing and Annotating :** Detected contours and their areas are drawn and annotated on the image.

8.**Displaying the Result :** The total surface area is printed to the console, and the image with annotated contours is displayed.

### Assumptions

1.**Object Types :** The script assumes that the objects in the image are flat and can be accurately represented by their 2D projections.

2.**Flat Object Assumption :** The calculated area is the surface area of the 2D projection of the object. For 3D objects, this may not represent the actual surface area.

3.**Contour Filtering :** Small contours (area less than 100 pixels) are considered noise and are filtered out. This threshold can be adjusted based on the specific requirements and image characteristics.

4.**Image Quality :** The script assumes that the input image is of reasonable quality, without excessive noise or extreme lighting conditions.

### Output Format

1.**Console Output :** The total surface area of all detected objects is printed to the console.

2.**Image Display :** The input image is displayed with detected contours and their corresponding surface areas annotated.
- Each contour is outlined in green.
- The area of each contour is displayed near the contour.


### Note

1.pip install opencv-python

2.save the file as filename.py
- Ex:- calculate_surface_area.py

3.Run the saved file in cmd
- python calculate_surface_area.py

