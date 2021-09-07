class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("현재 차량의 속도는 {} Kph 입니다.".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':
    my_car = Car()
    print("차량에 연결되었습니다.")

    while True:
        action = input("[A] 가속 [B] 감속 [O] 주행거리 [S] 평균속도")

        if action not in "ABOS" or len(action) != 1:
            print("해당 멸영은 실행할 수 없습니다.")
            continue

        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("현재까지 주행거리 {}km 입니다.".format(my_car.odometer))
        elif action == 'S':
            print("평균속도 {}kph 입니다.".format(my_car.average_speed()))

        my_car.step()
        my_car.say_state()