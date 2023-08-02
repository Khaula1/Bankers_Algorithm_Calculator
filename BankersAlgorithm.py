from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def refresh_entries():     
    # Clear the existing entries
        for row_entries in max_entries:
            for entry in row_entries:
                entry.delete(0, END)

        for row_entries in allocation_entries:
            for entry in row_entries:
                entry.delete(0, END)
        
        for entry in available_entries:
            entry.delete(0,END)



def is_safe_state(P, R, Allocation, Max, Available):
    # Initialize the need matrix
    Need = [[0] * R for _ in range(P)]
    
    # Calculate the need matrix
    for i in range(P):
        for j in range(R):
            Need[i][j] = Max[i][j] - Allocation[i][j]
    
    # Initialize the Finish and Work arrays
    Finish = [False] * P
    Work = Available.copy()
    
    # Find a safe sequence
    safe_sequence = []
    while True:
        # Find an index i such that both Finish[i] is False and Need[i] is less than or equal to Work
        found = False
        for i in range(P):
            if not Finish[i] and all(Need[i][j] <= Work[j] for j in range(R)):
                found = True
                break
        
        if not found:
            break
        
        # Add the process i to the safe sequence
        safe_sequence.append(i)
        
        # Update the Work and Finish arrays
        for j in range(R):
            Work[j] += Allocation[i][j]
        Finish[i] = True
    
    # Check if the safe sequence includes all processes
    if len(safe_sequence) == P:
        return True, safe_sequence
    else:
        return False, None


def calculate_safe_sequence():
    # Get the input values
    try:
        P = int(processes_entry.get())
        R = int(resources_entry.get())

        # Get the maximum matrix
        max_matrix = []
        for i in range(P):
            row = []
            for j in range(R):
                value = int(max_entries[i][j].get())
                row.append(value)
            max_matrix.append(row)

        # Get the allocation matrix
        allocation_matrix = []
        for i in range(P):
            row = []
            for j in range(R):
                value = int(allocation_entries[i][j].get())
                row.append(value)
            allocation_matrix.append(row)

        # Get the available resources
        available_resources = []
        for j in range(R):
            value = int(available_entries[j].get())
            available_resources.append(value)
    

        # Check if the state is safe and get the safe sequence
        is_safe, safe_sequence = is_safe_state(P, R, allocation_matrix, max_matrix, available_resources)

        # Display the result
        if is_safe:
            safe_sequence_label.config(text="Safe Sequence \n" + "\n".join(str(p) for p in safe_sequence))
        else:
            safe_sequence_label.config(text="The state is unsafe.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values.")


ws=Tk()
ws.title('Bankers Algorithm')
ws.geometry('1200x800')
ws.configure(bg='lightyellow')



# Create labels and entry fields for processes and resources
processes_label = Label(ws, text="Enter No. of Processes", font= ('Courier 13 bold '),
background="peachpuff2")
processes_label.grid(row=0, column=0, padx=5, pady=7, sticky="e")
processes_entry = Entry(ws, width=15,borderwidth=1, relief='solid')
processes_entry.grid(row=0, column=1, padx=5, pady=7)

resources_label = Label(ws, text="Enter No. of Resources", font= ('Courier 13 bold '),
background="peachpuff2")
resources_label.grid(row=1, column=0, padx=5, pady=7, sticky="e")
resources_entry = Entry(ws, width=15,borderwidth=1, relief='solid')
resources_entry.grid(row=1, column=1, padx=5, pady=7)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MAX ALLOCATION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

max_label = Label(ws, text=" Maximum Allocation :", font= ('Courier 13 bold '),
background="peachpuff2")
max_label.grid(row=2, column=0, padx=50, pady=10, sticky="e")

# Define the headings
column_headings = ['A', 'B', 'C', 'D', 'E']
row_headings = ['P0', 'P1', 'P2', 'P3', 'P4']

# Add column headings
for j, heading in enumerate(column_headings):
    label = Label(ws, text=heading, font=('Arial', 12, 'bold'),background='lightyellow')
    label.grid(row=2, column=j+1, padx=2, pady=2)

# Add row headings
for i, heading in enumerate(row_headings):
    label = Label(ws, text=heading, font=('Arial', 12, 'bold'),background='lightyellow')
    label.grid(row=i+3, column=0, padx=1, pady=2)


max_entries = []
for i in range(5):
    row_entries = []
    for j in range(5):
        entry = Entry(ws, width=15,borderwidth=1, relief='solid')
        entry.grid(row=i+3, column=j+1, padx=2, pady=2)
        row_entries.append(entry)
    max_entries.append(row_entries)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Allocated resources >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Create labels and entry fields for allocation matrix

allocation_label = Label(ws, text=" Allocation Matrix : ", font= ('Courier 13 bold '),
background="peachpuff2")
allocation_label.grid(row=8, column=0, padx=45, pady=10, sticky="e")

# Define the headings
column_headings = ['A', 'B', 'C', 'D', 'E']
row_headings = ['P0', 'P1', 'P2', 'P3', 'P4']


# Add column headings
for j, heading in enumerate(column_headings):
    label = Label(ws, text=heading, font=('Arial', 12, 'bold'),background='lightyellow')
    label.grid(row=8, column=j+1, padx=2, pady=2)

# Add row headings
for i, heading in enumerate(row_headings):
    label = Label(ws, text=heading, font=('Arial', 12, 'bold'),background='lightyellow')
    label.grid(row=i+9, column=0, padx=1, pady=2)

allocation_entries = []
for i in range(5):
    row_entries = []
    for j in range(5):
        entry = Entry(ws, width=15,borderwidth=1, relief='solid')
        entry.grid(row=i+9, column=j+1, padx=2, pady=2)
        row_entries.append(entry)
    allocation_entries.append(row_entries)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Available Matrix>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Create labels and entry fields for available resources
available_label = Label(ws, text=" Available Resources:", font= ('Courier 13 bold '),background="peachpuff2")
available_label.grid(row=14, column=0, padx=50, pady=10, sticky="e")
# Define the headings
column_headings = ['A', 'B', 'C', 'D', 'E']

# Add column headings
for j, heading in enumerate(column_headings):
    label = Label(ws, text=heading, font=('Arial', 12, 'bold'),background='lightyellow')
    label.grid(row=14, column=j+1, padx=2, pady=2)

available_entries = []
for j in range(5):
    entry = Entry(ws, width=15,borderwidth=1, relief='solid')
    entry.grid(row=16, column=j+1, padx=2, pady=2)
    available_entries.append(entry)



# Create a button to calculate the safe sequence
calculate_button = Button(ws, text="Calculate", command= calculate_safe_sequence,activeforeground="red",activebackground="pink", width=10, height=1, borderwidth=3, relief='solid', font='Courier 14 bold')
calculate_button.grid(row=21, column=1, columnspan=5, padx=5, pady=10)

# Create a label to display the safe sequence
safe_sequence_label = Label(ws, text="Safe Sequence", font= ("TIMES NEW ROMAN", 20 ,"bold"),background="peachpuff2")
safe_sequence_label.grid(row=0, column=6, columnspan=6,rowspan=6, padx=80)

refresh_button = Button(ws, text="Refresh", command=refresh_entries,activeforeground="red",activebackground="pink", width=10, height=1, borderwidth=3, relief='solid', font='Courier 14 bold')
refresh_button.grid(row=21, column=3,columnspan=5, padx=5, pady=10)



ws.mainloop()

