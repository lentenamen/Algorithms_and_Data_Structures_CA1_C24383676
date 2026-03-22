from sorter.sorter_adt import Sorter

class InsertionSort(Sorter):
    def sort(self, data, key=lambda x: x):
        arr = data.copy()
        n = len(arr)

        for i in range(1, n):
            current = arr[i]
            j = i - 1

            # Shift elements to the right until correct spot is found
            while j >= 0 and key(arr[j]) > key(current):
                arr[j + 1] = arr[j]
                j -= 1

            # Insert the element
            arr[j + 1] = current

        return arr
