def ertelenmis_anuite(A, i, n, d):
    toplam = 0
    for t in range(d + 1, d + n + 1):
        toplam += A / (1 + i) ** t
    return toplam


def artan_anuite(A, i, n, g):
    toplam = 0
    for t in range(1, n + 1):
        toplam += (A + (t - 1) * g) / (1 + i) ** t
    return toplam


def azalan_anuite(A, i, n, g):
    toplam = 0
    for t in range(1, n + 1):
        toplam += (A - (t - 1) * g) / (1 + i) ** t
    return toplam


def degisken_faizli_anuite(A, faiz_oranlari):
    toplam = 0
    carpim = 1
    for i in faiz_oranlari:
        carpim *= (1 + i)
        toplam += A / carpim
    return toplam
