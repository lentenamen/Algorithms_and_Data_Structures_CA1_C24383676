from data_loader.data_loader import VehicleDataLoader
from business.company import Company
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort
from sorter.bubble_sort_optimized import BubbleSortOP
import time

def print_menu():
    print("\n========== Vehicles Data Menu ==========")
    print("1. Show total vehicle count")
    print("2. Choose sorting algorithm")
    print("3. Sort vehicles (using selected algorithm)")
    print("4. Show Top N vehicles")
    print("5. Exit")
    print("=======================================")

def choose_sorter():
    print("\nChoose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")
    print("6. Bubble Sort Optimized")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            return BubbleSort()
        case "2":
            return SelectionSort()
        case "3":
            return InsertionSort()
        case "4":
            return QuickSort()
        case "5":
            return MergeSort()
        case "6":
            return BubbleSortOP()
        case _:
            print("Invalid choice. Defaulting to Quick Sort.")

def main():
    # Load data
    loader = VehicleDataLoader("data/source/vehicles.csv")
    #change size here
    vehicles_data = loader.get_data_by_size(10000)
    # Create company
    company = Company("Dealership", vehicles_data)
    # Default sorter
    current_sorter = QuickSort()

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                print("Total Vehicle Records:",company.total_vehicle_count())
            
            case "2":
                current_sorter = choose_sorter()
                print("Sorting algorithm selected successfully.")

            case "3":
                start = time.perf_counter()
                sorted_vehicles = company.sort_vehicles(
                current_sorter,
                key_function=lambda x: x.Price
                )
                end = time.perf_counter()
                print(f"\nSorting completed in {end - start:.6f} seconds.")
                print("First 5 results by price:")
                for vehicle in sorted_vehicles[:5]:
                    print(vehicle)

            case "4":
                n = int(input("Enter N: "))
                print(f"Retrieving top {n} vehicles using {current_sorter.__class__.__name__}...")
                top_vehicles = company.get_top_vehicles(current_sorter, n)
                print(f"\nTop {n} Vehicles:")
                for vehicle in top_vehicles:
                    print(vehicle)
            
            case "6":
                print("Exiting program...")
                break
            case _:
                print("Invalid choice. Please try again.")