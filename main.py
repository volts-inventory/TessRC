import navigation
import time

r = navigation.RobotCar()

r.run()

r.move(2)
time.sleep(3)
r.move()
time.sleep(0.5)
r.move(-1)
time.sleep(0.5)
r.turn(90)
time.sleep(1)
r.move(2)
time.sleep(1)
r.move()
time.sleep(0.5)
r.move(-1)
time.sleep(0.5)
r.turn()
time.sleep(1)
r.move(2)
time.sleep(1)
r.move()
time.sleep(0.5)
r.move(-1)
time.sleep(0.5)
r.move()
time.sleep(5)

# for i in range(-80, 90, 20):
#     r.turn(i)
#     time.sleep(0.5)

# r.turn()
