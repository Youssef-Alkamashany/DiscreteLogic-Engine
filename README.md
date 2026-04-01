# ⚡ DiscreteLogic: The Boolean Equivalence Architect

## 🌐 Vision
[cite_start]**DiscreteLogic** is a high-fidelity simulator designed to automate the rigorous verification of Boolean expressions[cite: 1, 2]. [cite_start]By leveraging the precision of Python and the power of combinatorial logic, it provides an immutable computational proof for discrete structures that are traditionally solved by hand[cite: 4, 39].

## 🧪 The Proof Objective
The engine is specifically optimized to validate the following logical identity:
[cite_start]**¬[(A ⊕ B) → (C ∧ D)] ≡ (A ⊕ B) ∧ (¬C ∨ ¬D)** [cite: 17, 33]

## 🚀 Core Engine Features
* [cite_start]**Virtual Logic Gate Array:** Full implementation of XOR, AND, OR, and NOT hardware-level logic gates[cite: 23, 24, 28, 55].
* [cite_start]**Automated State Exploration:** Uses `itertools` to exhaustively test the entire 16-state truth space for variables A, B, C, and D[cite: 14, 31, 35].
* [cite_start]**Independent Pipeline Verification:** * **LHS Pipeline:** Executes XOR-AND-IMPLICATION-NEGATION sequence[cite: 21, 26].
    * [cite_start]**RHS Pipeline:** Executes dual-NOT-OR-AND sequence[cite: 27, 29].
* [cite_start]**Equivalence Matcher:** A dedicated parity-check algorithm that confirms absolute logical consistency across all inputs[cite: 30, 48].
* [cite_start]**Dual-Mode Data Visualization:** Seamlessly toggles between High/Low (Binary 0/1) and True/False (T/F) data representations[cite: 2, 5, 31, 35].

## 🛠️ Technical Architecture
* [cite_start]**Core Language:** Python 3.x [cite: 4]
* [cite_start]**Combinatorial Library:** `itertools` [cite: 14]
* [cite_start]**Logic Framework:** Discrete Mathematics & Digital Circuit Design [cite: 1, 55]
* [cite_start]**Methodology:** Procedural Boolean Proofing [cite: 18, 20]

## 📊 Analytical Output Structure
The engine generates a structured matrix detailing every intermediate logical step:
1. [cite_start]**Inputs:** A, B, C, D [cite: 22, 43]
2. [cite_start]**Intermediate Gates:** XOR (A^B), AND (C.D), NOTs (~C, ~D) [cite: 23, 24, 28]
3. [cite_start]**Compound Gates:** Implication (->), OR (v) [cite: 25, 32]
4. [cite_start]**Parity Check:** Final Equivalence Match [cite: 30, 48]

---
[cite_start]*Developed for the Discrete Mathematics Research Project* [cite: 1, 8]
