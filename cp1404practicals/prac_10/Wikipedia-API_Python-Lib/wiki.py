import wikipedia

MENU = """\nChoices:
s)earch phrase
p)age title
q)uit
>>> """


def main():
    user_choice = input(MENU).lower()
    while user_choice != "q":
        if user_choice == "s":
            phrase = input("\nEnter a phrase: ")
            search_by_phrase(phrase)
        elif user_choice == "p":
            title = input("\nEnter a page title: ")
            search_by_title(title)
        else:
            print("Invalid choice, try again!")
        user_choice = input(MENU).lower()
    print("\nThanks for using wiki.py")


def search_by_phrase(phrase: str) -> str:
    """Search wikipedia by phrase, print results"""
    try:
        print("\nHERE IS YOUR SEARCH RESULT:\n\t" + wikipedia.summary(phrase))

    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        options_dict = {i: v for i, v in enumerate(options, start=1)}
        for i, v in options_dict.items():
            print(f"{i:>3} - {v}")
        print(
            f"\nThe phrase '{phrase}' is too ambiguous, try to use one of the {len(options)} following options:")
        repick_number = int(input("Enter option number: "))
        search_by_phrase(phrase=options_dict[repick_number])


def search_by_title(page_title: str) -> None:
    """Search wikipedia by page title, print results"""
    try:
        search_result = wikipedia.page(title=page_title)
        print(
            f"\nHere is your search result:\nTitle: {search_result.title}\nURL: {search_result.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        options_dict = {i: v for i, v in enumerate(options, start=1)}
        for i, v in options_dict.items():
            print(f"{i:>3} - {v}")
        print(
            f"\nThe title '{page_title}' is too ambiguous, try to use one of the {len(options)} following options:")
        repick_number = int(input("Enter option number: "))
        search_by_title(page_title=options_dict[repick_number])


if __name__ == "__main__":
    main()
