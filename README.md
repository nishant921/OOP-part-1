# Python OOP

A collection of Python programs and examples covering the fundamentals of **Object-Oriented Programming (OOP)**.

## 📚 Topics Covered

* What is OOP?
* Classes and Objects
* Banking Application
* Methods vs Functions
* Class Diagrams
* Magic / Dunder Methods
* Constructor and its benefits
* Concept of `self`
* Creating a `Fraction` Class
* Operator Overloading:

  * `__str__()`
  * `__add__()`
  * `__sub__()`
  * `__mul__()`
  * `__truediv__()`

## 🎯 Learning Objectives

By completing these programs, you will learn how to:

* Understand the fundamentals of OOP
* Create and use classes and objects
* Work with constructors and instance attributes
* Understand the purpose of `self`
* Differentiate between functions and methods
* Use magic/dunder methods
* Implement operator overloading
* Build practical applications using OOP concepts

## 🛠️ Technologies

* **Language:** Python
* **Library:** Python Standard Library

## 📁 Project Structure

```text
OOP/
├── banking_application.py
├── fraction.py
├── magic_methods.py
├── class_diagram/
└── README.md
```

> File names may vary depending on the implementation.

## ▶️ How to Run

Make sure Python is installed on your system.

```bash
python filename.py
```

For example:

```bash
python fraction.py
```

## 📌 Key Concepts

### Classes & Objects

A **class** is a blueprint for creating objects, while an **object** is an instance of a class.

### Constructor

The `__init__()` method initializes an object's attributes when the object is created.

### `self`

`self` refers to the **current object** and is used to access its attributes and methods.

### Magic / Dunder Methods

Special methods surrounded by double underscores, such as `__init__()` and `__str__()`, that allow classes to define special behavior.

### Operator Overloading

Dunder methods can be used to define how operators behave with custom objects.

For example:

```python
fraction1 + fraction2
```

can internally use:

```python
fraction1.__add__(fraction2)
```

## 🚀 Outcome

This repository provides hands-on practice with Python's **Object-Oriented Programming concepts**, progressing from basic classes and objects to custom classes and operator overloading.
