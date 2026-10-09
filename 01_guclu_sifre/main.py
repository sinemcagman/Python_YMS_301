import string


def parola_kontrol_et(parola):
    puan = 0

    if len(parola) >= 8:
        puan += 1

    buyuk_var = False
    kucuk_var = False
    rakam_eklendi = False
    ozel_eklendi = False

    for karakter in parola:
        if karakter.isupper():
            buyuk_var = True
        elif karakter.islower():
            kucuk_var = True
        elif karakter.isdigit() and not rakam_eklendi:
            puan += 1
            rakam_eklendi = True
        elif karakter in string.punctuation and not ozel_eklendi:
            puan += 1
            ozel_eklendi = True

    if buyuk_var and kucuk_var:
        puan += 1

    if puan <= 1:
        durum = "ZAYIF"
    elif puan <= 3:
        durum = "ORTA"
    else:
        durum = "GÜÇLÜ"

    return puan, durum 


test_parolasi = input("Lütfen test etmek istediğiniz parolayı girin: ")
puan, durum = parola_kontrol_et(test_parolasi)

print(f"Puan: {puan}/4")
print(f"Parola Gücü: {durum}")