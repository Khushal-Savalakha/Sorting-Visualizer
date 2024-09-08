import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while i <= j:
        while i <= j and arr[i] <= pivot:
            visualize_sorting(arr, pivot_index=low, left_index=i, right_index=j)
            i += 1
        while i <= j and arr[j] > pivot:
            visualize_sorting(arr, pivot_index=low, left_index=i, right_index=j)
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            visualize_sorting(arr, pivot_index=low, left_index=i, right_index=j)
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        m = partition(arr, low, high)
        quick_sort(arr, low, m - 1)
        quick_sort(arr, m + 1, high)

def visualize_sorting(arr, pivot_index=None, left_index=None, right_index=None):
    plt.clf()
    colors = ['skyblue'] * len(arr)
    if pivot_index is not None:
        colors[pivot_index] = 'orange'
    if left_index is not None:
        colors[left_index] = 'magenta'
    if right_index is not None:
        colors[right_index] = 'yellow'
    plt.bar(range(len(arr)), arr, color=colors)
    for i in range(len(arr)):
        plt.text(i, arr[i], str(arr[i]), ha='center', va='bottom')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Quick Sort Visualization')
    
    # Create legend patches
    plt.legend(handles=[Patch(color=color, label=label) for color, label in [('orange', 'Pivot'), ('magenta', 'Left Cursor'), ('yellow', 'Right Cursor')]])
    
    plt.pause(2)

def initialize_visualization():
    arr = eval(input("Enter numbers to sort: "))
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)