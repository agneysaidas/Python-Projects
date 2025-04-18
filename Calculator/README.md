# 🧮 Simple Python Calculator
Welcome to the Simple Python Calculator project! This is a beginner-friendly command-line calculator built in Python that performs basic arithmetic operations — addition, subtraction, multiplication, and division — with a looping interface for continued calculations. 🎉

## 🚀 Features
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🔁 Continue calculations with previous results
- 🖼️ ASCII art welcome screen (requires art module or custom ASCII file)

## 🧠 How It Works
1. The user is prompted to enter the first number.
2. A list of operations is displayed.
3. The user picks an operation and inputs the next number.
4. The result is displayed.
5. The user can choose to continue with the result or start a new calculation.

## 📝 Example

```python
Enter first number: 10  
+  
-  
*  
/  
Pick an operation: *  
Enter next number: 5  
10.0 * 5.0 = 50.0  
Type 'y' to continue calculating with 50.0, or type 'n' to start new calculation: y  
+  
-  
*  
/  
Pick an operation: -  
Enter next number: 20  
50.0 - 20.0 = 30.0  
```

## ⚠️ Notes
- ❗ No error handling for division by zero — use with care!
- 🔁 The calculator restarts using recursion. For very long sessions, consider converting to a loop to avoid recursion depth issues.

## 💡 Ideas for Improvement
- Add support for more operations (exponents, modulus, etc.)
- Handle invalid input gracefully
- Add error handling for division by zero
- Create a GUI or web version of the calculator


Crafted with 💻 and ❤️ by Agney!
