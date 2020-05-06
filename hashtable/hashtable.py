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

        Collision Resolution by Chaining
        Put:
            Find the hash index
            Search the list for the key
            If it's there, replace the value
            If it's not, append a new record to the list
        """
        # Find index based on key being passed in
        index = self.hash_index(key)
        # Check storage with above index
        existing_entry = self.storage[index]

        new_entry = HashTableEntry(key, value)

        # Check to see if that hash index exists:
        if existing_entry:
            last_entry = None
            # Look through this hash index list
            while existing_entry:
                # Search list for key
                if existing_entry.key == key:
                    # Found an existing key, can replace the value
                    existing_entry.value = value
                    return
                # Continue looking through list until None
                last_entry = existing_entry
                existing_entry = existing_entry.next
            # Did not find existing key, add to end of this hash index list
            last_entry.next = new_entry

        # If hash index doesn't exists, can add new entry in that spot
        else:
            self.storage[index] = new_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.

        Collision Resolution by Chaining
        Delete:
            Find the hash index
            Search the list for the key
            If found, delete the node from the list, (return the node or value?)
            Else return None
        """
        # Find index based on key being passed in
        index = self.hash_index(key)
        # Check storage with above index
        existing_entry = self.storage[index]

        # Check to see if that hash index exists:
        if existing_entry:
            last_entry = None
            # Look through this hash index list
            while existing_entry:
                # Search list for key
                if existing_entry.key == key:
                    # If matches key, set the last entry's next in list to next hash index--deletes but moves following up
                    if last_entry:
                        last_entry.next = existing_entry.next
                    else:
                        # if nothing else in list, set the next hash index to current spot
                        self.storage[index] = existing_entry.next
                # Continue looking through list until None
                last_entry = existing_entry
                existing_entry = existing_entry.next
        else:
            # key is not found, print warning
            print('No key found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.

        Collision Resolution by Chaining
        Get:
            Find the hash index
            Search the list for the key
            If found, return the value
            Else return None
        """
        # Find index based on key being passed in
        index = self.hash_index(key)
        # Check storage with above index
        existing_entry = self.storage[index]

        # Check to see if that hash index exists:
        if existing_entry:
            # Look through this hash index list
            while existing_entry:
                # Search list for key
                if existing_entry.key == key:
                    # If found, return value
                    return existing_entry.value
                # Continue looking through list until None
                existing_entry = existing_entry.next
        else:
            # key is not found, return None
            return None

    def resize(self, new_capacity):
        """
        Updates capacity of the hash table based on new_capacity and
        rehash all key/value pairs.

        Implement this.
        """

        prev_storage = self.storage

        # Step 1: make a new, bigger table/array
        # ....Update capacity on new capacity
        # ....Update storage with new capacity

        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        # Step 2: go through all the old elements, and hash into the new list
        # Look through each key value pair in previous storage
        for i in range(len(prev_storage)):
            # Check previous storage with i as index
            existing_entry = prev_storage[i]

            # Check to see if that hash index exists:
            if existing_entry:
                # Look through this hash index list
                while existing_entry:
                    if existing_entry.key:
                        # If found, rehash to new storage
                        self.put(existing_entry.key, existing_entry.value)
                    # Continue looking through list until None
                    existing_entry = existing_entry.next


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
    ht.resize(1024)
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
