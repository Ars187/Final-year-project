import cv2
import numpy as np
import pytesseract
import numpy as np
def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)
pytesseract.pytesseract.tesseract_cmd = "D:\\Project\\Tesseract\\tesseract.exe"
# img = cv2.imread("D:\\Project\\img1.png")
# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(grey, (5,5), 0)
# cv2.imshow("image", blur) 
# cv2.waitKey(0)
# blur = noise_removal(grey)
# cv2.imshow("image", blur) 
# cv2.waitKey(0)
# img1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,3,2)
# cv2.imshow("image", img1) 
# cv2.waitKey(0)
# text = pytesseract.image_to_string(img1)
# print(text)



# Path to video file
video_path = r"D:\Project\Dataset\Cws\mit038\segmentation\videos\MIT8_06S18_L02_300k.mp4"

# Interval between key frames (in seconds)
interval_seconds = 120

# Open video file
video = cv2.VideoCapture(video_path)

# Get video properties
fps = video.get(cv2.CAP_PROP_FPS)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculate frame interval
interval_frames = int(fps * interval_seconds)

# Current frame index
frame_index = 0

# Open video file
video = cv2.VideoCapture(video_path)
file1 = open(r"D:\Project\ocr_text\res.txt", "w")
# Loop through frames
# Loop through frames
while frame_index < total_frames:
    # Set the frame index
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    
    # Read the frame
    ret, frame = video.read()
    
    if not ret:
        break
    
    # Convert frame to grayscale (if necessary)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = noise_removal(grey)
    img1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,3,2)
    # Perform OCR
    text = pytesseract.image_to_string(img1)
    
    # Display the recognized text
    file1.write(text)
    frame_index += interval_frames
    # Display the frame (optional)
    # cv2.imshow('Frame', frame)
    
    # Press 'q' to quit
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
file1.close()
# Release video object
video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
