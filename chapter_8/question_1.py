#child up stairs N times. can hop 1, 2, 3 steps. How many different ways can the child run up the stairs.


def step_hops(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    total = step_hops(n-1)
    total += step_hops(n-2)
    total += step_hops(n-3)
    return total

#using dynamic programming
def step_hops_dyn(n, memo):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    if memo[n-1]:
        return memo[n-1]
    else:
        total = step_hops_dyn(n-1, memo) + step_hops_dyn(n-2, memo) + step_hops_dyn(n-3, memo)
        memo[n-1] = total
    return memo[n-1]

if __name__ == "__main__":
    examples = [100, 3, 4, 10]

    for example in examples:
        print(step_hops_dyn(example, [False]*example))

