import sys
with open("bakery.csv", "r+", encoding="utf-8") as f:
    startFromLine = int(sys.argv[1])
    linesCounter = 1
    len_lines = 0
    flag = True
    for line in f:
        if linesCounter == startFromLine:
            if linesCounter == 1:
                f.seek(0)
                f.write(sys.argv[2])
                flag = False
                break
            else:
                f.seek(len_lines + 2)
                f.write(sys.argv[2])
                flag = False
                break
        linesCounter += 1
        len_lines += len(line)
    if flag is True:
        print("Такой записи не существует")
