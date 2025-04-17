from picarx import Picarx  # Import the PiCar Library to use functions to control a robot	
import time		      # Import time module Needed for the delay function 

if __name__ == "__main__":   # Run only when commanded
    try:				 # Start of Try-Catch-Finally
        px = Picarx()		 # Create an instance of PiCar to start using func.

        px.forward(180)            # Changed from 30 to increase distance traveled & Duration
        time.sleep(0.5)	         # Wait 0.5 ms while moving forward

# Start gradually turning from 0 degrees to 35 degrees to the right
        for angle in range(0,35):
            px.set_dir_servo_angle(angle)   # Move to the incrementing angle in for loop
            time.sleep(0.01)      # Wait for 0.01 ms

# Start gradually turning from 35 degrees to -35 degrees to the left
        for angle in range(35,-35,-1):
            px.set_dir_servo_angle(angle) # Move to the incrementing angle in for loop
            time.sleep(0.01)     # Wait for 0.01 ms

# Start gradually turning from 0 degrees to 35 degrees to the left
        for angle in range(-35,0):
            px.set_dir_servo_angle(angle) # Move to the incrementing angle in for loop
            time.sleep(0.01)		  # Wait for 0.01 ms

        px.forward(0) 			# Stop moving
        time.sleep(1)			# Wait for 1 ms

 # Comment pattern repeats
        for angle in range(0,35):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(0,35):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)

    finally:
        px.forward(0) 	# Stop moving