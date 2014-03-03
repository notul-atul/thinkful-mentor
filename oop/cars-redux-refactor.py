class Car(object):

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def accelerate(self, amount=10, car_speed=0):
        accelerate = []
        new_speed = self.speed + amount + car_speed
        accelerate.extend([new_speed,"\nYour car accelerated to {}.".format(new_speed)])
        return accelerate

    def check_speed(self, current_speed):
        if current_speed > 70:
            return "You're speeding! Watch out for cops!"
        else:
            return "You're under the speed limit."


# ----------- #

my_car = Car("red",10)
speed = my_car.accelerate(50)
print speed[1]
print my_car.check_speed(speed[0])
speed = my_car.accelerate(20, speed[0])
print speed[1]
print my_car.check_speed(speed[0])
speed = my_car.accelerate(-60, speed[0])
print speed[1]
print my_car.check_speed(speed[0])

print "\n------------"

my_blue_car = Car("blue",40)
speed = my_car.accelerate(10)
print speed[1]
print my_car.check_speed(speed[0])
speed = my_car.accelerate(20, speed[0])
print speed[1]
print my_car.check_speed(speed[0])
speed = my_car.accelerate(40, speed[0])
print speed[1]
print my_car.check_speed(speed[0])


# ----------- #

"""
To Do -

1. Create a new method called "pulled_over()". 
Use logic to deterime that if a cop is nearby, you will get pulled over if you are speeding. 
Otherwise you're in the clear.
2. Change the "accelerate()" method to show whether a car has accelerated or decelerated.
"""

