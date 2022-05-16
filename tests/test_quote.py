import unittest
from app.models import Quote

class QuoteModelTest(unittest.TestCase):
    def setUp(self):
        self.new_quote= Quote(author="annet", id=1, quote="Everyday is a new day")

    def test_instance(self):
         self.assertTrue(isinstance(self.new_quote, Quote))

    def test_initialization(self):
        self.assertEqual(self.new_quote.author, 'annet' )
        self.assertEqual(self.new_quote.quote, 'Everyday is a new day') 