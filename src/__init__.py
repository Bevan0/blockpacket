# This merely exists for no reason other than to have the parse function be "blockpacket.parse()"
# other than "blockpacket.parser.parse()"

from parser import Parser

def parse(packet):
    Parser.parse_packet(packet)
