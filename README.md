# 🧭 Pathfinding Visualizer – School Project for Algorithmics Class

This project visualizes the behavior of pathfinding algorithms (**A\*** and **Dijkstra**) on a 2D grid. It allows interactive placement of obstacles, start and end points, and lets you observe how the algorithms find the shortest path.

---

## 🛠️ Technologies Used

- **Python 3**
- **Pygame** – for rendering and input handling

---

## 🔍 Features

- Interactive, resizable grid
- Set:
  - **Start** point
  - **End** point
  - **Walls** (obstacles)
- Two pathfinding algorithms:
  - `A*` (press **A**)
  - `Dijkstra` (press **D**)
- Reset the grid (press **R**)
- Color legend and usage instructions displayed on screen

---

## 🎨 Color Legend

| Element       | Color         |
|---------------|---------------|
| Start         | Green         |
| End           | Red           |
| Wall          | Black         |
| Open tile     | Turquoise     |
| Closed tile   | Purple        |
| Final path    | Yellow        |
| Empty tile    | White         |

---

## 🎮 Controls

- **Left Mouse Button** – draw start, end, or walls
- **Right Mouse Button** – erase tiles
- **A** – run A\* algorithm
- **D** – run Dijkstra's algorithm
- **R** – reset the grid

---

## 🧠 What I Learned

- How A\* and Dijkstra's algorithms work and how to implement them
- Basics of working with **Pygame**: rendering, handling input, etc.
- Organizing code in a modular way
- Representing graphs as 2D grids (adjacency via neighbors)

---

## 📁 File Structure
```bash
project-root/
│
├── src/
│   ├── main.py         # Main game loop and event handling
│   ├── astar.py        # A* algorithm implementation
│   ├── dikstra.py      # Dijkstra's algorithm implementation
│   ├── tile.py         # Tile class – represents one cell on the grid
│   ├── config.py       # Constants: colors, grid size, cell size, etc.
│
├── README.md           # Project description and documentation
├── requirements.txt    # Dependencies (e.g., pygame)
```
---

## ✅ Requirements

- Python 3.8+
- Pygame (`pip install pygame`) or (`pip install -r requirements.txt`)

---

## 🚀 How to Run

From the `src` folder, run:

```bash
python main.py
```

Thanks for checking out my project! 🎓 Feel free to explore and modify the code.
