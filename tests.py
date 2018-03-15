import unittest
from hextorgb import hextorgb

class TestHexToRGB(unittest.TestCase):
    def test_invalid_hex_letters(self):
        self.assertEqual(hextorgb("#ERF011"), -1)

    def test_invalid_hex_length(self):
        self.assertEqual(hextorgb("#EF011"), -1)

    def test_valid_hex_with_hash(self):
        self.assertEqual(hextorgb("#EFF01E"), (239,240,30))
        self.assertEqual(hextorgb("#EFEFEF"), (239,239,239))
        self.assertEqual(hextorgb("#12FFED"), (18,255,237))

    def test_valid_hex_without_hash(self):
        self.assertEqual(hextorgb("EFF01E"), (239,240,30))
        self.assertEqual(hextorgb("EFEFEF"), (239,239,239))
        self.assertEqual(hextorgb("12FFED"), (18,255,237))

if __name__ == '__main__':
    unittest.main()