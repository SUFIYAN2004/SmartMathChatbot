#📐 Smart Math Chatbot 🤖
A Streamlit-based intelligent chatbot for solving various math problems using natural language input. It supports arithmetic, symbolic integration/differentiation, and matrix operations using SymPy, NumPy, and Python's math module.

#🔍 Features
✅ Natural language input parsing
➕ Arithmetic calculations (e.g., "What is 5 plus 6?")
∫ Symbolic integration and differentiation (e.g., "Integrate x^2")
🧮 Matrix operations: add, subtract, multiply (dot product)
🧠 Memory of chat history using Streamlit session state
📜 LaTeX rendering of symbolic results
🎈 Balloons for successful computations

#🚀 Demo
Run locally with Streamlit:
bash '''
streamlit run app.py
'''

#🛠️ Tech Stack
Streamlit – UI and chat interface
SymPy – Symbolic math engine
NumPy – Matrix operations
Math – Arithmetic support
Regex – Input cleaning and parsing

#📦 Installation
Clone the repo
bash
git clone https://github.com/SUFIYAN2004/SmartMathChatbot.git
cd smartmathchatbot

#Create a virtual environment (optional but recommended)
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#Install dependencies

bash
pip install -r requirements.txt
