import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def plot_snow_peak(incline):
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

    # Define the range of x and y values for the snow peak
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)

    # Define the z values for the snow peak
    z = x**2 + y**2

    # Apply incline
    z = z * np.sin(np.radians(incline))

    # Plot the snow peak
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Snow Peak with {incline} Degree Incline')

    return fig

def update_plot():
    incline = incline_var.get()
    fig = plot_snow_peak(incline)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)

app = tk.Tk()
app.title("Snow Peak Incline Visualizer")

frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10)

# Set default value to -50 degrees
incline_var = tk.DoubleVar(value=-50)

incline_label = ttk.Label(frame, text="Incline (degrees):")
incline_label.grid(row=0, column=0, padx=5, pady=5)
incline_entry = ttk.Entry(frame, textvariable=incline_var)
incline_entry.grid(row=0, column=1, padx=5, pady=5)

plot_button = ttk.Button(frame, text="Plot Snow Peak", command=update_plot)
plot_button.grid(row=0, column=2, padx=5, pady=5)

app.mainloop()
