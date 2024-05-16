s = input()
def doi_xung(string_text):
    if string_text == string_text[::-1]:
        return True

print(doi_xung(s))