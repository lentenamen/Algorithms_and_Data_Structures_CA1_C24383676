from sorter.sorter_adt import Sorter

class QuickSort(Sorter):
    def sort(self, data, key=lambda x: x):
        #copy
        arr = data.copy()

        def partition(data, low, high):
            #choose last element as the pivot
            pivot = data[high]
            i = low - 1

            #scan through subarrays and move smaller elements into proper regions
            for j in range(low, high):
                if key(data[j]) <= key(pivot):
                    i += 1
                    
                    data[i], data[j] = data[j], data[i]

            data[i + 1], data[high] = data[high], data[i + 1]
            return i + 1

        #recursive quicksort
        def quicksort(data, low=0, high=None):
            if high is None:
                high = len(data) - 1

            if low < high:
                pivot_index = partition(data, low, high)
                #sort left partition
                quicksort(data, low, pivot_index - 1)
                #sort right
                quicksort(data, pivot_index + 1, high)

        quicksort(arr)
        return arr
    