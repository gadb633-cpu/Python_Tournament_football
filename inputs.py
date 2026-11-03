def get_choice_menu():
    choice = int(input("Choose an option(0-10): "))
    return choice

def get_id(msg):
    id_ = int(input(f"{msg}:"))
    return id_

def get_name(msg):
    name = input(f"{msg}:")
    return name

def get_goals(msg):
    goals = int(input(f"{msg}:"))