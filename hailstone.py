"""Search OSU CSE Software 2221"""


def hail_stone(init_value: int) -> None:
    """
    Perform the Hailstone algorithm
    http://web.cse.ohio-state.edu/software/2221/web-sw1/extras/instructions/hailstone-series.html
    """

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
