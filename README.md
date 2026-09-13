# 🔥 Advanced Network Packet Analyzer

![Architecture](figures/architecture.png)

> **Python | Scapy | TCP/IP | PCAP | Protocol Dissection | Network Analytics | CLI | Testing | CI**

A Wireshark-inspired packet analysis toolkit that converts raw packets into structured, queryable records and then produces network-level analytics.

## Supported protocols
- TCP
- UDP
- HTTP (plaintext request metadata)
- DNS
- ICMP

## Packet view
```text
Source IP | Destination IP | Protocol | Port | Packet Size | Info
```

Captured metadata includes timestamp, IPv4 addresses, protocol, ports, packet size, TTL, TCP flags and protocol-specific fields.

## Architecture
```text
PCAP / LIVE INTERFACE
        ↓
     CAPTURE
        ↓
   PROTOCOL PARSER
        ↓
   PacketRecord
        ↓
 ┌──────┼─────────┐
 ↓      ↓         ↓
Stats Conversations Export
 ↓      ↓         ↓
Protocols Endpoints CSV/JSON
Traffic   Ports
Flags
```

## Advanced features
- PCAP-first reproducible analysis
- optional authorised live capture
- TCP flag extraction
- plaintext HTTP method/Host/path extraction
- DNS query/type extraction
- ICMP type/code extraction
- protocol distribution
- traffic volume by protocol
- endpoint conversation analysis
- destination-port analysis
- explainable heuristic flags
- CSV and JSON export
- unit tests
- Ruff linting
- GitHub Actions CI

## Quick start
```bash
pip install -r requirements-dev.txt
python examples/generate_demo_pcap.py
python -m packet_analyzer --pcap pcaps/demo.pcap --csv packets.csv --json packets.json
```

## Live capture
Only inspect an interface you are authorised to monitor:
```bash
python -m packet_analyzer --live <interface> --count 100 --filter "ip"
```

## Example analytics
```text
PROTOCOLS
TCP / UDP / HTTP / DNS / ICMP

TRAFFIC
protocol | packets | bytes

CONVERSATIONS
endpoint A | endpoint B | packets | bytes

HEURISTIC FLAGS
SYN | large-packet | echo-request | sensitive-port
```


