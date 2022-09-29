"""
Perform the Hailstone algorithm
http://web.cse.ohio-state.edu/software/2221/web-sw1/extras/instructions/hailstone-series.html
"""


def hail_stone(init_value: int) -> None:
    """Takes an integer, and returns a list of integers where an even integer appends int/2 and an odd appends 3(int) + 1"""
    try:
        value = int(init_value)
        if value <= 0:
            raise ValueError
    except ValueError:
        print("Enter a positive int greater than 0 next time")
        return

    output = []
    while value != 1:
        output.append(value)
        if value % 2 == 0:
            value = int(value / 2)
        else:
            value = 3 * value + 1
    output.append(1)

    print(f"Series: {output}")
    print(f"Length of Series: {len(output):,}")
    print(f"Max of Series: {max(output):,}")
    repeat = input("Do you want to repeat? ")
    if repeat == "y":
        main()


def main() -> None:
    value = input("Enter int greater than 0: ")
    hail_stone(value)


if __name__ == "__main__":
    main()
