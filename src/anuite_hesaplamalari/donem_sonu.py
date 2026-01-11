def donem_sonu_anuite_bugunku_deger(taksit, faiz_orani, donem_sayisi):
    """
    Dönem sonu ödemeli (ordinary annuity) anüitenin bugünkü değerini hesaplar.

    Parametreler:
    taksit (float): Her dönem ödenen tutar
    faiz_orani (float): Dönemlik faiz oranı (ör. 0.05)
    donem_sayisi (int): Toplam dönem sayısı
    """
    return taksit * (1 - (1 + faiz_orani) ** (-donem_sayisi)) / faiz_orani