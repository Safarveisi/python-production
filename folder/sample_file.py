name = "Peter"
name.capitalize()

match name:
    case "Peter": print("You are who you are claiming to be")
    case _: print("We have no idea who you are")

def sum(a: int, b: int) -> int:
    return sum([a, b])

result = sum(a=2, b=3)
print(result)