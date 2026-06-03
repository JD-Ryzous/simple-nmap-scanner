import os
import re
import subprocess
from datetime import datetime

from colorama import init, Fore

from risk_rules import get_risk

init(autoreset=True)

REPORT_DIR = "reports"

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)


def save_report(target, scan_type, output):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{REPORT_DIR}/report_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(output)

    print(Fore.GREEN + f"\n[+] Report Saved: {filename}")


def parse_ports(output):

    ports = []

    pattern = r"(\d+)/tcp\s+open\s+([a-zA-Z0-9\-]+)"

    matches = re.findall(pattern, output)

    for port, service in matches:
        ports.append((port, service))

    return ports


def display_summary(target, ports):

    print(Fore.CYAN)
    print("=" * 40)
    print("SCAN SUMMARY")
    print("=" * 40)

    print(f"\nTarget: {target}")
    print(f"Open Ports Found: {len(ports)}\n")

    print("PORT\tSERVICE\tRISK")

    for port, service in ports:

        risk = get_risk(service)

        print(f"{port}\t{service.upper()}\t{risk}")

    print("\n" + "=" * 40)


def run_scan(args, target, scan_type):

    try:

        result = subprocess.run(
            args,
            capture_output=True,
            text=True
        )

        output = result.stdout

        ports = parse_ports(output)

        display_summary(target, ports)

        save_report(target, scan_type, output)

    except Exception as e:

        print(Fore.RED + f"\nError: {e}")


def view_reports():

    files = os.listdir(REPORT_DIR)

    if not files:
        print(Fore.RED + "\nNo Reports Found\n")
        return

    print("\nSaved Reports:\n")

    for file in files:
        print(file)


while True:

    print(Fore.GREEN)
    print("=" * 40)
    print("NMAP SECURITY SCANNER")
    print("=" * 40)

    print("1. Quick Scan")
    print("2. Service Detection")
    print("3. OS Detection")
    print("4. Full Scan")
    print("5. View Reports")
    print("6. Exit")

    choice = input("\nChoose Option: ")

    if choice == "6":
        break

    if choice == "5":
        view_reports()
        continue

    target = input("\nEnter Target: ")

    if choice == "1":

        run_scan(
            ["nmap", target],
            target,
            "Quick Scan"
        )

    elif choice == "2":

        run_scan(
            ["nmap", "-sV", target],
            target,
            "Service Detection"
        )

    elif choice == "3":

        run_scan(
            ["nmap", "-O", target],
            target,
            "OS Detection"
        )

    elif choice == "4":

        run_scan(
            ["nmap", "-A", target],
            target,
            "Full Scan"
        )

    else:

        print(Fore.RED + "\nInvalid Option\n")
