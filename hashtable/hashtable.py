class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable(object):
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
    # To make your FNV-1 hash correct, add this as the last line of the loop:
    # total &= 0xffffffffffffffff  # 64-bit (16 f's)

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash & 0xffffffff

    # To make your DJB2 hash correct, add this as the last line of the loop:
    # total &= 0xffffffff  # 32-bit (8 f's)

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        new_entry = HashTableEntry(key, value)
        existing_entry = self.storage[index]

        if existing_entry:
            last_entry = None
            while existing_entry:
                if existing_entry.key == key:
                    # Found an existing key, can replace the value
                    existing_entry.value = value
                    return
                last_entry = existing_entry
                existing_entry = existing_entry.next
                # Did not find existing key, add to end of storage
            last_entry.next = new_entry
        else:
            self.storage[index] = new_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        existing_entry = self.storage[index]
        if existing_entry:
            last_entry = None
            while existing_entry:
                if existing_entry.pair.key == key:
                    if last_entry:
                        last_entry.next = existing_entry.next
                    else:
                        self.storage[index] = existing_entry.next
                last_entry = existing_entry
                existing_entry = existing_entry.next
        else:
            # key is not found
            print('No key found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        existing_entry = self.storage[index]
        if existing_entry:
            while existing_entry:
                if existing_entry.key == key:
                    return existing_entry.value
                existing_entry = existing_entry.next
        else:
            # key is not found
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.

        ht2 = HashTable(len(self.storage)*2)
        for i in range(len(self.storage)):
            if self.storage[i] is None:
                continue

            for kvp in self.storage[i]:
                ht2.add(kvp[0], kvp[1])
        self.storage = ht2.storage
"""


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
