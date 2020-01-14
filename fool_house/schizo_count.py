schizo_count = [
    "ноль",
    "целковый",
    "чекушка",
    "порнушка",
    "пердушка",
    "засерушка",
    "жучок",
    "мудачок",
    "хуй на воротничок",
    "дурачок"
]


def from_int_to_schizo_str(num):
    base = len(schizo_count)  # 10 digits
    res = []
    while True:
        r = num % base
        res.append(schizo_count[r])
        num //= base
        if num == 0:
            break
    return ".".join(res[::-1])
