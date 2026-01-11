from .donem_sonu import donem_sonu_anuite_bugunku_deger


def donem_basi_anuite_bugunku_deger(taksit, faiz_orani, donem_sayisi):
    """
    Dönem başı ödemeli (annuity due) anüitenin bugünkü değerini hesaplar.

    Parametreler:
    taksit (float): Her dönem ödenen tutar
    faiz_orani (float): Dönemlik faiz oranı
    donem_sayisi (int): Toplam dönem sayısı
    """
    return donem_sonu_anuite_bugunku_deger(
        taksit, faiz_orani, donem_sayisi
    ) * (1 + faiz_orani)