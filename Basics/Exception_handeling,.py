# 1. What is Exception Handling?
# Exception is an error that occurs during program execution.
# Example:
# print(10/0)
# Output:
# ZeroDivisionError: division by zero
# Exception handling allows us to handle such errors so that the program does not crash.
# 2. try – except
# Basic syntax:
# try:
# risky code
# except:
# code to handle error
# Example:
# try:
# num = int(input("Enter number: "))
# print(10/num)
# except:
# print("Some error occurred")
# 3. Handling Specific Exceptions
# Python allows handling specific exceptions.
# Example:
# try:
# num = int(input("Enter number: "))
# print(10/num)
# except ZeroDivisionError:
# print("Cannot divide by zero")
# except ValueError:
# print("Invalid input. Please enter a number")
# Common Exceptions:
# ValueError → invalid datatype
# TypeError → wrong data type operation
# IndexError → list index out of range
# KeyError → dictionary key not found
# FileNotFoundError → file missing
# 4. Multiple Exceptions
# try:
# a = int(input())
# b = int(input())
# print(a/b)
# except (ValueError, ZeroDivisionError):
# print("Invalid input or division by zero")
# 5. else Block
# The else block runs only if no exception occurs.
# try:
# num = int(input("Enter number: "))
# except ValueError:
# print("Invalid input")
# else:
# print("Square =", num*num)
# 6. finally Block
# The finally block always executes.
# try:
# f = open("data.txt")
# except FileNotFoundError:
# print("File not found")
# finally:
# print("Program finished")
# Used mostly for:
# ● closing files
# ● closing database connections
# ● cleanup operations
# 7. raise Keyword
# Used to manually generate exceptions.
# Example:
# age = int(input("Enter age: "))
# if age < 18:
# raise Exception("Not eligible")
# print("You can vote")
# 8. Custom Exceptions
# You can create your own exception classes.
# Example:
# class InsufficientBalanceError(Exception):
# pass
# Usage:
# balance = 500
# withdraw = int(input("Enter amount"))
# if withdraw > balance:
# raise InsufficientBalanceError("Not enough balance")
