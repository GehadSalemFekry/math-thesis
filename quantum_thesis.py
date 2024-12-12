from manim import *
from manim_slides import Slide
import random
import numpy as np

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\newcommand{\ket}[1]{\left| #1 \right\rangle}")
myTemplate.add_to_preamble(r"\newcommand{\bra}[1]{\left\langle #1 \right|}")
myTemplate.add_to_preamble(
    r"\newcommand{\braket}[2]{\left\langle #1 \vphantom{#2} \right| \left. #2 \vphantom{#1} \right\rangle}"
)


class FromQuantumToHSP(Slide):
    def clear(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def add_slide_number(self, current_slide):
        slide_number = Text(f"{current_slide}", font_size=24, color=GRAY).to_corner(
            DOWN + RIGHT
        )
        self.add(slide_number)

    def intro(self):
        title_tex = Tex(
            r"From Quantum Computing\\to the Hidden Subgroup Problem",  # Added line break
            color=ORANGE,
            font_size=60,  # Increased font size for the title
        )
        title_tex.shift(2 * UP)
        self.play(Write(title_tex))

        author = Tex(
            r"Author: {Gehad Salem}", color=GREEN, font_size=40
        )  # Increased font size
        gold = ManimColor.from_rgb((229, 184, 11))
        supervisors = Tex(
            r"Supervisor: {Dr. Isabel Müller}",
            color=gold,
            font_size=50,  # Increased font size
        )
        author.next_to(title_tex, DOWN)
        author.shift(DOWN)
        supervisors.next_to(author, DOWN)
        self.play(Write(author))
        self.play(Write(supervisors))

        senior_thesis = Tex(
            r"\textit{Mathematics Senior Thesis - Fall 2024}",
            color=WHITE,
            font_size=40,  # Increased font size
        )
        senior_thesis.next_to(supervisors, DOWN)
        senior_thesis.shift(DOWN)
        auc = Tex(
            r"{The American University in Cairo}", color=WHITE, font_size=40
        )  # Increased font size
        auc.next_to(senior_thesis, DOWN)
        self.play(Write(senior_thesis))
        self.play(Write(auc))
        self.next_slide()
        self.clear()

    def table_of_contents(self):
        self.add_slide_number(2)

        title = Tex("Table of Content", font_size=48, color=BLUE)
        title.to_edge(UP)

        contents = (
            VGroup(
                Tex("1. What is a Qubit?", font_size=36, color=YELLOW),
                Tex("2. Quantum Circuits", font_size=36, color=YELLOW),
                Tex("3. Motivating Problems", font_size=36, color=YELLOW),
                Tex("4. Hidden Subgroup Problem", font_size=36, color=YELLOW),
            )
            .arrange(DOWN, buff=0.5)
            .next_to(title, DOWN, buff=1.5)
        )

        self.play(Write(title))
        self.play(
            LaggedStart(*[Write(item) for item in contents], lag_ratio=0.5), run_time=2
        )
        self.next_slide()
        self.clear()

    def classical_quantum_computation(self):
        self.add_slide_number(3)
        classical_label = Tex(
            "Classical Computation",
            color=BLUE,
            font_size=48,  # Increased font size
        ).to_edge(UP)
        self.play(Write(classical_label))

        # Label for "Bit"
        bit_label = Tex("Bit Stream:", font_size=42, color=ORANGE).next_to(
            classical_label, DOWN, buff=1.5
        )
        self.play(Write(bit_label))

        # Create and display bit stream
        bit_stream = VGroup(
            *[
                Tex(f"{bit}", font_size=38, color=WHITE).move_to(LEFT * (5 - i / 2))
                for i, bit in enumerate("0110101101" * 2)
            ]
        )
        # self.play(
        #     LaggedStart(
        #         *[Write(bit) for bit in bit_stream], lag_ratio=0.1, run_time=0.3
        #     )
        # )  # Faster display with less delay
        for bit in bit_stream:
            self.play(Write(bit), run_time=0.2)

        self.next_slide()
        self.play(FadeOut(bit_stream), FadeOut(bit_label))
        self.add_slide_number(4)

        zero_circle = Circle(radius=1.5, fill_color=BLACK, fill_opacity=1, color=BLUE)
        zero_label = Tex("Bit", font_size=42, color=BLUE).next_to(
            zero_circle, UP, buff=0.1
        )
        zero_text = Tex("0", color=YELLOW, font_size=48).next_to(
            zero_circle, RIGHT, buff=0.5
        )

        # Create the second circle (light/1)
        one_circle = Circle(radius=1.5, fill_color=WHITE, fill_opacity=1, color=BLUE)
        one_label = Tex("Bit", font_size=42, color=BLUE).next_to(
            one_circle, UP, buff=0.1
        )
        one_text = Tex("1", color=YELLOW, font_size=48).next_to(
            one_circle, RIGHT, buff=0.5
        )

        # Position the circles side by side
        zero_circle.shift(LEFT * 3)
        zero_label.shift(LEFT * 3)
        zero_text.shift(LEFT * 3)

        one_circle.shift(RIGHT * 3)
        one_label.shift(RIGHT * 3)
        one_text.shift(RIGHT * 3)

        self.play(Write(zero_label), Write(zero_text), DrawBorderThenFill(zero_circle))

        # Animate the drawing of the second circle (1)
        self.play(Write(one_label), Write(one_text), DrawBorderThenFill(one_circle))

        # bit_circle = Circle(radius=1.5, fill_color=BLACK, fill_opacity=1, color=BLUE)
        # bit_label = Tex("Bit", font_size=42, color=BLUE).next_to(
        #     bit_circle, UP, buff=0.1
        # )
        # self.play(Write(bit_label))
        # bit_text = Tex("0", color=YELLOW, font_size=48).next_to(
        #     bit_circle, RIGHT, buff=0.5
        # )

        # self.play(Write(bit_text), DrawBorderThenFill(bit_circle))
        # bit_text_new = Tex("1", color=YELLOW, font_size=48).next_to(
        #     bit_circle, RIGHT, buff=0.5
        # )

        # Toggle between "0" and "1" with color transitions
        # for _ in range(5):
        #     self.play(
        #         bit_circle.animate.set_fill(WHITE),
        #         FadeOut(bit_text),
        #         FadeIn(bit_text_new),
        #         run_time=0.5,
        #     )
        #     self.play(
        #         bit_circle.animate.set_fill(BLACK),
        #         FadeOut(bit_text_new),
        #         FadeIn(bit_text),
        #         run_time=0.5,
        #     )

        self.next_slide()
        self.clear()

        self.add_slide_number(5)
        quantum_label = Tex("Quantum Computation", color=GREEN, font_size=48).to_edge(
            UP
        )
        self.play(Write(quantum_label))

        # Setup Qubit visualization
        # TODO: Let it be 2 circles with one totally dark and the other totally light
        qubit_sphere = Circle(radius=1.5, color=GREEN)
        qubit_label = Tex("Qubit", color=GREEN, font_size=42).next_to(
            qubit_sphere, UP, buff=0.1
        )
        self.play(Create(qubit_sphere), Write(qubit_label))

        qubit_0 = Tex("0", color=YELLOW, font_size=48)
        qubit_1 = Tex("1", color=YELLOW, font_size=48)
        qubit_text = (
            VGroup(qubit_0, qubit_1)
            .arrange(buff=-0.6)
            .move_to(qubit_sphere.get_center() + RIGHT * 2)
        )

        self.play(Write(qubit_text))

        # Continuous looping of color transitions to reflect different superposition states
        for _ in range(2):
            alphas = [random.random() for _ in range(10)]
            for alpha in alphas:
                mixed_color = interpolate_color(WHITE, BLACK, alpha)
                color_transition = Circle(
                    radius=1.5, fill_color=mixed_color, fill_opacity=1, color=GREEN
                )
                # Transition to the new color to simulate changing quantum states
                self.play(
                    Transform(qubit_sphere, color_transition),
                    run_time=0.3,
                )

        self.play(Indicate(qubit_0, color=YELLOW), Indicate(qubit_1, color=YELLOW))

        self.next_slide()
        self.clear()

        # Qubit definition

        self.add_slide_number(6)
        classical_label.to_edge(UP).shift(LEFT * 3)
        zero_label.next_to(classical_label, DOWN, buff=0.5)
        zero_circle.next_to(zero_label, DOWN, buff=0.5)
        zero_text.next_to(zero_circle, RIGHT, buff=0.5)
        bit_def = Tex(
            r"A bit is a number \\from the set \{0, 1\}.", color=ORANGE, font_size=30
        ).next_to(zero_circle, DOWN, buff=0.5)

        quantum_label.to_edge(UP).shift(RIGHT * 3)
        qubit_label.next_to(quantum_label, DOWN, buff=0.5)
        qubit_sphere.set_fill_color(GRAY)
        qubit_sphere.next_to(qubit_label, DOWN, buff=0.4)
        qubit_text.next_to(qubit_sphere, RIGHT, buff=0.5)
        qubit_def = Tex(
            r"A qubit (or quantum-bit) \\is a unit vector in $\mathbb{C}^2$.",
            color=ORANGE,
            font_size=30,
        ).next_to(qubit_sphere, DOWN, buff=0.5)

        classical_group = VGroup(
            classical_label, zero_label, zero_circle, zero_text, bit_def
        ).move_to(LEFT * 3)

        quantum_group = VGroup(
            quantum_label, qubit_label, qubit_sphere, qubit_text, qubit_def
        ).move_to(RIGHT * 3)

        self.play(
            FadeIn(classical_group),
            FadeIn(quantum_group),
        )

        self.next_slide()
        self.clear()

    def spin_analogy(self):
        self.add_slide_number(7)
        analogy_label = Tex("Electron Spin Analogy", color=BLUE, font_size=40).to_edge(
            UP
        )
        self.play(Write(analogy_label))

        # Arrows for Spin Up and Spin Down
        spin_up = Arrow(start=ORIGIN, end=UP * 2, color=BLUE, buff=0).shift(LEFT * 3)
        spin_up_label = Tex("Spin Up", color=BLUE, font_size=36).next_to(spin_up, RIGHT)
        self.play(GrowArrow(spin_up), Write(spin_up_label))

        spin_down = Arrow(start=UP * 2, end=ORIGIN, color=RED, buff=0).shift(RIGHT * 3)
        spin_down_label = Tex("Spin Down", color=RED, font_size=36).next_to(
            spin_down, RIGHT
        )
        self.play(GrowArrow(spin_down), Write(spin_down_label))

        # Mixed state explanation
        mixed_state = (
            Tex(
                "Superposition State: a combination of Spin Up and Spin Down",
                color=ORANGE,
                font_size=36,
            )
            .to_edge(DOWN)
            .shift(UP * 2)
        )
        self.next_slide()
        self.play(Write(mixed_state))

        # Mixed state dynamic animation
        mixed_spin = Arrow(start=ORIGIN, end=UP * 2, color=PURPLE, buff=0)
        mixed_spin.move_to(ORIGIN)
        self.play(GrowArrow(mixed_spin))
        for _ in range(5):
            self.play(
                mixed_spin.animate.put_start_and_end_on(ORIGIN, UP * 2), run_time=0.3
            )
            self.play(
                mixed_spin.animate.put_start_and_end_on(UP * 2, ORIGIN), run_time=0.3
            )

        conclusion_note = (
            Tex(
                "Now we understand what a qubit is and what superposition means.",
                color=GREEN,
                font_size=36,
            )
            .to_edge(DOWN)
            .shift(UP)
        )
        self.next_slide()
        self.play(FadeOut(mixed_spin))
        self.play(Write(conclusion_note))
        self.next_slide()
        self.clear()

    def math_representation(self):
        self.add_slide_number(8)
        title = Tex(
            "Mathematical Representation of Qubits", color=BLUE, font_size=48
        ).to_edge(UP)

        # Introduction to Dirac Notation
        dirac_intro = Tex(
            "Dirac Notation (Bra-Ket Notation):", color=BLUE, font_size=42
        ).next_to(title, DOWN, buff=0.5)

        bra_definition = (
            Tex(
                r"Bra: $\langle v|$ represents a row vector",
                color=ORANGE,
                font_size=38,
            )
            .next_to(dirac_intro, DOWN, buff=0.75)
            .to_edge(LEFT, buff=0.5)
        )

        # Example of a bra vector
        bra_example = (
            Tex(
                r"$\langle 0| = \begin{bmatrix} 1 & 0 \end{bmatrix}$",
                color=YELLOW,
                font_size=40,
            )
            # .next_to(bra_definition, DOWN, buff=0.5)
            .to_edge(DOWN * 2)
        )

        # Define a ket
        ket_definition = (
            Tex(
                r"Ket: $|v\rangle$ represents a column vector",
                color=ORANGE,
                font_size=38,
            )
            .next_to(bra_definition, DOWN, buff=0.5)
            .to_edge(LEFT, buff=0.5)
        )

        # Example of a ket vector
        ket_example = Tex(
            r"$|1\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$",
            color=YELLOW,
            font_size=40,
        ).to_edge(DOWN * 2)

        ket_zero = (
            Tex(
                r"$|0\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$",
                color=YELLOW,
                font_size=38,
            )
            .to_edge(RIGHT * 2)
            .shift(UP * 1.5)
        )

        ket_one = Tex(
            r"$|1\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$",
            color=YELLOW,
            font_size=38,
        ).next_to(ket_zero, DOWN, buff=0.5)

        # Write content sequentially
        self.play(Write(title))
        self.play(Write(dirac_intro))
        self.next_slide()
        self.play(Write(bra_definition))
        self.play(Write(bra_example))
        self.next_slide()
        self.play(FadeOut(bra_example))
        self.play(Write(ket_definition))
        self.play(Write(ket_example))
        self.next_slide()
        self.play(FadeOut(ket_example))  # Fade out the example

        # Explain computational basis used in quantum
        computational_basis = (
            Tex(
                r"Computational basis states $|0\rangle$ and $|1\rangle$ ",
                r"are used to describe the state of a qubit.",
                color=BLUE,
                font_size=38,
            )
            .next_to(ket_definition, DOWN, buff=1)
            .to_edge(LEFT, buff=0.5)
        )

        self.play(Write(computational_basis), Write(ket_zero), Write(ket_one))
        self.next_slide()

        general_state = Tex(
            r"$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$",
            r"$= \alpha \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \beta \begin{bmatrix} 0 \\ 1 \end{bmatrix}$",
            r"$= \begin{bmatrix} \alpha \\ \beta \end{bmatrix}$",
            color=YELLOW,
            font_size=38,
        ).to_edge(DOWN * 2)

        self.play(Write(general_state))
        self.next_slide()
        self.clear()

    def quantum_states_ex(self):
        self.add_slide_number(9)
        title = Tex(
            "Some Important 1-Qubit Quantum States", color=BLUE, font_size=48
        ).to_edge(UP)

        # Definition of a Quantum State Vector
        # state_vector_definition = Tex(
        #     r"Definition: \textit{Quantum State vector}. ",
        #     r"The state of a quantum system is a (column) unit vector in $\mathbb{C}^{2n}$, ",
        #     r"where $n$ is the number of qubits in the system.",
        #     font_size=24,
        #     color=BLUE,  # Use a different color to distinguish from the qubit definition
        # ).next_to(qubit_definition, DOWN, buff=0.5)

        # self.play(Write(state_vector_definition))
        # self.next_slide()
        # Draw the circle and quantum states

        circle = Circle(radius=2)

        self.play(Write(title))
        self.play(Create(circle))

        states = {
            r"$|1\rangle$": UP * 2,  # Up direction for |0>
            r"$|0\rangle$": RIGHT * 2,  # Right direction for |1>
            r"$|+\rangle$": np.sqrt(2) * RIGHT
            + np.sqrt(2) * UP,  # 45 degrees right of vertical
            r"$|-\rangle$": np.sqrt(2) * RIGHT
            + np.sqrt(2) * DOWN,  # 45 degrees left of vertical
        }

        # Create the lines from the center to the labels and add state labels
        for label, pos in states.items():
            line = Line(ORIGIN, pos)
            state_label = Tex(label, font_size=40).move_to(pos * 1.2)
            self.play(Create(line), Write(state_label), run_time=1)

        state_matrices = {
            r"$|0\rangle$": r"$\begin{bmatrix} 1 \\ 0 \end{bmatrix}$",
            r"$|1\rangle$": r"$\begin{bmatrix} 0 \\ 1 \end{bmatrix}$",
            r"$|+\rangle$": r"$\dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}$",
            r"$|-\rangle$": r"$\dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -1 \end{bmatrix}$",
        }

        matrices = VGroup()
        for i, (label, matrix) in enumerate(state_matrices.items()):
            matrix_text = Tex(f"{label}: {matrix}", color=YELLOW, font_size=40)

            # increase the spacing between the matrices
            if i < 2:
                matrix_text.to_edge(LEFT, buff=1).shift(DOWN * 2 * i)
            else:
                matrix_text.to_edge(RIGHT, buff=1).shift(DOWN * 2 * (i - 2))

            # TODO: Adding the term computational and fourier basis
            matrices.add(matrix_text)

        for matrix in matrices:
            self.play(Write(matrix))

        self.next_slide()
        self.clear()

    def inner_product(self):
        self.add_slide_number(10)
        title = Tex(
            "Quantum Matrices: Gates and Transformations", color=BLUE, font_size=48
        ).to_edge(UP)
        self.play(Write(title))
        self.next_slide()

        # Inner Product Explanation
        inner_product = Tex(
            r"Inner Product: ",
            r"Dot product between quantum states ",
            r"$\braket{x}{y} = \braket{y}{x}^*$",
            tex_template=myTemplate,
            font_size=36,
            color=GREEN,
        ).next_to(title, DOWN, buff=0.5)

        # Visualize inner product with example vectors
        ket_x = Tex(
            r"$\ket{x} = \begin{bmatrix} a \\ b \end{bmatrix}$",
            font_size=32,
            tex_template=myTemplate,
            color=YELLOW,
        )

        ket_y = Tex(
            r"$\ket{y} = \begin{bmatrix} c \\ d \end{bmatrix}$",
            font_size=32,
            tex_template=myTemplate,
            color=YELLOW,
        )

        ket_group = VGroup(ket_x, ket_y).arrange(RIGHT, buff=1)
        ket_group.next_to(inner_product, DOWN, buff=0.5)

        # Inner product calculation
        inner_product_calc = Tex(
            r"$\braket{x}{y} = \bra{x} \ket{y} = \begin{bmatrix} a^* & b^* \end{bmatrix} \cdot   \begin{bmatrix} c \\ d \end{bmatrix} = a^*c + b^*d$",
            font_size=32,
            color=YELLOW,
            tex_template=myTemplate,
        ).next_to(ket_group, DOWN, buff=0.5)

        self.play(Write(inner_product))
        self.next_slide()
        self.play(Write(ket_x), Write(ket_y))
        self.play(Write(inner_product_calc))
        self.next_slide()

        # Unitary Matrix Definition
        unitary_matrix_def = Tex(
            r"Unitary Matrix \( U \): Preserves Inner Product ",
            r"$\braket{U\psi_1}{U\psi_2} = \braket{\psi_1}{\psi_2}$",
            tex_template=myTemplate,
            font_size=36,
            color=ORANGE,
        ).next_to(inner_product_calc, DOWN, buff=0.5)

        # Visualize unitary transformation
        original_state = Tex(
            r"Original State: $\ket{\psi_1}$",
            font_size=32,
            tex_template=myTemplate,
        )

        # Arrow to show transformation
        transformation_arrow = Arrow(
            start=ORIGIN, end=RIGHT * 2, color=PURPLE, buff=0
        ).next_to(original_state, RIGHT, buff=0.5)

        transformed_state = Tex(
            r"Transformed State: $U\ket{\psi_1}$",
            font_size=32,
            tex_template=myTemplate,
        ).next_to(transformation_arrow, RIGHT, buff=0.5)

        transformation_group = VGroup(
            original_state, transformed_state, transformation_arrow
        ).next_to(unitary_matrix_def, DOWN, buff=0.5)

        self.play(Write(unitary_matrix_def))
        self.next_slide()
        self.play(
            Write(original_state),
            Write(transformed_state),
            Create(transformation_arrow),
        )
        self.next_slide()

        # Quantum Algorithm Illustration
        algorithm_title = Tex(
            "Quantum Algorithm: A Sequence of Unitary Matrices (Gates)",
            color=BLUE_D,
            font_size=40,
        ).to_edge(DOWN)

        self.play(Write(algorithm_title))
        self.next_slide()
        self.clear()

        # hadamard_explanation = Tex(
        #     r"The Hadamard gate $H$ is particularly useful because it maps the computational basis $ \{ \ket{0}, \ket{1} \} $"
        #     r"to the fourier basis $ \{ \ket{+}, \ket{-} \} $ and vice versa. The matrix representation of $H$ is:",
        #     r"$H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}. $",
        #     r"Applying $H$ to $\ket{0}$ yields $\ket{+}$:",
        #     r"$H \ket{0} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} "
        #     r"= \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \ket{+}. $",
        #     r"Similarly, $H\ket{1} = \ket{-}$, $H\ket{+} = \ket{0}$, and $H\ket{-} = \ket{1}$. ",
        #     tex_template=myTemplate,
        #     font_size=24,
        # )

        # self.play(Write(hadamard_explanation))
        # self.next_slide()
        # self.clear()

    def unitary_gates_explanation(self):
        self.add_slide_number(11)
        title = Tex("Quantum Unitary Gates", color=BLUE, font_size=48).to_edge(UP)
        self.play(Write(title))
        self.next_slide()

        # Define gates and their matrices
        gates = {
            "Identity Gate": {
                "symbol": r"$I$",
                "matrix": r"$\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$",
                "description": "Leaves the qubit unchanged",
            },
            "NOT Gate (X Gate)": {
                "symbol": r"$X$",
                "matrix": r"$\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$",
                "description": "Flips the qubit state",
            },
            "Hadamard Gate": {
                "symbol": r"$H$",
                "matrix": r"$\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$",
                "description": "Creates superposition",
            },
        }

        # Create gate representations
        gate_group = VGroup()
        for i, (name, gate_info) in enumerate(gates.items()):
            # Gate name
            gate_name = Tex(name, color=GREEN, font_size=36)

            # Gate symbol and matrix
            gate_symbol = Tex(
                f"{gate_info['symbol']} = {gate_info['matrix']}",
                color=YELLOW,
                font_size=32,
            )

            # Description
            gate_description = Tex(gate_info["description"], color=ORANGE, font_size=28)

            # Vertical arrangement of gate info
            gate_info_group = VGroup(gate_name, gate_symbol, gate_description).arrange(
                DOWN, buff=0.3
            )

            # Position gates
            gate_info_group.shift(LEFT * (4 - 4 * i) + UP * 1)
            gate_group.add(gate_info_group)

        # Animate gates
        for gate_info in gate_group:
            self.play(Write(gate_info))
        self.next_slide()

        # NOT Gate Application Example
        example_title = Tex(
            "Example: NOT Gate on $\ket{0}$",
            color=BLUE_D,
            font_size=40,
            tex_template=myTemplate,
        ).to_edge(DOWN * 4)

        # Initial state |0>
        initial_state = Tex(
            r"Initial State: $\ket{0} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$",
            color=GREEN,
            font_size=36,
            tex_template=myTemplate,
        )

        # Result of application
        result_state = Tex(
            r"$X\ket{0} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \ket{1}$",
            color=YELLOW,
            font_size=36,
            tex_template=myTemplate,
        )

        # Arrange example components
        example_group = (
            VGroup(
                initial_state,
                Tex(r"$\xrightarrow{\text{NOT Gate}}$", font_size=30),
                result_state,
            )
            .arrange(RIGHT, buff=0.5)
            .next_to(example_title, DOWN, buff=0.5)
        )

        # Animate example
        self.play(Write(example_title))
        self.next_slide()

        for item in example_group:
            self.play(Write(item))

        self.next_slide()
        self.clear()

    def measurement(self):
        self.add_slide_number(12)
        measurement_title = Tex(
            "Quantum Measurement", color=BLUE, font_size=48
        ).to_edge(UP)
        self.play(Write(measurement_title))

        # Measurement Definition
        measurement_def = Tex(
            r"When a quantum state is measured, it collapses to one of the basis states ",
            r"with a probability determined by the square of the amplitude ",
            r"of its coefficient in that state.",
            font_size=38,
        ).next_to(measurement_title, DOWN, buff=0.5)
        self.play(Write(measurement_def))

        # Quantum State Representation
        state_psi = MathTex(
            r"\ket{\psi} = \alpha \ket{0} + \beta \ket{1}",
            font_size=36,
            color=YELLOW,
            tex_template=myTemplate,
        ).next_to(measurement_def, DOWN, buff=0.5)
        self.play(Write(state_psi))

        # Coefficients and Probabilities
        alpha_val = 0.6  # Example values for demonstration
        beta_val = np.sqrt(1 - alpha_val**2)

        # Probability Calculation
        prob_0 = Tex(
            r"$p(0) = |\alpha|^2 =$" + f" {alpha_val**2:.2f}",
            font_size=32,
            color=YELLOW,
        ).next_to(state_psi, DOWN, buff=0.5)
        prob_1 = Tex(
            r"$p(1) = |\beta|^2 =$" + f" {beta_val**2:.2f}",
            font_size=32,
            color=YELLOW,
        ).next_to(prob_0, DOWN, buff=0.2)

        self.play(Write(prob_0), Write(prob_1))
        self.next_slide()

        # Simulation of the measurement process
        measurement_outcome = np.random.choice([0, 1], p=[alpha_val**2, beta_val**2])
        outcome_label = Tex(
            rf"Measurement outcome: $\ket{{{measurement_outcome}}}$",
            font_size=38,
            tex_template=myTemplate,
            color=GREEN,
        ).next_to(prob_1, DOWN, buff=1)

        # Animate the collapse of the state
        self.play(
            Transform(
                state_psi,
                Tex(
                    rf"$\ket{{{measurement_outcome}}}$",
                    font_size=36,
                    tex_template=myTemplate,
                    color=ORANGE,
                ).move_to(state_psi.get_center()),
            )
        )
        self.play(Write(outcome_label))
        self.next_slide()
        self.clear()

    def quantum_vs_classical(self):
        self.add_slide_number(13)
        title = Tex("Quantum vs Classical Circuits", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Simplified key points with improved layout and emphasis
        points = (
            VGroup(
                Tex(
                    "Is quantum computation as good as classical? Is it higher?",
                    font_size=38,
                    color=GREEN,
                ),
                Tex(
                    "Classical computations are generally irreversible (e.g., AND function).",
                    font_size=38,
                    color=RED,
                ),
                Tex(
                    "Quantum circuits require reversibility, achieved with unitary operations.",
                    font_size=38,
                    color=TEAL,
                ),
                Tex(
                    "Any classical circuit can be efficiently converted into a quantum circuit.",
                    font_size=38,
                    color=ORANGE,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.6)
            .next_to(title, DOWN, buff=1.5)
        )

        # Staggered animation with highlights
        for point in points:
            self.play(
                FadeIn(point, scale=1.1),  # Slight scale effect
                point.animate.set_opacity(1),  # Full opacity on focus
            )
            self.next_slide()

        self.next_slide()
        self.clear()

    def bernstein_vazirani(self):
        self.add_slide_number(14)
        title = Tex("Bernstein-Vazirani Problem", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Problem description
        problem_desc = Tex(
            r"Given an oracle (black-box) that implements a function ",
            r"$f: \{0, 1\}^n \to \{0, 1\}$, where $f(x)$ is the dot product between ",
            r"$x$ and a secret string $s \in \{0, 1\}^n$ modulo 2: ",
            r"$f(x) = x \cdot s = x_1 s_1 \oplus x_2 s_2 \oplus \cdots \oplus x_n s_n$, ",
            r"find $s$.",
            color=ORANGE,
            font_size=38,
        ).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(problem_desc))
        self.next_slide()

        # Classical strategy
        classical_strategy = (
            VGroup(
                Tex("Classical Solution (bit by bit):", font_size=36, color=BLUE_D),
                Tex(r"$f(1000\cdots 0) = s_1$", font_size=32, color=YELLOW),
                Tex(r"$f(0100\cdots 0) = s_2$", font_size=32, color=YELLOW),
                Tex(r"$f(0010\cdots 0) = s_3$", font_size=32, color=YELLOW),
                Tex(r"$\vdots$", font_size=32, color=YELLOW),
                Tex(r"$f(0000\cdots 1) = s_n$", font_size=32, color=YELLOW),
            )
            .arrange(DOWN)
            .next_to(problem_desc, DOWN, buff=0.5)
        )

        self.play(LaggedStart(*[Write(mob) for mob in classical_strategy]))
        self.next_slide()

        # Quantum advantage
        quantum_advantage = Tex(
            r"Quantum advantage: \textbf{Only one query} is needed to find $s$.",
            font_size=38,
            color=GREEN,
        ).next_to(classical_strategy, DOWN, buff=0.5)

        self.play(FadeIn(quantum_advantage, scale=1.1), run_time=1.5)
        self.next_slide()
        self.clear()

    def bernstein_vazirani_solution(self):
        self.add_slide_number(15)
        title = Tex(
            "Quantum Solution to Bernstein-Vazirani Problem", font_size=48, color=BLUE
        ).to_edge(UP)
        self.play(Write(title))

        problem_desc = Tex(
            r"Given an oracle (black-box) that implements a function ",
            r"$f: \{0, 1\}^n \to \{0, 1\}$, where $f(x)$ is the dot product between ",
            r"$x$ and a secret string $s \in \{0, 1\}^n$ modulo 2: ",
            r"$f(x) = x \cdot s = x_1 s_1 \oplus x_2 s_2 \oplus \cdots \oplus x_n s_n$, ",
            r"find $s$.",
            color=ORANGE,
            font_size=38,
        ).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(problem_desc))

        # Step 1: Initialization and Hadamard Transformation
        step1_text = Tex(
            r"\textbf{Step 1: Initializing the Uniform Superposition (Rotate)}",
            font_size=32,
        ).to_edge(LEFT + UP * 6.5)
        step1_equation = Tex(
            r"$\ket{0}^{\otimes n} \xrightarrow{H^{\otimes n}} \dfrac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} \ket{x}$",
            font_size=32,
            color=YELLOW,
            tex_template=myTemplate,
        ).to_edge(DOWN)

        self.play(Write(step1_text))
        self.next_slide()
        self.play(Write(step1_equation))

        self.next_slide()
        self.play(FadeOut(step1_equation))

        # Step 2: Application of the Oracle
        step2_text = (
            Tex(
                r"\textbf{Step 2: Applying the Oracle Transformation (Compute)}",
                font_size=32,
            )
            .next_to(step1_text, DOWN, buff=0.5)
            .align_to(step1_text, LEFT)
        )
        step2_equation = Tex(
            r"$\dfrac{1}{\sqrt{2^n}} \displaystyle\sum_{x \in \{0,1\}^n} (-1)^{f(x)} \ket{x}$",
            font_size=32,
            color=YELLOW,
            tex_template=myTemplate,
        ).to_edge(DOWN)

        self.play(Write(step2_text))
        self.next_slide()
        self.play(Write(step2_equation))
        self.next_slide()
        self.play(FadeOut(step2_equation))

        # Step 3: Hadamard Transformation
        step3_text = (
            Tex(
                r"\textbf{Step 3: Final Hadamard Transform (Rotate)}",
                font_size=32,
                color=WHITE,
            )
            .next_to(step2_text, DOWN, buff=0.5)
            .align_to(step1_text, LEFT)
        )
        step3_equation = Tex(
            r"$H^{\otimes n} \left( \dfrac{1}{\sqrt{2^n}} \displaystyle\sum_{x \in \{0,1\}^n} (-1)^{f(x)} \ket{x} \right) = \ket{s}$",
            font_size=32,
            color=YELLOW,
            tex_template=myTemplate,
        ).to_edge(DOWN)

        self.play(Write(step3_text))
        self.next_slide()
        self.play(Write(step3_equation))
        self.next_slide()
        self.play(FadeOut(step3_equation))

        # Final Result Highlight
        result_text = Tex(
            r"\textbf{Result:} Directly obtain $\ket{s}$ \textbf{with a single query}",
            font_size=38,
            color=GREEN,
            tex_template=myTemplate,
        ).to_edge(DOWN * 2)

        self.play(FadeIn(result_text, scale=1.1))
        self.next_slide()
        self.clear()

    def simons_problem(self):
        # Enhanced title with subtle animation
        self.add_slide_number(16)
        title = Tex("Simon's Problem", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Problem description with more dynamic presentation
        problem_desc = Tex(
            r"Given an oracle function $f : \{0,1\}^n \rightarrow \{0,1\}^n$, "
            r"with a secret string $s \neq 0^n$, such that for all $x$ and $y$, ",
            r"$f(x) = f(y) \iff y = x \oplus s$ ",
            r"find $s$.",
            font_size=38,
            color=ORANGE,
        ).next_to(title, DOWN, buff=0.5)

        # Animate problem description with emphasis
        self.play(Write(problem_desc))
        self.next_slide()

        # Significance with visual highlight
        significance = (
            VGroup(
                Tex(r"\textbf{Significance:}", font_size=36, color=BLUE),
                Tex(
                    r"Demonstrates an \textbf{exponential speedup} of quantum algorithms",
                    r"\\Inspired the development of Shor's algorithm",
                    font_size=30,
                    color=TEAL,
                ),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(problem_desc, DOWN, buff=0.5)
        )

        self.play(Write(significance))
        self.next_slide()

        # Complexity comparison with visual distinction
        complexities = (
            VGroup(
                Tex(r"\textbf{Computational Complexity:}", font_size=36, color=PURPLE),
                VGroup(
                    Tex(r"Classical Approach: $O(2^{n/2})$", font_size=30, color=RED),
                    Tex(r"Quantum Approach: $O(n)$", font_size=30, color=GREEN),
                ).arrange(DOWN, buff=0.3),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(significance, DOWN, buff=0.5)
        )

        self.play(Write(complexities))
        self.next_slide()
        self.play(FadeOut(significance), FadeOut(complexities))
        self.add_slide_number(17)

        # Enhanced example with more context
        example = (
            VGroup(
                Tex(r"\textbf{Concrete Example:}", font_size=36, color=BLUE),
                Tex(
                    r"Let \( n = 3 \) and secret string \( s = 110 \):",
                    r"\[ f(000) = 101 \]",
                    r"\[ f(100) = 000 \]",
                    r"\[ f(001) = 110 \]",
                    r"\[ f(111) = 110 \]",
                    r"Note: \( f(001) = f(111) \), so \( 001 \oplus 111 = 110 \)",
                    font_size=30,
                    color=YELLOW,
                ),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(problem_desc, DOWN, buff=0.5)
        )

        self.play(FadeIn(example[0]), Write(example[1]))
        self.next_slide()

        # Final summary with quantum emphasis
        quantum_magic = Tex(
            r"\textbf{Quantum Magic:} Solving in \( O(n) \) instead of \( O(2^{n/2}) \)",
            font_size=36,
            color=GREEN,
        ).next_to(example, DOWN, buff=0.5)

        self.play(FadeIn(quantum_magic, scale=1.1), run_time=1.5)

        self.next_slide()
        self.clear()

    def period_finding(self):
        self.add_slide_number(18)
        title = Tex(
            "Period-Finding Problem in Shor's Algorithm", font_size=48, color=BLUE
        ).to_edge(UP)
        self.play(Write(title))

        # Main Problem of Shor's Algorithm
        main_problem = Tex(
            r"Main Problem: \textbf{Factorization}", font_size=40, color=RED
        ).next_to(title, DOWN, buff=0.75)
        self.play(Write(main_problem))
        self.next_slide()

        # Mapping to Period Finding
        mapping = Tex(
            r"Factorization is mapped to \textbf{Period Finding}",
            font_size=40,
            color=GREEN,
        ).next_to(main_problem, DOWN, buff=0.5)
        self.play(Write(mapping))

        # Definition of the Period-Finding Problem
        definition = Tex(
            r"Period-Finding Problem: ",
            r"Given a function $f : \mathbb{N} \to \mathbb{N}$, ",
            r"with the promise that $f(x) = f(y) \iff s \mid (y - x)$, ",
            r"find the period $s$.",
            font_size=38,
            color=ORANGE,
        ).next_to(mapping, DOWN, buff=0.75)
        self.play(Write(definition))
        self.next_slide()

        # Example of Periodicity
        function_graph = Tex(
            r"If $f(x) = f(x+s)$ for some integer $s$, then $s$ is the period.",
            font_size=34,
        ).next_to(definition, DOWN, buff=0.5)

        self.play(Write(function_graph))
        self.next_slide()
        self.clear()

    def hidden_subgroup_problem(self):
        self.add_slide_number(19)
        title = Tex("The Hidden Subgroup Problem", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # Problem Statement
        subgroup_hiding_definition = Tex(
            r"Given a group $G$, a subgroup $H \leq G$, and a set $X$, ",
            r"a function $f : G \to X$ \textbf{hides} the subgroup $H$ if for all ",
            r"$g_1, g_2 \in G$, $f(g_1) = f(g_2)$ if and only if $g_1 H = g_2 H$. ",
            r"Equivalently, $f$ is constant on each coset of $H$, but ",
            r"it is different between the different cosets of $H$.",
            font_size=38,
            color=ORANGE,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(subgroup_hiding_definition))

        # Hidden Subgroup Problem Description
        hidden_subgroup_problem = Tex(
            r"Hidden subgroup problem: Let $G$ be a group, $X$ a finite set, and ",
            r"$f : G \to X$ a function oracle that hides a subgroup $H \leq G$. Find $H$.",
            font_size=34,
        ).next_to(subgroup_hiding_definition, DOWN, buff=0.5)
        self.play(Write(hidden_subgroup_problem))

        group_circle = Circle(radius=1.5, color=BLUE).shift(LEFT * 3 + DOWN * 2.5)
        subgroup_circle = Circle(radius=1, color=RED).move_to(group_circle.get_center())
        group_label = Tex("$G$", font_size=24).next_to(group_circle, UP, buff=0.2)
        subgroup_label = Tex("$H$", font_size=24).next_to(subgroup_circle, UP, buff=0.2)

        self.play(
            Create(group_circle),
            Write(group_label),
            Create(subgroup_circle),
            Write(subgroup_label),
        )

        # Introduce the coset map κ
        kappa_label = Tex(r"$f: G \to \mathcal{X}$", font_size=32, color=GREEN).next_to(
            group_circle, RIGHT, buff=1
        )
        self.play(Write(kappa_label))

        # Visualize the coset map
        coset_circle = Circle(radius=1.5, color=YELLOW).shift(RIGHT * 4 + DOWN * 2.5)
        coset_label = Tex(r"$\mathcal{X}$", font_size=24).next_to(
            coset_circle, UP, buff=0.2
        )

        coset_element = Dot(color=YELLOW).move_to(
            coset_circle.get_center() + 0.5 * np.array([np.cos(0), np.sin(0), 0])
        )

        self.next_slide()
        self.play(
            Create(coset_circle), Write(coset_label), GrowFromCenter(coset_element)
        )

        group_elements = VGroup(
            *[
                Dot(color=BLUE).move_to(
                    group_circle.get_center()
                    + 0.5
                    * np.array([np.cos(i * 2 * PI / 8), np.sin(i * 2 * PI / 8), 0])
                )
                for i in range(8)
            ]
        )
        self.play(Create(group_elements))

        self.next_slide(loop=True)
        self.play(
            *[
                ReplacementTransform(group_element, coset_element.copy())
                for group_element in group_elements
            ]
        )

        self.next_slide()
        self.clear()

    def hsp_examples(self):
        self.add_slide_number(20)
        title = Tex(
            "Reductions to the Hidden Subgroup Problem", font_size=42, color=BLUE
        ).to_edge(UP)
        self.play(Write(title))

        header = (
            VGroup(
                Tex("Problem", font_size=36, color=BLUE),
                Tex("Group", font_size=36, color=BLUE),
            )
            .arrange(RIGHT, buff=2)
            .next_to(title, DOWN, buff=1)
        )

        # Define the problems and corresponding groups in separate lists
        problems = [
            "Simon's Factoring/Period Finding",
            "Discrete Log",
            "Pell's Equation/Principal Ideal Problem",
            "Graph Isomorphism",
            "Shortest Vector Problem",
        ]

        groups = [
            "$\\mathbb{Z}_2^n$",
            "$\\mathbb{Z}_N$",
            "$\\mathbb{Z}_N \\times \\mathbb{Z}_N$, $\\mathbb{R}$",
            "$S_n$ (Symmetric Group)",
            "$D_N$ (Dihedral Group)",
        ]

        # Creating separate VGroups for problems and groups
        problem_texts = VGroup(
            *[Tex(problem, font_size=32) for problem in problems]
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        group_texts = VGroup(*[Tex(group, font_size=32) for group in groups]).arrange(
            DOWN, buff=0.5, aligned_edge=LEFT
        )

        # Organize the columns next to each other
        table = VGroup(problem_texts, group_texts).arrange(RIGHT, buff=2)
        table.next_to(header, DOWN, buff=0.5)

        # Draw header and table
        self.play(Write(header))
        self.play(Write(table))

        # self.play(Write(abelian_label), Write(non_abelian_label))

        self.next_slide()
        self.clear()

    def thank_you(self):
        self.add_slide_number(21)
        thank_you = Text("Thank You!", font_size=64, color=BLUE).shift(UP)
        self.play(Write(thank_you))

        # Any questions text
        any_questions = Text("Any Questions?", font_size=48, color=YELLOW).next_to(
            thank_you, DOWN, buff=1
        )
        self.play(Write(any_questions))

    def construct(self):
        self.intro()
        self.table_of_contents()
        self.classical_quantum_computation()
        self.spin_analogy()
        self.math_representation()
        self.quantum_states_ex()
        self.inner_product()
        self.unitary_gates_explanation()
        self.measurement()
        self.quantum_vs_classical()
        self.bernstein_vazirani()
        self.bernstein_vazirani_solution()
        self.simons_problem()
        self.period_finding()
        self.hidden_subgroup_problem()
        self.hsp_examples()
        self.thank_you()
