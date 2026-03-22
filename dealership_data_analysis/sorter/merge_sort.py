from sorter.sorter_adt import Sorter

class MergeSort(Sorter):
    def sort(self, data, key=lambda x: x):
        arr = data.copy()

        def merge(left, right):
            result = []
            i = j = 0

            # Merge while both lists have elements
            while i < len(left) and j < len(right):
                if key(left[i]) <= key(right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Add remaining elements from left 
            while i < len(left):
                result.append(left[i])
                i += 1

            # Add remaining elements from right 
            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        def mergesort(list):
            if len(list) <= 1:
                return list

            mid = len(list) // 2
            left = mergesort(list[:mid])
            right = mergesort(list[mid:])
            return merge(left, right)

        return mergesort(arr)