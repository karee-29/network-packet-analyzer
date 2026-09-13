# Demo
```bash
pip install -r requirements-dev.txt
python examples/generate_demo_pcap.py
python -m packet_analyzer --pcap pcaps/demo.pcap --csv packets.csv --json packets.json
```
Live mode, only on an authorised interface:
```bash
python -m packet_analyzer --live <interface> --count 100 --filter "ip"
```
