import unittest
import sys, os

sys.path.append(os.getcwd())
from shoe_store import *


class Test_Shoe_store(unittest.TestCase):
    def test_receiving_sneakers(self):
        self.assertEqual(Nikefactory().createsneakers().receiving_sneakers(), 'Create Nikesneakers')
        self.assertEqual(Adidasfactory().createsneakers().receiving_sneakers(), 'Create Adidassneakers')

    def test_style_slates(self):
        self.assertEqual(Nikefactory().createslates().receiving_slates(), 'Create Nikeslates')
        self.assertEqual(Adidasfactory().createslates().receiving_slates(), 'Create Adidasslates')
