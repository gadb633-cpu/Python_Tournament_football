
def get_id(msg):
    try:
        id_ = int(input(f"{msg}:"))
        return id_
    except ValueError:
        print("is not num,try agien!!")
        return False

def get_name(msg):
    name = input(f"{msg}:").lower()
    return name

def get_goals(msg):
    goals = int(input(f"{msg}:"))