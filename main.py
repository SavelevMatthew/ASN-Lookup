import whoisRequests
import simpleTracert
from argparse import ArgumentParser
from sys import argv


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('HOST', help="The ip address of the target")
    p.add_argument('-p', type=str, default="TestMessage",
                   help="The data to send in the IMCP packet.")
    p.add_argument('-m', type=int, default=1500,
                   help="Maximum count of hops (default: 1500)")
    p.add_argument('-a', type=int, default=3,
                   help="Maximum count of whoisRequests (default: 3)")

    arg = p.parse_args(argv[1:])

    print("\nTracing route to {} over a maximum of {} hops...\n"
          .format(arg.HOST, arg.m))
    print("{0:<4} : {1:<18} : {2}".format("#", "HOST", "ASN"))
    t = simpleTracert.Tracer(arg.HOST, arg.p, arg.m)
    for hop in t.get_iterator():
        print("{0:<4} : {1:<18} : {2}"
              .format(hop[0], hop[1], whoisRequests.try_get_ASN(hop[1],
                                                                arg.a)))
