def bilesik_anuite_donem_sonu_bugunku_deger(
    taksit,
    yillik_faiz_orani,
    yilda_odeme_sayisi,
    yil_sayisi
):
    """
    Ödeme periyodu ile faiz periyodu farklı olan
    dönem sonu ödemeli bileşik anüitenin bugünkü değerini hesaplar.

    Parametreler:
    taksit (float): Her ödeme döneminde yapılan ödeme tutarı
    yillik_faiz_orani (float): Yıllık nominal faiz oranı (ör. 0.12)
    yilda_odeme_sayisi (int): Yıldaki ödeme sayısı (ör. 12 = aylık)
    yil_sayisi (int): Toplam yıl sayısı
    """

    i = yillik_faiz_orani / yilda_odeme_sayisi
    n = yilda_odeme_sayisi * yil_sayisi

    return taksit * (1 - (1 + i) ** (-n)) / i
