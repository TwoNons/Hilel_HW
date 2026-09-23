class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            print(f"Сторона ромба повинна бути більше 0. Введiть iнше число")
            self.side_a = int(input())
            return
        super().__setattr__(name, value)
        if name == "angle_a":
            self.angle_b = 180 - value

romb = Rhombus(5, 90)
print(romb.side_a)
print(romb.angle_a)
print(romb.angle_b)