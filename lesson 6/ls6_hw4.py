"""
Реализуйте базовый класс Car.
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool
        self.go()
        self.show_speed()
        self.turn()
        self.stop()

    def go(self):
        print(f'Машина "{self.color} {self.name}" поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        if self.is_police == True:
            print('Машина повернула направо')
        else:
            print('Машина повернула налево')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')
        max_town_speed = 60
        if self.speed > max_town_speed:
            print(f'Скорость превышена на {self.speed - max_town_speed} км/ч')

class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')
        max_work_speed = 40
        if self.speed > max_work_speed:
            print(f'Скорость превышена на {self.speed - max_work_speed} км/ч')

class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

lada = TownCar(80, 'Белая', 'Lada', True)
ferrari = SportCar(100, 'Желтый', 'Ferrari', False)
bmw = WorkCar(50, 'Черный', 'BMW', False)
ford = PoliceCar(70, 'Серебристый', 'Ford', True)