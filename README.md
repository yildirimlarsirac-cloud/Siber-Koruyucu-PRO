# 🛡️ Siber Koruyucu PRO - Cybersecurity & AI Defense Center

**Siber Koruyucu PRO** is a modern, tabbed desktop cybersecurity and AI-powered anomaly detection application built with Python and Tkinter. Designed to protect everyday users from common digital threats, it combines password security, phishing detection, live network auditing, and IoT sensor protection in a single lightweight tool.

## 🚀 Key Features

- **🔑 Password Shield (Şifre Kalkanı):** Analyzes password strength, estimates brute-force cracking time, and generates cryptographically strong 16-character passwords.
- **🌐 Phishing Link Radar (Link Radarı):** Scans URLs against 6 cybersecurity rules to detect phishing traps, raw IP links, `@` redirection tricks, and suspicious keywords.
- **📡 Live Network & Wi-Fi Shield (Ağ Kalkanı):** Audits the connected Wi-Fi network's encryption protocol (WPA2/WPA3 vs. Open/WEP) and scans for vulnerable open system ports (Ports 21, 23, 445, 3389).
- **❄️ AI IoT Cold-Storage Shield (AI IoT Kalkanı):** Uses statistical anomaly detection (mean & standard deviation analysis) to catch sudden temperature spikes or defrost manipulation cyberattacks on smart refrigeration systems.
- **📋 Automated Security Logs (Kayıtlar):** Records every scan and blocked threat with timestamps into a local report (`siber_rapor.txt`).

## 🛠️ Technologies Used

- **Language:** Python 3
- **GUI Framework:** Tkinter (`ttk`)
- **Modules:** `re`, `statistics`, `socket`, `subprocess`, `random`, `datetime`

## 💻 How to Run

1. Make sure **Python 3** is installed on your Windows PC.
2. Download `Siber Koruyucu PRO.pyw` from this repository.
3. Double-click `Siber Koruyucu PRO.pyw` to launch the application directly with no background terminal window.
