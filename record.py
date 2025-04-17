from picamera2 import Picamera2, Preview
import cv2
import os
import time

# Counter for saved images
count = 0

# Folder path to save calibration images
path = 'calib_images/'

# Create the folder if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path)

# Initialize the PiCamera2
picam2 = Picamera2()

# Set up the camera configuration
camera_config = picam2.create_preview_configuration(main={"format": "BGR888", "size": (640, 480)})
picam2.configure(camera_config)

# Start the camera
picam2.start()
time.sleep(3)  # Allow time for camera to warm up

# Capture loop
try:
    while True:
        # Capture frame from PiCamera2
        frame = picam2.capture_array()

        # Display the frame
        cv2.imshow('Current frame', frame)

        # Keyboard interaction
        k = cv2.waitKey(2) & 0xFF
        if k == ord('q'):  # Press 'q' to quit
            break

        # Save every 10th frame
        if count % 10 == 0:
            filename = os.path.join(path, f'{count}.jpg')
            cv2.imwrite(filename, frame)
            print(f"Saved {filename}")
        count += 1

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    # Clean up: stop camera and close windows
    picam2.stop()
    cv2.destroyAllWindows()
    print("Camera stopped and windows closed.")
