import random
import time


class Search:

    def __init__(self, list_data):
        self.data = list_data

    def linear_search(self, value):
        start_time = time.time()
        for i, val in enumerate(self.data):
            if val == value:
                end_time = time.time()
                print("Total Time taken: %.8f" % (end_time - start_time))
                return i

        end_time = time.time()
        print("Total Time taken: %.8f" % (end_time - start_time))
        return False

    def binary_search(self, value):
        start_time = time.time()
        self.data = sorted(self.data)
        ret_index = self.__re_binary_search(0, len(self.data) - 1, value)
        print(ret_index)
        end_time = time.time()
        print("Total Time taken: %.8f" % (end_time - start_time))
        return ret_index

    def __re_binary_search(self, low, high, value):
        if low > high:
            return 0

        mid = int((low + high) / 2)
        if self.data[mid] == value:
            return mid
        else:
            if self.data[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
            return self.__re_binary_search(low, high, value)

    def interpolation_search(self, value):
        start_time = time.time()
        self.data = sorted(self.data)
        ret_index = self.__re_interpolation_search(0, len(self.data) - 1, value)
        end_time = time.time()
        print("Total Time taken: %.8f" % (end_time - start_time))
        return ret_index

    def __re_interpolation_search(self, low, high, value):

        if low == high or self.data[low] == self.data[high]:
            return 0

        mid = int(low + (high - low) / (self.data[high] - self.data[low]) * (value - self.data[low]))
        if self.data[mid] == value:
            return mid
        else:
            if self.data[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
            return self.__re_interpolation_search(low, high, value)


if __name__ == '__main__':
    data = [random.randint(1, 100) for _ in range(5000000)]
    search_value = 59
    search = Search(data)

    # index = search.linear_search(search_value)
    # index = search.binary_search(search_value)
    index = search.interpolation_search(search_value)

    if index:
        print("{} found in index = {}".format(search_value, index))
    else:
        print("{} not found in the list".format(search_value))