# Airport Operations System (AOS)

## Overview
A lightweight Command-Line Interface (CLI) application in Python designed to track and manage airport logistics across four key operational areas: Airlines, Flights, Passengers, and Staff.

## Features
- **Security:** Startup login authentication with a 3-attempt lockout mechanism.
- **Airlines:** Track operating carriers, fleet size, and route counts.
- **Flight Board:** Monitor flight schedules, gates, runways, arrival/departure times, and status.
- **Passengers:** Maintain traveler records linked to flight numbers using unique PNRs.
- **Employees & Payroll:** Manage workforce records with an analytics tool computing Average, Minimum, and Maximum salaries.

## Technologies Used
- Python 3.x
- `tabulate` library for console tables

## Installation & Running
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run the application:

Bash
python main.py
Default Credentials
Username: admin

Password: airport_admin_123

Testing Instructions
Login Verification: Enter wrong credentials 3 times to verify system termination; log in with valid credentials to reach the dashboard.

CRUD Validation: Add and delete records across all 4 menus, verifying list updates via the display option.

Reporting Check: Populate employee salaries and run option 4 (Report) to verify mathematical accuracy of payroll metrics.
