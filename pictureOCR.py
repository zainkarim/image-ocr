import cv2
import easyocr
import matplotlib.pyplot as plt

# Create image variable
image_path = input('Enter the name of the file you would like to read or paste in its location: ')

# Use OpenCV to read in the image 
img = cv2.imread(image_path)

# Create a text detector with Easy OCR
reader = easyocr.Reader(['en'], gpu=True)

# Create a threshold for identifying text
threshold = 0.10

# Detext the text in the image
text_data = reader.readtext(img)

# Draw bounding boxes and write text on image
for t in text_data:
    print(t)

    bounding_box, output_text, score = t
    
    # Only draw boxes and output text if score is > threshold
    if score > threshold:    
        # Draw boxes
        cv2.rectangle(img, bounding_box[0], bounding_box[2], (0, 255, 0), 5)
        # Write text
        cv2.putText(img, output_text, bounding_box[3], cv2.FONT_HERSHEY_SIMPLEX, 4.25, (255, 0, 255), 9)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGRA2RGB))
plt.show()