# Image Processing Project Report

## Introduction
This project aims to separate text and visual elements from an image using a Vision API and basic image segmentation techniques.

## Technologies Used
- **Google Cloud Vision API**: For text extraction (OCR).
- **OpenCV**: For visual element segmentation.
- **Python**: For scripting and automation.

## Implementation Details

### Text Extraction
The `text_extraction.py` script uses Google Cloud Vision API to extract text from an image. The text is retrieved along with its coordinates.

### Visual Element Segmentation
The `visual_segmentation.py` script uses OpenCV to detect and isolate visual elements. Techniques like edge detection and contour detection are employed.

### HTML Generation
The `html_generator.py` script converts the extracted text and visual elements into a basic HTML structure, embedding text within `<p>` tags and visual elements within `<img>` tags.

## Challenges Encountered
- **OCR Accuracy**: Handling OCR inaccuracies and noise in the text extraction process.
- **Visual Element Detection**: Isolating meaningful visual elements while filtering out noise and irrelevant parts.

## Conclusion
This project successfully separates text and visual elements from images and generates an HTML representation. Future improvements could include advanced layout handling and more robust visual element detection.
