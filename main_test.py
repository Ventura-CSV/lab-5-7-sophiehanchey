
import main


def test_main():
    numbers = [5, 4, 3, 2, 1]

    first, others = main.splitlist(numbers)
    print(others)

    assert first == 1
    assert others[0] == 4
    assert others[1] == 3
    assert others[2] == 2
    assert others[3] == 5
# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
