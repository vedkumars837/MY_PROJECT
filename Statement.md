# T-Shirt Size Classification using k-Nearest Neighbors (k-NN)

## 1. Project Overview
This project implements a **Machine Learning** algorithm from scratch using pure Python. The goal is to predict the T-shirt size ('Small' or 'Large') of a person based on two physical features:
* Height (in cm)
* Weight (in kg)

Instead of using external libraries like `scikit-learn` or `pandas`, this project demonstrates the internal logic of the **k-Nearest Neighbors (k-NN)** algorithm using standard lists and loops.

---

## 2. Problem Statement
Given a dataset of users with known heights, weights, and T-shirt sizes, the system must classify a new user into the correct category (Small/Large) by analyzing their physical similarity to the existing data.

**Input:** User Height (cm) and Weight (kg).
**Output:** Predicted Label (e.g., "Large T-Shirt").

---

## 3. The Algorithm & Logic
The project relies on the **k-Nearest Neighbors** approach. The core logic follows these steps:

### A. Data Representation
The data is stored as a list of lists, where each row represents a person:
```python
[150, 45, 'Small T-Shirt'] # [Height, Weight, Label]
