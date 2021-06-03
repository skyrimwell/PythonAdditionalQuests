def naive_mul(x, y, res=0):
    for _ in range(y):
        res += x
    return res


def test_naive_mul():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y
    print("Тесты пройдены")

test_naive_mul()