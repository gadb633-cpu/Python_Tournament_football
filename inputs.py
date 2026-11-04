
def get_num(msg):
    try:
        num = int(input(f"{msg}:").strip())
        return num
    except ValueError:
        print("is not num,try agien!!")
        return False

def get_name(msg):
    name = input(f"{msg}:").lower()
    return name
