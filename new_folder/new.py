def get_digits(n: int, sub_instance_size: int) -> list[int]:
    digits = []
    while n > 0:
        digits.append(n % (10**sub_instance_size))
        n //= 10**sub_instance_size
    return digits


d = [
    10011100001,
    10000011110,
    1001111000,
    1010000111,
    110101010,
    101010101,
    10000000,
    10000000,
    1000000,
    1000000,
    100000,
    100000,
    10000,
    10000,
    1000,
    1000,
    100,
    100,
    10,
    10,
    1,
    1,
    44522222221,
    44511111110,
]
