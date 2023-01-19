import main;


test_collection_1 = [3, -1, -1]
test_collection_2 = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
test_collection_3 = []
test_collection_4 = [9]

# First approach
def test_most_frequent_item_count_1():
    assert main.most_frequent_item_count_1(test_collection_1) == 2
    assert main.most_frequent_item_count_1(test_collection_2) == 5
    assert main.most_frequent_item_count_1(test_collection_3) == 0
    assert main.most_frequent_item_count_1(test_collection_4) == 1

# Second approach
def test_most_frequent_item_count_1():
    assert main.most_frequent_item_count_2(test_collection_1) == 2
    assert main.most_frequent_item_count_2(test_collection_2) == 5
    assert main.most_frequent_item_count_2(test_collection_3) == 0
    assert main.most_frequent_item_count_2(test_collection_4) == 1

# Third approach
def test_most_frequent_item_count_1():
    assert main.most_frequent_item_count_3(test_collection_1) == 2
    assert main.most_frequent_item_count_3(test_collection_2) == 5
    assert main.most_frequent_item_count_3(test_collection_3) == 0
    assert main.most_frequent_item_count_3(test_collection_4) == 1
