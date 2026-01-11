from src.anuite_hesaplamalari import (
    donem_sonu_anuite_bugunku_deger,
    donem_basi_anuite_bugunku_deger,
    bilesik_anuite_donem_sonu_bugunku_deger,
    surekli_anuite_bugunku_deger
)


def test_anuite_fonksiyonlari():
    assert donem_sonu_anuite_bugunku_deger(1000, 0.05, 10) > 0
    assert donem_basi_anuite_bugunku_deger(1000, 0.05, 10) > 0
    assert bilesik_anuite_donem_sonu_bugunku_deger(1000, 0.12, 12, 5) > 0
    assert surekli_anuite_bugunku_deger(1000, 0.05) > 0
