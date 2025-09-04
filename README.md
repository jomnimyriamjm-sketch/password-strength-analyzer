
# 🔐 Password Strength Analyzer (Offline)
## 📖 Project Overview
This project analyzes and scores password strength using entropy, character diversity, and common patterns.  
It also explores leaked password datasets to visualize trends and weaknesses.  

⚠️ **Ethics Note:** Do **not** use real personal passwords in this tool. Only test with fake/demo ones.

---

## ⚡ Features
- ✅ **CLI Tool** – Check the strength of any password from the terminal.  
- 📊 **EDA (Exploratory Data Analysis)** – Charts of leaked password patterns.  
- 🔍 **Pattern Detection** – Detects common sequences (e.g., `12345`, `qwerty`).  
- 🌐 **a Web App** – User-friendly Streamlit interface.  

---

## 🛠️ Installation

### Prerequisites
- Python **3.10+**  
- VS Code (recommended)  

### Setup
```bash
# Clone this repo or download it
cd pw-strength-analyzer

# Create virtual environment (optional but recommended)
python -m venv .venv

# Activate it
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
🚀 Usage
CLI (Command Line)
Run the analyzer:

bash
Copy code
python src/score.py
Example:

pgsql
Copy code
Enter a password (or q to quit): 123456
{'label': 'Very weak', 'bits': 19.9}

Enter a password (or q to quit): A7v!kP2#
{'label': 'Strong', 'bits': 52.9}
Streamlit App (Optional UI)
Install Streamlit if not already installed:

bash
Copy code
pip install streamlit
Run the app:

bash
Copy code
streamlit run app.py
Then open http://localhost:8501 in your browser.

📊 Data Analysis
Dataset: Top 10k most common passwords (public dataset).

Results & charts are saved in data/reports/.

Example analyses:

Password length distribution

Most common passwords

Character type usage (letters, digits, symbols)

📂 Project Structure
bash
Copy code
pw-strength-analyzer/
│
├─ src/              # Python scripts
│   ├─ score.py      # CLI password analyzer
│   ├─ eda.py        # Data exploration
│   └─ patterns.py   # Pattern checks
│
├─ data/
│   ├─ raw/          # raw password datasets
│   ├─ interim/      # cleaned/sample data
│   └─ reports/      # generated charts/results
│
├─ app.py            # Streamlit UI
├─ requirements.txt  # Dependencies
└─ README.md         # Documentation

👨‍💻 Jomni Myriam 
Created with ❤️ using Python.
