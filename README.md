# 👕 T-Shirt Size Predictor: k-Nearest Neighbors (k-NN) from Scratch

## 1. 🚀 Project Overview
This project is an implementation of the **k-Nearest Neighbors (k-NN)** machine learning algorithm built entirely from scratch in Python, without relying on advanced external libraries (like `scikit-learn` or `pandas`).

The goal is to classify a new user's optimal T-shirt size ('Small' or 'Large') based on two input features: **Height (cm)** and **Weight (kg)**. It serves as an excellent demonstration of core machine learning principles, particularly distance calculation and classification by majority vote.

---

## 2. ✨ Key Features
* **Pure Python Implementation:** The k-NN algorithm, including the distance function and prediction logic, is implemented using only standard Python functionality.
* **Euclidean Distance:** Utilizes the Euclidean formula to mathematically calculate the "closeness" between the input user and existing data points.
    $$
    \text{Distance} = \sqrt{(h_{new} - h_{existing})^2 + (w_{new} - w_{existing})^2}
    $$
* **Custom Dataset:** Uses a small, hardcoded dataset to train the model, making the process transparent and easy to trace.
* **Dynamic User Input:** Prompts the user to enter their height and weight for real-time prediction.
* **Classification by Voting:** Determines the predicted size by letting the **k** closest neighbors vote on the outcome.

---

## 3. 🛠️ Technologies/Tools Used
* **Language:** Python 3.x
* **Core Libraries:** The built-in `math` module (specifically for the square root function).
* **Concepts:** Euclidean Geometry, List Comprehensions, Sorting Algorithms, Data Classification.

---

## 4. ⚙️ Installation & Running the Project

### Prerequisites
You only need to have **Python 3.x** installed on your system.

### Steps to Run
1.  **Clone the repository (if applicable) or save the file:**
    ```bash
    # If using Git
    git clone [your-repo-link]
    cd t-shirt-knn-classifier 
    
    # If not using Git, ensure your Python file is saved (e.g., as main.py)
    ```

2.  **Execute the script:**
    Run the main Python file from your terminal:
    ```bash
    python main.py
    ```

---

## 5. 🧪 Instructions for Testing

The script will prompt you for input in the terminal. The model will automatically use $k=3$ (3 nearest neighbors) for prediction.

### Example Test Case 1: Expected 'Small T-Shirt'
| Prompt | Input |
| :--- | :--- |
| Enter your height in cm: | **155** |
| Enter your weight in kg: | **47** |
| **Predicted Size:** | **Small T-Shirt** |

### Example Test Case 2: Expected 'Large T-Shirt'
| Prompt | Input |
| :--- | :--- |
| Enter your height in cm: | **178** |
| Enter your weight in kg: | **75** |
| **Predicted Size:** | **Large T-Shirt** |

### Example Test Case 3: Borderline Case (Test Point)
Try the following point to see how the distance calculation works on the boundary:
| Prompt | Input |
| :--- | :--- |
| Enter your height in cm: | **176** |
| Enter your weight in kg: | **72** |
| **Predicted Size:** | **Large T-Shirt** |
*(This point is closer to the Large T-Shirt cluster)*

---

## 📸 Screenshots (Optional)

<img width="1146" height="215" alt="Screenshot 2025-11-22 162842" src="https://github.com/user-attachments/assets/f9cd34c6-6535-4801-8137-4ffc00975ad8" />


<img width="1152" height="227" alt="Screenshot 2025-11-22 162144" src="https://github.com/user-attachments/assets/725073a2-e07a-45ed-a3af-0eb5bc4b15d8" />

