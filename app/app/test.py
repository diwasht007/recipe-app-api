"""
Example test

"""

from django.test import SimpleTestCase

from app import calc

class calcTest(SimpleTestCase):
    """Test calc module"""
    def test_add_numbers(self):
        res = calc.add(5,6)
        
        self.assertEqual(res,11)
    