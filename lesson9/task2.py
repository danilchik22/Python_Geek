class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def quantity(self, weight_asfh_1cm, quan_cm):
        return self._length * self._width * weight_asfh_1cm * quan_cm


if __name__ == "__main__":
    while True:
        weight_asfh = input("Введите количество кг асфальта требуемого на 1 кв.см:  ")
        quan_cm = input("Введите количество сантиметров толщины полотна:  ")
        try:
            weight_asfh = float(weight_asfh)
            quan_cm = float(quan_cm)
            break
        except:
            print("Вводить можно только числа. Попробуйте еще раз.")
    road1 = Road(20, 5000)
    quan = road1.quantity(weight_asfh, quan_cm)
    if quan > 1000:
        print(f"{quan/1000} тонн")
    else:
        print(f"{quan} кг")
