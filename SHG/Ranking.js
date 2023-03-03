// Define the set of items to be compared
const items = ['A', 'B', 'C', 'D'];

// Initialize the comparison matrix with zeros
const matrix = [];
for (let i = 0; i < items.length; i++) {
matrix[i] = Array(items.length).fill(0);
}

// For each pair of items, ask the user to indicate their preference
for (let i = 0; i < items.length; i++) {
for (let j = i+1; j < items.length; j++) {
// if the user enters an invalid input, keep asking until they enter a valid input
while (true) {
let winner = prompt(Enter your preference for ${items[i]} vs ${items[j]}: );
if (winner === items[i]) {
score = 1;
break;
} else if (winner === items[j]) {
score = 0;
break;
}
}
matrix[i][j] = score;
matrix[j][i] = 1 - score;
console.log("Matrix:\n", matrix);
}
}

// Compute the weighted sum of the scores for each item
const weighted_sum = matrix.map(row => row.reduce((acc, val) => acc + val, 0));
console.log(weighted_sum);

// Rank the items based on their weighted sum of scores
const ranked_items = items.sort((a, b) => weighted_sum[items.indexOf(b)] - weighted_sum[items.indexOf(a)]);
console.log("Ranked items:", ranked_items);
