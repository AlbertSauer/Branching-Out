import json


def load_users():
    """Load users from users.json and return as a list."""
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(name):
    users = load_users()

    filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]

    if not filtered_users:
        print(f"No users found with name: {name}")
    else:
        print(f"Users with name '{name}':")
        for user in filtered_users:
            print(user)


def filter_users_by_age(min_age=None, max_age=None):
    """
    Filter users by age.
    Assumes each user is a dict with an "age" key.
    """
    users = load_users()
    filtered_users = []

    for user in users:
        age = user.get("age")
        if age is None:
            continue  # skip users without an age

        # Apply min and max filters if they are provided
        if min_age is not None and age < min_age:
            continue
        if max_age is not None and age > max_age:
            continue

        filtered_users.append(user)

    if not filtered_users:
        print("No users found for the given age range.")
    else:
        print("Users matching the age filter:")
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? ('name' or 'age'): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        print("You can leave a value blank to skip that bound.")
        min_age_input = input("Enter minimum age (or press Enter to skip): ").strip()
        max_age_input = input("Enter maximum age (or press Enter to skip): ").strip()

        # Convert to int or None
        min_age = int(min_age_input) if min_age_input else None
        max_age = int(max_age_input) if max_age_input else None

        filter_users_by_age(min_age=min_age, max_age=max_age)

    else:
        print("Filtering by that option is not yet supported.")
