# Mini Inventory Manager

A simple console-based Inventory Management System built using Python. The application allows a shop to manage products, stock quantities, and basic inventory operations while applying fundamental DSA concepts.

## Project Overview

The Mini Inventory Manager helps a small shop maintain its product inventory.

Each product contains:

* Product ID
* Product Name
* Price
* Quantity

The system supports adding products, displaying inventory, searching products, and updating stock quantities.

The complete team project also includes DSA-based operations such as Linked List traversal, Sliding Window, and Two Pointers.

## Technologies Used

* **Language:** Python
* **Application Type:** Console Application
* **Data Structure:** Linked List
* **Algorithms:** Enumeration, Sliding Window, Two Pointers

## Project Structure

```text
Team-3-batch-A/
│
├── main.py
├── product.py
├── inventory.py
├── linked_list.py
├── algorithms.py
├── README.md
└── .gitignore
```

## Features

### 1. Add Product

Allows the user to add a new product with:

* Product ID
* Product Name
* Price
* Quantity

The system prevents duplicate product IDs and invalid negative values.

### 2. Display Inventory

Displays all products currently stored in the inventory.

Example:

```text
ID        Name           Price       Quantity  Value
------------------------------------------------------------
101       Pen            20.00       50        1000.00
102       Book           100.00      20        2000.00
103       Bag            800.00      10        8000.00
104       Bottle         300.00      15        4500.00
```

### 3. Search Product

Products can be searched using:

* Product ID
* Product Name

### 4. Update Quantity

Allows the user to update the available stock quantity of an existing product.

Negative quantities are not allowed.

### 5. Total Inventory Value

The value of each product is calculated as:

```text
Product Value = Price × Quantity
```

The total inventory value is calculated by adding the values of all products.

### 6. Maximum K-Product Value

Uses the **Sliding Window** technique to find the maximum total value of `k` consecutive products.

### 7. Product Pair Search

Uses the **Two Pointer** technique to find two product prices whose sum equals a given target price.

The prices are sorted before applying the Two Pointer algorithm.

## DSA Concepts

### Enumeration / Traversal

Enumeration is used to visit each product and perform operations such as:

* Displaying products
* Searching products
* Calculating inventory value

Time Complexity:

```text
O(n)
```

### Linked List

A custom Linked List is used to manage the product collection.

Each node contains:

```text
Product + Next Node
```

Basic traversal takes:

```text
O(n)
```

### Sliding Window

Sliding Window is used to find the maximum value of `k` consecutive products.

Instead of calculating every group from scratch, the algorithm:

1. Calculates the first window.
2. Removes the outgoing product value.
3. Adds the incoming product value.
4. Compares the current window with the maximum.

Time Complexity:

```text
O(n)
```

### Two Pointers

Two Pointers are used to find product price pairs that equal a target value.

The prices are first sorted.

Then:

* If the sum is smaller than the target → move the left pointer.
* If the sum is larger than the target → move the right pointer.
* If the sum equals the target → pair found.

Sorting:

```text
O(n log n)
```

Two Pointer search:

```text
O(n)
```

Overall:

```text
O(n log n)
```

## Complexity Analysis

| Operation                |    Time Complexity |
| ------------------------ | -----------------: |
| Add Product              |               O(n) |
| Display Inventory        |               O(n) |
| Search by ID             |               O(n) |
| Search by Name           |               O(n) |
| Update Quantity          |               O(n) |
| Total Inventory Value    |               O(n) |
| Sliding Window           |               O(n) |
| Two Pointer Search       | O(n) after sorting |
| Sorting for Two Pointers |         O(n log n) |

## Edge Cases

The application handles:

* Empty inventory
* One product
* Duplicate product IDs
* Zero price
* Zero quantity
* Negative price
* Negative quantity
* Product not found
* Target pair does not exist
* `k` larger than the number of products
* Invalid user input

## How to Run

Make sure Python is installed.

Clone the repository and navigate to the project directory:

```bash
cd Team-3-batch-A
```

Run the application:

```bash
python main.py
```

## Console Menu

```text
==================================================
          MINI INVENTORY MANAGER
==================================================
1. Add Product
2. Display Inventory
3. Search Product
4. Update Quantity
5. Total Inventory Value
6. Maximum K-Product Value
7. Product Pair Search
8. Exit
==================================================
```

## Sample Products

|  ID | Name   | Price | Quantity |
| --: | ------ | ----: | -------: |
| 101 | Pen    |    20 |       50 |
| 102 | Book   |   100 |       20 |
| 103 | Bag    |   800 |       10 |
| 104 | Bottle |   300 |       15 |

## Team Contributions

### Member 1 — Basic Inventory Management

* Product class
* Add Product
* Display Inventory
* Search Product
* Update Quantity
* Input validation
* Console menu integration

### Member 2 — Linked List and Inventory Analysis

* Custom Linked List
* Node operations
* Traversal
* Enumeration
* Total Inventory Value

### Member 3 — Algorithmic Features

* Sliding Window
* Two Pointer
* Price sorting
* Algorithm testing
* Complexity analysis

## Project Goal

The goal of this project is to build a small working inventory management application while applying fundamental Data Structures and Algorithms concepts in a practical problem.

## Future Improvements

Possible future enhancements include:

* Product deletion
* Product editing
* File/database storage
* User authentication
* GUI interface
* Low-stock alerts
* Sales and purchase tracking

Ajay's explanation-  https://drive.google.com/file/d/1DYCAeEqIPAh2-XQKjBabtl2kVV1T9qnT/view?usp=sharing
Dharshni Sivasankar's explanation-  https://drive.google.com/file/d/1MTkXNM6H0BqX06-I_hdZ1sh_qtYUN9lG/view?usp=sharing

