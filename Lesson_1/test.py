class Robot:
    def __init__(self, e):
        self.energy = e

    def say_energy(self):
        print (u"Осталось {0} энергии".format(self.energy))


class RobotSpamer(Robot):
    def activate(self):
        if self.energy != 0:
            print("Spam" * 1000)
            print(u"Я заспамил весь экран!")
            self.energy -= 1
        else:
            print(u"Моя энергия равна нулю и я не могу выполнить это действие!")


class RobotSpamerToActivate(RobotSpamer):
    activated = False  # Изначально робот выключен

    def power_on(self):
        self.activated = True

    def power_off(self):
        self.activated = False

    # Методы включения и выключения робота
    def activate(self):
        if not self.activated:  # Если робот выключен
            print(u"Я выключен и не могу выполнить это действие!")
        else:
            super(RobotSpamerToActivate, self).activate()


spamer = RobotSpamerToActivate(2)
dir(spamer)
spamer.activate()
spamer.power_on()
spamer.activate()
spamer.activate()
spamer.activate()
