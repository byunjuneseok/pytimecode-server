import unittest
from timecode.timecode import Timecode


class TestTimecode(unittest.TestCase):
    def test_constructor(self):
        test_timecode_2997_df = Timecode(29.97, True)
        test_timecode_2997_ndf = Timecode(29.97, False)
        test_timecode_2997_df.set_current_time(second=1)
        test_timecode_2997_df.set_current_time()

        self.assertEqual(0, 0)
