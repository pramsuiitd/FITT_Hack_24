from packet import Packet
from Encryption import Decrypt, Encrypt
import random

class Node:
    def __init__(self, sudo_addr, real_addr, public_key) -> None:
        self.sudo_addr = sudo_addr
        self.real_addr = real_addr
        self.route_table = dict()
        self.public_key = public_key

    def update_route_table(self, sudo_des, sudo_nxt, hops):
        self.route_table[sudo_des] = (hops, sudo_nxt)
        return self.route_table
    
    def generate_packet(self, data, des, version):
        encrypter = Encrypt(self.sudo_addr, self.public_key)
        encrypted_data = encrypter.encryptPayload(data, des)
        encrypted_src = encrypter.encryptSrcID()
        bloom_filter_payload = None
        packet = Packet(encrypted_src, des, random.randint(100, 10000), encrypted_data, bloom_filter_payload, version)
        return packet
        
    def recieve_packet(self, packet: Packet):
        if packet.dest_id == self.sudo_addr:
            self.analyze_packet(packet)
            return "-1"
        next_node = self.route_table[packet.dest_id][1]
        return next_node

    def analyze_packet(self, packet: Packet):
        decrypter = Decrypt(srcID = self.sudo_addr)
        data = decrypter.decryptPayload(self.real_addr, packet.general_payload)
        print(data)



        


        
