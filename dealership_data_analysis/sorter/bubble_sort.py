from sorter.sorter_adt import Sorter

class BubbleSort(Sorter):
    def sort(self, data, key=lambda x: x):
        n = len(data)
        # Make a copy so we don't mutate original list (optional)
        arr = data.copy()

        #compare current element and next element and if left > right then swap
        for i in range(n):
            for j in range(0, n - 1):
                if key(arr[j]) > key(arr[j + 1]):
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        return arr