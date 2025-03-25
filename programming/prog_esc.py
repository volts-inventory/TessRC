import navigation
import time

r = navigation.RobotCar()

r.run()

input("Press for Forward\n")

r.move(10)

input("Press for Reverse\n")

r.move(-10)