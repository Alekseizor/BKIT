import unittest
import sys, os
from unittest.mock import patch, Mock

import shoe_store

sys.path.append(os.getcwd())
from shoe_store import *


class Test_shoe_store(unittest.TestCase):
    @patch.object(shoe_store.sneakers, 'color_sneakers')
    def test_style_slates(self, mock_color_sneakers):
        mock_color_sneakers.return_value = "Create Adidasslates(replacement)"
        self.assertEqual(Adidasfactory().createslates().style_slates(Adidasfactory().createsneakers()),"Цвет кроссовок был Create Adidasslates(replacement)")
