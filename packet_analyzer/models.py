from dataclasses import dataclass
from typing import Optional
@dataclass
class PacketRecord:
    timestamp: float; source_ip: str; destination_ip: str; protocol: str
    source_port: Optional[int]=None; destination_port: Optional[int]=None
    packet_size: int=0; ttl: Optional[int]=None; tcp_flags: Optional[str]=None
    dns_query: Optional[str]=None; dns_type: Optional[str]=None
    http_method: Optional[str]=None; http_host: Optional[str]=None; http_path: Optional[str]=None
    icmp_type: Optional[int]=None; icmp_code: Optional[int]=None; info: str=""
    def to_dict(self): return self.__dict__.copy()
