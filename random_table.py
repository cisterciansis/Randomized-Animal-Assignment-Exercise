import tkinter as tk
from tkinter import ttk
import random

# =============================================================================
# Template: Randomized Animal Assignment Exercise
#
# This exercise is designed to help you learn Python GUI programming with Tkinter,
# understand basic randomization, and see how to structure a small application.
#
# What does the program do?
# - It simulates random assignments of animals from 4 cages (each with 5 animals)
#   into 4 treatment groups.
# - In each cage, one treatment group is randomly chosen to get 2 animals,
#   and the remaining 3 groups get 1 animal each.
# - The results are shown in a table. A button lets you re-randomize the assignments.
#
# Exercise ideas:
# 1. Modify the number of cages or animals.
# 2. Change or extend the treatment groups.
# 3. Experiment with different GUI styles or add new features.
#
# Enjoy learning and building Tori!
# =============================================================================

def randomize_assignments():
    """
    Randomly assigns animals from different cages to treatment groups.
    
    There are 4 cages, each with 5 animals (identified by unique ear notches).
    For each cage:
      - One treatment group is randomly selected to get 2 animals.
      - The other groups get 1 animal each.
    
    Returns:
        rows: A list of tuples (cage, ear_notch, group) representing the assignment.
        treatments: A dictionary mapping group names to (Drug, Co-treatment) values.
    """
    cages = [1, 2, 3, 4]
    ear_notches = ["Top Left", "Top Right", "Bottom Left", "Bottom Right", "No Notch"]
    
    # Define treatment groups and their corresponding treatments.
    treatments = {
        "Group1": ("Liraglutide", "Treatment"),
        "Group2": ("Saline", "Treatment"),
        "Group3": ("Saline", "PBS"),
        "Group4": ("Liraglutide", "Saline")
    }
    
    # Shuffle treatment groups to decide which group gets the extra (2 animals) in each cage.
    groups = list(treatments.keys())
    random.shuffle(groups)
    
    rows = []
    for cage in cages:
        # The group that gets 2 animals in this cage.
        extra_group = groups[cage - 1]  
        # The remaining groups get 1 animal each.
        other_groups = [g for g in treatments if g != extra_group]
        
        # Shuffle ear notches for random assignment within the cage.
        ear_list = ear_notches.copy()
        random.shuffle(ear_list)
        
        # Assign two animals to the extra group.
        rows.append((cage, ear_list[0], extra_group))
        rows.append((cage, ear_list[1], extra_group))
        
        # Randomize the order of the other groups and assign one animal each.
        random.shuffle(other_groups)
        for i, group in enumerate(other_groups):
            rows.append((cage, ear_list[i + 2], group))
            
    return rows, treatments

def update_table(tree):
    """
    Clears and updates the table with new randomized assignments.
    
    Args:
        tree: The Treeview widget that displays the table.
    """
    # Clear all existing rows from the table.
    for row in tree.get_children():
        tree.delete(row)
    
    # Generate new assignments.
    rows, treatments = randomize_assignments()
    
    # Insert each new row into the table.
    for cage, ear, group in rows:
        drug, cotreatment = treatments[group]
        tree.insert("", "end", values=(cage, ear, drug, cotreatment))

# =============================================================================
# Main Application Window Setup
# =============================================================================

# Create the main window.
root = tk.Tk()
root.title("Randomized Animal Assignments - Python Exercise")
root.geometry("600x400")  # Adjust the window size as needed.

# Set a theme for a clean look using ttk styles.
style = ttk.Style(root)
style.theme_use("clam")  # Experiment with 'clam', 'alt', 'default', etc.

# =============================================================================
# Creating the Table
# =============================================================================

# Create a Treeview widget to display the table.
columns = ("Cage", "Ear Notch", "Drug", "Co-treatment")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Configure the table headers and set column properties.
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=140, anchor="center")
tree.pack(fill="both", expand=True, padx=10, pady=10)

# =============================================================================
# Creating the Randomize Button
# =============================================================================

# Create a frame to hold the button.
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Create a button that re-randomizes the assignments when clicked.
randomize_button = tk.Button(button_frame, text="Randomize", font=("Helvetica", 12),
                             command=lambda: update_table(tree))
randomize_button.pack()

# =============================================================================
# Initialize the Table and Run the Application
# =============================================================================

# Populate the table with initial random assignments.
update_table(tree)

# Start the Tkinter event loop.
root.mainloop()
