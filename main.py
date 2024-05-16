from algorithm.merkle_tree import compute_merkle_list


def test_compute_merkle_tree_list0():
    
    transactions = [6, 4, 9, 2, 1, 5, 2, 0]
    merkle_list = compute_merkle_list(transactions, lambda x: (7 * x + 5) % 10)
    print(merkle_list)


def test_compute_merkle_tree_list1():
    
    transactions = [7, 20, 3, 17, 8, 11, 14, 1]
    merkle_list = compute_merkle_list(transactions, lambda x: (7 * x + 11) % 23)
    print(merkle_list)


def test_compute_merkle_tree_list2():
    
    transactions = []
    h = lambda x: (7 * x + 11) % 23
    merkle_list = compute_merkle_list(transactions, h)
    print(merkle_list)


def main():
    #test_compute_merkle_tree_list0()
    #test_compute_merkle_tree_list1()
    test_compute_merkle_tree_list2()


if __name__ == '__main__':
    main()