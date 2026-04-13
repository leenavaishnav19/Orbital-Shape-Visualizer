import tkinter as tk
from tkinter import messagebox
import plotly.graph_objects as go

from s_orbital import generate_s_orbital
from p_orbital import generate_p_orbital
from d_orbital import generate_d_orbital


# Function to plot orbital
def plot_orbital(x, y, z, title):
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        )
    )

    fig.show()


# Button functions
def show_s():
    x, y, z = generate_s_orbital()
    plot_orbital(x, y, z, "s-Orbital")


def show_p():
    x, y, z = generate_p_orbital()
    plot_orbital(x, y, z, "p-Orbital")


def show_d():
    x, y, z = generate_d_orbital()
    plot_orbital(x, y, z, "d-Orbital")


# Create window
root = tk.Tk()
root.title("Orbital Shape Visualizer")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="Orbital Shape Visualizer", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Buttons
btn_s = tk.Button(root, text="Show s-Orbital", width=20, command=show_s)
btn_s.pack(pady=10)

btn_p = tk.Button(root, text="Show p-Orbital", width=20, command=show_p)
btn_p.pack(pady=10)

btn_d = tk.Button(root, text="Show d-Orbital", width=20, command=show_d)
btn_d.pack(pady=10)

# Exit button
btn_exit = tk.Button(root, text="Exit", width=20, command=root.quit)
btn_exit.pack(pady=20)

# Run app
root.mainloop()
