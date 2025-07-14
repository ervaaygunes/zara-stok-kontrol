import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager # Bu satırı yorum satırı yapıyoruz veya siliyoruz
# from plyer import notification # Bu satırı yorum satırı yapıyoruz veya siliyoruz
import time
import threading
import json

# ChromeDriver dosyasının yolu
CHROMEDRIVER_PATH = "./chromedriver" # chromedriver dosyasını bu klasöre attığınızdan emin olun

class ZaraStokKontrol:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Zara Stok Takip Programı")
        self.pencere.geometry("500x300")
        
        # Ana frame
        self.ana_frame = ttk.Frame(self.pencere, padding="10")
        self.ana_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # URL girişi
        ttk.Label(self.ana_frame, text="Zara Ürün Linki:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.url_giris = ttk.Entry(self.ana_frame, width=50)
        self.url_giris.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Beden girişi
        ttk.Label(self.ana_frame, text="Beden (Numara): ").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.beden_giris = ttk.Entry(self.ana_frame, width=10)
        self.beden_giris.grid(row=2, column=1, sticky=(tk.W), pady=5)
        
        # Kontrol butonu
        self.kontrol_buton = ttk.Button(self.ana_frame, text="Stoğu Kontrol Et", command=self.stok_kontrol_baslat)
        self.kontrol_buton.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Sonuç etiketi
        self.sonuc_etiketi = ttk.Label(self.ana_frame, text="Sonuç: Henüz kontrol edilmedi")
        self.sonuc_etiketi.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Son kontrol zamanı
        self.son_kontrol_etiketi = ttk.Label(self.ana_frame, text="Son kontrol: -")
        self.son_kontrol_etiketi.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Otomatik kontrol
        self.otomatik_kontrol_var = tk.BooleanVar()
        self.otomatik_kontrol_check = ttk.Checkbutton(
            self.ana_frame, 
            text="Otomatik kontrol (5 dakikada bir)", 
            variable=self.otomatik_kontrol_var
        )
        self.otomatik_kontrol_check.grid(row=6, column=0, columnspan=2, pady=5)
        
        self.kontrol_thread = None
        self.calisiyor = False

    def stok_kontrol(self):
        try:
            chrome_options = Options()
            # chrome_options.add_argument("--headless")  # Görünmez modda çalıştır
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            service = Service(CHROMEDRIVER_PATH)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            url = self.url_giris.get()
            beden = self.beden_giris.get().strip() # Beden bilgisini al ve boşlukları temizle

            if not url:
                messagebox.showerror("Hata", "Lütfen bir ürün linki girin.")
                self.calisiyor = False
                return
            if not beden:
                messagebox.showerror("Hata", "Lütfen kontrol etmek istediğiniz bedeni girin.")
                self.calisiyor = False
                return

            driver.get(url)
            
            # Sayfanın yüklenmesini bekle (genel bir element bekleyebiliriz)
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "script")) # Sayfadaki script etiketlerinin yüklenmesini bekleyelim
            )
            
            stok_var = False
            try:
                # JSON-LD verilerini içeren script etiketini bul
                script_elements = driver.find_elements(By.XPATH, "//script[@type='application/ld+json']")
                product_data = None

                for script_element in script_elements:
                    script_content = script_element.get_attribute("innerHTML")
                    # JSON-LD içeriğini kontrol etmek için daha basit bir string karşılaştırması
                    if "Product" in script_content and "https://schema.org/" in script_content:
                        try:
                            product_data = json.loads(script_content)
                            if isinstance(product_data, list):
                                break # Eğer liste ise doğru veriyi bulduk
                            else:
                                product_data = None # Eğer tek bir ürünse, diğer scriptleri kontrol et
                        except json.JSONDecodeError:
                            continue
                
                if not product_data:
                    self.sonuc_etiketi.config(text="Sonuç: Ürün verisi bulunamadı.")
                    self.calisiyor = False
                    driver.quit()
                    return

                # Belirtilen beden için stok durumunu kontrol et
                beden_bulundu = False
                for item in product_data:
                    if item.get("@type") == "Product" and str(item.get("size")).lower() == beden.lower():
                        beden_bulundu = True
                        if item.get("offers") and item["offers"].get("availability") == "https://schema.org/InStock":
                            stok_var = True
                            break
                
                if not beden_bulundu:
                    self.sonuc_etiketi.config(text=f"Sonuç: Belirtilen beden ({beden}) bulunamadı. Lütfen bedeni doğru girdiğinizden emin olun.")
                elif stok_var:
                    self.sonuc_etiketi.config(text=f"Sonuç: {beden} numara stokta var ✅")
                    messagebox.showinfo("Zara Stok Bildirimi", f"Ürün {beden} numara stoğa geldi! Hemen kontrol edin.")
                else:
                    self.sonuc_etiketi.config(text=f"Sonuç: {beden} numara stokta yok ❌")

            except Exception as e:
                self.sonuc_etiketi.config(text=f"Sonuç: Stok durumu kontrol edilemedi. Hata: {str(e)}")
            
            driver.quit()
            
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")
            self.sonuc_etiketi.config(text="Sonuç: Hata oluştu")
        
        finally:
            self.son_kontrol_etiketi.config(text=f"Son kontrol: {time.strftime('%d.%m.%Y - %H:%M')}")
            self.calisiyor = False

    def stok_kontrol_baslat(self):
        if not self.calisiyor:
            self.calisiyor = True
            self.kontrol_thread = threading.Thread(target=self.stok_kontrol)
            self.kontrol_thread.start()
            
            if self.otomatik_kontrol_var.get():
                self.otomatik_kontrol_baslat()

    def otomatik_kontrol_baslat(self):
        if self.otomatik_kontrol_var.get() and not self.calisiyor:
            self.stok_kontrol_baslat()
            self.pencere.after(300000, self.otomatik_kontrol_baslat)  # 5 dakika = 300000 ms

    def baslat(self):
        self.pencere.mainloop()

if __name__ == "__main__":
    uygulama = ZaraStokKontrol()
    uygulama.baslat() 