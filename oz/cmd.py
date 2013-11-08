import argparse
import re
import sys
from dns import zone
try: from cStringIO import StringIO
except ImportError: from StringIO import StringIO
from oz.opt import optimise

def _cli():
    parser = argparse.ArgumentParser(description='DNS Zone Optimizer.')
    parser.add_argument('base', help='Base (Infrastructure) Zone')
    parser.add_argument('-r', dest='infra_re', default=r'^[a-zA-Z]+[0-9]+\.',
                        help='Infrastructure name regexp')
    parser.add_argument('zone', default="-", help='Zone to Optimise')
    args = parser.parse_args()
    
    args.infra_re = re.compile(args.infra_re)

    def _parse(filename):
        if filename == "-":
            fp = sys.stdin
        else:
            fp = open(filename, "r")
        z = zone.from_file(fp, check_origin=False)
        fp.close()
        return z

    b = _parse(args.base)
    z = _parse(args.zone)

    optimise(b, z, args.infra_re)
