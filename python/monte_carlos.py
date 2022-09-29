"""
Perform the Monte Carlos estimate, which approximates the area of a circle
https://web.cse.ohio-state.edu/software/2221/web-sw1/extras/instructions/monte-carlo-estimation/monte-carlo-estimation.html
"""

from math import sqrt
from random import uniform
from time import perf_counter


def monte_carlos(points: int = 1000) -> float:
    """Approximates the area of a circle of radius 1 in a square of 2.0 x 2.0 dimensions."""

    lst_points = [(uniform(0, 2), uniform(0, 2)) for _ in range(points)]

    count_in: int = 0
    for point in lst_points:
        if sqrt((point[0] - 1)**2 + (point[1] - 1)**2) <= 1:
            count_in += 1

    percent: float = count_in/points
    return (4*percent)


def monte_carlos_2(points: int = 1000) -> float:
    """Approximates the area of a quarter of a circle, with a radius of 2, in a square of 2.0 x 2.0 dimensions."""

    lst_points = [(uniform(0, 2), uniform(0, 2)) for _ in range(points)]

    count_in: int = 0
    for point in lst_points:
        if sqrt((point[0] - 0)**2 + (point[1] - 0)**2) <= 2:
            count_in += 1

    percent = count_in/points
    return (4*percent)


def main() -> None:
    start = perf_counter()
    print(f"Approximate Area of the Circle #1: {monte_carlos(100_000)}")
    end = perf_counter()
    print(f"Time taken: {end - start} s\n")

    start = perf_counter()
    print(f"Approximate Area of 1/4th Circle #2: {monte_carlos_2(100_000)}")
    end = perf_counter()
    print(f"Time taken = {end-start}")


if __name__ == "__main__":
    main()

"""
What is the area of a circle of radius 1?
~ 3.141...

How well does your program estimate it?
With 100,000 points generated, my program accurately measures the area of the circle to the first decimal point (2 point 70% acc.)

How is the estimate affected by the number of points generated?
The estimate becomes more accurate as the number of points generated is increased. However, the speed of the algorithm
decreases as more points are generated.

"""
