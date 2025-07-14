Proje Adı:
Zara Dinamik Ürün Stok Takip Programı (Selenium Tabanlı)

1. 🔍 Problem Tanımı
Zara’nın web sitesi dinamik olarak çalıştığı için, kullanıcılar almak istedikleri ürünün stok durumunu elle sık sık kontrol etmek zorunda kalıyor. Özellikle çok çabuk tükenen popüler ürünler için bu işlem zahmetli. Kullanıcıların istedikleri ürünü kolayca takip etmelerini sağlayacak, otomatik stok kontrolü yapan ve uyarı veren bir programa ihtiyaç vardır.

2. 🎯 Ürün Hedefi
Zara’daki belirli bir ürünün stok durumunu dinamik olarak kontrol eden, tarayıcı üzerinden sayfayı yükleyip stok bilgisini okuyan ve stoğa geldiğinde kullanıcıya uyarı veren basit bir masaüstü uygulama geliştirmek.

3. 👥 Hedef Kitle
	•	Zara’dan sıklıkla alışveriş yapan kullanıcılar
	•	Tükenen ürünleri yeniden almak isteyenler
	•	Otomatik bildirim sistemine ihtiyaç duyan alışveriş tutkunları

4. 🧩 Özellik Listesi
✅ Minimum Özellikler (MVP)
	•	Kullanıcıdan ürün URL’si alma
	•	Selenium ile sayfayı dinamik olarak açma
	•	Sayfada stok bilgisine göre karar verme
	•	Stok varsa: bildirim gösterme (popup, sesli uyarı)
	•	Basit bir arayüz (Tkinter)
	•	Hata durumlarında kullanıcıya açıklama gösterme
🆕 Gelişmiş Özellikler (Opsiyonel)
	•	Belirli aralıklarla arka planda otomatik kontrol
	•	E-posta veya masaüstü bildirimi
	•	Birden fazla ürün için takip desteği
	•	Selenium işlemini sessiz (headless) modda çalıştırma

5. 🖥️ Teknik Gereksinimler
Bileşen
Açıklama
Programlama Dili
Python 3.x
Arayüz
Tkinter
Web Kontrol
Selenium (ChromeDriver veya EdgeDriver ile)
Bildirim
tkinter.messagebox veya playsound
Bağımlılıklar
selenium, tkinter, time, os


6. ⚙️ Gereken Kurulumlar
	•	Python 3
	•	pip install selenium
	•	ChromeDriver ya da EdgeDriver indirilmeli ve çalıştırılabilir klasöre eklenmeli
	•	Tkinter (Python ile hazır gelir)

7. 🖼️ Arayüz Tasarımı (Wireframe)
text
KopyalaDüzenle
+---------------------------------------------+
| Zara Stok Takip Programı                    |
+---------------------------------------------+
| [ Zara Ürün Linki: _____________________ ]  |
|                                             |
| [ Stoğu Kontrol Et ]                        |
|                                             |
| Sonuç: [Stokta yok ❌ / Stokta var ✅ ]      |
|                                             |
| Son kontrol: [07.06.2025 - 14:38]           |
+---------------------------------------------+

8. 🔄 Çalışma Akışı
	1	Kullanıcı programı başlatır
	2	Zara ürün linkini girer
	3	“Stoğu Kontrol Et” butonuna basar
	4	Selenium, Chrome veya Edge ile sayfayı açar
	5	Sayfa içeriği yüklenince, "Tükendi" veya "Stokta" gibi metin aranır
	6	Sonuca göre kullanıcıya popup bildirim gösterilir
	7	Kullanıcı isterse işlemi tekrarlayabilir


9. 📈 Başarı Kriterleri
	•	Kullanıcı doğru ürün linkini girdiğinde, sistem stok bilgisini düzgün analiz edebilmeli ✅
	•	Stok geldiğinde kullanıcıya bildirim gösterilmeli ✅
	•	Uygulama çökmeden, kullanıcı dostu arayüzle çalışmalı ✅
	•	Zara sayfa yapısı değiştiğinde kolay güncellenebilir olmalı ⚙️
