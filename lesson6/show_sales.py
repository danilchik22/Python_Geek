import sys
from itertools import islice

with open("bakery.csv", "r", encoding="utf-8") as f:
    if len(sys.argv) == 1:
        list_records = [el.strip() for el in list(f.readlines())]
    elif len(sys.argv) == 3:
        list_records = [el.strip() for el in list(islice(f, int(sys.argv[1])-1, int(sys.argv[2])))]
    elif len(sys.argv) == 2:
        list_records = [el.strip() for el in list(islice(f, int(sys.argv[1]) - 1, None))]
    for record in list_records:
        print(record)