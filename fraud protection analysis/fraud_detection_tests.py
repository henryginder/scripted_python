import fraud_detection as fd


def test_extract_election_vote_counts():
    ans = [1131111, 16920, 7246, 837858]
    filename = 'election-iran-2009.csv'
    cols = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]

    assert fd.extract_election_vote_counts(filename, cols)[:4] == ans
    print('Extract election vote counts test passed')


def test_ones_and_tens_histogram():
    ans = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
           0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
           0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
           0.047619047619047616]

    assert fd.ones_and_tens_histogram([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                                      144, 233, 377, 610, 987, 1597, 2584,
                                      4181, 6765]) == ans
    print('Ones and tens histogram test passed')


def test_mean_squared_error():
    assert fd.mean_squared_error([1, 4, 9], [6, 5, 4]) == 17.0
    print('Mean squared error test passed')


def test_calculate_mse_with_uniform():
    filename = 'election-iran-2009.csv'
    cols = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    ex = fd.extract_election_vote_counts(filename, cols)
    hist = fd.ones_and_tens_histogram(ex)
    assert round(fd.calculate_mse_with_uniform(hist), 14) == 0.00073958333333


def main():
    test_extract_election_vote_counts()
    test_ones_and_tens_histogram()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()
    print('All tests passed!')


if __name__ == "__main__":
    main()
