def _decor_calc(validation):
    def decor_calc(funct):
        def wrapper(*args):
            validation(args)
            return funct(*args)

        return wrapper

    return decor_calc


def validation(args):
    if len(args) > 1 or args[0] < 0:
        raise ValueError()


@_decor_calc(validation)
def calc_cube(x):
    return x ** 3


print(calc_cube(9))