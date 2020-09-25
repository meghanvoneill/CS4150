

def main():

    d_and_k = input()
    dk = d_and_k.split()
    d = int(dk[0])
    k = int(dk[1])

    galaxies = []
    k_majority = k / 2
    majority_count = 0

    # (x, y) coordinates need to be stored as longs to avoid overflow and roundoff error.
    # Python3 uses longs for ints, so an int cast here guarantees we are using a long.
    for i in range(k):
        x_and_y = input()
        xy = x_and_y.split()
        xy[0] = int(xy[0])
        xy[1] = int(xy[1])

        # Check if star belongs in any galaxies.
        for j in range(len(galaxies)):
            if distance_in_range(xy, galaxies[j]['point'], d):
                galaxies[j]['star count'] += 1
                # If this is now the biggest galaxy, update the majority count.
                if galaxies[j]['star count'] > majority_count:
                    majority_count = galaxies[j]['star count']
                break
        # Otherwise, we found a new galaxy.
        else:
            galaxy = {'point': xy, 'star count': 1}
            galaxies.append(galaxy)
            if len(galaxies) > k_majority:
                return 'NO'

    if majority_count > k_majority:
        print(majority_count)
    else:
        print('NO')

    return


def majority_galaxy(galaxies, k):
    k_majority = k / 2
    majority_count = 0

    if len(galaxies) > k_majority:
        return 'NO'
    else:
        for galaxy in galaxies:
            if galaxy['star count'] > majority_count:
                majority_count = galaxy['star count']

    if majority_count <= k_majority:
        return 'NO'
    else:
        return majority_count


def distance_in_range(star_1, star_2, d):

    squares_summed = pow((star_1[0] - star_2[0]), 2) + pow((star_1[1] - star_2[1]), 2)
    d_squared = pow(d, 2)

    if squares_summed <= d_squared:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

