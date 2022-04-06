import utils
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and utils.currency_rates(sys.argv[1]) is not None:
        print(str(utils.currency_rates(sys.argv[1])[0]) + " " + str(utils.currency_rates(sys.argv[1])[1]))
    else:
        print(None)
