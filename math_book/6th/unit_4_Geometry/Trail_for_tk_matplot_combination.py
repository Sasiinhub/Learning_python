import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GeometryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hybrid Geometry App")
        
        # 1. Create a standard Matplotlib figure and 50x50 grid
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.ax.set_facecolor('#C8E6C9') 
        self.ax.set_xlim(0, 50)
        self.ax.set_ylim(0, 50)
        self.ax.grid(True, color='#81C784')
        
        # 2. EMBED the Matplotlib chart into our Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # 3. Add a standard Tkinter Button to trigger the growth loop
        self.btn = tk.Button(self.root, text="Grow Ray Dynamically", command=self.start_growth)
        self.btn.pack(side=tk.BOTTOM, pady=10)
        
        # Initialize ray data
        self.ray_x = [5]
        self.ray_y = [5]
        self.line, = self.ax.plot([], [], color='black', linewidth=2)

    def start_growth(self):
        """A clean Tkinter-managed loop to step-by-step grow a Matplotlib line."""
        current_x = self.ray_x[-1]
        current_y = self.ray_y[-1]
        
        if current_x < 45:
            # Grow the line data coordinates by 1 unit
            self.ray_x.append(current_x + 1)
            self.ray_y.append(current_y + 1)
            
            # Update the line with new coordinates
            self.line.set_data(self.ray_x, self.ray_y)
            
            # Redraw just the canvas cleanly
            self.canvas.draw_idle()
            
            # Tell Tkinter to repeat this function in 50 milliseconds (The loop)
            self.root.after(50, self.start_growth)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryApp(root)
    root.mainloop()



