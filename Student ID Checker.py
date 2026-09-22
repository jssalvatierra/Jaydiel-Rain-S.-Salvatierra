import re
id = input("Pls enter your id format, for example 2026-1234: ")

if re.fullmatch(r"\d{4}-\d{4}", id):
    print("Valid student ID")
else:
    print("Invalid student ID")