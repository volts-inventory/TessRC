import config
import pigpio
import threading
import time

class RobotCar():

    def __init__(self):
        self.current_throttle, self.last_throttle  = config.NEUTRAL_SPEED_DC, config.NEUTRAL_SPEED_DC
        self.current_steer, self.last_steer = None, None
       
        self.pi = pigpio.pi()
        self.pi.set_mode(config.STEER_PIN, pigpio.OUTPUT) 
        self.pi.set_mode(config.THROTTLE_PIN, pigpio.OUTPUT) 

        self.steer_thread = threading.Thread(target=self._run_steer, args=())
        self.drive_thread = threading.Thread(target=self._run_drive, args=())
       
    # -90 is left to 0 is neutral to 90 is right
    def turn(self, angle = 0):
        
        angle = 85 if angle > 85 else angle
        angle = -85 if angle < -85 else angle
        print(f"Turn Angle: {angle}")
        self.current_steer = float(round((1/36 * angle) + config.STEER_STRAIGHT_DC, 2))

    # -10 to 10
    # I think this is wrong and why reverse doesn't work
    def move(self, speed = 0):
        print(f"Move Speed: {speed}")
        self.current_throttle = float(round((1/4 * speed) + config.NEUTRAL_SPEED_DC, 2))

    def _run_steer(self):
        while True:
            time.sleep(0.02)
            if self.last_steer != self.current_steer:
                print(self.current_steer, self.current_throttle)   
                self.last_steer = self.current_steer
            self.pi.hardware_PWM(config.STEER_PIN, config.STEER_FREQ, int(self.current_steer * 10000))
    
    def _run_drive(self):
        while True:
            time.sleep(0.02)
            if self.last_throttle != self.current_throttle:
                print(self.current_steer, self.current_throttle)        
                self.last_throttle = self.current_throttle
            self.pi.hardware_PWM(config.THROTTLE_PIN, config.THROTTLE_FREQ, int(self.current_throttle * 10000))

    def run(self):
        self.drive_thread.start()
        self.steer_thread.start()
        self.turn()
        self.move()
        # init to esc time to sync
        time.sleep(2)

            
            



