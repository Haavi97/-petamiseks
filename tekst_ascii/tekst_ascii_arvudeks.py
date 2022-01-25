def tekst_ascii_arvudeks(tekst: str) -> str:
    return ' '.join(map(lambda x: str(ord(x)), tekst))


def ascii_arvudest_tekstiks(tekst: str) -> str:
    return ''.join(map(lambda x: chr(int(x)), tekst.split(' ')))


def tekst_ascii_arvudeks_failist(fn: str, fout: str) -> str:
    with open(fn, 'r') as f:
        output = tekst_ascii_arvudeks(f.read())
    with open(fout, 'w') as f:
        f.write(output)
    return output


def ascii_arvudest_tekstiks_failist(fn: str, fout: str) -> str:
    with open(fn, 'r') as f:
        output = ascii_arvudest_tekstiks(f.read())
    with open(fout, 'w') as f:
        f.write(output)
    return output


def display_menu() -> None:
    print('Vali mida tegema:')
    print('\t1. Arvust tekstiks.')
    print('\t2. Tekstist arvuks.')
    print('\t3. Arvust tekstiks. Failid')
    print('\t4. Tekstist arvuks. Failid')
    print('\t5. Vaikimisi. Näide\n')
    print('\t0, q või exit lõpetamiseks.\n')


if __name__ == '__main__':
    while True:
        display_menu()
        user_input = input()
        if user_input in ['0', 'q', 'exit']:
            break
        elif user_input == '1':
            print(ascii_arvudest_tekstiks(input('Palun, sisesta sõne: ')))
        elif user_input == '2':
            print(tekst_ascii_arvudeks(input('Palun, sisesta sõne: ')))
        elif user_input == '3':
            print(ascii_arvudest_tekstiks_failist(
                input('Palun, sisesta sisend faili: '), 'väljund.txt'))
        elif user_input == '4':
            print(tekst_ascii_arvudeks_failist(
                input('Palun, sisesta sisend faili: '), 'väljund.txt'))
        elif user_input == '5':
            print(tekst_ascii_arvudeks_failist(
                'näide.txt', 'väljund.txt'))
        else:
            print('Palun, sisestage õiget valikud.')
