''' กลุ่ม ขาเขว
 64010736 รุงนภา พฤษพฤก
 64010808 วิภาดา วรสัจจา '''

from tkinter import Tk, Label, Entry, Button, StringVar

def determine_triangle_type():

  try:
    side1 = int(side1_entry.get())
    side2 = int(side2_entry.get())
    side3 = int(side3_entry.get())

    # Check for degenerate case (all zeros)
    if side1 == 0 and side2 == 0 and side3 == 0:
      result_var.set("Triangle with all sides zero doesn't exist.")
      return
  
    # Check for number between 0-999
    if side1 > 999 or side2 > 999 or side3 > 999:
      result_var.set("Please enter a number between 0-999")
      return
  
    # Check for number between 0-999
    if side1 < 0 or side2 < 0 or side3 < 0:
      result_var.set("Please enter a number between 0-999")
      return

    # Check for right triangle using Pythagorean Theorem
    is_right_triangle = False
    if side1**2 + side2**2 == side3**2 or side2**2 + side3**2 == side1**2 or side1**2 + side3**2 == side2**2:
      is_right_triangle = True

    # Check for triangle types based on side lengths
    
    if side1 == side2 and side2 == side3:
      triangle_type = "Equilateral Triangle" #All sides equal
    elif side1 == side2 or side2 == side3 or side1 == side3:
      triangle_type = "Isosceles Triangle" #Two sides equal
    else:
      triangle_type = "Scalene Triangle" #All sides different

    # Combine triangle type and right triangle information
    if is_right_triangle:
      result_var.set("Right Triangle")
    else:
      result_var.set(triangle_type)

  except ValueError:
    # Handle invalid input (non-numeric values)
    result_var.set("Invalid input. Please enter a number between 0-999.")

# Create the main window
root = Tk()
root.geometry("800x500")
root.configure(bg="#D6D7EC")
root.title("Triangle Type Determinator")

side1_label = Label(root, text="Enter the length of sides" ,bg="#D6D7EC" ,font=("Arial", 25))
side1_label.grid(row=0,  columnspan=2 ,padx=100, pady=20)

# Informative labels for side lengths
side1_label = Label(root, text="Side 1",bg="#D6D7EC" ,font=("Arial", 25))
side1_label.grid(row=1, column=0 ,padx=60, pady=15)

side2_label = Label(root, text="Side 2" ,bg="#D6D7EC" ,font=("Arial", 25))
side2_label.grid(row=2, column=0 ,padx=60, pady=15)

side3_label = Label(root, text="Side 3" ,bg="#D6D7EC" ,font=("Arial", 25))
side3_label.grid(row=3, column=0 ,padx=60, pady=15)

# Entry boxes for side lengths
side1_entry = Entry(root,bg="#CCCC02" ,font=("Arial", 25))
side1_entry.grid(row=1, column=1 ,padx=0, pady=10)

side2_entry = Entry(root,bg="#CCCC02" ,font=("Arial", 25))
side2_entry.grid(row=2, column=1 ,padx=0, pady=10)

side3_entry = Entry(root,bg="#CCCC02" ,font=("Arial", 25))
side3_entry.grid(row=3, column=1 ,padx=0, pady=10)

# String variable to hold the result
result_var = StringVar()

# Labels for result
result_label = Label(root, text="Result" ,bg="#D6D7EC" ,font=("Arial", 25))
result_label.grid(row=4, column=1 ,padx=0, pady=15)

result_display = Label(root, textvariable=result_var ,bg="#CCCC02" ,font=("Arial", 25))
result_display.grid(row=5, column=1 ,padx=0, pady=15)

# Button to trigger calculation
calculate_button = Button(root, text="Enter", command=determine_triangle_type ,bg="#CCCC02"  ,font=("Arial", 25))
calculate_button.grid(row=5, columnspan=1 ,padx=0, pady=15)

# Run the main event loop
root.mainloop()