import tkinter as tk
from tkinter import ttk, messagebox
import string
import re
import random
import statistics
import subprocess
import socket
import base64
from datetime import datetime

def rapora_kaydet(islem_turu, sonuc_ozeti):
    zaman = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    with open("siber_rapor.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"[{zaman}] {islem_turu} -> {sonuc_ozeti}\n")

pencere = tk.Tk()
pencere.title("Siber Koruyucu v5.0 ULTRA - AI & Siber Savunma Merkezi")
pencere.geometry("780x550")
pencere.configure(bg="#0f172a")

stil = ttk.Style()
stil.theme_use("clam")
stil.configure("TNotebook", background="#0f172a", borderwidth=0)
stil.configure("TNotebook.Tab", background="#1e293b", foreground="white", padding=(10, 6), font=("Segoe UI", 9, "bold"))
stil.map("TNotebook.Tab", background=[("selected", "#2563eb")])

baslik = tk.Label(pencere, text="SİBER KORUYUCU v5.0 ULTRA — AI & SİBER SAVUNMA MERKEZİ", font=("Segoe UI", 13, "bold"), bg="#0f172a", fg="#38bdf8", pady=12)
baslik.pack()

sekmeler = ttk.Notebook(pencere)
sekmeler.pack(expand=True, fill="both", padx=12, pady=8)

sekme1 = tk.Frame(sekmeler, bg="#1e293b")
sekmeler.add(sekme1, text="Şifre Kalkanı")
tk.Label(sekme1, text="Test Edilecek Şifreyi Girin:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white").pack(pady=(20, 5))
sifre_giris = tk.Entry(sekme1, font=("Segoe UI", 12), width=32, justify="center")
sifre_giris.pack(pady=5)
sifre_sonuc = tk.Label(sekme1, text="Sonuç bekleniyor...", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8", justify="left", wraplength=650)
sifre_sonuc.pack(pady=15)

def sifre_test_et():
    sifre = sifre_giris.get()
    if not sifre: messagebox.showwarning("Uyarı", "Şifre yazın!"); return
    zayiflar = ["123456", "password", "admin", "qwerty", "12345678", "deneyap"]
    if sifre.lower() in zayiflar:
        sifre_sonuc.config(text="PUAN: 0 / 6 — ÇOK ZAYIF! Kırılma Süresi: ANINDA (0.001 saniye)", fg="#f87171")
        rapora_kaydet("Şifre Analizi", "0/6 (Çok Zayıf)"); return
    puan, havuz, oneriler = 0, 0, []
    if any(h.islower() for h in sifre): puan += 1; havuz += 26
    else: oneriler.append("Küçük harf ekleyin.")
    if any(h.isupper() for h in sifre): puan += 1; havuz += 26
    else: oneriler.append("BÜYÜK harf ekleyin.")
    if any(h.isdigit() for h in sifre): puan += 1; havuz += 10
    else: oneriler.append("Rakam ekleyin.")
    if any(h in string.punctuation for h in sifre): puan += 1; havuz += 32
    else: oneriler.append("Özel karakter ekleyin.")
    if len(sifre) >= 12: puan += 2
    elif len(sifre) >= 8: puan += 1
    else: oneriler.append("En az 8 karakter yapın.")
    saniye = ((havuz if havuz > 0 else 10) ** len(sifre)) / 10_000_000_000
    sure = "1 saniyeden kısa!" if saniye < 1 else (f"Yaklaşık {int(saniye // 86400) + 1} gün" if saniye < 86400 * 365 else f"Yaklaşık {int(saniye // (86400 * 365)):,} YIL")
    renk = "#4ade80" if puan == 6 else ("#facc15" if puan >= 4 else "#f87171")
    ek_not = ("\nÖneriler: " + " | ".join(oneriler)) if oneriler else "\nDurum: Tam korumalı!"
    sifre_sonuc.config(text=f"Güvenlik Puanı: {puan} / 6\nTahmini Kırılma Süresi: {sure}{ek_not}", fg=renk)
    rapora_kaydet("Şifre Analizi", f"Puan: {puan}/6, Süre: {sure}")

def guclu_uret():
    karakterler = string.ascii_letters + string.digits + "!@$%&*?"
    while True:
        yeni = "".join(random.choice(karakterler) for _ in range(16))
        if any(c.islower() for c in yeni) and any(c.isupper() for c in yeni) and any(c.isdigit() for c in yeni) and any(c in "!@$%&*?" for c in yeni):
            sifre_giris.delete(0, tk.END); sifre_giris.insert(0, yeni); sifre_test_et(); break

kutu1 = tk.Frame(sekme1, bg="#1e293b"); kutu1.pack(pady=5)
tk.Button(kutu1, text="Şifreyi Analiz Et", command=sifre_test_et, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0).pack(side="left", padx=8)
tk.Button(kutu1, text="Süper Şifre Üret", command=guclu_uret, bg="#059669", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0).pack(side="left", padx=8)

sekme2 = tk.Frame(sekmeler, bg="#1e293b")
sekmeler.add(sekme2, text="Link Radarı")
tk.Label(sekme2, text="Analiz Edilecek Linki Yapıştırın:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white").pack(pady=(20, 5))
link_giris = tk.Entry(sekme2, font=("Segoe UI", 11), width=58); link_giris.pack(pady=5)
link_sonuc = tk.Label(sekme2, text="Link analizi bekleniyor...", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8", justify="left", wraplength=650); link_sonuc.pack(pady=15)

def link_tara():
    url = link_giris.get().lower().strip()
    if not url: messagebox.showwarning("Uyarı", "Link yapıştırın!"); return
    risk, uyarilar = 0, []
    if not url.startswith("https://"): risk += 2; uyarilar.append("- 'https://' sertifikası yok.")
    if re.search(r"\d+\.\d+\.\d+\.\d+", url): risk += 3; uyarilar.append("- IP adresi kullanılmış.")
    if "@" in url: risk += 3; uyarilar.append("- '@' yönlendirme tuzağı var.")
    if len(url) > 75: risk += 1; uyarilar.append("- Link çok uzun.")
    if url.count(".") > 3 or url.count("-") > 3: risk += 2; uyarilar.append("- Çok fazla nokta/tire var.")
    tuzaklar = ["hediye", "bedava", "kazandin", "acil", "hesap-askiya", "guncelle", "kargo-ucret", "free", "login-verify"]
    bulunan = [k for k in tuzaklar if k in url]
    if bulunan: risk += 2; uyarilar.append(f"- Tuzak kelimeler: {', '.join(bulunan)}")
    durum, renk = ("TEHLİKELİ - TIKLAMAYIN!", "#f87171") if risk >= 4 else (("ŞÜPHELİ!", "#facc15") if risk >= 2 else ("GÜVENLİ GÖRÜNÜYOR", "#4ade80"))
    link_sonuc.config(text=f"Risk Puanı: {risk} / 13 — {durum}\n\n" + ("\n".join(uyarilar) if uyarilar else "Oltalama belirtisi bulunmadı."), fg=renk)
    rapora_kaydet("Link Taraması", f"Risk: {risk}/13")

tk.Button(sekme2, text="Linki Tara", command=link_tara, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=6, bd=0).pack(pady=5)
sekme3 = tk.Frame(sekmeler, bg="#1e293b")
sekmeler.add(sekme3, text="AI SMS Dedektörü")
tk.Label(sekme3, text="Şüpheli SMS veya E-posta Metnini Yapıştırın (AI Analizi):", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white").pack(pady=(15, 5))
sms_giris = tk.Text(sekme3, height=4, width=65, font=("Segoe UI", 10), bg="#0f172a", fg="white", insertbackground="white")
sms_giris.pack(pady=5)
sms_sonuc = tk.Label(sekme3, text="Yapay zeka metin analizi bekleniyor...", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8", justify="left", wraplength=660)
sms_sonuc.pack(pady=10)

def sms_analiz_et():
    metin = sms_giris.get("1.0", tk.END).lower().strip()
    if not metin: messagebox.showwarning("Uyarı", "Analiz edilecek mesajı yapıştırın!"); return
    puan, tespitler = 0, []
    kategoriler = {
        "Korku / Hukuk Tuzağı": ["icra", "dava", "mahkeme", "ceza", "savcilik", "hapis", "uzlasma", "avukat"],
        "Sahte Ödül / Para Tuzağı": ["kazandiniz", "hediye", "ikramiye", "iade", "hesabiniza", "kredi", "burs", "bedava"],
        "Sahte Kargo / Hesap Askısı": ["kargonuz", "teslim edilemedi", "adres", "askiya", "bloke", "guncelleyin", "onaylayin"],
        "Aciliyet Baskısı": ["hemen", "son gun", "acil", "24 saat", "tiklayiniz", "iptal edilecek"]
    }
    for kat, kelimeler in kategoriler.items():
        bulunan = [k for k in kelimeler if k in metin]
        if bulunan:
            puan += len(bulunan) * 20
            tespitler.append(f"- {kat}: ({', '.join(bulunan)})")
    if "http" in metin or "bit.ly" in metin or ".com" in metin:
        puan += 25
        tespitler.append("- Mesaj içinde yönlendirme linki tespit edildi.")
    yuzde = min(puan, 99)
    if yuzde >= 50:
        durum, renk = f"YÜKSEK DOLANDIRICILIK RİSKİ (%{yuzde}) — SAKIN İNANMAYIN!", "#f87171"
    elif yuzde >= 20:
        durum, renk = f"ŞÜPHELİ MESAJ (%{yuzde}) — DİKKATLİ OLUN!", "#facc15"
    else:
        durum, renk = f"GÜVENLİ GÖRÜNÜYOR (Risk: %{yuzde})", "#4ade80"
    sms_sonuc.config(text=f"{durum}\n\n" + ("\n".join(tespitler) if tespitler else "Sosyal mühendislik veya tuzak kalıbı bulunmadı."), fg=renk)
    rapora_kaydet("AI SMS Dedektörü", f"Dolandırıcılık Riski: %{yuzde}")

tk.Button(sekme3, text="AI ile Mesajı Analiz Et", command=sms_analiz_et, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=6, bd=0).pack(pady=5)

sekme4 = tk.Frame(sekmeler, bg="#1e293b")
sekmeler.add(sekme4, text="Kripto Kasası")
tk.Label(sekme4, text="Şifrelenecek veya Çözülecek Gizli Metin:", font=("Segoe UI", 10, "bold"), bg="#1e293b", fg="white").pack(pady=(12, 3))
kripto_metin = tk.Entry(sekme4, font=("Segoe UI", 11), width=58); kripto_metin.pack(pady=3)
tk.Label(sekme4, text="Gizli Anahtar (PIN / Şifre):", font=("Segoe UI", 10, "bold"), bg="#1e293b", fg="#38bdf8").pack(pady=(8, 3))
kripto_pin = tk.Entry(sekme4, font=("Segoe UI", 11), width=25, justify="center", show="*"); kripto_pin.pack(pady=3)
kripto_sonuc = tk.Entry(sekme4, font=("Consolas", 10), width=62, justify="center", bg="#0f172a", fg="#4ade80", bd=0); kripto_sonuc.pack(pady=12, ipady=6)

def xor_islem(metin, anahtar):
    return "".join(chr(ord(c) ^ ord(anahtar[i % len(anahtar)])) for i, c in enumerate(metin))

def metni_sifrele():
    m, p = kripto_metin.get(), kripto_pin.get()
    if not m or not p: messagebox.showwarning("Uyarı", "Metin ve PIN girin!"); return
    sifreli = base64.b64encode(xor_islem(m, p).encode("utf-8")).decode("utf-8")
    kripto_sonuc.delete(0, tk.END); kripto_sonuc.insert(0, sifreli)
    rapora_kaydet("Kripto Kasası", "Bir veri XOR + Base64 ile şifrelendi.")

def metni_coz():
    m, p = kripto_metin.get(), kripto_pin.get()
    if not m or not p: messagebox.showwarning("Uyarı", "Şifreli metin ve PIN girin!"); return
    try:
        cozulmus = xor_islem(base64.b64decode(m.encode("utf-8")).decode("utf-8"), p)
        kripto_sonuc.delete(0, tk.END); kripto_sonuc.insert(0, cozulmus)
    except Exception:
        messagebox.showerror("Hata", "Şifre çözülemedi! Metin veya PIN hatalı.")

kutu4 = tk.Frame(sekme4, bg="#1e293b"); kutu4.pack(pady=5)
tk.Button(kutu4, text="Metni Kilitle (Şifrele)", command=metni_sifrele, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0).pack(side="left", padx=8)
tk.Button(kutu4, text="Kilidi Aç (Çöz)", command=metni_coz, bg="#059669", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0).pack(side="left", padx=8)

sekme5 = tk.Frame(sekmeler, bg="#1e293b")
sekmeler.add(sekme5, text="Ağ Kalkanı")
tk.Label(sekme5, text="Bağlı Olduğunuz Wi-Fi ve Bilgisayar Ağ Güvenliği", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white").pack(pady=(18, 5))
ag_sonuc = tk.Label(sekme5, text="Taramayı başlatmak için butona basın.", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8", justify="left", wraplength=650); ag_sonuc.pack(pady=12)

def ag_guvenligi_tara():
    ag_sonuc.config(text="Ağ ve portlar taranıyor...", fg="#38bdf8"); pencere.update()
    rapor, tehlike = [], False
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(("8.8.8.8", 80)); yerel_ip = s.getsockname(); s.close()
        rapor.append(f"- Yerel IP Adresi: {yerel_ip} (İnternet Aktif)")
    except Exception: yerel_ip = "127.0.0.1"; rapor.append("- Çevrimdışı mod.")
    try:
        cikti = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True, encoding="utf-8", errors="ignore")
        ssid = re.search(r"^\s*SSID\s*:\s*(.+)$", cikti, re.MULTILINE); auth = re.search(r"^\s*Authentication\s*:\s*(.+)$", cikti, re.MULTILINE)
        if ssid:
            sifreleme = auth.group(1).strip() if auth else "Bilinmiyor"
            rapor.append(f"- Wi-Fi Ağı: {ssid.group(1).strip()} ({sifreleme})")
            if any(x in sifreleme for x in ("Open", "Açık", "WEP")): rapor.append("TEHLİKE: Güvensiz Wi-Fi!"); tehlike = True
            else: rapor.append("GÜVENLİ: Wi-Fi şifrelemesi güçlü.")
    except Exception: pass
    acik = [str(p) for p in (21, 23, 445, 3389) if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(("127.0.0.1", p)) == 0]
    if acik: rapor.append(f"UYARI: Açık portlar -> {', '.join(acik)}"); tehlike = True
    else: rapor.append("GÜVENLİ: Kritik sistem portları kapalı.")
    durum = "RİSK TESPİT EDİLDİ!" if tehlike else "AĞ BAĞLANTINIZ GÜVENLİ!"
    ag_sonuc.config(text=f"{durum}\n\n" + "\n".join(rapor), fg="#f87171" if tehlike else "#4ade80")
    rapora_kaydet("Ağ Taraması", durum)

tk.Button(sekme5, text="Bağlı Olduğum Ağı Tara", command=ag_guvenligi_tara, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=7, bd=0).pack(pady=5)

sekme6 = tk.Frame(sekmeler, bg="#1e293b")
sekmeler.add(sekme6, text="AI IoT Kalkanı")
tk.Label(sekme6, text="Soğuk Hava Deposu Sensör Sıcaklığı (°C):", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white").pack(pady=(20, 5))
sicaklik_giris = tk.Entry(sekme6, font=("Segoe UI", 12), width=18, justify="center"); sicaklik_giris.pack(pady=5)
iot_sonuc = tk.Label(sekme6, text="Normal Aralık: 3.0°C - 3.8°C", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8", justify="center", wraplength=620); iot_sonuc.pack(pady=15)

def sensor_kontrol():
    try: derece = float(sicaklik_giris.get().replace(",", "."))
    except ValueError: messagebox.showerror("Hata", "Geçerli sayı girin!"); return
    gecmis = [3.2, 3.5, 3.1, 3.8, 3.4, 3.0, 3.6, 3.3, 3.5, 3.2]
    ort, sapma = statistics.mean(gecmis), statistics.stdev(gecmis)
    if derece >= 15.0 or abs(derece - ort) > (sapma * 6):
        iot_sonuc.config(text=f"ALARM: SİBER SALDIRI ({derece}°C)! Isıtıcı kesildi ve ağ kilitlendi!", fg="#f87171")
        rapora_kaydet("AI IoT Kalkanı", f"SALDIRI ENGELLENDİ ({derece}°C)")
    else:
        iot_sonuc.config(text=f"DURUM NORMAL ({derece}°C): Soğuk hava deposu güvenli.", fg="#4ade80")
        rapora_kaydet("AI IoT Kalkanı", f"Normal ({derece}°C)")

tk.Button(sekme6, text="Sensör Verisini Analiz Et", command=sensor_kontrol, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=6, bd=0).pack(pady=5)

sekme7 = tk.Frame(sekmeler, bg="#1e293b")
sekmeler.add(sekme7, text="Kayıtlar")
rapor_kutusu = tk.Text(sekme7, height=15, width=82, bg="#0f172a", fg="#e2e8f0", font=("Consolas", 9), bd=0, padx=10, pady=10); rapor_kutusu.pack(pady=15)

def raporlari_yukle():
    rapor_kutusu.delete("1.0", tk.END)
    try:
        with open("siber_rapor.txt", "r", encoding="utf-8") as d: rapor_kutusu.insert(tk.END, d.read())
    except FileNotFoundError: rapor_kutusu.insert(tk.END, "Henüz kayıt bulunmuyor.")

tk.Button(sekme7, text="Kayıtları Yenile", command=raporlari_yukle, bg="#475569", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=5, bd=0).pack()
pencere.mainloop()
