''' RTP Packet
'''
__author__ = 'Tibbers'
# import sys
from time import time
# from VideoStream import VideoStream


# import VideoStream
HEADER_SIZE = 12

class RtpPacket:
    '''Rtp Packet class'''
    #header = bytearray(HEADER_SIZE)
    #HEADER_SIZE = 12

    def __init__(self):
        self.header = bytearray(HEADER_SIZE)
        self.payload = None

    def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
        """Encode the RTP packet with header fields and payload."""

        timestamp = int(time())
        print("timestamp: " + str(timestamp))
        self.header = bytearray(HEADER_SIZE)
        #--------------
        # TO COMPLETE
        #--------------
        # Fill the header bytearray with RTP header fields

        #RTP-version filed(V), must set to 2
        #padding(P),extension(X),number of contributing sources(CC) and marker(M) fields all set to zero in this lab

        #Because we have no other contributing sources(field CC == 0),the CSRC-field does not exist
        #Thus the length of the packet header is therefore 12 bytes

        #Above all done in ServerWorker.py

        # ...
        #header[] =

        #header[0] = version + padding + extension + cc + seqnum + marker + pt + ssrc
        self.header[0] = (version << 6) & 0xC0 # 2 bits
        self.header[0] = self.header[0] | padding << 5  # 1 bit
        self.header[0] = self.header[0] | extension << 4  # 1 bit
        self.header[0] = self.header[0] | (cc & 0x0F)  # 4 bits
        self.header[1] = marker << 7  # 1 bit
        self.header[1] = self.header[1] | (pt & 0x7f) # 7 bits
        # TODO, when seqnum > 65535, it will overflow?
        self.header[2] = (seqnum & 0xFF00)>> 8  # 16 bits total, this is first 8
        self.header[3] = (seqnum & 0xFF) # second 8
        # 32 bit timestamp
        self.header[4] = (timestamp >> 24) & 0xFF
        self.header[5] = (timestamp >> 16) & 0xFF
        self.header[6] = (timestamp >> 8) & 0xFF
        self.header[7] = timestamp & 0xFF
        # 32 bit ssrc
        self.header[8] = ssrc >> 24
        self.header[9] = (ssrc >> 16) & 0xFF
        self.header[10] = (ssrc >> 8) & 0xFF
        self.header[11] = ssrc & 0xFF


        # Get the payload from the argument
        # self.payload = ...
        self.payload = payload

    def decode(self, byteStream):
        """Decode the RTP packet."""

        #print byteStream[:HEADER_SIZE]
        self.header = bytearray(byteStream[:HEADER_SIZE])   #temporary solved

        self.payload = byteStream[HEADER_SIZE:]

    def version(self):
        """Return RTP version."""
        return int(self.header[0] >> 6)

    def seqNum(self):
        """Return sequence (frame) number."""
        seqNum = self.header[2] << 8 | self.header[3]  #header[2] shift left for 8 bits then does bit or with header[3]
        return int(seqNum)

    def timestamp(self):
        """Return timestamp."""
        timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
        return int(timestamp)

    def payloadType(self):
        """Return payload type."""
        pt = self.header[1] & 127
        return int(pt)

    def getPayload(self):
        """Return payload."""
        return self.payload

    def getPacket(self):
        """Return RTP packet."""
        return self.header + self.payload
