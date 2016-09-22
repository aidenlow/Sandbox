from Prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages_list = [ruby, python, vb]

    print("The dynamically typed languages are")

    for language in languages_list:
        if language.is_dynamic():
            print(language.name)


main()
