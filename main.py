import os
from text_extraction import extract_text
from visual_segmentation import segment_visual_elements
from html_generator import generate_html

def main(image_path, output_dir):
    # Extract text
    extracted_text = extract_text(image_path)
    print("Extracted text:", extracted_text)
    
    # Segment visual elements
    visual_elements = segment_visual_elements(image_path, output_dir)
    print("Visual elements:", visual_elements)
    
    # Generate HTML
    generate_html(extracted_text, visual_elements, os.path.join(output_dir, "output.html"))
    print("HTML file generated at:", os.path.join(output_dir, "output.html"))

if __name__ == "__main__":
    # Use raw string for file path
    image_path = r"input_images\test.png"
    output_dir = r"output"
    os.makedirs(output_dir, exist_ok=True)
    main(image_path, output_dir)
