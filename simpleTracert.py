from scapy.all import *
from argparse import ArgumentParser
from sys import argv
from time import time

# shut up scapy
conf.verb = 0


class Tracer:
    def __init__(self, dst, payload, max_ttl):
        self.hops = []
        self.ttl = 1
        self.dst = dst
        self.payload = payload
        self.max_ttl = max_ttl

    def trace(self, ttl, try_count=0):
        if ttl > self.max_ttl:
            return

        p = IP(ttl=ttl, dst=self.dst)
        r = sr1(p/ICMP()/self.payload, timeout=1)
        if r:
            self.hops.append((ttl, r.src))
            yield (ttl, r.src)
            if r.src == self.dst:
                return
            else:
                for src in self.trace(ttl+1):
                    yield src
        else:
            return

    def get_iterator(self):
        return self.trace(self.ttl)
