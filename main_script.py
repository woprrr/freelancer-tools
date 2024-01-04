from enum import Enum
from business_logic import calculate_monthly_income, adjust_dar
from config import Messages

class UserChoice(Enum):
    YES = 'oui'
    NO = 'non'

PROMPT_DAR = "🌟 Entrez votre Taux Journalier Moyen (en euros) : "
PROMPT_WORK_DAYS = "📅 Entrez le nombre de jours de travail par semaine : "
PROMPT_MODIFY_DAYS = "🔄 Souhaitez-vous modifier le nombre de jours travaillés tout en conservant votre revenu mensuel ? (oui/non) : "
PROMPT_NEW_WORK_DAYS = "📅 Entrez le nouveau nombre de jours de travail par semaine : "

def request_freelancer_info():
    print(Messages.REM_TITLE)
    dar = float(input(PROMPT_DAR))
    work_days_per_week = int(input(PROMPT_WORK_DAYS))
    return dar, work_days_per_week

def main():
    dar, work_days_per_week = request_freelancer_info()
    monthly_income = calculate_monthly_income(dar, work_days_per_week)
    print(Messages.MONTHLY_INCOME.format(monthly_income))

    print(Messages.ADJUST_MODIFY_DAYS)
    modify_days = input(PROMPT_MODIFY_DAYS).lower()
    while modify_days not in [choice.value for choice in UserChoice]:
        print(Messages.INVALID_CHOICE)
        modify_days = input(PROMPT_MODIFY_DAYS).lower()

    if modify_days == UserChoice.YES.value:
        new_work_days_per_week = int(input(PROMPT_NEW_WORK_DAYS))
        new_dar = adjust_dar(monthly_income, new_work_days_per_week)
        print(Messages.NEW_DAR.format(new_work_days_per_week, new_dar))
    else:
        print(Messages.NO_MODIFICATION)

if __name__ == "__main__":
    main()
