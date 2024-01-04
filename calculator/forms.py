from django import forms


class CalculatorForm(forms.Form):
    dar = forms.FloatField(label="Taux Journalier Moyen (en euros)")
    work_days_per_week = forms.IntegerField(
        label="Nombre de jours de travail par semaine"
    )
