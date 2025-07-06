import streamlit as st
import math
import re
import numpy as np
from sympy import symbols, sympify, integrate, diff, latex

x = symbols('x')

st.set_page_config(page_title="Math Chatbot")
st.title("Smart Math Chatbot")

# Word replacements to symbols
REPLACEMENTS = {
    "plus": "+", "minus": "-", "times": "*", "multiplied by": "*",
    "divided by": "/", "into": "*", "over": "/", "power of": "**",
    "square root of": "math.sqrt", "sqrt": "math.sqrt",
    "log": "math.log10", "ln": "math.log",
}

def clean_input(text):
    text = text.lower()
    text = re.sub(r"what is|calculate|compute|evaluate", "", text)
    for word, symbol in REPLACEMENTS.items():
        text = text.replace(word, symbol)
    return text.strip()

def safe_eval(expr):
    try:
        return eval(expr, {"__builtins__": None}, {"math": math})
    except Exception as e:
        return f"Eval error: {e}"

def handle_integration(expr):
    try:
        return integrate(sympify(expr), x)
    except Exception as e:
        return f"Integration error: {e}"

def handle_differentiation(expr):
    try:
        return diff(sympify(expr), x)
    except Exception as e:
        return f"Differentiation error: {e}"

def handle_matrix_op(text):
    try:
        pattern = r"\[\[.*?\]\]"
        matrices = re.findall(pattern, text)
        if len(matrices) < 2:
            return "Provide two matrices."

        mat1 = np.array(eval(matrices[0]))
        mat2 = np.array(eval(matrices[1]))

        if "add" in text:
            return mat1 + mat2
        elif "subtract" in text:
            return mat1 - mat2
        elif "multiply" in text or "dot" in text:
            return np.matmul(mat1, mat2)
        else:
            return "Unknown matrix operation."

    except Exception as e:
        return f"Matrix error: {e}"

# Session-based chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input box
user_input = st.chat_input("Ask me anything math-related...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    if user_input.lower().startswith("integrate"):
        expr = user_input.replace("integrate", "").strip()
        result = handle_integration(expr)

    elif user_input.lower().startswith("differentiate"):
        expr = user_input.replace("differentiate", "").strip()
        result = handle_differentiation(expr)

    elif "matrix" in user_input or "[[" in user_input:
        result = handle_matrix_op(user_input)

    else:
        parsed = clean_input(user_input)
        result = safe_eval(parsed)

    # Format symbolic result
    if hasattr(result, "free_symbols"):
        response = f"LaTeX Result: \n\n${latex(result)}$"
    else:
        response = str(result)

    if "error" not in response.lower():
        st.balloons()

    st.session_state.chat_history.append(("assistant", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message("user" if sender == "user" else "assistant"):
        if message.startswith("LaTeX Result"):
            st.latex(message.replace("LaTeX Result: \n\n", "").replace("$", ""))
        else:
            st.markdown(message)
