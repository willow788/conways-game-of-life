# Conway’s Game of Life — Interactive Visualization

An interactive implementation of **Conway’s Game of Life**, a classic cellular automaton demonstrating emergent behavior from simple local rules.
This project features real-time animation, user interaction, age-based coloring, and efficient neighbor computation using convolution.

---

## Features

* Interactive grid with mouse and keyboard controls
* Age-based cell coloring to visualize cell longevity
* Efficient neighbor counting using 2D convolution
* Toroidal grid (wrap-around edges)
* Preset pattern support (Glider)
* Pause, reset, and clear functionality
* Real-time animation using Matplotlib

---

## Rules of the Game

Each cell follows four simple rules:

1. A live cell with fewer than two neighbors dies
2. A live cell with two or three neighbors survives
3. A live cell with more than three neighbors dies
4. A dead cell with exactly three neighbors becomes alive

Despite their simplicity, these rules produce complex and unpredictable patterns over time.

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* SciPy

---

## Installation

Install the required dependencies:

```bash
pip install numpy matplotlib scipy
```

---

## Usage

Run the script:

```bash
python game_of_life.py
```

---

## Controls

| Action         | Key / Mouse |
| -------------- | ----------- |
| Toggle cell    | Mouse click |
| Pause / Resume | Space       |
| Randomize grid | `r`         |
| Clear grid     | `c`         |
| Spawn glider   | `g`         |

---

## Visualization

* Cell color intensity represents **cell age**
* Older cells appear brighter, creating visible trails
* The grid wraps around edges, allowing continuous motion

---

## Project Structure

```text
.
├── game_of_life.py
└── README.md
```

---

## Learning Outcomes

* Understanding cellular automata and emergent behavior
* Applying convolution for efficient neighbor computation
* Building interactive visualizations in Python
* Managing real-time animation and user input

---

## Future Enhancements

* Additional preset patterns
* GIF or video export
* Rule customization
* Speed control via UI
* Multi-state cellular automata

---

## License

This project is released under the MIT License.

