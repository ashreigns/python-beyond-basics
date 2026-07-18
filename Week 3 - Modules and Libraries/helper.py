def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def palindrom_mu(metin):
    temiz_metin = metin.lower().replace(" ", "")
    return temiz_metin == temiz_metin[::-1]

def ebob_bul(a, b):
    while b:
        a, b = b, a % b
    return a
def ekok_bul(a, b):
    return int((a * b) / ebob_bul(a, b))
