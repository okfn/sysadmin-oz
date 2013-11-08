from dns.rdatatype import A, CNAME, ANY
from dns.rdataclass import IN
from dns import rdataset

import sys

def mkaddrtbl(z):
    addrs = {}
    for name, dnsnode in z.iteritems():
        name = "%s.%s" % (name, z.origin)
        for addr in dnsnode.find_rdataset(IN, A, create=True):
            names = addrs.setdefault(addr.to_text(), [])
            names.append(name)
    return addrs

def optimise(base, zone, ir):
    addrtbl = mkaddrtbl(base)
    for name, dnsnode in zone.iteritems():
        fqdn = "%s.%s" % (name, zone.origin)
        rds = dnsnode.find_rdataset(IN, A, create=True)
        for addr in rds:
            revnames = addrtbl.get(addr.to_text(), [])
            for rev in revnames:
                if rev == fqdn : continue
                if ir.match(rev):
                    rs = rdataset.from_text(IN, CNAME, rds.ttl, rev)
                    zone[name] = rs

    zone.to_file(sys.stdout, relativize=False)
