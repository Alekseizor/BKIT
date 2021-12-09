import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class Test_bikvadrat(unittest.TestCase):
    def test_bikvadrat(self):
        self.assertEqual(bikvadrat(1, -2, 1), [1, -1])
        self.assertEqual(bikvadrat(1, -6, 9), [1.7320508075688772, -1.7320508075688772])
