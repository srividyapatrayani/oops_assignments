import math
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self._is_engine_started = False
        self._current_speed=0
    def start_engine(self):
        self._is_engine_started = True

    def stop_engine(self):
        self._is_engine_started = False

    def accelerate(self):
        if self._is_engine_started == False:
            print("Car has not started yet")
        else:
            self._current_speed += self.acceleration
            if self._current_speed > self.max_speed:
                self._current_speed = self.max_speed

    def apply_brakes(self):
        self._current_speed -= self.tyre_friction
        if self._current_speed < 0:
            self._current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Peep Peep\nBeep Beep")
        else:
            print("Car has not started yet")
    @property
    def current_speed(self):
        car.accelerate()
        return self._current_speed
    def is_engine_started(self):
        return self._is_engine_started
class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self.max_cargo_weight = max_cargo_weight
        self.load = 0

    def load_cargo(self, cargo_weight):
        if self.is_engine_started == True:
            print("Cannot load cargo during motion")
        elif (cargo_weight + self.load > self.max_cargo_weight):
            print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
        else:
            if cargo_weight>0:
                self.load += cargo_weight
            else:
                print("ValueError: Invalid value for cargo_weight")

    def unload_cargo(self, cargo_weight):
        if self.is_engine_started == True:
            print("Cannot unload cargo during motion")
        else:
            self.load -= cargo_weight
            if self.load < 0:
                self.load = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Car has not started yet")


class RaceCar(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self.nitro = 0

    def accelerate(self):
        if self.nitro > 0 and self.is_engine_started:
            self._current_speed = self._current_speed+math.ceil(0.3*self.acceleration)
            self.nitro = self.nitro - 10
        super().accelerate()

    def apply_brakes(self):
        if racecar._current_speed>(self.max_speed/2):
            self.nitro+=10
            self._current_speed=self._current_speed-self.tyre_friction
    def sound_horn(self):
        if self.is_engine_started:
            print("Peep Peep\nBeep Beep")
        else:
            print("Car has not started yet")


car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)


truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)



racecar = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)
racecar.start_engine()
racecar.accelerate()
racecar.accelerate()
racecar.accelerate()
print(racecar._current_speed)
racecar.apply_brakes()
print(racecar._current_speed)
print(racecar.nitro)
racecar.accelerate()
print(racecar._current_speed)
racecar.nitro
print(racecar.nitro)
car.sound_horn()


