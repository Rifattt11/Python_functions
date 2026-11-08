
import re


def find_abbreviation(s):
    return re.findall(r'\b[А-ЯЁA-Z]{2,6}\b', s)


print(*find_abbreviation(input()))