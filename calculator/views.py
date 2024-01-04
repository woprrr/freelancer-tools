from django.shortcuts import render
from .forms import CalculatorForm
from .shared.business_logic import calculate_monthly_income


def calculate_view(request):
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            dar = form.cleaned_data["dar"]
            work_days_per_week = form.cleaned_data["work_days_per_week"]
            monthly_income = calculate_monthly_income(dar, work_days_per_week)
            return render(request, "result.html", {"monthly_income": monthly_income})
    else:
        form = CalculatorForm()

    return render(request, "index.html", {"form": form})
