import os
import random
import time
from jõulusõim import jõulusõim


def main():
    KÕRGUS = 24#os.get_terminal_size()[1]
    LAIUS = 80#os.get_terminal_size()[0]
    TIHEDUS = 10
    UUENDAMIS_AEG = 0.3

    clear = "cls"
    if os.name == "posix":
        clear = "clear"

    os.system(clear)

    lumehelves = []
    while True:
        ekraan = [' ']*(KÕRGUS*LAIUS) # [' ' for _ in range(KÕRGUS*LAIUS)]
        for _ in range(TIHEDUS):
            lumehelves.append([random.randint(0, LAIUS-1), 0])
        if lumehelves[0][1] >= KÕRGUS:
            lumehelves = lumehelves[TIHEDUS:]
        for i in range(len(lumehelves)):
            ekraan[lumehelves[i][0]+lumehelves[i][1]*LAIUS] = '❄️'
            lumehelves[i][1] += 1

        os.system(clear)
        tulemus = ''
        for index, char in enumerate(ekraan):
            if index % LAIUS == 0:
                tulemus += '\n'
            else:
                tulemus += char
        print(tulemus)
        time.sleep(UUENDAMIS_AEG)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(jõulusõim)
