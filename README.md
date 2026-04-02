# ⚡ DiscreteLogic: The Boolean Equivalence Architect

## 🌐 Vision
**DiscreteLogic** is a high-fidelity simulator designed to automate the rigorous verification of Boolean expressions. By leveraging the precision of Python and the power of combinatorial logic, it provides an immutable computational proof for discrete structures that are traditionally solved by hand.

## 🧪 The Proof Objective
The engine is specifically optimized to validate the following logical identity:
**¬[(A ⊕ B) → (C ∧ D)] ≡ (A ⊕ B) ∧ (¬C ∨ ¬D)**

## 🚀 Core Engine Features
* **Virtual Logic Gate Array:** Full implementation of XOR, AND, OR, and NOT hardware-level logic gates.
* **Automated State Exploration:** Uses `itertools` to exhaustively test the entire 16-state truth space for variables A, B, C, and D.
* **Independent Pipeline Verification:**
    * **LHS Pipeline:** Executes XOR-AND-IMPLICATION-NEGATION sequence.
    * **RHS Pipeline:** Executes dual-NOT-OR-AND sequence.
* **Equivalence Matcher:** A dedicated parity-check algorithm that confirms absolute logical consistency across all inputs.
* **Dual-Mode Data Visualization:** Seamlessly toggles between High/Low (Binary 0/1) and True/False (T/F) data representations.

## 🛠️ Technical Architecture
* **Core Language:** Python 3.x
* **Combinatorial Library:** `itertools`
* **Logic Framework:** Discrete Mathematics & Digital Circuit Design
* **Methodology:** Procedural Boolean Proofing

## 📊 Analytical Output Structure
The engine generates a structured matrix detailing every intermediate logical step:
1. **Inputs:** A, B, C, D
2. **Intermediate Gates:** XOR (A^B), AND (C.D), NOTs (~C, ~D)
3. **Compound Gates:** Implication (->), OR (v)
4. **Parity Check:** Final Equivalence Match

---

### 👤 Author
**Youssef Alkamashany**
* 🚀 **Aspiring MLOps & AI Data Engineer**.
* 💼 **Team Leader** | Digital Egypt Pioneers Initiative (DEPI).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-alkamashany-18261132b)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Youssef-Alkamashany)

---
<p align="center">"Developed for the Discrete Mathematics Research Project"</p>
