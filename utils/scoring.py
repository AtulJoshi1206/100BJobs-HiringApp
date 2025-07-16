# utils/scoring.py

def calculate_score(row):
    score = 0

    # 1. Experience
    experience_years = len(row.get('work_experiences', []))
    score += experience_years * 10

    # 2. Availability
    if 'full-time' in row.get('work_availability', []):
        score += 20

    # 3. Salary
    salary_raw = row.get('annual_salary_expectation', {}).get('full-time', '$0')
    try:
        salary = int(salary_raw.replace('$', '').replace(',', ''))
        if salary < 100000:
            score += 15
        elif salary < 120000:
            score += 10
    except:
        pass

    return score
