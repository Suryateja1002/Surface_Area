# import the packages
#!pip install opencv-python

import cv2
import numpy as np

# calculating the surface area
def calculate_surface_area(image_path):
    # Load the image using cv2
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found or cannot be loaded.")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive thresholding to handle varying lighting conditions
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Initialize total area
    total_area = 0
    
    # Loop over the contours
    for contour in contours:
        # Calculate the area of each contour
        area = cv2.contourArea(contour)
        
        # Optionally filter out small contours
        if area > 100:  # Adjust this threshold as needed
            total_area += area
            
            # Draw the contour and the area on the image
            cv2.drawContours(image, [contour], -1, (111, 0, 255), 1)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(image, f"Area: {area:.2f}", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (220, 255, 0), 1)
    
    # Display the total area
    print(f"Total surface area: {total_area:.2f}")
    
    # Show the image with contours and areas
    cv2.imshow("Detected Objects", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
calculate_surface_area("b1.jfif")
