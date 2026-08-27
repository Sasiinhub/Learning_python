'''import tkinter as tk

root = tk.Tk()
root.title("Single line")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
canvas.create_line(100,100,350,100)
root.mainloop()
'''



'''
#import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# 1. Turn on the grid lines
plt.grid(True, color='green', linestyle='-', linewidth=0.5)

# 2. Set the background color to a very light green (mint)
plt.gca().set_facecolor('#E8F5E9') 

# 3. Show your graph paper!
plt.show()

'''


import matplotlib.pyplot as plt

# 1. Provide the X coordinates, then the Y coordinates
# Line goes from point (1, 2) to point (5, 10)
x_coordinates = [1, 10]
y_coordinates = [5, 5]

# 2. Plot the line
plt.plot(x_coordinates, y_coordinates, color='blue', linewidth=3)

# 3. Open the window and display the graph paper
plt.show()

