# Döviz Kuru Tahmini
## Hakkında
Döviz Kuru Tahmini, geçmişteki döviz kuru verilerine dayanarak gelecekteki döviz kuru tahminlerini yapan bir grafiksel kullanıcı arayüzü (GUI) uygulamasıdır. Uygulama, ARIMA (Otomatik Regresif Entegre Hareketli Ortalama) modelini kullanarak tahminler yapar.

## Özellikler
CSV dosyasını seçme
Tarih sütunu ve döviz kuru sütunu isimlerini belirtme
Gelecekteki bir tarih için döviz kuru tahminini yapma
Tahmin edilen döviz kuru değerini gösterme
## Gereksinimler
```
Python 3.x
PyQt5 kütüphanesi
statsmodels kütüphanesi
pandas kütüphanesi
```
## Kullanım
Uygulamayı çalıştırın.
"CSV Dosyasını Seç" butonunu tıklatarak bir CSV dosyasını seçin.
Tarih sütunu ve döviz kuru sütunu isimlerini ilgili alanlara girin.
Gelecekteki bir tarih için döviz kuru tahminini yapın.
"Tahmin Et" butonunu tıklatarak tahmin edilen döviz kuru değerini görün.
## Not
CSV dosyasında tarih sütunu ve döviz kuru sütunu olmalıdır.
Tarih sütunu YYYY-MM-DD formatında olmalıdır.
Döviz kuru sütunu sayısal değerler olmalıdır.
Uygulama, günlük veri olarak kabul edilir ve eksik değerleri lineer interpolasyon ile doldurur.
## Lisans
Bu uygulama, MIT Lisansı altında lisanslanmıştır. Detaylı bilgi için LICENSE dosyasına bakın.
