import math

# 1. The "Database" (List of Lists)
# Format: [Height(cm), Weight(kg), Label]
dataset = [
    [150, 45, 'Small T-Shirt'],
    [160, 50, 'Small T-Shirt'],
    [155, 48, 'Small T-Shirt'],
    [175, 70, 'Large T-Shirt'],
    [180, 85, 'Large T-Shirt'],
    [178, 75, 'Large T-Shirt']
]

# 2. The Math: Euclidean Distance Function
def calculate_distance(point1, point2):
    distance = 0.0
    # Loop through dimensions (Height, Weight) excluding the Label
    for i in range(len(point1)): 
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance)

# 3. The Algorithm: k-Nearest Neighbors
def get_neighbors(train_data, test_point, k):
    distances = []
    
    # Calculate distance to ALL training points
    for row in train_data:
        # row[:-1] means "take all numbers except the last text label"
        dist = calculate_distance(test_point, row[:-1])
        distances.append((row, dist))
        
    # Sort by distance (smallest distance first)
    distances.sort(key=lambda x: x[1])
    
    # Get top k neighbors
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
        
    return neighbors

# 4. The Prediction Logic
def predict_classification(train_data, test_point, k):
    neighbors = get_neighbors(train_data, test_point, k)
    
    # Extract labels from neighbors
    output_values = [row[-1] for row in neighbors]
    
    # Find the most common label (Manual "Mode" calculation)
    prediction = max(set(output_values), key=output_values.count)
    return prediction

# --- VISUALIZATION CONCEPT ---
# The algorithm essentially plots your input on a 2D graph relative to the dataset.
# It looks at the 'k' closest points to decide the label.

# 5. Testing with User Input
print("--- T-Shirt Size Predictor ---")

# Get input from user and convert to float (decimal number)
try:
    h_input = input("Enter your height in cm: ")
    user_height = float(h_input)

    w_input = input("Enter your weight in kg: ")
    user_weight = float(w_input)

    new_person = [user_height, user_weight]
    k_value = 3

    result = predict_classification(dataset, new_person, k_value)

    print("-" * 30)
    print(f"For a person of height {new_person[0]}cm and weight {new_person[1]}kg:")
    print(f"Predicted Size: {result}")

except ValueError:
    print("Error: Please make sure you enter only numbers for height and weight.")