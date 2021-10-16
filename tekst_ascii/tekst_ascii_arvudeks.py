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


if __name__ == '__main__':
    print("Tõlkides antud 'näide.txt' -> 'väljund.txt':")
    print(tekst_ascii_arvudeks_failist('näide.txt', 'väljund.txt'))
    print('Kontrollides, et see töötab vastupidi ka. ')
    print(ascii_arvudest_tekstiks_failist('väljund.txt', 'tagasi.txt'))
    print(tekst_ascii_arvudeks(input('Palun, sisesta teksti muundamiseks: ')))
