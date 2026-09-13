# Interview Guide
**Architecture:** capture → parser → normalised PacketRecord → analytics → export.
**Why normalise?** It decouples Scapy from the analytics layer and makes testing easier.
**HTTP:** detects plaintext request lines and Host headers; it does not decrypt HTTPS.
**DNS:** extracts query names/types from DNS over UDP.
**PCAP-first:** deterministic, reproducible and safer for demos than privileged live capture.
**Production extensions:** IPv6, TLS metadata, richer dissectors, persistent storage, streaming, RBAC and distributed capture.
