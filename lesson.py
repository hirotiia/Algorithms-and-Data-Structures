class Person(object):
    def talk(self):
        print('person talk')

class Car(object):
    def drive(self):
        print('car drive')

class Person_Car_Robot(Person, Car):
    def fly(self):
        print('I can fly')

person_car_robot = Person_Car_Robot()
person_car_robot.talk()
person_car_robot.drive()
person_car_robot.fly()