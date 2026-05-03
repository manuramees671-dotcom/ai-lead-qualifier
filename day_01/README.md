# Day 1: The Foundation — Core Logic & Lead Categorization

## Overview
The goal of Day 1 was to establish the primary business logic for the **AI Lead Qualification System**. This phase focused on translating "System 1" human decision-making rules into a repeatable Python script designed for Kerala SMBs. The script evaluates incoming business leads and assigns a priority status based on engagement timing and financial readiness.

---

## Technical Implementation

### 1. Categorization Logic (The Scoring Engine)
The engine uses a specific hierarchy of conditions to determine the "temperature" of a lead:
*   **Hot**: Leads that enquired within the last 7 days **AND** explicitly mentioned a budget.
*   **Warm**: Leads that enquired within the last 15 days.
*   **Cold**: Leads that fall outside the 15-day window or lack immediate qualification markers.

### 2. Python Fundamentals Used
This initial version served as a baseline to implement core Python control flow and data handling:
*   **Conditional Logic**: Utilized `if`, `elif`, and `else` blocks to handle the decision tree and ensure every lead receives a status.
*   **Data Structures**: Used Python dictionaries to store lead attributes (name, days since enquiry, budget status) and lists to manage multiple leads.
*   **Standard Output**: Used `print()` functions to output the results directly to the terminal for immediate verification.

---
