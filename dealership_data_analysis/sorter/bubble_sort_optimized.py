from sorter.sorter_adt import Sorter

class BubbleSortOP(Sorter):
    def sort(self, data, key=lambda x: x):
        arr = data.copy()
        n = len(arr)

        for i in range(n):
            swapped = False

            # After each pass, the last i elements are already sorted
            for j in range(0, n - 1 - i):
                if key(arr[j]) > key(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            # If no swaps happened, the list is already sorted
            if not swapped:
                break

        return arr