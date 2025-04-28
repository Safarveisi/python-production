"""Let's test some code formatting and linting."""

NAME = "Peter"
NAME.capitalize()

match NAME:

    case "Peter":
        print("You are who you are claiming to be")

    case _:

        print("We have no idea who you are")


def new_sum(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


VALUE = "hi"
VALUE.strip("a").strip("b").strip("c").strip("d").strip("e").strip("f").strip(
    "g"
).strip("h").strip("h").strip("h").strip("h").strip("h").strip("h").strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
).strip(
    "h"
)

RESULT = new_sum(a=2, b=3)
print(RESULT)


def many_args(
    a: int,
    b: int,
) -> int:
    """Return the sum of a and b."""
    return a + b


RESULT = many_args(
    a=2,
    b=3,
)
