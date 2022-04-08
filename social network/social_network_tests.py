import social_network as sn


def test_practice_graph(practice_graph):
    assert len(practice_graph.nodes()) == 6
    assert len(practice_graph.edges()) == 8

    # Test shape of practice graph
    assert set(practice_graph.neighbors("A")) == set(["B", "C"])
    assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
    assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
    assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
    assert set(practice_graph.neighbors("E")) == set(["D"])
    assert set(practice_graph.neighbors("F")) == set(["C", "D"])
    print("practice graph tests passed")


def test_rj_graph(rj):
    assert len(rj.nodes()) == 11
    assert len(rj.edges()) == 17

    # Test shape of Romeo-and-Juliet graph
    assert set(rj.neighbors("Nurse")) == set(["Juliet"])
    assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
    assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
    assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
    assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet",
                                              "Mercutio"])
    assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
    assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo",
                                                "Benvolio"])
    assert set(rj.neighbors("Capulet")) == \
        set(["Juliet", "Tybalt", "Paris", "Escalus"])
    assert set(rj.neighbors("Escalus")) == \
        set(["Paris", "Mercutio", "Montague", "Capulet"])
    assert set(rj.neighbors("Juliet")) == \
        set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
    assert set(rj.neighbors("Romeo")) == \
        set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])
    print("romeo and juliet graph tests passed")


def test_friends(rj):
    assert sn.friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def test_friends_of_friends(rj):
    assert sn.friends_of_friends(rj, "Mercutio") == \
        set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])
    print("friends of friends test passed")


def test_common_friends(practice_graph, rj):
    assert sn.common_friends(practice_graph, "A", "B") == set(['C'])
    assert sn.common_friends(practice_graph, "A", "D") == set(['B', 'C'])
    assert sn.common_friends(practice_graph, "A", "E") == set([])
    assert sn.common_friends(practice_graph, "A", "F") == set(['C'])
    assert sn.common_friends(rj, "Mercutio", "Nurse") == set()
    assert sn.common_friends(rj, "Mercutio", "Romeo") == set()
    assert sn.common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
    assert sn.common_friends(rj, "Mercutio", "Capulet") == set(["Escalus",
                                                                "Paris"])
    print("common friends tests passed")


def test_number_of_common_friends_map(practice_graph, rj):
    assert sn.number_of_common_friends_map(practice_graph, "A") == {'D': 2,
                                                                    'F': 1}
    assert sn.number_of_common_friends_map(rj, "Mercutio") == \
        {'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1,
                                      'Juliet': 1, 'Montague': 2}
    print("number of common friends map tests passed")


def test_number_map_to_sorted_list():
    assert sn.number_map_to_sorted_list({"a": 5, "b": 2, "c": 7, "d": 5,
                                        "e": 5}) == ['c', 'a', 'd', 'e', 'b']
    print("number map to sorted list test passed")


def test_recommend_by_number_of_common_friends(practice_graph, rj):
    assert sn.recommend_by_number_of_common_friends(practice_graph, "A") == \
        ['D', 'F']
    assert sn.recommend_by_number_of_common_friends(rj, "Mercutio") == [
      'Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']
    print("recommend by number of common friends tests passed")


def test_influence_map(rj):
    assert sn.influence_map(rj, "Mercutio") == \
     {'Benvolio': 0.2, 'Capulet': 0.5833333333333333,
      'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45}
    print("influence map test passed")


def test_recommend_by_influence(rj):
    assert sn.recommend_by_influence(rj, "Mercutio") == \
     ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']
    print("recommend by influence test passed")


if __name__ == "__main__":
    test_practice_graph(sn.practice_graph)
    test_rj_graph(sn.rj)
    test_friends(sn.rj)
    test_friends_of_friends(sn.rj)
    test_common_friends(sn.practice_graph, sn.rj)
    test_number_of_common_friends_map(sn.practice_graph, sn.rj)
    test_number_map_to_sorted_list()
    test_recommend_by_number_of_common_friends(sn.practice_graph, sn.rj)
    test_influence_map(sn.rj)
    test_recommend_by_influence(sn.rj)
    print("all tests passed")
