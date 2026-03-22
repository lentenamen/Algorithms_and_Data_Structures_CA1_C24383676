from sorter.sorter_adt import Sorter

class SelectionSort(Sorter):
    def sort(self, data, key=lambda x: x):
        # make a copy so original list isnt modified
        arr = data.copy()
        n = len(arr)

        # iterate over the position where next min will go
        for i in range(n - 1):
            min_index = i

            # compare next element with assumed min
            for j in range(i + 1, n):
                if key(arr[j]) < key(arr[min_index]):
                    min_index = j

            #if smaller element is found swap it 
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr
