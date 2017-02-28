import stl
from nose2.tools import params
import unittest

class TestSTLAST(unittest.TestCase):
    def test_and(self):
        phi = stl.parse("x")
        self.assertEqual(stl.TOP, stl.TOP | phi)
        self.assertEqual(stl.BOT, stl.BOT & phi)
        self.assertEqual(stl.TOP, stl.TOP & stl.TOP)
        self.assertEqual(stl.BOT, stl.BOT | stl.BOT)
        self.assertEqual(stl.TOP, stl.TOP | stl.BOT)
        self.assertEqual(stl.BOT, stl.TOP & stl.BOT)