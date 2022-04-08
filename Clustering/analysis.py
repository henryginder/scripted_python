# Name: Henry Ginder
# CSE 160
# Homework 4


from kmeans import assign_data, assert_dict_eq
from utils import load_centroids, read_data


def update_assignment(data, labels, centroids):
    """Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "labels".

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.
    """

    centroid_dict = {}

    for i in centroids.keys():

        label = []

        for j in data:

            index = data.index(j)

            key = assign_data(j, centroids)

            if key == i and key not in centroid_dict:

                centroid_dict[key] = []

                label.append(labels[index])

            elif key == i:

                label.append(labels[index])

        if len(label) > 0:

            centroid_dict[i] = label

    return centroid_dict


def majority_count(labels):
    """Return the count of the majority labels in the label list

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list
    """

    count = 0

    for i in labels:

        if i == max(set(labels), key=labels.count):

            count += 1

    return count


def accuracy(data, labels, centroids):
    """Calculate the accuracy of the algorithm. You should use
    update_assignment and majority_count (that you previously implemented)

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a float representing the accuracy of the algorithm
    """

    acc_dict = update_assignment(data, labels, centroids)
    m_l = 0
    m_c = 0

    for i in acc_dict.values():

        label = majority_count(i)

        m_l += label

        for j in i:

            m_c += 1

    return m_l / m_c


# helper functions
def setup_for_tests():
    """Creates are returns data for testing analysis methods.

    Returns: data, a list of data points
             labels, numeric labels for each data point
             random_centroids, three 4D centroids
             bad_centroids, three non-random 4D centroids
                with poor starting values
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    data = [
            [-1.01714716,  0.95954521,  1.20493919,  0.34804443],
            [-1.36639346, -0.38664658, -1.02232584, -1.05902604],
            [1.13659605, -2.47109085, -0.83996912, -0.24579457],
            [-1.48090019, -1.47491857, -0.6221167,  1.79055006],
            [-0.31237952,  0.73762417,  0.39042814, -1.1308523],
            [-0.83095884, -1.73002213, -0.01361636, -0.32652741],
            [-0.78645408,  1.98342914,  0.31944446, -0.41656898],
            [-1.06190687,  0.34481172, -0.70359847, -0.27828666],
            [-2.01157677,  2.93965872,  0.32334723, -0.1659333],
            [-0.56669023, -0.06943413,  1.46053764,  0.01723844]
        ]
    labels = [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    random_centroids = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [-0.71767545, 1.2309971, -1.00348728, -0.38204247],
            "centroid3": [-1.71767545, 0.29971, 0.00328728, -0.38204247],
        }
    bad_centroids = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [10, 10, 10, 10],
            "centroid3": [-10, 1, -10, 10],
        }
    return data, labels, random_centroids, bad_centroids


# tests begin
def test_update_assignment():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    data, labels, random_centroids, bad_centroids = setup_for_tests()

    # random
    answer = {'centroid3': [0, 1, 2, 1, 2, 2, 0], 'centroid1': [0],
              'centroid2': [1, 0]}
    assert_dict_eq(update_assignment(data, labels, random_centroids), answer)

    # bad
    answer = {'centroid1': [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]}
    assert_dict_eq(update_assignment(data, labels, bad_centroids), answer)
    print("test_update_assignment passed")


def test_majority_count():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # single
    assert majority_count([0, 0, 0, 0, 0, 0]) == 6

    # mixed
    assert majority_count([0, 0, 1, 1, 0, 0]) == 4
    assert majority_count([0, 2, 2, 2, 3, 3, 0, 1, 1, 0, 0]) == 4

    # tied max count
    assert majority_count([0, 2, 2, 2, 0, 2, 0, 0]) == 4
    print("test_majority_count passed")


def test_accuracy():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    data, labels, random_centroids, bad_centroids = setup_for_tests()

    # random
    answer = 0.5
    assert abs(accuracy(data, labels, random_centroids) - answer) < 1e-5

    # bad
    answer = 0.4
    assert abs(accuracy(data, labels, bad_centroids) - answer) < 1e-5
    print("test_accuracy passed")


def main_test():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    test_update_assignment()
    test_majority_count()
    test_accuracy()
    print("all tests passed.")


if __name__ == "__main__":
    centroids = load_centroids("mnist_final_centroids.csv")

    # main_test()

    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))

# LEAVE YOUR ANSWERS HERE...
# 1. What happened to the centroids? Why are there fewer than 10?
# Since the program ran and figured 10 was far too many centroids for our data
# 2. What's the accuracy of the algorithm on MNIST? By looking at the
# centroids, which digits are easier to be distinguished by the algorithm,
# and which are harder?
# The accuracy is 0.582. By looking at the centroids I can see that it can
# better distiguish certain digits better than others. In my opinion it has
# a harder time with 6, 9, 2, even 8 a little bit. While 1, 7, and 0 were a bit
# more obvious.
