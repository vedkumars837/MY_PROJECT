# 📐 Pure Python $k$-Nearest Neighbors (k-NN) Classifier

A **zero-dependency** implementation of the $k$-Nearest Neighbors (k-NN) algorithm written entirely using the **Python Standard Library**.

This project's goal is to demonstrate the core logic of similarity-based classification by building a lightweight classifier that categorizes a new data point (e.g., a person's height and weight) based on the class of its closest neighbors in a predefined dataset. 

---

## ✨ Why This Project is Important

| Feature | Benefit |
| :--- | :--- |
| **Zero Dependencies** | The script runs on **any** Python installation. **No `pip install` required!** Ideal for embedded systems or simple scripts. |
| **Core Understanding** | By manually implementing the distance formula, you gain a deep understanding of how machine learning measures **"similarity"** in data. |
| **Customizable** | The underlying dataset can be easily swapped for any $N$-dimensional classification problem (e.g., flower species, fruit features, or spam detection). |

---

## 🚀 How It Works: The k-NN Algorithm

The k-Nearest Neighbors algorithm is a non-parametric, **lazy learning** method. Classification is achieved by a majority vote of its $k$ closest neighbors.

### Algorithm Steps

1.  **Input:** Define a new, unlabeled data point $P_{\text{new}}$ (e.g., `[170, 65]`).
2.  **Distance Calculation:** Calculate the **Euclidean Distance** between $P_{\text{new}}$ and *every* training point $P_{\text{train}}$ in the dataset.
    $$D(P_1, P_2) = \sqrt{\sum_{i=1}^{n} (x_{1i} - x_{2i})^2}$$
3.  **Sort:** Store all distances and their corresponding labels, then **sort** the list from smallest distance to largest distance.
4.  **Select Neighbors:** Select the **top $k$** points (e.g., $k=3$) with the smallest distances.
5.  **Vote:** The predicted class is the **most frequent label** among the $k$ selected neighbors.

---

## 📋 Implementation Details

The classifier is built exclusively with standard Python features:

* **Data Storage:** Python **Lists of Lists** mimic a spreadsheet or database.
* **Distance:** The built-in **`math`** module is used for the square root.
* **Sorting:** Python's built-in **`.sort()`** function and a `lambda` expression handle the distance ranking.

### Dataset Schema (Example: T-Shirt Sizing)

| Feature 1 (Index 0) | Feature 2 (Index 1) | Label (Index 2) |
| :---: | :---: | :---: |
| **Height (cm)** | **Weight (kg)** | **T-Shirt Size** |
| 150 | 45 | 'Small T-Shirt' |
| 178 | 75 | 'Large T-Shirt' |
| ... | ... | ... |

---

## 💻 Code Structure

| Function | Purpose | Tools Used |
| :--- | :--- | :--- |
| `dataset` | The hardcoded list of lists containing the training data. | List |
| `calculate_distance()` | Calculates the Euclidean distance between two points. | `math.sqrt()` |
| `get_neighbors()` | Calculates all distances, sorts them, and returns the top $k$ neighbors. | `.sort(key=lambda x: x[1])` |
| `predict_classification()` | Takes the labels from the $k$ neighbors and finds the majority (the "vote"). | `max(set(), key=list.count)` |

---

## ⚙️ Installation and Execution

1.  Save the provided Python code as a file named `knn_classifier.py`.
2.  Run the file from your terminal:

```bash
python knn_classifier.py
