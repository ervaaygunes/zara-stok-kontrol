# Zara Stok Takip Programı

Bu program, Zara web sitesindeki ürünlerin stok durumunu otomatik olarak kontrol eder ve ürün stoğa geldiğinde bildirim verir.

## Özellikler

- Zara ürün linki ile stok kontrolü
- Otomatik stok kontrolü (5 dakikada bir)
- Masaüstü bildirimleri
- Kullanıcı dostu arayüz
- Çoklu platform desteği (Windows, macOS, Linux)

## Kurulum ve Çalıştırma

Programı başka bir bilgisayarda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Proje Dosyalarını Kopyalama

`zara_stok_kontrol.py`, `requirements.txt` ve **manuel olarak indirdiğiniz `chromedriver` dosyasını** (bu dosyanın `zara_stok_kontrol.py` ile aynı klasörde olduğundan emin olun) yeni bilgisayarınızda istediğiniz bir klasöre aktarın.

### 2. Python Kurulumu

Yeni bilgisayarda Python 3.x yüklü değilse, [python.org](https://www.python.org/downloads/) adresinden indirip kurun. Kurulum sırasında "Add Python to PATH" veya benzeri bir seçeneği işaretlediğinizden emin olun.

### 3. ChromeDriver'ı İndirme (Manuel)

Tarayıcınızın sürümüne uygun ChromeDriver'ı manuel olarak indirmeniz gerekmektedir. Chrome tarayıcınızın sürümünü (Chrome > Yardım > Google Chrome Hakkında) kontrol edin ve aşağıdaki linkten uygun ChromeDriver sürümünü indirin:

- [ChromeDriver İndirme Sayfası](https://googlechromelabs.github.io/chrome-for-testing/)

İndirdiğiniz `.zip` dosyasını açın ve içinden çıkan `chromedriver` dosyasını proje klasörünüzün içine, `zara_stok_kontrol.py` dosyasının yanına kopyalayın.

### 4. Terminali Açın ve Proje Klasörüne Gidin

Terminali veya Komut İstemi'ni açın ve proje dosyalarını kopyaladığınız klasöre gidin. Örnek:

```bash
cd /Users/KullaniciAdi/Desktop/zara_stok_kontrol # macOS/Linux
# veya
cd C:\Users\KullaniciAdi\Desktop\zara_stok_kontrol # Windows
```

### 5. Sanal Ortam Oluşturma ve Aktifleştirme

Programın bağımlılıklarını izole etmek için bir sanal ortam oluşturun:

```bash
python3 -m venv venv
```
(Windows'ta `python -m venv venv` de işe yarayabilir.)

Sanal ortamı aktifleştirin:

*   **macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```
*   **Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
*   **Windows (Command Prompt):**
    ```cmd
    venv\Scripts\activate.bat
    ```
(Sanal ortam aktif olduğunda, terminal satırının başında `(venv)` yazısını göreceksiniz.)

### 6. Gerekli Kütüphaneleri Yükleme

Sanal ortam aktifken, `requirements.txt` dosyasındaki tüm kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

### 7. ChromeDriver'a Yürütülebilir İzin Verme (Sadece macOS/Linux)

macOS veya Linux kullanıyorsanız, indirdiğiniz `chromedriver` dosyasına çalıştırma izni vermeniz gerekebilir. Proje klasörünüzdeyken şu komutu çalıştırın:

```bash
chmod +x chromedriver
```

### 8. Programı Başlatma

Artık uygulamayı başlatmaya hazırsınız:

```bash
python zara_stok_kontrol.py
```

## Kullanım

1.  Açılan program arayüzüne Zara ürün linkini girin.
2.  "Stoğu Kontrol Et" butonuna tıklayın.
3.  İsterseniz "Otomatik kontrol" seçeneğini işaretleyerek, programın belirli aralıklarla stok kontrolü yapmasını sağlayabilirsiniz.

## Notlar

-   Program, tarayıcıyı varsayılan olarak görünmez (headless) modda kullanmaz. Tarayıcının açılmasını istemiyorsanız, `zara_stok_kontrol.py` dosyasındaki `chrome_options.add_argument("--headless")` satırının başındaki `#` işaretini kaldırabilirsiniz.
-   Stok durumu değiştiğinde masaüstü bildirimi alırsınız (Windows ve macOS'ta çalışır).
-   Otomatik kontrol seçeneği işaretliyse, program varsayılan olarak 5 dakikada bir kontrol yapar.

---
