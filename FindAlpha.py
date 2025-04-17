from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
    # Motor Power (V_in) #
        px.forward(100)
    # Time run #
        time.sleep(1.5)
    #stop#
        px.forward(0)
        time.sleep(1)


    finally:
        px.forward(0)