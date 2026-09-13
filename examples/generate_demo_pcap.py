from scapy.all import *
p=[IP(src="192.168.1.10",dst="93.184.216.34")/TCP(sport=49152,dport=80,flags="S"),
IP(src="192.168.1.10",dst="93.184.216.34")/TCP(sport=49152,dport=80,flags="PA")/Raw(load=b"GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n"),
IP(src="192.168.1.10",dst="8.8.8.8")/UDP(sport=53000,dport=53)/DNS(rd=1,qd=DNSQR(qname="example.com")),
IP(src="192.168.1.10",dst="1.1.1.1")/ICMP(type=8),IP(src="10.0.0.5",dst="10.0.0.20")/TCP(sport=4000,dport=445,flags="S")]
wrpcap("pcaps/demo.pcap",p);print("created pcaps/demo.pcap")
