# Importing modules

import json

# Dictionary holding various members and amount contributed and main data file

members = {}
DATA_FILE = "members.json"

# Core Functions

def show_menu():
    print("========== NJANGI LEDGER =========")
    print("1 Register Member\n2 Record Contribution\n3 Check Member\n4 Group Summary\n0 Save & Quit")
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return None

    if choice not in (0, 1, 2, 3, 4):
        print("Please choose a valid option (0-4).")
        return None

    return choice


def load_data():
    global members
    try:
        with open(DATA_FILE, "r") as f:
            members = json.load(f)
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No existing data found. Starting with an empty ledger.")
        members = {}
    except json.JSONDecodeError:
        print("Data file is corrupted or empty. Starting with an empty ledger.")
        members = {}


def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(members, f, indent=4)
        print("Data saved successfully!")
    except Exception as e:
        print(f"Something went wrong while saving: {e}")


def register_member():
    name = input("Please enter member's name: ").strip().title()
    if name == "":
        print("Incorrect name! cannot proceed")
        return None
    elif name in members:
        print(f"Sorry {name} has already been registered as member!")
        return None
    else:
        print(f"Registering {name} as new member...")
        members[name] = []
        print("Member registered successfully.")
    return name


def record_contribution():
    name = input("Please enter member's name: ").strip().title()
    if name in members:
        try:
            amount = int(input(f"Please enter the amount contributed by {name}: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            return

        if amount <= 0:
            print("Invalid amount!")
        else:
            print(f"Recording a contribution of {amount} XAF to {name}...")
            members[name].append(amount)
            total = get_total_contribution(name)
            print(f"Amount of {amount} XAF recorded successfully! {name}'s total is now {total} XAF")
    else:
        print(f"Sorry {name} has not been registered yet!")


def check_member():
    name = input("Please enter member's name: ").strip().title()
    if name in members:
        total_contribution = get_total_contribution(name)
        print(f"{name} contributed a total of {total_contribution} XAF")
        return total_contribution
    else:
        print(f"Sorry {name} has not been registered!")
        return None


def group_summary():
    member_count = len(members)
    total_pot = sum(get_total_contribution(name) for name in members)
    top_contributor = find_top_contributor()

    summary = {
        "member_count": member_count,
        "total_pot": total_pot,
        "top_contributor": top_contributor
    }
    return summary


def find_top_contributor():
    if not members:
        print("Cannot find top contributor: no members registered yet!")
        return None
    return max(members, key = get_total_contribution)

# Helper Functions

def get_total_contribution(name):
    # Calculate the total amount contributed by a single member.
    return sum(members.get(name, []))

# Main Program

def main():
    load_data()

    while True:
        choice = show_menu()
        if choice is None:
            continue

        if choice == 1:
            register_member()
        elif choice == 2:
            record_contribution()
        elif choice == 3:
            check_member()
        elif choice == 4:
            summary = group_summary()
            print(f"\n--- Group Summary ---")
            print(f"Total members: {summary['member_count']}")
            print(f"Total pot: {summary['total_pot']} XAF")
            if summary['top_contributor'] is not None:
                top_name = summary['top_contributor']
                print(f"Top contributor: {top_name} ({get_total_contribution(top_name)} XAF)")
            print("----------------------\n")
        elif choice == 0:
            save_data()
            print("Goodbye!")
            break

main()