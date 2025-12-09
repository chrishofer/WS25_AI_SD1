# We assume that list is not empty and has at least one element
def mean(data:list[float]) -> float:
    if len(data) == 0: # um divison / 0 zu verhindern
        return 0.0
    m = 0
    for value in data:
        m = m + value

    return m / len(data)








print(f'statistics Ausgabe:{__name__}')

def generate_lotto_numbers(count: int) -> list[int]:
    """
    Generate a dummy list of lotto numbers.

    This placeholder implementation always returns a simple
    ascending sequence starting at 1, with as many elements
    as specified in `count`.

    Parameters
    ----------
    count : int
        Number of lotto numbers to return.

    Returns
    -------
    list of int
        A list containing integers from 1 to `count`.
    """
    return list(range(1, count + 1))


if __name__ == '__main__':

    l1 = [10, 20, 30]
    print(mean(l1))

    l2 = [5, 0.0, -5.0]
    print(mean(l2))

