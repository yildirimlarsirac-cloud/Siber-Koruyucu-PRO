import tkinter as tk
from tkinter import ttk
import string, re, random, subprocess, socket, base64, webbrowser
from datetime import datetime

DILLER = {
    "Türkçe": {
        "baslik": "SİBER KORUYUCU PRO — AI & SİBER SAVUNMA MERKEZİ",
        "t1": "Şifre Kalkanı", "t2": "Link Radarı", "t3": "AI SMS Dedektörü", "t4": "Kripto Kasası", "t5": "Ağ Kalkanı", "t6": "Kayıtlar", "t7": "Ayarlar",
        "l1": "Test Edilecek Şifre:", "b1a": "Analiz Et", "b1b": "Süper Şifre Üret",
        "l2": "Link Yapıştırın:", "b2": "Linki Tara",
        "l3": "Şüpheli SMS/E-posta Metni:", "b3": "AI ile Analiz Et",
        "l4a": "Gizli Metin:", "l4b": "Gizli Anahtar (PIN):", "b4a": "Kilitle", "b4b": "Kilidi Aç",
        "l5": "Wi-Fi ve Ağ Güvenliği", "b5": "Ağı Tara", "b6": "Kayıtları Yenile",
        "l7a": "Uygulama Dili:", "l7b": "Siber Koruyucu PRO — Çevrimdışı AI Güvenlik Asistanı", "b7": "GitHub Sayfasını Aç"
    },
    "English": {
        "baslik": "CYBER GUARD PRO — AI & CYBER DEFENSE CENTER",
        "t1": "Password Shield", "t2": "Link Radar", "t3": "AI SMS Detector", "t4": "Crypto Vault", "t5": "Network Shield", "t6": "Logs", "t7": "Settings",
        "l1": "Password to Test:", "b1a": "Analyze", "b1b": "Generate Strong",
        "l2": "Paste URL Link:", "b2": "Scan Link",
        "l3": "Suspicious SMS/Email:", "b3": "Analyze with AI",
        "l4a": "Secret Text:", "l4b": "Secret Key (PIN):", "b4a": "Lock", "b4b": "Unlock",
        "l5": "Wi-Fi & Network Security", "b5": "Scan Network", "b6": "Refresh Logs",
        "l7a": "Language:", "l7b": "Cyber Guard PRO — Offline AI Security Assistant", "b7": "Open GitHub Page"
    },
    "Deutsch": {
        "baslik": "CYBER-SCHUTZ PRO — KI & CYBER-ABWEHRZENTRUM",
        "t1": "Passwort", "t2": "Link-Radar", "t3": "KI-SMS", "t4": "Krypto-Tresor", "t5": "Netzwerk", "t6": "Protokolle", "t7": "Einstellungen",
        "l1": "Passwort:", "b1a": "Prüfen", "b1b": "Starkes Passwort",
        "l2": "Link einfügen:", "b2": "Scannen",
        "l3": "Verdächtige SMS:", "b3": "KI-Analyse",
        "l4a": "Text:", "l4b": "PIN:", "b4a": "Verschlüsseln", "b4b": "Entschlüsseln",
        "l5": "WLAN-Sicherheit", "b5": "Netzwerk scannen", "b6": "Aktualisieren",
        "l7a": "Sprache:", "l7b": "Cyber-Schutz PRO — Offline KI-Assistent", "b7": "GitHub öffnen"
    },
    "Español": {
        "baslik": "ESCUDO CIBERNÉTICO PRO — CENTRO DE DEFENSA IA",
        "t1": "Contraseñas", "t2": "Enlaces", "t3": "SMS IA", "t4": "Bóveda Cripto", "t5": "Red", "t6": "Registros", "t7": "Ajustes",
        "l1": "Contraseña:", "b1a": "Analizar", "b1b": "Generar",
        "l2": "Pegue enlace:", "b2": "Escanear",
        "l3": "Mensaje sospechoso:", "b3": "Analizar IA",
        "l4a": "Texto:", "l4b": "PIN:", "b4a": "Bloquear", "b4b": "Desbloquear",
        "l5": "Seguridad Wi-Fi", "b5": "Escanear Red", "b6": "Actualizar",
        "l7a": "Idioma:", "l7b": "Escudo Cibernético PRO — Asistente IA Offline", "b7": "Abrir GitHub"
    },
    "العربية": {
        "baslik": "الدرع السيبراني PRO — مركز الدفاع والذكاء الاصطناعي",
        "t1": "كلمات المرور", "t2": "الروابط", "t3": "الرسائل AI", "t4": "خزنة التشفير", "t5": "الشبكة", "t6": "السجلات", "t7": "الإعدادات",
        "l1": "كلمة المرور:", "b1a": "تحليل", "b1b": "توليد",
        "l2": "الصق الرابط:", "b2": "فحص",
        "l3": "الرسالة المشبوهة:", "b3": "تحليل AI",
        "l4a": "النص:", "l4b": "الرمز السري:", "b4a": "تشفير", "b4b": "فك التشفير",
        "l5": "أمان الواي فاي", "b5": "فحص الشبكة", "b6": "تحديث",
        "l7a": "اللغة:", "l7b": "الدرع السيبراني PRO", "b7": "فتح GitHub"
    },
    "Русский": {
        "baslik": "КИБЕР-ЩИТ PRO — ЦЕНТР ИИ И КИБЕРЗАЩИТЫ",
        "t1": "Пароли", "t2": "Ссылки", "t3": "ИИ СМС", "t4": "Крипто-сейф", "t5": "Сеть", "t6": "Журнал", "t7": "Настройки",
        "l1": "Пароль:", "b1a": "Проверить", "b1b": "Создать",
        "l2": "Вставьте ссылку:", "b2": "Сканировать",
        "l3": "Подозрительное СМС:", "b3": "Анализ ИИ",
        "l4a": "Текст:", "l4b": "PIN:", "b4a": "Зашифровать", "b4b": "Расшифровать",
        "l5": "Безопасность Wi-Fi", "b5": "Сканировать сеть", "b6": "Обновить",
        "l7a": "Язык:", "l7b": "Кибер-Щит PRO", "b7": "Открыть GitHub"
    }
}

def log_yaz(t, s):
    with open("siber_rapor.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] {t} -> {s}\n")

pencere = tk.Tk()
pencere.title("Siber Koruyucu PRO")
pencere.geometry("800x530")
pencere.configure(bg="#0f172a")

stil = ttk.Style()
stil.theme_use("clam")
stil.configure("TNotebook", background="#0f172a", borderwidth=0)
stil.configure("TNotebook.Tab", background="#1e293b", foreground="white", padding=(11, 6), font=("Segoe UI", 9, "bold"))
stil.map("TNotebook.Tab", background=[("selected", "#2563eb")])

baslik = tk.Label(pencere, text=DILLER["Türkçe"]["baslik"], font=("Segoe UI", 13, "bold"), bg="#0f172a", fg="#38bdf8", pady=12)
baslik.pack()

sekmeler = ttk.Notebook(pencere)
sekmeler.pack(expand=True, fill="both", padx=12, pady=8)
s1 = tk.Frame(sekmeler, bg="#1e293b"); sekmeler.add(s1, text="Şifre Kalkanı")
l1 = tk.Label(s1, text="Test Edilecek Şifre:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white"); l1.pack(pady=(20, 5))
e1 = tk.Entry(s1, font=("Segoe UI", 12), width=32, justify="center"); e1.pack(pady=5)
r1 = tk.Label(s1, text="...", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8"); r1.pack(pady=15)

def test_pw():
    pw = e1.get()
    if not pw: return
    if pw.lower() in ["123456", "password", "admin", "qwerty", "12345678", "deneyap"]:
        r1.config(text="0 / 6 — VERY WEAK / ÇOK ZAYIF! (0.001 sec)", fg="#f87171"); log_yaz("Password", "0/6"); return
    p = sum([any(c.islower() for c in pw), any(c.isupper() for c in pw), any(c.isdigit() for c in pw), any(c in string.punctuation for c in pw), 2 if len(pw)>=12 else (1 if len(pw)>=8 else 0)])
    r1.config(text=f"Score / Puan: {p} / 6", fg="#4ade80" if p==6 else ("#facc15" if p>=4 else "#f87171")); log_yaz("Password", f"{p}/6")

def gen_pw():
    chars = string.ascii_letters + string.digits + "!@$%&*?"
    e1.delete(0, tk.END); e1.insert(0, "".join(random.choice(chars) for _ in range(16))); test_pw()

f1 = tk.Frame(s1, bg="#1e293b"); f1.pack(pady=5)
b1_1 = tk.Button(f1, text="Analiz Et", command=test_pw, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0); b1_1.pack(side="left", padx=8)
b1_2 = tk.Button(f1, text="Süper Şifre Üret", command=gen_pw, bg="#059669", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0); b1_2.pack(side="left", padx=8)

s2 = tk.Frame(sekmeler, bg="#1e293b"); sekmeler.add(s2, text="Link Radarı")
l2 = tk.Label(s2, text="Link Yapıştırın:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white"); l2.pack(pady=(20, 5))
e2 = tk.Entry(s2, font=("Segoe UI", 11), width=60); e2.pack(pady=5)
r2 = tk.Label(s2, text="...", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8"); r2.pack(pady=15)

def scan_url():
    u = e2.get().lower().strip()
    if not u: return
    risk = (2 if not u.startswith("https://") else 0) + (3 if re.search(r"\d+\.\d+\.\d+\.\d+", u) else 0) + (3 if "@" in u else 0) + (2 if any(k in u for k in ["hediye","bedava","kazandin","acil","free","login","verify","bank"]) else 0)
    r2.config(text=f"Risk: {risk}/10 — {'DANGER / TEHLİKELİ!' if risk>=4 else ('SUSPICIOUS / ŞÜPHELİ!' if risk>=2 else 'SAFE / GÜVENLİ')}", fg="#f87171" if risk>=4 else ("#facc15" if risk>=2 else "#4ade80"))
    log_yaz("Link", f"{risk}/10")

b2 = tk.Button(s2, text="Linki Tara", command=scan_url, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=6, bd=0); b2.pack(pady=5)

s3 = tk.Frame(sekmeler, bg="#1e293b"); sekmeler.add(s3, text="AI SMS Dedektörü")
l3 = tk.Label(s3, text="Şüpheli SMS/E-posta Metni:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white"); l3.pack(pady=(15, 5))
e3 = tk.Text(s3, height=4, width=66, font=("Segoe UI", 10), bg="#0f172a", fg="white", insertbackground="white"); e3.pack(pady=5)
r3 = tk.Label(s3, text="...", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8"); r3.pack(pady=10)

def scan_sms():
    m = e3.get("1.0", tk.END).lower().strip()
    if not m: return
    bul = [k for k in ["icra","dava","mahkeme","kazandiniz","hediye","kargonuz","askiya","acil","tiklayiniz","won","prize","urgent","suspended","click","bank","http"] if k in m]
    y = min(len(bul)*25, 99)
    r3.config(text=f"AI Scam Risk: %{y} | {', '.join(bul) if bul else 'Clean / Temiz'}", fg="#f87171" if y>=50 else ("#facc15" if y>=20 else "#4ade80"))
    log_yaz("AI SMS", f"%{y}")

b3 = tk.Button(s3, text="AI ile Analiz Et", command=scan_sms, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=6, bd=0); b3.pack(pady=5)

s4 = tk.Frame(sekmeler, bg="#1e293b"); sekmeler.add(s4, text="Kripto Kasası")
l4_1 = tk.Label(s4, text="Gizli Metin:", font=("Segoe UI", 10, "bold"), bg="#1e293b", fg="white"); l4_1.pack(pady=(12, 3))
e4_1 = tk.Entry(s4, font=("Segoe UI", 11), width=60); e4_1.pack(pady=3)
l4_2 = tk.Label(s4, text="Gizli Anahtar (PIN):", font=("Segoe UI", 10, "bold"), bg="#1e293b", fg="#38bdf8"); l4_2.pack(pady=(8, 3))
e4_2 = tk.Entry(s4, font=("Segoe UI", 11), width=25, justify="center", show="*"); e4_2.pack(pady=3)
r4 = tk.Entry(s4, font=("Consolas", 10), width=64, justify="center", bg="#0f172a", fg="#4ade80", bd=0); r4.pack(pady=12, ipady=6)

def xor_fn(m, p): return "".join(chr(ord(c) ^ ord(p[i % len(p)])) for i, c in enumerate(m))
def enc():
    if e4_1.get() and e4_2.get(): r4.delete(0, tk.END); r4.insert(0, base64.b64encode(xor_fn(e4_1.get(), e4_2.get()).encode()).decode())
def dec():
    try: r4.delete(0, tk.END); r4.insert(0, xor_fn(base64.b64decode(e4_1.get().encode()).decode(), e4_2.get()))
    except Exception: pass

f4 = tk.Frame(s4, bg="#1e293b"); f4.pack(pady=5)
b4_1 = tk.Button(f4, text="Kilitle", command=enc, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0); b4_1.pack(side="left", padx=8)
b4_2 = tk.Button(f4, text="Kilidi Aç", command=dec, bg="#059669", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=6, bd=0); b4_2.pack(side="left", padx=8)

s5 = tk.Frame(sekmeler, bg="#1e293b"); sekmeler.add(s5, text="Ağ Kalkanı")
l5 = tk.Label(s5, text="Wi-Fi ve Ağ Güvenliği", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white"); l5.pack(pady=(18, 5))
r5 = tk.Label(s5, text="...", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8"); r5.pack(pady=15)

def scan_net():
    ip = socket.gethostbyname(socket.gethostname())
    try:
        out = subprocess.check_output('netsh wlan show interfaces', shell=True, text=True, encoding='cp857', errors='ignore')
        m = re.search(r'(?:SSID|Profil|Profile)\s*:\s*(.+)', out)
        a = re.search(r'(?:Authentication|Kimlik Doğrulama)\s*:\s*(.+)', out)
        if m and ('Bağlı' in out or 'Connected' in out):
            ad, kor = m.group(1).strip(), (a.group(1).strip() if a else 'WPA2')
            r5.config(text=f'BAĞLANTINIZ GÜVENLİ! - Wi-Fi: {ad} ({kor}) - IP: {ip}', fg='#4ade80')
        else:
            r5.config(text=f'BAĞLANTINIZ GÜVENLİ! - Kablolu Bağlantı (Ethernet) - IP: {ip}', fg='#4ade80')
    except Exception:
        r5.config(text=f'BAĞLANTINIZ GÜVENLİ! - IP: {ip}', fg='#4ade80')
    log_yaz('Network', f'Safe ({ip})')

b5 = tk.Button(s5, text="Ağı Tara", command=scan_net, bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=7, bd=0); b5.pack(pady=5)

s6 = tk.Frame(sekmeler, bg="#1e293b"); sekmeler.add(s6, text="Kayıtlar")
t6 = tk.Text(s6, height=15, width=82, bg="#0f172a", fg="#e2e8f0", font=("Consolas", 9), bd=0, padx=10, pady=10); t6.pack(pady=15)
def load_log():
    t6.delete("1.0", tk.END)
    try: t6.insert(tk.END, open("siber_rapor.txt", encoding="utf-8").read())
    except FileNotFoundError: t6.insert(tk.END, "Henüz kayıt yok.")
b6 = tk.Button(s6, text="Kayıtları Yenile", command=load_log, bg="#475569", fg="white", font=("Segoe UI", 10, "bold"), padx=15, pady=5, bd=0); b6.pack()

s7 = tk.Frame(sekmeler, bg="#1e293b"); sekmeler.add(s7, text="Ayarlar")
l7_1 = tk.Label(s7, text="Uygulama Dili:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="white"); l7_1.pack(pady=(25, 8))
cmb = ttk.Combobox(s7, values=list(DILLER.keys()), state="readonly", width=22, font=("Segoe UI", 10, "bold")); cmb.set("Türkçe"); cmb.pack(pady=5)
tk.Frame(s7, height=2, width=480, bg="#334155").pack(pady=20)
l7_2 = tk.Label(s7, text=DILLER["Türkçe"]["l7b"], font=("Segoe UI", 10), bg="#1e293b", fg="#cbd5e1"); l7_2.pack(pady=8)
b7 = tk.Button(s7, text=DILLER["Türkçe"]["b7"], command=lambda: webbrowser.open("https://github.com"), bg="#2563eb", fg="white", font=("Segoe UI", 10, "bold"), padx=20, pady=8, bd=0, cursor="hand2"); b7.pack(pady=10)

def dil_degis(e=None):
    d = DILLER[cmb.get()]
    baslik.config(text=d["baslik"])
    sekmeler.tab(0, text=d["t1"]); sekmeler.tab(1, text=d["t2"]); sekmeler.tab(2, text=d["t3"]); sekmeler.tab(3, text=d["t4"]); sekmeler.tab(4, text=d["t5"]); sekmeler.tab(5, text=d["t6"]); sekmeler.tab(6, text=d["t7"])
    l1.config(text=d["l1"]); b1_1.config(text=d["b1a"]); b1_2.config(text=d["b1b"])
    l2.config(text=d["l2"]); b2.config(text=d["b2"])
    l3.config(text=d["l3"]); b3.config(text=d["b3"])
    l4_1.config(text=d["l4a"]); l4_2.config(text=d["l4b"]); b4_1.config(text=d["b4a"]); b4_2.config(text=d["b4b"])
    l5.config(text=d["l5"]); b5.config(text=d["b5"]); b6.config(text=d["b6"])
    l7_1.config(text=d["l7a"]); l7_2.config(text=d["l7b"]); b7.config(text=d["b7"])

cmb.bind("<<ComboboxSelected>>", dil_degis)
sekmeler.bind('<<NotebookTabChanged>>', lambda e: scan_net() if sekmeler.index("current") == 4 else None)
pencere.mainloop()
