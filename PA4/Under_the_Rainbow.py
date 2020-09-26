import math


# Written by Meghan V. O'Neill for CS 4150 at the University of Utah, Fall 2020.
def main():

    n = int(input())
    dist = []

    for i in range(n + 1):
        dist.append(int(input()))

    min_penalty = penalty(dist)
    print(int(min_penalty))

    return


# min from i + 1 <= k <= n: {(400 - (distance[k] - distance[i]))^2 + penalty(k)}
def penalty(dist, i=0, penalties={}):

    k = i + 1
    n = len(dist)

    if k == n:
        return 0

    if i in penalties.keys():
        return penalties[i]

    min_p = math.inf

    for k in range(i + 1, n):
        p_of_i = 400 - (dist[k] - dist[i])
        calculated_penalty = p_of_i * p_of_i + penalty(dist, k, penalties)
        min_p = min(calculated_penalty, min_p)

    penalties[i] = min_p
    return min_p


if __name__ == '__main__':
    main()

