Documentation

Project Overview

This system is an automated lead qualification engine developed to address operational inefficiencies in SMB sales funnels, specifically targeting coaching centers in the Kozhikode region.

Market Context: Local centers typically receive ~200 leads per month. Manual processing results in significant resource waste, as the average conversion rate is 10%. This tool automates the filtering process to prioritize high-intent leads.

Technical Specification

1. Data Model

The system processes lead objects structured as Python dictionaries:

name (str): Unique identifier for the prospect.

days_since_enquiry (int): Measure of lead recency.

budget_mentioned (bool): Indicator of financial intent.

2. Validation Layer

The engine includes a sanitization gate using .strip(). This ensures that malformed data or empty string entries are caught and logged as a "DATA ERROR" instead of causing system failure.

3. Rule Engine Logic

The qualification follows a deterministic scoring model:

HOT: Enquiries < 7 days old with explicit budget intent.

WARM: Enquiries < 15 days old.

COLD: All other valid entries.

4. Output

Standardized terminal reporting is generated via f-string interpolation.

Usage

python3 leads_v1.py
