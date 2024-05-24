import cv2
import os

def segment_visual_elements(image_path, output_dir):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    visual_elements = []
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:  # Filtering small contours
            element = image[y:y+h, x:x+w]
            element_path = os.path.join(output_dir, f'element_{i}.png')
            cv2.imwrite(element_path, element)
            visual_elements.append(element_path)
    
    return visual_elements
