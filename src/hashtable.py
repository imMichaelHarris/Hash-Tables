# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        
        Take key and Return an index


        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # myhash = self.count
        # for i in key:
        #     # print(ord(i))
        #     myhash = ((ord(i) + myhash)) % self.capacity
            
        # print(f"myhash {myhash}")
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        
        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Use hash function to get an index and store the value in that index
        # If key doesn't exist error
        index = self._hash_mod(key)
        # print(f"count, {self.count}, {self.capacity}")
        if self.storage[index] is not None:
            print("Warning")
            return
        if self.count >= self.capacity:
            # print("Nope")
            self.resize()
            
        # if index > self.count:
        #     print("Ha")
        #     return
        self.storage[index] = value
        self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash(key)
        # print(index)
        if self.storage[index] == None:
            print("ERROR!")
        else:
            self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash(key)
        print(self._hash(key))
        print(self.storage[0])
        if self.storage[index] == None:
            return None
        else:
            # print("else", self.storage[index])
            return self.storage[index]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

my_table = HashTable(8)
# my_table.insert("bimmy", "hey")
my_table.insert("key-0", "val-0")
my_table.insert("key-1", "val-1")
my_table.insert("key-2", "val-2")
my_table.insert("key-3", "val-3")
my_table.insert("key-4", "val-4")
my_table.insert("key-5", "val-5")
my_table.insert("key-6", "val-6")
my_table.insert("key-7", "val-7")
my_table.insert("key-8", "val-8")
my_table.insert("key-9", "val-9")

my_table.retrieve("key-0")

# print(my_table.storage)
# my_table.retrieve("bimmy")
# print(my_table.storage)

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
