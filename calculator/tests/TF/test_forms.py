from django.test import TestCase
from django.urls import reverse
from calculator.forms import CalculatorForm


class CalculateViewTests(TestCase):
    def test_form_get_request(self):
        response = self.client.get(reverse("calculate"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertIsInstance(response.context["form"], CalculatorForm)

    def test_valid_form_post_request(self):
        form_data = {"dar": 500, "work_days_per_week": 5}
        response = self.client.post(reverse("calculate"), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "result.html")
        self.assertIn("monthly_income", response.context)
        self.assertEqual(response.context["monthly_income"], 10000)

    def test_invalid_form_post_request(self):
        form_data = {"dar": "invalid", "work_days_per_week": "invalid"}
        response = self.client.post(reverse("calculate"), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertIsInstance(response.context["form"], CalculatorForm)
        self.assertFalse(response.context["form"].is_valid())
