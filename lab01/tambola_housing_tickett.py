import tkinter as tk
import numpy as np

# Functions from your original code
def generate_matrix():
    matrix = np.zeros((3, 9), dtype=int)
    for row in range(3):
        indices = np.random.choice(9, size=5, replace=False)
        numbers = np.arange(row*9 + 1, row*9 + 10)
        matrix[row, indices] = numbers[:5]

    for col in range(matrix.shape[1]):
        if np.all(matrix[:, col] == 0):
            random_row = np.random.randint(0, matrix.shape[0])
            matrix[random_row, col] = col * 9 + 1 + random_row    
    return matrix

def modify_matrix(matrix):
    for col in range(matrix.shape[1]):
        min_val = col * 10 + 1
        max_val = min_val + 9
        for row in range(matrix.shape[0]):
            if matrix[row, col] > 0:
                matrix[row, col] = np.random.randint(min_val, max_val + 1)
    return matrix

def sort_columns(matrix):
    for col in range(matrix.shape[1]):
        non_zero_values = sorted([val for val in matrix[:, col] if val > 0])
        non_zero_idx = 0
        for row in range(matrix.shape[0]):
            if matrix[row, col] > 0:
                matrix[row, col] = non_zero_values[non_zero_idx]
                non_zero_idx += 1
    return matrix

# GUI function to display the matrix
def display_matrix(matrix):
    root = tk.Tk()
    root.title("Ticket Matrix")

    colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845']  # Example color palette

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            value = matrix[row, col]
            if value > 0:
                label = tk.Label(root, text=str(value), bg=colors[col % len(colors)], 
                                 font=("Helvetica", 16), width=5, height=2, borderwidth=2, relief="groove")
                label.grid(row=row, column=col, padx=5, pady=5)
            else:
                label = tk.Label(root, text="", width=5, height=2)
                label.grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()

# Generate, modify, and sort the matrix
matrix = generate_matrix()
modified_matrix = modify_matrix(matrix)
sorted_matrix = sort_columns(modified_matrix)

# Display the matrix with GUI
display_matrix(sorted_matrix)
