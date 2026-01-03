# 📐 Project Design Overview

## 🎯 1. Project Purpose

The **Student Academic Management System (SAMS)** is a local, command-line based
application designed to help students manage academic records such as grades
and activities.

The project emphasizes **clarity**, **modularity**, and **educational value**
rather than enterprise-level scalability.

---

## 🧱 2. Architectural Style

The project follows a **simplified Model–View–Controller (MVC)** inspired design.

- 🗃️ **Model**: Core data logic and persistence
- 🖥️ **View**: Command-line user interface
- 🎛️ **Controller**: Application flow and orchestration

This structure keeps responsibilities clearly separated and easy to understand
for learners.

---

## 📦 3. Module Responsibilities

### ▶️ `main.py`
- Application entry point
- Initializes configuration and starts the main UI loop
- Coordinates interactions between UI and core logic

---

### 🖥️ `ui.py`
- Handles all command-line interactions
- Displays menus and prompts
- Collects and validates basic user input
- ❌ Does **NOT** contain business logic

---

### 🧠 `core.py`
- Contains the core data management logic
- Handles CRUD operations for academic records
- Manages CSV file reading and writing
- Acts as the primary **Model** layer

---

### ⚙️ `config.py`
- Stores configuration constants such as:
  - File paths
  - Column definitions
  - Application settings
- Centralizes values to avoid hard-coded literals

---

### 📊 `viz.py`
- Responsible for data visualization
- Uses plotting libraries to generate academic performance charts
- Reads data via the core module, **not directly from files**

---

### 🤖 `ai.py`
- Experimental module for future intelligent features
- Intended for:
  - Performance insights
  - Trend analysis
  - Academic recommendations
- Currently optional and non-critical to core functionality

---

## 💾 4. Data Storage

- Data is stored locally using **CSV files**
- This approach was chosen for:
  - ✅ Simplicity
  - ✅ Transparency
  - ✅ Ease of learning and debugging

### ⚠️ Limitations
- Not suitable for concurrent users
- No built-in encryption or access control

---

## ⚖️ 5. Design Trade-offs

### ✅ Advantages
- Simple and easy to understand
- Clear separation of concerns
- Beginner-friendly structure
- Easy to extend for learning purposes

### ❌ Limitations
- Limited scalability
- No database backend
- No authentication or role management

These trade-offs are **intentional**, keeping the project focused on
**local usage and educational value**.
