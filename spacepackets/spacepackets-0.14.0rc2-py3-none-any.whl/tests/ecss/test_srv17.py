from unittest import TestCase

from spacepackets.ccsds import CdsShortTimestamp
from spacepackets.ecss import PusService
from spacepackets.ecss.pus_17_test import Service17Tm


class TestSrv17Tm(TestCase):
    def setUp(self) -> None:
        self.srv17_tm = Service17Tm(subservice=1, time_provider=None)
        self.srv17_tm.pus_tm.apid = 0x72

    def test_state(self):
        self.assertEqual(
            self.srv17_tm.sp_header, self.srv17_tm.pus_tm.space_packet_header
        )
        self.assertEqual(self.srv17_tm.service, PusService.S17_TEST)
        self.assertEqual(self.srv17_tm.subservice, 1)
        self.assertEqual(self.srv17_tm.time_provider, None)
        self.assertEqual(self.srv17_tm.apid, 0x72)
        self.assertEqual(self.srv17_tm.source_data, bytes())

    def test_other_state(self):
        srv17_with_data = Service17Tm(
            subservice=128,
            time_provider=CdsShortTimestamp(0, 0),
            source_data=bytes([0, 1, 2]),
        )
        self.assertEqual(srv17_with_data.source_data, bytes([0, 1, 2]))
        self.assertEqual(srv17_with_data.time_provider, CdsShortTimestamp(0, 0))
