# Orbital-Shape-Visualizer

## Project Description

The **Orbital Shape Visualizer** is a computational chemistry project that visualizes atomic orbitals in 3D using Python. It helps in understanding the shapes of electron probability distributions derived from **Quantum Mechanics** and the **Schrödinger Equation**.

This project provides an interactive way to explore:

* s-orbital (spherical)
* p-orbital (dumbbell-shaped)
* d-orbital (complex clover shapes)

---

## Objectives

* To visualize atomic orbitals in 3D
* To understand electron density distribution
* To apply computational techniques in chemistry
* To create an interactive learning tool

---

## Technologies Used

* Python
* NumPy
* Plotly (for 3D visualization)
* Tkinter (for GUI)

---

## Features

* 3D interactive orbital visualization
* Supports s, p, and d orbitals
* GUI with buttons (no typing required)
* Rotation and zoom functionality
* Simple and user-friendly interface

---

## Project Structure

```
orbital-shape-visualizer/
│── main.py
│── gui.py
│── orbitals/
│    ├── s_orbital.py
│    ├── p_orbital.py
│    ├── d_orbital.py
│── requirements.txt
│── README.md
```

---

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/orbital-shape-visualizer.git
```

2. Navigate to the folder:

```
cd orbital-shape-visualizer
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## How to Run

### Run Terminal Version

```
python main.py
```

Enter:

* `1` → s-orbital
* `2` → p-orbital
* `3` → d-orbital

---

### Run GUI Version (Recommended)

```
python gui.py
```

Click buttons to visualize orbitals.

---

## Output

* s-orbital → spherical shape
* p-orbital → dumbbell shape
* d-orbital → complex clover shape

Interactive 3D graph opens in browser with zoom and rotation.

---

## Screenshots


### s orbital
<img width="1352" height="682" alt="Screenshot 2026-04-11 195450" src="https://github.com/user-attachments/assets/c27fd4fd-21c3-44f2-a553-f8732e4b4d4e" />


### p orbital
<img width="672" height="631" alt="Screenshot 2026-04-11 194936" src="https://github.com/user-attachments/assets/9058f07e-cff1-4f15-b2a7-d9434cf546f8" />


### d orbital
<img width="673" height="632" alt="Screenshot 2026-04-11 195135" src="https://github.com/user-attachments/assets/f5cdc98d-5ee4-4d07-83f1-42ef6605ce3e" />


---

## Theory

Atomic orbitals represent the probability distribution of electrons around the nucleus.
These shapes are obtained by solving the Schrödinger Equation in Quantum Mechanics.

* **s-orbital**: Spherical symmetry
* **p-orbital**: Two lobes along axes
* **d-orbital**: Complex multi-lobed shapes

---

## Future Enhancements

* Add color coding for positive and negative phases
* Include more orbitals (f-orbitals)
* Develop web-based visualization
* Add animations

---

## Author

Leena Vaishnav (25BCE11206)


---

## 📄 License

This project is for educational purposes.
