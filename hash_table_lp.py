"""Simple version of hash table for non-negative integers implementing Linear Probing

Does not keep track of load factor
Can run into infinite loop when inserting or searching
"""


class HashTableLP:
    SIZE = 10
    UNOCCUPIED = -1                 # No key set to value -1

    def __init__(self):
        """Constructs a new hash table initialized with values UNOCCUPIED"""
        self.data = [self.UNOCCUPIED] * self.SIZE

    def hash(self, key):
        """Hash function to determine the hash value of a key

        Args:
            key (int): Key to hash

        Returns:
            (int): The value of the hash
        """
        return key % self.SIZE

    def insert(self, key):
        """Inserts a key into the hash table

        Args:
            key (int): Key to be inserted
        """
        # Start at this location
        location = self.hash(key)

        # Find an empty spot to put the data
        while True:
            if self.data[location] == self.UNOCCUPIED:
                # Location is free
                break
            # Location is occupied, try the next one
            location = (location + 1) % self.SIZE

        # Insert the new element
        self.data[location] = key

    def search(self, key):
        """Searches for a key in the hash table

        If found, the index of the key in the hash table is returned
        If not found, -1 is returned

        Args:
            key (int): Key to search for in hash table

        Returns:
            (int): Index of the key in the hash table (if found), otherwise -1
        """
        # Start at this location
        location = self.hash(key)

        while True:
            if self.data[location] == self.UNOCCUPIED:
                # Element not in the table
                return -1
            if self.data[location] == key:
                # Element found
                return location
            # Location is occupied, try the next one
            location = (location + 1) % self.SIZE

    def display(self):
        """Displays data in the hash table"""
        print(self.data)
