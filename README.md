# From Quantum Computing to the Hidden Subgroup Problem - Thesis Presentation

## Overview

This repository contains the presentation materials for my thesis as part of my Mathematics degree. The thesis explores the necessary quantum computing background needed to study the hidden subgroup problem.

## Tools and Technologies

- **Manim**: Used for creating visualizations in the presentation.
- **Python**: All scripts for generating the presentation visuals.

## Getting Started with Manim in This Repository

If you are new to this repository and would like to work with the Manim animations included, here are the steps you can follow to set up your environment and start rendering the animations.

### 1. Clone the Repository

First, you need to clone this repository to your local machine. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/yourusername/thesis-presentation.git
cd thesis-presentation
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage the dependencies and Python versions for this project. You can create and activate a virtual environment by running:

```bash
# For macOS/Linux:
python3 -m venv env
source env/bin/activate

# For Windows:
python -m venv env
.\env\Scripts\activate
```

### 3. Install Dependencies

Once your virtual environment is activated, you can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Render Manim Animations

To render the Manim animations in this presentation:

```bash
manim-slides render quantum_thesis.py FromQuantumToHSP
```

### 5. Viewing the Animation

After rendering, you can view the interactive presentation by running:

```bash
manim-slides FromQuantumToHSP
```

Also, a compiled video of the presentation slides can be viewed [here](./FromQuantumToHSP.mp4).
