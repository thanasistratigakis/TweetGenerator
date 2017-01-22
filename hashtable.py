#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def __iter__(self):
        for bucket in self.buckets:
            if bucket:
                for item in bucket:
                    yield item

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def _bucket(self, key):
        """Return the bucket where the given key would be stored"""
        index = self._bucket_index(key)
        return self.buckets[index]

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # Count number of key-value entries in each of the buckets
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count
        pass

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        bucket = self._bucket(key)
        for item_key, item_value in bucket:
            if key == item_key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # Check if the given key exists and return its associated value
        bucket = self._bucket(key)
        for item_key, item_value in bucket:
            if key == item_key:
                return item_value
        raise KeyError('Cannot Linked List is Empty')
        pass

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # Insert or update the given key-value entry into a bucket
        bucket = self._bucket(key)
        item = bucket.find(lambda item: item[0] == key)
        new_item = (key, value)
        if item is not None:
            bucket.delete(item)
            bucket.append(new_item)
        else:
            bucket.append(new_item)

        pass

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # Find the given key and delete its entry if found
        bucket = self._bucket(key)
        item = bucket.find(lambda item: item[0] == key)
        if item is not None:
            bucket.delete(item)
        else:
            raise KeyError('Cannot delete items that dont exist')
        pass

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        keys = []
        for bucket in self.buckets:
            for key, value in bucket:
                keys.append(key)
        return keys
        pass

    def values(self):
        """Return a list of all values in this hash table"""
        # Collect all values in each of the buckets
        values = []
        for bucket in self.buckets:
            for key, value in bucket:
                values.append(value)
        return values
        pass
