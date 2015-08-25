from unittest import TestCase
from berlinclock.BerlinClockConverter import BerlinClockConverter

__author__ = 'SekthDroid'


class BerlinClockConverterTest(TestCase):
    def test_should_return_single_minutes_row(self):
        berlin_clock = BerlinClockConverter()
        self.assertEqual("OOOO", berlin_clock.get_single_minutes("00:00:00"))
        self.assertEqual("YYYY", berlin_clock.get_single_minutes("23:59:59"))
        self.assertEqual("YYOO", berlin_clock.get_single_minutes("12:32:00"))
        self.assertEqual("YYYY", berlin_clock.get_single_minutes("12:34:00"))
        self.assertEqual("OOOO", berlin_clock.get_single_minutes("12:35:00"))

    def test_should_return_five_minutes_row(self):
        berlin_clock = BerlinClockConverter()
        self.assertEqual("OOOOOOOOOOO", berlin_clock.get_five_minutes("00:00:00"))
        self.assertEqual("YYRYYRYYRYY", berlin_clock.get_five_minutes("23:59:59"))
        self.assertEqual("OOOOOOOOOOO", berlin_clock.get_five_minutes("12:04:00"))
        self.assertEqual("YYRYOOOOOOO", berlin_clock.get_five_minutes("12:23:00"))
        self.assertEqual("YYRYYRYOOOO", berlin_clock.get_five_minutes("12:35:00"))