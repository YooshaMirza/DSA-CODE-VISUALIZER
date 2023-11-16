import tkinter as tk
import time

root = tk.Tk()
root.title("Algorithm Visualizer")
root.geometry("800x600")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

data = [64, 34, 25, 12, 22, 11, 90]

def draw_bars(data, selected=[]):
    canvas.delete("all")
    canvas_width = 600
    canvas_height = 400
    bar_width = canvas_width / len(data)
    offset = 10
    for i, height in enumerate(data):
        color = "sky blue" if i in selected else "light green"
        x0 = i * bar_width + offset
        y0 = canvas_height - height
        x1 = (i + 1) * bar_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(height))

    root.update()

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_bars(data)
                time.sleep(0.5)

def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
            draw_bars(data, [i, j])
            time.sleep(0.5)
        data[i], data[min_index] = data[min_index], data[i]
        draw_bars(data, [i])
        time.sleep(0.5)

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_bars(data, [i, j + 1])
            time.sleep(0.5)
        data[j + 1] = key
        draw_bars(data, [i, j + 1])
        time.sleep(0.5)

def linear_search(data, target):
    for i in range(len(data)):
        draw_bars(data, [i])
        time.sleep(0.5)
        if data[i] == target:
            draw_bars(data, [i])
            return i
    return -1

def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            draw_bars(data, [mid])
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        draw_bars(data, [mid, left, right])
        time.sleep(0.5)
    return -1

def run_algorithm(algorithm):
    global data
    if algorithm == 'Bubble Sort':
        bubble_sort(data)
    elif algorithm == 'Selection Sort':
        selection_sort(data)
    elif algorithm == 'Insertion Sort':
        insertion_sort(data)

def search_data(algorithm):
    target = int(entry.get())
    if algorithm == 'Linear Search':
        result = linear_search(data, target)
    elif algorithm == 'Binary Search':
        result = binary_search(data, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")

def set_input():
    global data
    input_string = entry.get()
    data = list(map(int, input_string.split(',')))
    draw_bars(data)

# Menu for algorithms
menubar = tk.Menu(root)

# Submenu for sorting algorithms
sort_menu = tk.Menu(menubar, tearoff=0)
sort_menu.add_command(label="Bubble Sort", command=lambda: run_algorithm('Bubble Sort'))
sort_menu.add_command(label="Selection Sort", command=lambda: run_algorithm('Selection Sort'))
sort_menu.add_command(label="Insertion Sort", command=lambda: run_algorithm('Insertion Sort'))

# Submenu for search algorithms
search_menu = tk.Menu(menubar, tearoff=0)
search_menu.add_command(label="Linear Search", command=lambda: search_data('Linear Search'))
search_menu.add_command(label="Binary Search", command=lambda: search_data('Binary Search'))

# Adding both submenus to the main menu
menubar.add_cascade(label="Sorting Algorithms", menu=sort_menu)
menubar.add_cascade(label="Search Algorithms", menu=search_menu)

# Setting the menu for the root window
root.config(menu=menubar)

# Entry for setting custom input
entry_label = tk.Label(root, text="Enter numbers:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()
set_button = tk.Button(root, text="Enter", command=set_input)
set_button.pack()

draw_bars(data)

root.mainloop()
