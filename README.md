# AI Lead Qualification System

A Python-based engine designed to automate the scoring of business leads. This project tracks my transition from basic logic to production-ready software architecture.

---

## Day 2: Production Hardening & Observability
**Focus: Resiliency and Structural Cleanliness**

On Day 2, I refactored the script to meet enterprise standards. Key improvements include:

- **Modular Architecture**: Rebuilt the engine using a 'Singular Specialist' function (`score_lead`) and a 'Master Manager' loop. This allows the system to scale easily.
- **The Indestructible Shield**: Implemented `try/except` blocks to handle real-world "dirty data" like missing keys (`KeyError`) or invalid data types (`TypeError`).
- **Professional Observability**: Integrated the Python `logging` module to create an automated audit trail in `app.log`.
- **Gatekeeping**: Added logic to automatically skip and log leads with empty or invalid names.

### How to Run (Day 2 Version)
1. Run `python3 lead_v2.py`.
2. View live results in the terminal.
3. Review `app.log` for the detailed technical history.

---

## Day 1: The Foundation
**Focus: Basic Logic & Lead Categorization**

- Built the initial logic to categorize leads as "Hot," "Warm," or "Cold."
- Used basic `if/elif/else` statements and `print()` functions.
- (Keep your original Day 1 notes here!)
