def validate_input(prompt):
    option = ""
    while option == "":
        print(prompt)
        option = input("> ").lower()
    return option

def get_with_options(prompt, options):
    action = ""
    while action not in options:
        print(prompt)
        for index, option in enumerate(options, 1):
            print(f"{index}. {option.capitalize()}")
        action = input("> ").lower()
    return action