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


def stetje_funkc(filename):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1
    return safe_count



filename = "day2input.txt"
safe_reports = stetje_funkc(filename)
print(f"Število varnih poročil: {safe_reports}")
