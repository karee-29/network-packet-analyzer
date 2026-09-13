from packet_analyzer.models import PacketRecord
from packet_analyzer.analytics import protocol_summary,traffic
def p(x,s):return PacketRecord(0,"a","b",x,packet_size=s)
def test_summary():assert protocol_summary([p("TCP",10),p("TCP",20),p("DNS",5)])[0]["packets"]==2
def test_traffic():assert traffic([p("TCP",10),p("DNS",50)])[0]["protocol"]=="DNS"
