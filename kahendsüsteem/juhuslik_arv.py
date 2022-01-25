from random import randint
from bitstring import BitArray

def juhuslik_arv(maximum: int) -> str:
    return BitArray(hex(randint(0,maximum))).bin

if __name__ == "__main__":
    while True:
        user_input = input('\nPalun, sisesta maximum täisarvu: ')
        if user_input == '0':
            break
        print(juhuslik_arv(int(user_input)))