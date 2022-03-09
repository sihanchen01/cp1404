from programming_language import ProgrammingLanguage, Typing

try:
    ruby = ProgrammingLanguage("Ruby", True, 1995, Typing.DYNAMIC)
    python = ProgrammingLanguage("Python", True, 1991, Typing.DYNAMIC)
    visual_basic = ProgrammingLanguage(
        "Visual Basic", False, 1991, Typing.STATIC)
    print(str(ruby))
    print(str(python))
    print(str(visual_basic))

    programming_languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)

except Exception as e:
    print(e)
