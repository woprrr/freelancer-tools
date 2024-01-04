from django.test import TestCase
from calculator.shared.business_logic import calculate_monthly_income, adjust_dar


class TestBusinessLogic(TestCase):
    def test_calculate_monthly_income(self):
        self.assertEqual(calculate_monthly_income(500, 5), 10000)
        self.assertEqual(calculate_monthly_income(1000, 4), 16000)
        self.assertEqual(calculate_monthly_income(0, 5), 0)

    def test_adjust_dar(self):
        self.assertEqual(adjust_dar(10000, 4), 625.0)
        self.assertEqual(adjust_dar(16000, 5), 800)
