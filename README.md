# Python Network Scanner

A Python-based network scanner that identifies open TCP ports using socket programming, service detection, and concurrent scanning techniques.

## Features

- Multi-threaded TCP port scanning
- Service identification
- Open port detection
- Scan report generation
- Fast concurrent scanning using ThreadPoolExecutor
- Beginner-friendly cybersecurity project

## Technologies Used

- Python
- Socket Programming
- TCP/IP Networking
- Concurrent Programming

## Project Structure

```text
python-network-scanner/
│
├── scanner.py
├── README.md
├── results.txt
└── screenshots/
    └── scan_result.png
```

## Usage

Run the scanner:

```bash
python scanner.py
```

Enter the target IP address when prompted.

Example:

```text
Enter Target IP Address: 127.0.0.1
```

## Example Output

```text
Starting Advanced Network Scan...

[OPEN] Port 80    Service: HTTP
[OPEN] Port 443   Service: HTTPS

Total Open Ports Found: 2
Report saved to results.txt
```

## Screenshot

scan_result.png

## Learning Outcomes

- Network Fundamentals
- TCP/IP Communication
- Socket Programming
- Port Scanning Concepts
- Concurrent Programming
- Cybersecurity Basics

## Disclaimer

This project is intended for educational purposes and authorized security testing only. Only scan systems that you own or have permission to assess.
