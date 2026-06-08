import socket
import time
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

target = input("Enter Target IP Address: ").strip()

open_ports = []

print("\nStarting Advanced Network Scan...")
print("-" * 50)

start_time = time.time()


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            output = f"[OPEN] Port {port:<5} Service: {service}"
            print(output)
            open_ports.append(output)

        sock.close()

    except Exception:
        pass


try:
    # Scan all ports in the dictionary concurrently
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(scan_port, COMMON_PORTS.keys())

    end_time = time.time()

    # Save report
    with open("results.txt", "w") as report:
        report.write("NETWORK SCAN REPORT\n")
        report.write("=" * 50 + "\n")
        report.write(f"Target: {target}\n")
        report.write(f"Scan Date: {time.ctime()}\n")
        report.write("=" * 50 + "\n\n")

        if open_ports:
            for port_result in open_ports:
                report.write(port_result + "\n")
        else:
            report.write("No open ports found.\n")

        report.write("\n")
        report.write("=" * 50 + "\n")
        report.write(f"Total Open Ports: {len(open_ports)}\n")
        report.write(
            f"Scan Time: {round(end_time - start_time, 2)} seconds\n"
        )

    print("-" * 50)
    print(f"Total Open Ports Found: {len(open_ports)}")
    print(f"Scan Time: {round(end_time - start_time, 2)} seconds")
    print("Report saved to results.txt")

except KeyboardInterrupt:
    print("\nScan cancelled by user.")

except socket.gaierror:
    print("Invalid IP address or hostname.")

except Exception as e:
    print("Error:", e)
