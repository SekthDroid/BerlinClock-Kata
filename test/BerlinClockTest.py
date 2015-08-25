from unittest import TestCase
from berlinclock.BerlinClockConverter import BerlinClockConverter

__author__ = 'SekthDroid'


class BerlinClockConverterTest(TestCase):
    def test_should_return_single_minutes_row(self):
        berlin_clock = self.create_berlin_clock()
        self.assertEqual("OOOO", berlin_clock.get_single_minutes("00:00:00"))
        self.assertEqual("YYYY", berlin_clock.get_single_minutes("23:59:59"))
        self.assertEqual("YYOO", berlin_clock.get_single_minutes("12:32:00"))
        self.assertEqual("YYYY", berlin_clock.get_single_minutes("12:34:00"))
        self.assertEqual("OOOO", berlin_clock.get_single_minutes("12:35:00"))

    def create_berlin_clock(self):
        berlin_clock = BerlinClockConverter()
        return berlin_clock

    def test_should_return_five_minutes_row(self):
        berlin_clock = self.create_berlin_clock()
        self.assertEqual("OOOOOOOOOOO", berlin_clock.get_five_minutes("00:00:00"))
        self.assertEqual("YYRYYRYYRYY", berlin_clock.get_five_minutes("23:59:59"))
        self.assertEqual("OOOOOOOOOOO", berlin_clock.get_five_minutes("12:04:00"))
        self.assertEqual("YYRYOOOOOOO", berlin_clock.get_five_minutes("12:23:00"))
        self.assertEqual("YYRYYRYOOOO", berlin_clock.get_five_minutes("12:35:00"))

    def test_should_return_single_hours_row(self):
        berlin_clock = self.create_berlin_clock()
        self.assertEqual("OOOO", berlin_clock.get_single_hours("00:00:00"))
        self.assertEqual("RRRO", berlin_clock.get_single_hours("23:59:59"))
        self.assertEqual("RROO", berlin_clock.get_single_hours("02:04:00"))
        self.assertEqual("RRRO", berlin_clock.get_single_hours("08:23:00"))
        self.assertEqual("RRRR", berlin_clock.get_single_hours("14:35:00"))