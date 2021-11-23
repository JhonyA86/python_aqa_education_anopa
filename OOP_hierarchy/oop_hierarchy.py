class Transport:

    number_of_transport = 0

    def __init__(self, speed, capacity, distance, kind):
        self.speed = speed
        self.capacity = capacity
        self.distance = distance
        self.kind = kind
        Transport.number_of_transport += 1

    @staticmethod
    def tr_intro_text():
        message = """Here is short information about different types of transport:
            """
        print(message)

    def tr_info(self):
        print(f"This is {self.kind} transport")
        print(f"It speed reaches {self.speed} km / h")
        print(f"It covers distances of more than {self.distance} km and can accommodate {self.capacity} passengers")

    @property
    def travel(self):
        return f"I'm travelling by {self.kind} transport"


class Airplane(Transport):

    def __init__(self, altitude, *args):
        self.altitude = altitude
        super().__init__(*args)

    def fly(self):
        print(f"Airplane is flying at average altitude {self.altitude} km")


class Bus(Transport):
    def __init__(self, wheels, *args):
        self.wheels = wheels
        super().__init__(*args)

    def drive(self):
        print(f"Big buses drive on at least {self.wheels} wheels")


class Car(Bus, Transport):
    def drive(self):
        print(f"My Car drive on {self.wheels} wheels with {self.speed} km/h")


class Ship(Transport):
    def travel(self):
        print(f"Enjoy travelling by {self.kind} transport especially on a cruise ship")


class Train(Transport):
    def __init__(self, train_car, *args):
        self.train_car = train_car
        super().__init__(*args)

    def ride(self):
        print(f"Our passenger train has {self.train_car} carriages")


plane = Airplane(11, 900, 250, 10000, "Air")
plane.tr_intro_text()
plane.tr_info()
plane.fly()
print(plane.travel)
print("============================================================================")

bus = Bus(6, 150, 100, 1000, "Auto")
bus.tr_info()
bus.drive()
print(bus.travel)

c = Car(4, 130, 100, 1000, "Auto")
c.drive()
print("============================================================================")

ship = Ship(80, 5000, 15000, "Sea")
ship.tr_info()
ship.travel()
print("============================================================================")

train = Train(25, 100, 500, 9000, "Railway")
train.tr_info()
train.ride()
print("============================================================================")
print(f"Total transport number: {Transport.number_of_transport}")
