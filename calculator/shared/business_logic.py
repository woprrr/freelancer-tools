def calculate_monthly_income(dar, work_days_per_week, weeks_per_month=4):
    return dar * work_days_per_week * weeks_per_month

def adjust_dar(monthly_income, new_work_days_per_week, weeks_per_month=4):
    return monthly_income / (new_work_days_per_week * weeks_per_month)
