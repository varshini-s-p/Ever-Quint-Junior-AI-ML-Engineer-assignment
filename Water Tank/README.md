# Water Tank Problem – EverQuint Assignment

This project is a frontend implementation of the classic **Water Tank / Trapping Rain Water**
problem using **Vanilla HTML, CSS, and JavaScript**. The solution computes the total units of
water trapped between blocks and visualizes the result using **SVG graphics**.

---

## Problem Statement
Given an array of non-negative integers representing the heights of blocks, compute the total
units of water that can be trapped between the blocks after rainfall.

The application should:
- Compute trapped water correctly
- Visually represent blocks and water units
- Use only Vanilla JavaScript and HTML/CSS

---

## Approach
The solution uses the standard **Left Max – Right Max** algorithm.

For each index `i`:
water[i] = max(0, min(leftMax[i], rightMax[i]) - height[i])


Where:
- `leftMax[i]` is the maximum height to the left of index `i`
- `rightMax[i]` is the maximum height to the right of index `i`

---

## Key Code Snippets

### Left and Right Maximum Precomputation
```javascript
leftMax[0] = heights[0];
for (let i = 1; i < n; i++) {
  leftMax[i] = Math.max(leftMax[i - 1], heights[i]);
}

rightMax[n - 1] = heights[n - 1];
for (let i = n - 2; i >= 0; i--) {
  rightMax[i] = Math.max(rightMax[i + 1], heights[i]);
}
Trapped Water Calculation
for (let i = 0; i < n; i++) {
  water[i] = Math.max(
    0,
    Math.min(leftMax[i], rightMax[i]) - heights[i]
  );
}

SVG Visualization Logic
svg.appendChild(waterRect);
svg.appendChild(blockRect);

Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)

Where n is the number of blocks.

Tech Stack

HTML5

CSS3

Vanilla JavaScript

SVG for visualization

Features

User input for block heights

Real-time computation of trapped water

SVG visualization of blocks and water

Table view showing water trapped at each index

Sample inputs for quick testing

Responsive UI

How to Run

Clone the repository

Open the index.html file in a browser
(or use VS Code Live Server for best experience)

No additional setup or dependencies are required.

Sample Inputs & Outputs
Input	Output
[3,0,2,0,4]	7
[0,1,0,2,1,0,1,3,2,1,2,1]	6
[1,1,1,1]	0
Assumptions

Block heights are non-negative integers

Empty input results in zero trapped water

Input validation is handled in the frontend

Author

Varshini
Junior AI/ML Engineer Candidate
