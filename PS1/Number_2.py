from binarytree import Node
import random
from PS1 import Friendship


def main():

    friends = {'Abra', 'Belinda', 'Connie', 'Dede', 'Ethel', 'Francine'}
    friendships = [Friendship.Friendship('Dede', 'Abra'), Friendship.Friendship('Abra', 'Belinda'),
                   Friendship.Friendship('Abra', 'Connie'),
                   Friendship.Friendship('Belinda', 'Connie'), Friendship.Friendship('Belinda', 'Dede'),
                   Friendship.Friendship('Dede', 'Connie'), Friendship.Friendship('Abra', 'Ethel'),
                   Friendship.Friendship('Francine', 'Abra'), Friendship.Friendship('Belinda', 'Francine'),
                   Friendship.Friendship('Belinda', 'Ethel'), Friendship.Friendship('Abra', 'Gale')]

    invited = party_planning_algorithm(friendships)
    print(invited)

    return


# Creates a hash set (dictionary) of friends with each individual's name as the key, and their friendship count as
#   the value.
# Input must be a list of friendships, where the value of 'first' is the first friend's name (as a string) in the
#   friendship, and the value of 'second' is the second friend's name in the relationship.
def initialize(friendships):
    names = {}
    counts = {1: {}}

    for f in friendships:

        if f.first in names:
            # Check if the count increase causes a change in position among neighbors in the ordered list, and
            #   move values as needed to remain sorted.
            names, counts = \
                update_count(names,
                             counts,
                             f.first,
                             names[f.first]['count'] + 1)
        else:
            names[f.first] = {'count': 1}
            counts[1][f.first] = 1

        if f.second in names:
            # Check if the count increase causes a change in position among neighbors in the ordered list, and
            #   move values as needed to remain sorted.
            names, counts = \
                update_count(names,
                             counts,
                             f.second,
                             names[f.second]['count'] + 1)
        else:
            names[f.second] = {'count': 1}
            counts[1][f.second] = 1

    return names, counts


# Given two dictionaries, keyed by name and count, respectively, a target name, and a new friend count,
#   update both dictionaries with appropriate values. The friend must exist in the name dictionary
#   to update a count beyond 1.
def update_count(name_dict, count_dict, name, count):
    if name not in name_dict.keys():
        return name_dict, count_dict

    name_dict[name]['count'] = count
    if count in count_dict.keys():
        count_dict[count][name] = count
    else:
        count_dict[count] = {name: count}
        count_dict[count - 1].pop(name, None)

    return name_dict, count_dict


def party_planning_algorithm(friendships):
    # while some p in invited with < 5 friends is in invited, uninvite(p)
    threshold = 5

    invited_name, invited_count = initialize(friendships)
    if len(invited_count[threshold].keys()) < 1:
        return {}

    print(invited_count)

    for key in list(invited_count):
        # uninvite(p)
        if key < threshold:
            invited_count.pop(key, None)

    return invited_count


if __name__ == '__main__':
    main()
