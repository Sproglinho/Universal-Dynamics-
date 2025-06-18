# Recursive Phase Solids

This repository implements the mathematical framework introduced in the paper:

**“Recursive Phase Rotors and Platonic Orbits on \( S^3 \)”**

The project generates all five Platonic solids by projecting a discrete sequence of quaternionic vectors on the 3-sphere \( S^3 \) into \( \mathbb{R}^3 \) using stereographic projection. These vectors are derived from phase-rotating exponential maps indexed recursively.

## 📐 Mathematical Background

The main map is defined as:
\[
q_n = (\cos \theta_n, \sin \theta_n, \cos 2\theta_n, \sin 2\theta_n), \quad \theta_n = \pi \cdot 2^n
\]
with normalization:
\[
\hat{q}_n = \frac{1}{\sqrt{2}} q_n \in S^3
\]

These rotors are projected into \( \mathbb{R}^3 \) using:
\[
\Pi(x, y, z, w) = \left( \frac{x}{1 - w}, \frac{y}{1 - w}, \frac{z}{1 - w} \right)
\]

By selecting finite index sets \( \mathcal{N}_{\text{solid}} \), one obtains the canonical vertex sets of the tetrahedron, cube, octahedron, icosahedron, and dodecahedron.

Theoretical details and proofs are given in the associated paper.

## 📁 Repository Contents

| File | Purpose |
|------|---------|
| `recursive_phase.py` | Core implementation of rotors, projection, and solid generation |
| `verify.py` | Edge-length checks and symmetry tests |
| `plot_solids.py` | 3D visualization using `matplotlib` |
| `notebook.ipynb` | Interactive demo with explanations and validation |
| `requirements.txt` | Dependencies (`numpy`, `matplotlib`, `scipy`) |
| `data/` | Optional: stores precomputed or exported vertex data |

## 🧪 How to Use

Clone the repository:

```bash
git clone https://github.com/your-username/recursive-phase-solids.git
cd recursive-phase-solids
pip install -r requirements.txt

<!-- Project documentation should be pasted here manually. -->
