
def calculate_investment(contribution, percentage, years):
    end_value = contribution * (1 + percentage/100) ** years
    return end_value