def caesari_siffreri(sõne: str, nihe: int) -> str:
    """
    See script nihutab kõik olemas teksti tähed mis on 
    ASCII tabelis 65->90 ehk siis A-Z. See eirab kõik 
    arvud mis pole selles vahemikus
    """
    return ''.join(map(lambda ta: chr(65 + (ta+nihe-65) % (91-65)),
                   filter(lambda ta: 64 < ta < 91,
                          map(lambda t: ord(t),
                              sõne.upper()))))


def caesari_desiffreri(sõne: str, nihe: int) -> str:
    """
    See script nihutab kõik olemas teksti tähed mis on 
    ASCII tabelis 65->90 ehk siis A-Z. See eirab kõik 
    arvud mis pole selles vahemikus
    """
    return ''.join(map(lambda ta: chr(65 + (ta-nihe-65+(91-65)) % (91-65)),
                   filter(lambda ta: 64 < ta < 91,
                          map(lambda t: ord(t),
                              sõne.upper()))))


def caesari_siffreri_lihtsustatud(sõne, nihe):
    """
    Lihtsam variant õpilastega jagama. 
    See script nihutab kõik olemas teksti tähed mis on 
    ASCII tabelis 65->90 ehk siis A-Z. See eirab kõik 
    arvud mis pole selles vahemikus
    """
    # muudame sõne nii, et oleks ainult suurte tähtedega.
    sõne = sõne.upper()
    # Arvutame tema ASCII tabeli kümnendsüsteemi arvud:
    sõne_arvud = []
    for tähe in sõne:
        tähe_arv = ord(tähe)
        # Filtreerime kas on vahemikus 65-90
        if 64 < tähe_arv < 91:
            sõne_arvud.append(tähe_arv)
    # Nihutame kõik arvud "nihe" võrra:
    nihutatud_arvud = []
    for tähe_arv in sõne_arvud:
        nihutatud = tähe_arv + nihe
        # Kui on üle 90 siis tuleb arvutada kui palju on
        # lisa ning alustada A-st, ehk siis 65
        if nihutatud > 90:
            nihutatud = (nihutatud - 91) + 65
        nihutatud_arvud.append(nihutatud)
    # Siis muundame tagasi arvudest tähtedesse
    sifreeritud_sõne = ''
    for nihutatud in nihutatud_arvud:
        sifreeritud_sõne += chr(nihutatud)

    # Tagastame sifreeritud sõne
    return sifreeritud_sõne


def display_menu() -> None:
    print('Vali mida tegema:')
    print('\t1. Šifreeri teksti.')
    print('\t2. Dešifreeri teksti.')
    print('\t0, q või exit lõpetamiseks.\n')


if __name__ == "__main__":
    try:
        while True:
            display_menu()
            kasutaja_sisend = input()
            if kasutaja_sisend in ['0', 'q', 'exit']:
                break
            elif kasutaja_sisend == '1':
                kasutaja_sisend = input(
                    '\nPalun, sisesta teksti šifreerimiseks (tähed A-Z): ')
                kasutaja_nihe = input(
                    '\nPalun, sisesta nihe šifreerimiseks (täisarv): ')
                print(caesari_siffreri(kasutaja_sisend, int(kasutaja_nihe)))
                print(caesari_siffreri_lihtsustatud(
                    kasutaja_sisend, int(kasutaja_nihe)))
            elif kasutaja_sisend == '2':            
                kasutaja_sisend = input(
                    '\nPalun, sisesta teksti dešifreerimiseks (tähed A-Z): ')
                kasutaja_nihe = input(
                    '\nPalun, sisesta nihe šifreerimiseks (täisarv): ')
                if kasutaja_sisend == '0':
                    break
                print(caesari_desiffreri(kasutaja_sisend, int(kasutaja_nihe)))
            else:
                print('Palun, sisestage õiget valikud.')
    except:
        print('Tõenäoliselt vale sisend. Tšau...')
