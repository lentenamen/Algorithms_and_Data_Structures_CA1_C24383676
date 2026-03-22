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

# Mileage_by_Year

def time_sort(sorter, data, key_function, runs=3):
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

#years 2020, 2021, 2022, 2023, 2024
def main():
    dataset_years = [2020, 2021, 2022, 2023, 2024]
    loader = VehicleDataLoader("data/source/vehicles.csv")
    algorithms = {
    "Bubble Sort": BubbleSort(),
    "Selection Sort": SelectionSort(),
    "Insertion Sort": InsertionSort(),
    "Quick Sort": QuickSort(),
    "Merge Sort": MergeSort(),
    "Bubble Sort Optimized": BubbleSortOP()
    }

    key_function = lambda vehicle: vehicle.Mileage
    # Store results
    results = {name: [] for name in algorithms.keys()}
    print("\nRunning automated performance analysis...\n")

    for year in dataset_years:
        print(f"Dataset years: {year}")
        data = loader.get_by_year(year)
        for name, sorter in algorithms.items():
            elapsed = time_sort(sorter, data,
            key_function)
            results[name].append(elapsed)
            print(f" {name}: {elapsed:.6f} seconds")
        print()

    # -----------------------------
    # Plot Results
    # -----------------------------
    plt.figure()
    for name, times in results.items():
        sns.lineplot(
            x=dataset_years,
            y=times,
            label=name
        )

    plt.xlabel("Years")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.grid(True)
    plt.legend()

    # Save the figure to a file
    plt.savefig("sorting_performance2.png", dpi=300, bbox_inches="tight")

    plt.show()

if __name__ == "__main__":
    main()