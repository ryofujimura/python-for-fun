import numpy as np

# Define the set of items to be compared
items = ['A', 'B', 'C', 'D']

# Initialize the comparison matrix with zeros
matrix = np.zeros((len(items), len(items)))

# For each pair of items, ask the user to indicate their preference
for i in range(len(items)):
    for j in range(i+1, len(items)):
        # if the user enters an invalid input, keep asking until they enter a valid input
        while True:
            winner = input(f"Enter your preference for {items[i]} vs {items[j]}: ")
            if winner == items[i]:
                score = 1
                break
            elif winner == items[j]:
                score = 0
                break
        matrix[i][j] = score
        matrix[j][i] = 1 - score
        print("Matrix:\n", matrix)

# Compute the weighted sum of the scores for each item
weighted_sum = np.sum(matrix, axis=1)
print(weighted_sum)


# Rank the items based on their weighted sum of scores
ranked_items = [x for _, x in sorted(zip(weighted_sum, items), reverse=True)]

print("Ranked items:", ranked_items)
