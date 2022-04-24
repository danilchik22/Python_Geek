import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color
        self.running()

    def running(self):
        while True:
            if self.__color == "красный":
                print("красный")
                time.sleep(7)
                self.__color = "жёлтый"
            elif self.__color == "жёлтый":
                print("жёлтый")
                time.sleep(2)
                self.__color = "зелёный"
            elif self.__color == "зелёный":
                print("зелёный")
                time.sleep(15)
                self.__color = "жёлтый"


if __name__ == "__main__":
    tr = TrafficLight("красный")