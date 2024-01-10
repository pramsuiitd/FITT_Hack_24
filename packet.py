# Start of python packet script


class Packet:    

    hop_count = 0
    version = ''

    def __init__(self,  src_id, dest_id, pkt_no, general_payload, bloom_filter_payload, version, ttl=512):
        self.src_id = src_id
        self.dest_id = dest_id
        self.pkt_no = pkt_no
        self.general_payload = general_payload
        self.bloom_filter_payload = bloom_filter_payload
        self.ttl = ttl # Time to leave parameter. 
                       # This packet is falsified, if the hop count exceeds than this value. 
    def access_hop(self):
        self.hop_count += 1
        return self.hop_count

    def version_begin(self, version):
        self.hop_count += 1
        self.version = version
        return
