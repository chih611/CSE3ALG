"""Tests the various hash table classes"""
from hash_table_lp import HashTableLP


def main():
    test_lp()
    # test_qp()
    # test_dh()
    # test_separate_chaining()


def test_lp():
    """Tests the hash table implementing Linear Probing"""
    hash_table = HashTableLP()

    # Test inserting (from the lecture)
    hash_table.insert(10)
    hash_table.insert(115)
    hash_table.insert(28)
    hash_table.insert(962)
    hash_table.insert(50)
    hash_table.insert(48)
    hash_table.insert(19)
    hash_table.display()

    # Test search
    key = 115
    print(f'Search key: {key}, location: {hash_table.search(key)}')

    key = 19
    print(f'Search key: {key}, location: {hash_table.search(key)}')

    key = 70
    print(f'Search key: {key}, location: {hash_table.search(key)}')


# def test_qp():
#     """Tests the hash table implementing Quadratic Probing"""
#     hash_table = HashTableQP()

#     # Test inserting (from the lecture)
#     hash_table.insert(7)
#     hash_table.insert(12)
#     hash_table.insert(17)
#     hash_table.insert(21)
#     hash_table.insert(27)
#     hash_table.insert(28)
#     hash_table.display()

#     # Test search
#     key = 7
#     print(f'Search key: {key}, location: {hash_table.search(key)}')

#     key = 37
#     print(f'Search key: {key}, location: {hash_table.search(key)}')

#     key = 39
#     print(f'Search key: {key}, location: {hash_table.search(key)}')


# def test_dh():
#     """Tests the hash table implementing Double Hashing"""
#     hash_table = HashTableDH()

#     # Test inserting (from the lecture)
#     hash_table.insert(7)
#     hash_table.insert(10)
#     hash_table.insert(17)
#     hash_table.insert(33)
#     hash_table.insert(20)
#     hash_table.insert(18)
#     hash_table.display()

#     # Test search
#     key = 34
#     print(f'Search key: {key}, location: {hash_table.search(key)}')

#     key = 7
#     print(f'Search key: {key}, location: {hash_table.search(key)}')

#     key = 20
#     print(f'Search key: {key}, location: {hash_table.search(key)}')


# def test_separate_chaining():
#     """Tests the hash table implementing Separate Chaining"""
#     hash_table = HashTableSeparateChaining()

#     # Test inserting (from the lecture)
#     hash_table.insert(7)
#     hash_table.insert(12)
#     hash_table.insert(17)
#     hash_table.insert(21)
#     hash_table.insert(27)
#     hash_table.insert(28)
#     hash_table.display()

#     # Test search
#     key = 17
#     print(f'Search key: {key}, contains: {hash_table.search(key)}')

#     key = 21
#     print(f'Search key: {key}, contains: {hash_table.search(key)}')

#     key = 100
#     print(f'Search key: {key}, contains: {hash_table.search(key)}')


if __name__ == '__main__':
    main()
