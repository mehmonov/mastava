from datetime import datetime

def time_since(value):
    now = datetime.now()
    diff = now - value

    periods = (
        (diff.days / 365, "yil", "yil"),
        (diff.days / 30, "oy", "oy"),
        (diff.days / 7, "hafta", "hafta"),
        (diff.days, "kun", "kun"),
        (diff.seconds / 3600, "soat", "soat"),
        (diff.seconds / 60, "minut", "minut"),
        (diff.seconds, "sekund", "sekund"),
    )

    for period, singular, plural in periods:
        if period:
            return "%d %s oldin" % (period, singular if period == 1 else plural)

    return "hozir"
