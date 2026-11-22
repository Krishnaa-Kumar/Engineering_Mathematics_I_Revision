# CalcVault M-1 | Engineering Mathematics-I Study Portal

> **IKG-PTU BTAM101-18 Syllabus • 100% Free & Open Access Academic Portal**  
> Curated with ❤️ by **Krishna Kumar** (B.Tech Cybersecurity, CGC College of Engineering, Landran).

---

## 🚀 Overview

**CalcVault M-1** is a comprehensive, interactive engineering mathematics study portal designed specifically for first-year engineering students preparing for the **IKG Punjab Technical University (IKG-PTU BTAM101-18)** examinations.

Modeled with the same modern, high-performance architecture as **ChemVault**, it provides structured theory notes, KaTeX mathematical proofs, verified university question banks, and rapid formula cheat sheets across all 5 syllabus units — completely free with zero paywalls.

---

## 🌟 Key Features

- **100% Free & Open Access**: No paywalls, no subscriptions, no locked features. Everything is open unconditionally for all students.
- **Complete Syllabus Coverage (5 Units)**:
  - **Unit 1**: Sequences & Infinite Series (Ratio, Cauchy, Leibnitz, p-Test, Taylor expansions).
  - **Unit 2**: Applications of Definite Integrals (Arc length, surface area, and volume of revolution for Cycloids, Ellipses, Cardioids, Circles).
  - **Unit 3**: Beta & Gamma Functions & Improper Integrals (Definitions, duplication formula, 7 reduction integrals, property proofs).
  - **Unit 4**: Multivariable Calculus (Partial differentiation, Euler's Theorem 1st & 2nd order with deductions, Chain rule, Maxima & Minima).
  - **Unit 5**: Multiple Integrals & Transformations (Double/triple integrals, change of order, polar transformations, Jacobians).
- **Global Search Modal (`Ctrl+K`)**: Instantly search topics, formulas, or derivations with live query matching.
- **Solved University Question Bank (`questions.html`)**: 26 high-probability university exam questions with step-by-step model derivations and interactive unit filters.
- **Formula & Constant Cheat Sheet (`formulas.html`)**: Standard invariants, high-yield theorem criteria, and 1-click copyable formula blocks.
- **Interactive Whiteboard Solver (`whiteboard.html`)**: Step-by-step animated whiteboard solver with evaluator traps and progress mastery tracking.
- **Crisp KaTeX Math Typesetting**: High-speed mathematical rendering on mobile and desktop.
- **1-Click Print & PDF Export**: Clean `@media print` styling to save any page as an A4 PDF without website clutter.
- **Dark & Light Mode**: Seamless theme switching with persistent preferences.

---

## 📂 Project Architecture

```
Engineering_Mathematics_I_Revision/
├── assets/
│   ├── css/
│   │   └── style.css            # Custom scrollbars, formula blocks, and print rules
│   ├── data/
│   │   └── units.json           # Structured JSON database of all 5 units & 26 questions
│   └── js/
│       ├── main.js              # Theme, global search (Ctrl+K), copy toast, shortcuts
│       ├── data.js              # Raw knowledge base for whiteboard engine
│       └── whiteboard.js        # Interactive lecture whiteboard solver
├── generate_site.py             # High-speed static site generator script
├── index.html                   # Overview portal & curriculum dashboard
├── formulas.html                # Formula & theorem cheat sheet
├── questions.html               # Solved university exam question bank
├── whiteboard.html              # Interactive whiteboard step-by-step solver
├── unit-1.html                  # Unit 1: Sequences & Infinite Series
├── unit-2.html                  # Unit 2: Definite Integral Applications
├── unit-3.html                  # Unit 3: Beta & Gamma Functions
├── unit-4.html                  # Unit 4: Multivariable Calculus
├── unit-5.html                  # Unit 5: Multiple Integrals & Transformations
├── .gitignore                   # Git ignore rules
└── README.md                    # Documentation
```

---

## 💻 How to Run Locally

Because CalcVault is a static web application built with modern HTML5, Tailwind CSS, KaTeX, and Vanilla JavaScript, no build steps or heavy dependencies are needed:

1. Clone the repository:
   ```bash
   git clone https://github.com/Krishnaa-Kumar/Engineering_Mathematics_I_Revision.git
   cd Engineering_Mathematics_I_Revision
   ```
2. Start a local server:
   ```bash
   python3 -m http.server 8080
   ```
   Open `http://localhost:8080` in your web browser.

3. To rebuild all pages from `assets/data/units.json`:
   ```bash
   python3 generate_site.py
   ```

---

## 👨‍💻 Author & Credits

- **Curated by**: Krishna Kumar
- **Branch**: B.Tech Cybersecurity, CGC College of Engineering, Landran (Mohali)
- **Target Course**: IKG-PTU BTAM101-18 (Engineering Mathematics-I)
- **License**: 100% Free & Open-Source Academic Resource.
