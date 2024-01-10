# Start of python packet script


class Packet:    

    def __init__(self,  src_id, dest_id, hop_count, pkt_no, general_payload, bloom_filter_payload, version, ttl=512):
        self.src_id = src_id
        self.dest_id = dest_id
        self.hop_count = hop_count
        self.pkt_no = pkt_no
        self.general_payload = general_payload
        self.bloom_filter_payload = bloom_filter_payload
        self.version = version # Type of packet.
        self.ttl = ttl # Time to leave parameter. 
                       # This packet is falsified, if the hop count exceeds than this value. 

    def access_hop(self):
        self.hop_count += 1
        return self.hop_count

    
