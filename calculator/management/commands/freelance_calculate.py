from django.core.management.base import BaseCommand
from calculator.shared.business_logic import calculate_monthly_income, adjust_dar
from calculator.config import Messages
from enum import Enum


class UserChoice(Enum):
    YES = "oui"
    NO = "non"


PROMPT_DAR = "🌟 Entrez votre Taux Journalier Moyen (en euros) : "
PROMPT_WORK_DAYS = "📅 Entrez le nombre de jours de travail par semaine : "
PROMPT_MODIFY_DAYS = "🔄 Souhaitez-vous modifier le nombre de jours travaillés tout en conservant votre revenu mensuel ? (oui/non) : "
PROMPT_NEW_WORK_DAYS = "📅 Entrez le nouveau nombre de jours de travail par semaine : "


class Command(BaseCommand):
    help = "Calculateur de rémunération pour freelances"

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-style", action="store_true", help="Diseable style output."
        )

    def handle(self, *args, **kwargs):
        self.no_style = kwargs.get("no_style", False)

        self.write_output(Messages.REM_TITLE)
        try:
            dar = float(self.get_input(PROMPT_DAR))
            work_days_per_week = int(self.get_input(PROMPT_WORK_DAYS))
        except ValueError as e:
            self.write_output(f"Erreur d'entrée: {e}", self.style.ERROR)
            return

        monthly_income = calculate_monthly_income(dar, work_days_per_week)
        self.write_output(
            Messages.MONTHLY_INCOME.format(monthly_income), self.style.SUCCESS
        )

        modify_days = self.get_input(PROMPT_MODIFY_DAYS).lower()
        while modify_days not in [choice.value for choice in UserChoice]:
            self.write_output(Messages.INVALID_CHOICE, self.style.ERROR)
            modify_days = self.get_input(PROMPT_MODIFY_DAYS).lower()

        if modify_days == UserChoice.YES.value:
            try:
                new_work_days_per_week = int(self.get_input(PROMPT_NEW_WORK_DAYS))
                new_dar = adjust_dar(monthly_income, new_work_days_per_week)
                self.write_output(
                    Messages.NEW_DAR.format(new_work_days_per_week, new_dar),
                    self.style.SUCCESS,
                )
            except ValueError as e:
                self.write_output(f"Erreur d'entrée: {e}", self.style.ERROR)
        else:
            self.write_output(Messages.NO_MODIFICATION)

    def write_output(self, message, style_function=None):
        if self.no_style or style_function is None:
            self.stdout.write(message)
        else:
            self.stdout.write(style_function(message))

    def get_input(self, prompt):
        return input(prompt)
