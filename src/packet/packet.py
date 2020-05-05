# This is a reference class we inherit when creating parsers
# None of these should be used unless creating new packets

class Packet:
    id = None

    def __init__(self):
        pass
    
    def parse_packet(self):
        pass
