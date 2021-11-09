import random


def main():
    keep_going = True
    names = []
    action = input_action()
    while keep_going:
        if action == str(1):
            person = input_name()
            names.append(person)
        elif action == str(2) or action == str(3):
            result = draw_names(names)
            display_names(result)
        else:
            keep_going = False

        if keep_going:
            action = input_action()
    exit()


def input_name():
    name = input("Enter name: ").strip()
    exclusion = input("Enter exclusion: ").strip()
    return {"name": name, "exclusion": exclusion, "picked": ""}


def draw_names(names_list):
    names = sorted(names_list, key=lambda i: i.get("exclusion"), reverse=True)
    result = []
    picked_names = []
    for person in names:
        exclusion = person["exclusion"]
        options = []
        for i in names:
            if i["name"] != exclusion and i["name"] != person["name"]:
                options.append(i["name"])

        pick = random.choice(options)
        while pick in picked_names:
            pick = random.choice(options)

        person["picked"] = pick
        picked_names.append(pick)
        result.append(person)

    return result


def input_action():
    action = input(
        """
            Enter a number to select an option
            1 - Add name
            2 - Draw names
            3 - Repick
            4 - Quit
        """
    )

    return action.strip()


def display_names(names_list):
    for i in names_list:
        name = i["name"]
        pick = i["picked"]
        output = f"{name} picked {pick}"
        print(output)


if __name__ == "__main__":
    main()
