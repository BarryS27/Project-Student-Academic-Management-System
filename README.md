# 🎓 Student Academic Management System (SAMS)

**A comprehensive, Python-based CLI tool designed for high school students to track academic performance, manage portfolios, and visualize progress.**

> **Status:** Active Development  
> **Python Version:** 3.8+

---

## 📖 Overview

SAMS is a personal data management system built with a modular **MVC (Model-View-Controller)** architecture. It moves beyond simple spreadsheets by offering a robust Command Line Interface (CLI) to manage Grades (G9-G12), Self-Development activities, and University applications.

Unlike basic scripts, SAMS includes **data persistence** (CSV), **input validation**, and **advanced data visualization** using Seaborn to analyze academic strengths.

## ✨ Key Features

### 1. 📊 Smart Data Management
- **Flexible Records**: Track grades, weights, and detailed scores (Q1-Q4) for multiple years (G9-G12).
- **Portfolio Tracking**: Manage non-academic data like "Self Development" skills and "Dream Schools".
- **CRUD Operations**: Fully supported **C**reate, **R**ead, **U**pdate, and **D**elete functionalities.
- **Auto-Save**: All changes are instantly persisted to local CSV files.

### 2. 🎨 Advanced Visualization
- **iOS-Style Analytics**: Integrated `viz.py` module generates aesthetic, "Apple-style" performance charts.
- **Seaborn & Matplotlib**: Uses advanced plotting libraries to visualize course performance based on total points.
- **Clean UI**: Visualizations feature rounded bars, pastel color palettes, and minimal "junk" (despined axes).

### 3. 🖥️ User Experience (UX) Focused
- **Human-Centric UI**: 1-based indexing for all lists (no more mental math converting 0-based indexes).
- **Tabulate Integration**: Data is presented in clean, rounded ASCII tables for high readability.
- **Menu-Driven**: No need to type complex table names; select operations via simple numeric menus.

---

## 🛠️ Tech Stack

- **Core Logic**: `Python`, `Pandas`, `NumPy`
- **Visualization**: `Seaborn`, `Matplotlib`
- **Interface**: `Tabulate`, `Console Input`
- **Data Storage**: CSV (Local File System)

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed. It is recommended to use a virtual environment.

### 1. Installation
Clone the repository and install the required dependencies:

```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt

### 2. Run the Application
Once dependencies are installed, start the system by running:

```bash
python main.py

.
├── main.py           # 🚀 Entry Point: Initializes the Controller
├── core.py           # 🧠 Model: Handles Data Logic & CSV CRUD operations
├── ui.py             # 🖥️ View: Handles User Interaction & Menu rendering
├── viz.py            # 🎨 Visualization: Generates Seaborn/Matplotlib charts
├── config.py         # ⚙️ Configuration: File paths & Column definitions
├── requirements.txt  # 📦 Dependencies list
├── .gitignore        # 🔒 Privacy: Excludes personal CSV data from Git
└── README.md         # 📖 Documentation
