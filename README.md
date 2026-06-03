# 🔍 Nmap Security Scanner

A Python-based Nmap Security Scanner that allows users to perform different types of network scans directly from the terminal.

## 🚀 Features

- Quick Scan
- Service Detection Scan
- OS Detection Scan
- Full Scan
- Automatic Report Saving
- Risk Analysis
- Scan Summary
- View Saved Reports
- Colored Terminal Output

---

## 📂 Project Structure

```text
nmap-scanner/

├── scanner.py
├── risk_rules.py
├── reports/
└── README.md
```

---

## ⚙️ Requirements

### Install Nmap

Kali Linux:

```bash
sudo apt update
sudo apt install nmap
```

Ubuntu:

```bash
sudo apt update
sudo apt install nmap
```

---

### Install Colorama

Kali Linux:

```bash
sudo apt install python3-colorama
```

OR

```bash
pip install colorama --break-system-packages
```

---

## ▶️ Running the Project

Navigate to project folder:

```bash
cd nmap-scanner
```

Run:

```bash
python3 scanner.py
```

---

## 🖥️ Menu

```text
================================
NMAP SECURITY SCANNER
================================

1. Quick Scan
2. Service Detection
3. OS Detection
4. Full Scan
5. View Reports
6. Exit
```

---

## 📌 Scan Types

### Quick Scan

```bash
nmap target
```

Example:

```bash
nmap scanme.nmap.org
```

---

### Service Detection

```bash
nmap -sV target
```

Detects running services and versions.

---

### OS Detection

```bash
nmap -O target
```

Attempts to identify the target operating system.

---

### Full Scan

```bash
nmap -A target
```

Performs aggressive scanning.

Includes:

- OS Detection
- Version Detection
- Script Scanning
- Traceroute

---

## 📄 Reports

All scan results are automatically saved in:

```text
reports/
```

Example:

```text
reports/
├── report_20260603_101200.txt
├── report_20260603_101530.txt
```

---

## ⚠️ Risk Analysis

The scanner classifies services into:

### HIGH RISK

- FTP
- Telnet
- RSH
- REXEC

### MEDIUM RISK

- SMTP
- SNMP

### LOW RISK

- Other Services

---

## 📊 Example Output

```text
================================
SCAN SUMMARY
================================

Target: scanme.nmap.org

Open Ports Found: 3

PORT    SERVICE    RISK

22      SSH        LOW
80      HTTP       LOW
443     HTTPS      LOW
```

---

## 🛡️ Disclaimer

This tool is intended for:

- Educational Purposes
- Authorized Security Testing
- Personal Lab Environments

Do NOT scan systems without permission.

---

## 👨‍💻 Author

Jegdish E

Cyber Security Student

GitHub:
https://github.com/JD-Ryzous

Portfolio:
https://portfolio-two-wheat-93.vercel.app

Always Learning. Always Securing.
