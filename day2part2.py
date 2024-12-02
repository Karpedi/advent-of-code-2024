def is_safe(report):
    narasca = True
    pada = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        # Preveri, ali je razlika izven dovoljenega obsega
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        # Posodobi naraščajoče ali padajoče stanje
        if diff > 0:
            pada = False
        elif diff < 0:
            narasca = False

    # Poročilo mora biti monotono (naraščajoče ali padajoče)
    return narasca or pada


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    # Preveri vse možne odstranitve enega nivoja
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Odstrani en nivo
        if is_safe(modified_report):
            return True

    return False


def count_safe_reports_with_dampener(filename):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1
    return safe_count


# Preberi podatke
filename = "day2input.txt"
safe_reports = count_safe_reports_with_dampener(filename)
print(f"Število varnih poročil (from unsafe reports): {safe_reports}")
