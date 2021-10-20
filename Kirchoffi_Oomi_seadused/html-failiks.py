import os

fn = 'Kirchoff_Oomi_seadused'


def main():
    import markdown

    with open(fn + '.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open(fn + '.html', 'w') as f:
        f.write(html)


try:
    main()
    print(fn + ' õigesti genereeritud')
except ModuleNotFoundError:
    command = 'pip install markdown --user'
    print('===== VIGA =====')
    print('Sul puudub markdown teeke.')
    print('\t' + command)
    kasutaja_sisend = input('Kas tahad installida markdown teeke? (jah/ei)')
    while True:
        if kasutaja_sisend == 'jah':
            os.system(command)
            kasutaja_sisend = input(
                "\nKas käivitan skripti uuesti?(loobumiseks sisesta '0')")
            if kasutaja_sisend == '0':
                pass
            else:
                print('Käivitan uuesti')
                os.system("python html-failiks.py")
            break
        elif kasutaja_sisend == 'ei':
            print('Kui see ei tööta, saad käsitsi teha' +
                  'Sa saad installida kasutades:' + command)
            break
        else:
            print("Palun, kirjuta 'Jah' või 'ei'")
