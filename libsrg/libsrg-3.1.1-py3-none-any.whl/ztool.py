#!/usr/bin/env python3
import sys

from libsrg.LoggingAppBase import LoggingAppBase
from libsrg.Runner import Runner
from libsrg.Runner2 import Runner2


class Ztool(LoggingAppBase):

    def __init__(self):
        super().__init__()

        self.first_snap = None
        self.n_snaps = None
        self.last_snap = None
        self.verb_lookup = {
            "prep": self.parse_prep,
            "copy": self.parse_copy,
            "xfer": self.parse_xfer,
            "info": self.parse_inventory,
        }

        self.report: list[str] = []

        all_verbs = self.verb_lookup.keys()
        self.parser.add_argument("verb", action='store', choices=all_verbs, default=None)
        self.parser.add_argument('--src_userat', help='user@host for src', dest='src_userat', type=str,
                                 default="root@localhost")
        self.parser.add_argument('--dst_userat', help='user@host for dst', dest='dst_userat', type=str,
                                 default="root@localhost")

        if len(sys.argv) < 2 or sys.argv[1] not in all_verbs:
            # this call enables logging and will fail with message
            self.perform_parse()
            self.logger.critical(f"bad verb: {sys.argv} not in {all_verbs}")
            exit()

        self.verb_lookup[sys.argv[1]]()

    def parse_prep(self):
        # setup any program specific command line arguments
        self.parser.add_argument('--pool', help='pool name', dest='pool', type=str, default="ZTINY")
        # invoke the parser
        self.perform_parse()
        #
        self.logger.info(f"after parsing {self.args}")
        #
        self.verify_pool()
        self.prep_pool()

    def parse_xfer(self):
        self.parser.add_argument('--src', help='source dataset', dest='src', type=str,
                                 default="ZRaid/MASTER/LIBVIRT_QEMU")
        self.parser.add_argument('--dst', help='destination dataset', dest='dst', type=str,
                                 default="ZRaid/COPYTEST/LIBVIRT_QEMU")
        self.parser.add_argument('--first', help='index of first snapshot', dest='first', type=int, default=0)
        self.parser.add_argument('--last', help='index of last snapshot', dest='last', type=int, default=-1)
        # invoke the parser
        self.perform_parse()
        #
        self.logger.info(f"after parsing {self.args}")
        #
        rs = Runner(["zfs", "get", "mountpoint", "-H", self.args.src, ], userat=self.args.src_userat)
        if len(rs.so_lines) != 1:
            raise Exception(f"expected one output line in {rs}")
        vol, mp, src_mountpoint, source = rs.so_lines[0].split()
        if source != "local":
            raise Exception(f"expected mountpoint to be local {rs}")

        self.do_copy()
        rs2 = Runner(["zfs", "inherit", "mountpoint",  self.args.src, ], userat=self.args.src_userat)
        rs2.log(throw=True)
        rd2 = Runner(["zfs", "set", f"mountpoint={src_mountpoint}",  self.args.dst, ], userat=self.args.dst_userat)
        rd2.log(throw=True)

    def parse_copy(self):
        self.parser.add_argument('--src', help='source dataset', dest='src', type=str,
                                 default="ZRaid/MASTER/LIBVIRT_QEMU")
        self.parser.add_argument('--dst', help='destination dataset', dest='dst', type=str,
                                 default="ZRaid/COPYTEST/LIBVIRT_QEMU")
        self.parser.add_argument('--first', help='index of first snapshot', dest='first', type=int, default=0)
        self.parser.add_argument('--last', help='index of last snapshot', dest='last', type=int, default=-1)
        # invoke the parser
        self.perform_parse()
        #
        self.logger.info(f"after parsing {self.args}")
        #
        self.do_copy()

    def prep_pool(self):
        self.create_vol("CLONES")
        self.create_vol("COPIES")
        self.create_vol("PRIMARY/NFSPUB")
        self.create_vol("PRIMARY/NFSUSER")
        self.create_vol("PRIMARY/NFSNONE")
        self.create_vol("MIGRATED")

        self.set_parent("PRIMARY/NFSNONE", "sharenfs", "off")
        self.set_parent("PRIMARY/NFSUSER", "sharenfs", "on")
        # noinspection PyPep8
        self.set_parent("PRIMARY/NFSPUB", "sharenfs",
                        "rw,wdelay,no_subtree_check,mountpoint,sec=sys,all_squash,anonuid=3300,anongid=3300,secure,async")

        self.set_parent("COPIES", "sharenfs", "off")
        self.set_parent("COPIES", "readonly", "on")

        self.set_parent("MIGRATED", "sharenfs", "off")

    def recursive_create(self,vol:str,userat:str):
        # read a param as proof of existance
        r0 = Runner(["zfs", "get", "readonly", "-H", vol, ], userat=userat)
        r0.log() # No throw here
        if not r0.success:
            # find parent
            parts = vol.split('/')
            if len(parts)<2:
                raise(f"no parent for {vol}")
            pvol = '/'.join(parts[0:-1])         # excludes last

            self.logger.info(f"{vol} not found, checking {pvol}")
            # ensure parent is ready
            self.recursive_create(pvol,userat)
            self.logger.info(f"{vol} not found, back from checking {pvol}")


            # see if parent was readonly and set readonly=off
            r1 = Runner(["zfs", "get", "readonly", "-H", pvol, ], userat=userat)
            r1.log(throw=True)
            if len(r1.so_lines) != 1:
                raise Exception(f"expected one output line in {r1}")
            _, _, old_ro, source = r1.so_lines[0].split('\t')
            if old_ro in ["on","True"]:
                r2 = Runner(["zfs", "set", "readonly=off", pvol, ], userat=userat)
                r2.log(throw=True)
            r3 = Runner(["zfs", "create",  vol ], userat=userat)
            r3.log(throw=True)
            if old_ro in ["on","True"]:
                if source == "local":
                    r4 = Runner(["zfs", "set", "readonly=on", pvol, ], userat=userat)
                    r4.log(throw=True)
                else:
                    r5 = Runner(["zfs", "inherit", "readonly", pvol, ], userat=userat)
                    r5.log(throw=True)

    def set_parent(self, parvol: str, vname: str, value: str):
        pool = self.args.pool
        vol = pool + "/" + parvol
        r1 = Runner(["zfs", "set", f"{vname}={value}", vol], userat=self.args.dst_userat)

        r2 = Runner(["zfs", "list", "-r", "-o", "name", vol, ], userat=self.args.dst_userat)
        for subv in r2.so_lines:
            if subv == vol:
                continue
            self.logger.info(subv)
            r3 = Runner(["zfs", "inherit", vname, subv], userat=self.args.dst_userat)
            self.logger.info(r3)

    def create_vol(self, vname: str):
        pool = self.args.pool
        vol = pool + "/" + vname

        r1 = Runner(["zfs", "create", "-p", "-u", vol], userat=self.args.dst_userat)
        r2 = Runner(["zfs", "list", vol], userat=self.args.dst_userat)
        if r2.success:
            self.logger.info(r2)
        else:
            self.logger.error(r1)
            self.logger.error(r2)
            exit()

    def verify_pool(self):
        if not self.args.pool:
            self.logger.error("--pool must be specified")
            exit()

        r = Runner(["zpool", "status", self.args.pool], userat=self.args.dst_userat)
        self.logger.info(r)

    def do_copy(self):
        rs = Runner(["zfs", "list", "-o", "name", "-t", "snapshot", "-r", "-H", self.args.src],
                    userat=self.args.src_userat)
        # for l in r.so_lines[0:5]:
        #     self.logger.info(l.split())
        # for l in r.so_lines[-5:]:
        #     self.logger.info(l.split())
        if len(rs.so_lines) < 1:
            self.logger.error("source dataset does not have any snapshots")
            exit(-1)
        self.first_snap = rs.so_lines[self.args.first]
        self.last_snap = rs.so_lines[self.args.last]
        self.n_snaps = len(rs.so_lines)

        self.recursive_create(self.args.dst,self.args.dst_userat)


        rd = Runner(["zfs", "list", "-o", "name", "-t", "snapshot", "-r", "-H", self.args.dst],
                    userat=self.args.dst_userat)

        if not rd.success:
            c = Runner(["zfs", "create", "-p", "-u", self.args.dst], userat=self.args.dst_userat)
            if c.success:
                self.logger.info(c)
            else:
                self.logger.error(c)
                exit()

        rd = Runner(["zfs", "list", "-o", "name", "-t", "snapshot", "-r", "-H", self.args.dst],
                    userat=self.args.dst_userat)
        if not rd.success:
            self.logger.error(rd)
            exit()

        src_snaps = set([x.split("@")[-1] for x in rs.so_lines])
        dst_snaps = set([x.split("@")[-1] for x in rd.so_lines])
        common_snaps = src_snaps.intersection(dst_snaps)
        if not common_snaps:
            self.logger.info(f"source does not have any snapshots matching {dst_snaps}")
            self.logger.info(f"--- Transfer initial snapshot ({self.args.first} of {self.n_snaps}) ---")
            cmd1 = ["zfs", "send", self.first_snap]
            cmd2 = ["zfs", "receive", "-F", "-u", self.args.dst]

            s = Runner2(cmd1, cmd2, userat1=self.args.src_userat, userat2=self.args.dst_userat)
            if s.success:
                self.logger.info(s)
            else:
                self.logger.error(s)
                exit()
        else:
            best = sorted(list(common_snaps))[-1]
            self.first_snap = f"{self.args.src}@{best}"
            self.logger.info(f"selected {self.first_snap} as last common snapshot")

        rd = Runner(["zfs", "list", "-o", "name", "-t", "snapshot", "-r", "-H", self.args.dst],
                    userat=self.args.dst_userat)
        if not rd.success:
            self.logger.error(rd)
            self.logger.error(f"Could not read snapshot from existing dst {self.args.dst}")
            exit()

        if self.first_snap == self.last_snap:
            self.logger.info(
                f"No incremental snapshots -- last common ({self.first_snap} is also last {self.last_snap}) ---")
        else:
            self.logger.info(f"Transfer incremental snapshots ({self.first_snap} to  {self.last_snap}) ---")
            cmd1 = ["zfs", "send", "-I", self.first_snap, self.last_snap]
            cmd2 = ["zfs", "receive", "-F", "-u", self.args.dst]
            s = Runner2(cmd1, cmd2, userat1=self.args.src_userat, userat2=self.args.dst_userat)
            if s.success:
                self.logger.info(s)
            else:
                self.logger.error(s)
                exit()

    def parse_inventory(self):
        self.parser.add_argument('pools', nargs="*", help='ZFS pools to inventory', type=str)
        self.parser.add_argument('--first', help='index of first snapshot', dest='first', type=int, default=0)
        self.parser.add_argument('--last', help='index of last snapshot', dest='last', type=int, default=-1)
        # invoke the parser
        self.perform_parse()
        #
        self.logger.info(f"after parsing {self.args}")
        #
        self.do_inventory()

    def do_inventory(self):
        if self.args.pools:
            for p in self.args.pools:
                self.process1pool(p)
        else:
            r0 = Runner(["zpool", "list", "-o", "name", "-H"], userat=self.args.dst_userat)
            if r0.success:
                for lin in r0.so_lines:
                    self.process1pool(lin)
        self.trailer()
        print()
        for line in self.report:
            print(line)
        print()

    def trailer(self):
        self.run_append(["zfs", "version"])
        self.run_append(["hostnamectl"])
        self.run_append(["date"])

    def run_append(self, cmd):
        r0 = Runner(cmd, userat=self.args.dst_userat)
        if r0.success:
            self.report.extend(r0.so_lines)
            self.report.append("")
        else:
            raise (Exception(r0))

    def process1pool(self, pool: str):
        r0 = Runner(["zpool", "status", pool], userat=self.args.dst_userat)
        if r0.success:
            self.report.extend(r0.so_lines)
            self.report.append("")
        else:
            raise (Exception(r0))
        r0 = Runner(["zfs", "list", "-o", "space,quota", "-r", pool], userat=self.args.dst_userat)
        if r0.success:
            self.report.extend(r0.so_lines)
            self.report.append("")
        else:
            raise (Exception(r0))

        # r = Runner(["zfs", "list", "-t", "snapshot", "-r", "-H", pool])
        r = Runner(["zfs", "list", "-H", "-o", "name", "-r", pool], userat=self.args.dst_userat)
        if r.success:
            for vol in r.so_lines:
                self.logger.info(f"{vol=}")
                self.process1vol(vol)

    def process1vol(self, vol: str):
        if "/" not in vol:
            return
        r = Runner(["zfs", "list", "-t", "snapshot", "-d", "1", "-H", "-o", "name", vol], userat=self.args.dst_userat)
        if r.success:
            if not r.so_lines:
                return
            first = r.so_lines[0]
            last = r.so_lines[-1]
            self.logger.info(f"{first} -- {last}")
            self.report.append(f"{last} ... {first}")

    @classmethod
    def demo(cls):
        app = Ztool()


if __name__ == '__main__':
    Ztool.demo()
