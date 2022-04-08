# Name: Henry Ginder
# CSE 160
# Homework 5

import networkx as nx
import matplotlib.pyplot as plt
# from operator import itemgetter

###
#  Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("E", "D")
practice_graph.add_edge("D", "B")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("F", "C")
practice_graph.add_edge("C", "D")


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph(practice_graph)


###
#  Problem 1b
###

rj = nx.Graph()
rj.add_edge('Juliet', 'Romeo')
rj.add_edge('Juliet', 'Nurse')
rj.add_edge('Juliet', 'Capulet')
rj.add_edge('Juliet', 'Tybalt')
rj.add_edge('Juliet', 'Friar Laurence')
rj.add_edge('Capulet', 'Tybalt')
rj.add_edge('Capulet', 'Paris')
rj.add_edge('Capulet', 'Escalus')
rj.add_edge('Mercutio', 'Escalus')
rj.add_edge('Mercutio', 'Paris')
rj.add_edge('Mercutio', 'Romeo')
rj.add_edge('Montague', 'Escalus')
rj.add_edge('Montague', 'Romeo')
rj.add_edge('Montague', 'Benvolio')
rj.add_edge('Romeo', 'Benvolio')
rj.add_edge('Romeo', 'Friar Laurence')
rj.add_edge('Escalus', 'Paris')


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
# draw_rj(rj)


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """

    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """

    fof = []
    friend_list = []

    for i in friends(graph, user):
        friend_list.append(i)

    for i in friends(graph, user):
        for j in friends(graph, i):
            if j == user or j in friend_list:
                pass
            else:
                fof.append(j)
    return set(fof)


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends that user1 and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """

    u1 = []
    u2 = []
    common = []

    for i in friends(graph, user1):
        u1.append(i)

    for i in friends(graph, user2):
        u2.append(i)

    for i in u1:
        if i in u2:
            common.append(i)

    return set(common)


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """

    cf_map = {}

    for i in friends(graph, user):
        for j in friends(graph, i):
            if j == user:
                pass
            elif j in friends(graph, user):
                pass
            else:
                x = len(list(common_friends(graph, user, j)))
                cf_map[j] = x

    return cf_map


def number_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """

    keys_list = []

    # sort through tuples, ordering by value (descending)
    s = sorted(map_with_number_vals.items(), key=lambda x: x[1], reverse=True)

    for i, j in s:
        keys_list.append(i)

    return keys_list


def recommend_by_number_of_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """

    d = number_of_common_friends_map(graph, user)

    # sort through tuples, ordering by value (descending), break ties
    # alphabetically
    sort_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

    k_l = []
    v_l = []

    for k, v in sort_d:
        k_l.append(k)
        v_l.append(v)

    return k_l


###
#  Problem 3
###


def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """

    i_map = {}

    for i in friends(graph, user):
        for j in friends(graph, i):
            if j in i_map or j == user or j in friends(graph, user):
                continue
            else:
                score = 0
                for c in common_friends(graph, user, j):
                    score += 1 / len(list(friends(graph, c)))
            i_map[j] = score

    return i_map


###
#  Problem 4
###


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """

    d = influence_map(graph, user)

    # sort through tuples, ordering by value (descending), break ties
    # alphabetically
    sort_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

    k_l = []
    v_l = []

    for k, v in sort_d:
        k_l.append(k)
        v_l.append(v)

    return k_l


###
#  Problem 5
###

facebook = nx.Graph()

f_file = open('./facebook-links.txt', 'r')

lines = f_file.readlines()

for i in lines:
    if isinstance(i, str):
        ppl = i.split('\t')
        facebook.add_edge(int(ppl[0]), int(ppl[1]))
    else:
        ppl = i.split('\t')
        facebook.add_edge((ppl[0]), (ppl[1]))

f_file.close()

assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090

###
#  Problem 6
###
print()
print("Problem 6:")
print()

common_list = []
for i in facebook.nodes():
    if i % 1000 == 0:
        comm = recommend_by_number_of_common_friends(facebook, i)
        common_list.append(comm)
        print('{} (by number_of_common_friends): {}'.format(i, comm[:10]))


###
#  Problem 7
###
print()
print("Problem 7:")
print()

infl_list = []
for i in facebook.nodes():
    if i % 1000 == 0:
        inf = recommend_by_influence(facebook, i)
        infl_list.append(inf)
        print('{} (by influence): {}'.format(i, inf[:10]))

###
#  Problem 8
###
print()
print("Problem 8:")
print()

# Checker

count = 0

for i in infl_list:
    if i in common_list:
        count += 1

print('Same: {}'.format(count))
print('Different: {}'.format(len(infl_list) - count))


###
#  Collaboration
###

# None
