
def get_num(msg):
    try:
        id_ = int(input(f"{msg}:").strip())
        return id_
    except ValueError:
        print("is not num,try agien!!")
        return False

def get_name(msg):
    name = input(f"{msg}:").lower()
    return name
