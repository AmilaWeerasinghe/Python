def increment(number: int, by: int) -> tuple:
    return number, number+by


print(increment(2, 3))


def save_user(**user):
    print(user)


save_user(id=1, name="admin")

# local and global variables
