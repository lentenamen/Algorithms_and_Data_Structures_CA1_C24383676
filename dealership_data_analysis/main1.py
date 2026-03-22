import time
import matplotlib.pyplot as plt
import seaborn as sns

from data_loader.data_loader import VehicleDataLoader
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort
from sorter.bubble_sort_optimized import BubbleSortOP

# Price_by_size

def time_sort(sorter, data, key_function, runs=1):
    """
    Returns average execution time over multiple runs
    (reduces timing noise).
    """
    total = 0
    for _ in range(runs):
        data_copy = data.copy()
        start = time.perf_counter()
        sorter.sort(data_copy, key=key_function)
        end = time.perf_counter()
        total += (end - start)
    return total / runs

#sizes 250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000
def main():
    dataset_sizes = [250, 500, 1000, 2000, 4000, 8000]
    loader = VehicleDataLoader("data/source/vehicles.csv")
    algorithms = {
    "Bubble Sort": BubbleSort(),
    "Selection Sort": SelectionSort(),
    "Insertion Sort": InsertionSort(),
    "Quick Sort": QuickSort(),
    "Merge Sort": MergeSort(),
    "Bubble Sort Optimized": BubbleSortOP()
    }

    key_function = lambda vehicle: vehicle.Price
    # Store results
    results = {name: [] for name in algorithms.keys()}
    print("\nRunning automated performance analysis...\n")

    for size in dataset_sizes:
        print(f"Dataset size: {size}")
        data = loader.get_data_by_size(size)
        for name, sorter in algorithms.items():
            elapsed = time_sort(sorter, data,
            key_function)
            results[name].append(elapsed)
            print(f" {name}: {elapsed:.6f} seconds")
        print()

    # -----------------------------
    # Plot Results up to 8000
    # The 8000 was manually changed in dataset_sizes
    # -----------------------------
    # used seaborn to save png rather than run it for ages
    plt.figure()
    for name, times in results.items():
        sns.lineplot(
            x=dataset_sizes,
            y=times,
            label=name
        )

    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.grid(True)
    plt.legend()

    # Save the figure to a file
    plt.savefig("sorting_performance.png", dpi=300, bbox_inches="tight")

    plt.show()

if __name__ == "__main__":
    main()