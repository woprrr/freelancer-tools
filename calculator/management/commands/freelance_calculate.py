from django.core.management.base import BaseCommand
from enum import Enum
from calculator.shared.business_logic import calculate_monthly_income, adjust_dar
from calculator.config import Messages


class UserChoice(Enum):
    YES = "oui"
    NO = "non"


PROMPT_DAR = "🌟 Entrez votre Taux Journalier Moyen (en euros) : "
PROMPT_WORK_DAYS = "📅 Entrez le nombre de jours de travail par semaine : "
PROMPT_MODIFY_DAYS = "🔄 Souhaitez-vous modifier le nombre de jours travaillés tout en conservant votre revenu mensuel ? (oui/non) : "
PROMPT_NEW_WORK_DAYS = "📅 Entrez le nouveau nombre de jours de travail par semaine : "


class Command(BaseCommand):
    help = "Calculateur de rémunération pour freelances"

    def handle(self, *args, **kwargs):
        self.stdout.write(Messages.REM_TITLE)

        try:
            dar = float(input(PROMPT_DAR))
            work_days_per_week = int(input(PROMPT_WORK_DAYS))
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f"Erreur d'entrée: {e}"))
            return

        monthly_income = calculate_monthly_income(dar, work_days_per_week)
        self.stdout.write(
            self.style.SUCCESS(Messages.MONTHLY_INCOME.format(monthly_income))
        )

        modify_days = input(PROMPT_MODIFY_DAYS).lower()
        while modify_days not in [choice.value for choice in UserChoice]:
            self.stdout.write(Messages.INVALID_CHOICE)
            modify_days = input(PROMPT_MODIFY_DAYS).lower()

        if modify_days == UserChoice.YES.value:
            try:
                new_work_days_per_week = int(input(PROMPT_NEW_WORK_DAYS))
                new_dar = adjust_dar(monthly_income, new_work_days_per_week)
                self.stdout.write(
                    self.style.SUCCESS(
                        Messages.NEW_DAR.format(new_work_days_per_week, new_dar)
                    )
                )
            except ValueError as e:
                self.stdout.write(self.style.ERROR(f"Erreur d'entrée: {e}"))
        else:
            self.stdout.write(Messages.NO_MODIFICATION)
