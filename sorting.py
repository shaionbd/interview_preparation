import random
import time


class Sorting:

    def __init__(self, data):
        self.data = data
        self.is_sorted = False
        self.n = len(data)

    def bubble_sort(self, indexed_by=False):
        start_time = time.time()
        for i in range(len(self.data)-1):
            is_swapped = False
            for j in range(len(self.data)-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    is_swapped = True
            if not is_swapped:
                break
        self.is_sorted = True
        end_time = time.time()
        print("Bubble sort Total Time taken: %.4f" % (end_time - start_time))

    def insertion_sort(self, left=0, right=None, is_print=True):
        start_time = time.time()
        if not right:
            right = self.n
        for i in range(left+1, right+1):
            val = self.data[i]
            j = i - 1
            while j >= left and self.data[j] > val:
                self.data[j+1] = self.data[j]
                j -= 1
            self.data[j+1] = val
        self.is_sorted = True
        end_time = time.time()
        if is_print:
            print("Insert sort Total Time taken: %.4f" % (end_time - start_time))

    def selection_sort(self):
        start_time = time.time()
        for i in range(len(self.data)-1):
            min_index = i
            for j in range(i+1, len(self.data)):
                if self.data[min_index] > self.data[j]:
                    min_index = j
            if min_index != i:
                self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

        self.is_sorted = True
        end_time = time.time()
        print("Selection Sort Total Time taken: %.4f" % (end_time - start_time))

    def mergesort(self):
        start_time = time.time()
        self.data = self.__merge_sort(self.data)
        self.is_sorted = True
        end_time = time.time()
        print("Merge sort Total Time taken: %.4f" % (end_time - start_time))

    def __merge_sort(self, list_data):
        n = len(list_data)
        if n == 1:
            return list_data
        left = list_data[: int(n/2)]
        right = list_data[int(n/2):]
        l1 = self.__merge_sort(left)
        l2 = self.__merge_sort(right)

        return self.__merge(l1, l2)

    def __merge(self, list1, list2):

        if not len(list1) or not len(list2):
            return list1 or list2

        merge_list = list()
        i = j = 0
        while len(merge_list) < len(list1) + len(list2):
            if list1[i] < list2[j]:
                merge_list.append(list1[i])
                i += 1
            else:
                merge_list.append(list2[j])
                j += 1
            if i == len(list1) or j == len(list2):
                merge_list.extend(list1[i:] or list2[j:])
                break
        return merge_list

    def __partition_func(self, left, right, pivot):
        left_pointer = left - 1

        for i in range(left, right):
            if self.data[i] <= pivot:
                left_pointer += 1
                self.data[left_pointer], self.data[i] = self.data[i], self.data[left_pointer]
        self.data[left_pointer+1], self.data[right] = self.data[right], self.data[left_pointer+1]
        return left_pointer

    def __quicksort(self, left, right):
        if right <= left:
            return
        else:
            pivot = self.data[right]
            partition = self.__partition_func(left, right, pivot)
            self.__quicksort(left, partition-1)
            self.__quicksort(partition+1, right)

    def quick_sort(self):
        start_time = time.time()
        n = len(self.data)
        self.__quicksort(0, n-1)
        self.is_sorted = True
        end_time = time.time()
        print("Total Time taken: %.4f" % (end_time - start_time))

    def tim_sort(self):
        """
        # ===================================================================================================== #
        #   We divide the Array into blocks known as Run. We sort those runs using insertion sort one by one    #
        #   and then merge those runs using combine function used in merge sort. If the size of Array is        #
        #   less than run, then Array get sorted just by using Insertion Sort. The size of run may vary         #
        #   from 32 to 64 depending upon the size of the array. Note that merge function performs well          #
        #   when sizes subarrays are powers of 2. The idea is based on the fact that insertion sort             #
        #   performs well for small arrays.                                                                     #
        # ===================================================================================================== #
        """
        start_time = time.time()
        RUN = 32
        n = len(self.data)
        for i in range(0, n, RUN):
            self.insertion_sort(left=i, right=min((i+(RUN-1)), (n-1)), is_print=False)
        jump = RUN
        while jump < n:
            for left in range(0, n, 2*jump):
                right = left + jump -1
                left_data = self.data[0:left]
                right_data = self.data[left: right]
                merge_data = self.__merge(left_data, right_data)
                self.data[0:right] = merge_data
            jump *= 2
        self.is_sorted = True
        end_time = time.time()
        print("Total Time taken: %.4f" % (end_time - start_time))

    def get_sorted_data(self):
        if self.is_sorted:
            self.is_sorted = False
            return self.data
        elif not self.data:
            return "Not data found!"
        return "Data is not sorted!"

    def get_unsort_data(self):
        if not self.is_sorted:
            return self.data
        elif not self.data:
            return "Not data found!"
        return "Data is sorted!"


if __name__ == '__main__':
    unsorted_data = [random.randint(1, 100) for _ in range(5000)]
    # unsorted_data = [random.randint(1, 100) for _ in range(10000)]
    # print(unsorted_data)
    sort = Sorting(unsorted_data)
    # sort.bubble_sort()
    # print(sort.get_sorted_data())
    # sort.insertion_sort(left=2, right=5000)
    # print(sort.get_sorted_data())
    # sort.selection_sort()
    # print(sort.get_sorted_data())
    # sort.mergesort()
    # print(sort.get_sorted_data())
    # sort.quick_sort()
    # print(sort.get_sorted_data())
    # print(sort.get_unsort_data())
    sort.tim_sort()
    print(sort.get_sorted_data())

    # bubble sort execution time = 3.8635
    # insertion sort execution time = 1.1994
    # selection sort execution time = 1.0255
    # merge sort execution time = 0.0660
    # quick sort execution time = 0.0241
    # Tim sort execution time = 0.0682
