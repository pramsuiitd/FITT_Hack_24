class node:
    def __init__(self, sudo_addr, real_addr) -> None:
        self.sudo_addr = sudo_addr
        self.real_addr = real_addr
        self.route_table = dict()

    def update_route_table(self, sudo_des, sudo_nxt, hops):
        self.route_table[sudo_des] = (hops, sudo_nxt)
        return self.route_table
        
