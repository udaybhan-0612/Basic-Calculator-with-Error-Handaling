import streamlit as st

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

# (Optional) Function to perform power calculation
def power(x, y):
    return x ** y

# --- Streamlit UI ---
st.title("Basic Calculator")

# Input widgets for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Radio buttons for operation selection
operation = st.radio(
    "Select an operation:",
    ('+', '-', '*', '/', '**')
)

result = None

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    try:
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
            # Handle the division by zero error specifically here for clarity
            if "Error" in str(result):
                st.error(result)
                result = None
        elif operation == '**':
            result = power(num1, num2)

        if result is not None:
            st.success(f"The result is: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")