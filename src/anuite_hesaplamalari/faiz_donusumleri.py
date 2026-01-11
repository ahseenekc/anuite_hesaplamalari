def nominalden_efektife(j, m):
    if j <= 0 or m <= 0:
        raise ValueError("Faiz oranı ve dönem sayısı pozitif olmalıdır")
    return (1 + j / m) ** m - 1


def efektiften_nominale(i, m):
    if i <= 0 or m <= 0:
        raise ValueError("Faiz oranı ve dönem sayısı pozitif olmalıdır")
    return m * ((1 + i) ** (1 / m) - 1)
