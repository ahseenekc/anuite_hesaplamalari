# Anüite Hesaplamaları

## Geliştirici Hakkında
- **Ad Soyad:** Ahsen Ekici  
- **Üniversite:** Selçuk Üniversitesi  
- **İletişim:** ekiciahsenn@gmail.com  

---

## Proje Hakkında

### Amaç
- Anüite hesaplamalarını Python programlama dili ile gerçekleştirmek  
- Aktüeryal ve finans matematiği kavramlarını uygulamalı hale getirmek  

### Kapsam
- Dönem sonu ödemeli anüite hesaplamaları  
- Dönem başı ödemeli anüite hesaplamaları  
- Bileşik anüite (ödeme dönemi ≠ faiz dönemi) hesaplamaları  
- Ertelenmiş anüite hesaplamaları  
- Artan ve azalan anüite hesaplamaları  
- Değişken faizli anüite hesaplamaları  
- Nominal ve efektif faiz dönüşümleri  

---

## Kurulum / Çalıştırma Adımları

```bash
git clone https://github.com/kullanici_adi/anuite_hesaplamalari.git
cd anuite_hesaplamalari

---

## Örnek Kullanım
from anuite_hesaplamalari import (
    donem_sonu_anuite,
    donem_basi_anuite,
    bilesik_anuite,
    ertelenmis_anuite,
    nominalden_efektife
)

donem_sonu_anuite(1000, 0.10, 5)
donem_basi_anuite(1000, 0.10, 5)
bilesik_anuite(500, 0.12, 12, 4, 10)
ertelenmis_anuite(1000, 0.08, 5, 3)
nominalden_efektife(0.12, 12)

---
### Parametrelerin Anlamları

| Parametre | Açıklama |
|----------|----------|
| **A** | Her dönem yapılan ödeme tutarı |
| **i** | Dönemsel faiz oranı |
| **n** | Toplam ödeme dönemi sayısı |
| **m** | Yıldaki faizlendirme sayısı (nominal faiz için) |
| **k** | Yıldaki ödeme sayısı |
| **d** | Erteleme süresi (ödemenin başlamadığı dönem sayısı) |
| **g** | Dönemsel artış / azalış tutarı |
| **j** | Nominal faiz oranı |

