from math import log10

# split up into pieces

# Assume we have n numbers with max size N

# then, the maximum carry we get is surely smaller than n
# if we have n summands which are all smaller than N, then
# N * n / N

# Hence, we get a maximum carry of n in every subproblem
# we have k * log_10(N) such subproblems, hence we get
# that first subproblem produces n carries
# the second one has now size n * n carries,
# so we get size of n^{k * log_10(N)} in the last step


a = [1000, 2000, 3000, 10, 15]
b = [
    9682655108113,
    17080203610709569,
    130765320,
    9913191329664,
    53148384174437887261290,
    406671514540705,
    1266155086759977093120,
    53149101542753508698112,
    3185784,
    53148401254630519909092,
    406901923182720,
    30129469486642793274,
    1265437718438997315786,
    1265438125110250475748,
    30846837807750150144,
    17080428661011072,
    30129479169291679716,
    5489105832,
    272223431137336673858435,
    326668117364804008630122,
]
c = [
    71,
    90,
    12,
    3,
    48,
    30,
    15,
    9,
    3,
    3,
    17,
    33,
    42,
    46,
    9,
    7,
    3,
    4,
    99,
    60,
    10,
    14,
]
k = 2


def new_instance(instance: list[int], k: int):
    size = int(log10(max(instance))) + 1
    sub_instance_size = size // k
    print(f"size: {size}")
    print(f"sub_instance_size = {sub_instance_size}")

    extra_step = False
    if size % k != 0:  # fits well
        extra_step = True

    print(extra_step)
    for i in range(k):
        sub_instance = [number % 10 ** (sub_instance_size) for number in instance]
        print(sub_instance)
        instance = [number // 10 ** (sub_instance_size) for number in instance]
        if extra_step and i == k - 1:
            break
        instance = [offset + a for offset in range(1, len(instance)) for a in instance]


# TODO: fix, is not correct/infeasable
def test_approach(instance: list[int], k: int):  # k = number of sub instances
    carries = list(range(1, len(instance)))
    size = int(log10(max(instance))) + 1
    sub_instance_size = size // k
    print(f"size: {size}")
    print(f"sub_instance_size = {sub_instance_size}")

    extra_step = False
    if size % k != 0:  # fits well
        extra_step = True

    print(extra_step)
    for i in range(k):
        sub_instance = [number % 10 ** (sub_instance_size) for number in instance]
        print(sub_instance)
        sol = solve_partition_py(sub_instance)

        instance = [number // 10 ** (sub_instance_size) for number in instance]
        instance = [offset + a for offset in carries for a in instance]
        if sol == False:
            print(f"Out: False at {i}-th iteration.")
            break
    else:
        if extra_step:
            sol = solve_partition_py(instance)
            if sol == False:
                print(f"Out: False at extra iteration.")
                return
        print("Out: True")


test_approach(d, 4)


def solve_partition_py(instance: list[int]):
    pass
