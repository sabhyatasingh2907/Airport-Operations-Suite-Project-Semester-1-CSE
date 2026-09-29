"Core operational engine and data management classes."
from tabulate import tabulate
class Authenticator:
    def init(self,user="admin",pwd="airport_admin_123",max_tries=3):
        self.user=user
        self.pwd=pwd
        self.max_tries=max_tries
    def authenticate(self):
        tries=self.max_tries
        print("\n--- ADMIN LOGIN REQUIRED ---")
        while tries>0:
            u=input("Username: ").strip()
            p=input("Password: ").strip()
            if u==self.user and p==self.pwd:
                print("Access Granted.\n")
                return True
            tries-=1
            print(f"Incorrect. {tries} attempt(s) remaining.")
        return False
class AirportManager:
    def init(self):
        self.airlines=[["Skyline Airways", "42", "65"]]
        self.flights=[["Skyline", "SK101", "A4", "08:30", "11:45", "On Time", "09L", "Dep"]]
        self.passengers=[["Alice Johnson", "PNR001", "SK101"]]
        self.employees=[["EMP101", "Carlos Gomez", "Agent", 52000.0, "Morning"]]
    @staticmethod
    def continue_prompt(section):
        while True:
            ans=input(f"Continue in {section}? (y/n): ").strip().lower()
            if ans in ["y", "yes"]:
                return True
            if ans in ["n", "no"]:
                return False
            print("Enter 'y' or 'n'.")
    def airlines_manager(self):
        headers=["Airline Name", "Fleet Size", "Destinations"]
        while True:
            print("\n--- AIRLINE REGISTRY ---\n1. Add  2. Delete  3. Display  4. Return")
            ch=input("Action (1-4): ").strip()
            if ch=="1":
                self.airlines.append([input("Airline Name: ").strip(), input("Fleet Count: ").strip(), input("Destinations: ").strip()])
                print("Record added.")
            elif ch=="2":
                target = input("Airline to remove: ").strip().lower()
                self.airlines = [a for a in self.airlines if a[0].lower() != target]
                print("Registry updated.")
            elif ch=="3":
                print(tabulate(self.airlines, headers=headers, tablefmt="fancy_grid") if self.airlines else "No records found.")
            elif ch=="4":
                break
            if not self.prompt_continue("Airlines"):
                break
    def flights_manager(self):
        headers = ["Airline", "Flight #", "Gate", "Dep", "ETA", "Status", "Runway", "Type"]
        while True:
            print("\n--- FLIGHT BOARD ---\n1. Add  2. Delete  3. Display  4. Return")
            ch=input("Action (1-4): ").strip()
            if ch=="1":
                self.flights.append([
                    input("Airline: ").strip(), input("Flight No: ").strip().upper(),
                    input("Gate: ").strip().upper(), input("Dep Time: ").strip(),
                    input("ETA: ").strip(), input("Status: ").strip(),
                    input("Runway: ").strip(), input("Type: ").strip()
                ])
                print("Flight logged.")
            elif ch=="2":
                target = input("Flight No to cancel: ").strip().upper()
                self.flights = [f for f in self.flights if f[1].upper() != target]
                print("Schedule updated.")
            elif ch=="3":
                print(tabulate(self.flights, headers=headers, tablefmt="fancy_grid") if self.flights else "No active flights.")
            elif ch=="4":
                break
            if not self.prompt_continue("Flights"):
                break
    def manage_passengers(self):
        headers=["Passenger Name", "PNR", "Flight #"]
        while True:
            print("\n--- PASSENGER MANIFEST ---\n1. Add  2. Delete  3. Display  4. Return")
            ch=input("Action (1-4): ").strip()
            if ch=="1":
                pnr=input("PNR: ").strip().upper()
                if any(p[1]==pnr for p in self.passengers):
                    print("Error: PNR already exists.")
                else:
                    self.passengers.append([input("Name: ").strip(), pnr, input("Flight No: ").strip().upper()])
                    print("Passenger registered.")
            elif ch=="2":
                target = input("PNR to delete: ").strip().upper()
                self.passengers = [p for p in self.passengers if p[1] != target]
                print("Manifest updated.")
            elif ch=="3":
                print(tabulate(self.passengers, headers=headers, tablefmt="fancy_grid") if self.passengers else "Manifest empty.")
            elif ch=="4":
                break
            if not self.prompt_continue("Passengers"):
                break
    def employees_manager(self):
        headers = ["Staff ID", "Name", "Role", "Salary ($)", "Shift"]
        while True:
            print("\n--- EMPLOYEE & PAYROLL ---\n1. Add  2. Delete  3. Display  4. Report  5. Return")
            ch = input("Action (1-5): ").strip()
            if ch=="1":
                try:
                    eid = input("Staff ID: ").strip().upper()
                    name = input("Name: ").strip()
                    role = input("Role: ").strip()
                    sal = float(input("Salary ($): ").strip())
                    shift = input("Shift: ").strip()
                    self.employees.append([eid, name, role, sal, shift])
                    print("Staff registered.")
                except ValueError:
                    print("Error: Salary must be numeric.")
            elif ch=="2":
                target=input("Staff ID to delete: ").strip().upper()
                self.employees=[e for e in self.employees if e[0] != target]
                print("Staff list updated.")
            elif ch=="3":
                fmt=[[e[0], e[1], e[2], f"${e[3]:,.2f}", e[4]] for e in self.employees]
                print(tabulate(fmt, headers=headers, tablefmt="fancy_grid") if self.employees else "No employee records.")
            elif ch=="4":
                if not self.employees:
                    print("No records available for analysis.")
                else:
                    sal=[e[3] for e in self.employees]
                    stats=[
                        ["Headcount", len(sal)],
                        ["Average Salary", f"${sum(sal)/len(sal):,.2f}"],
                        ["Maximum Salary", f"${max(sal):,.2f}"],
                        ["Minimum Salary", f"${min(sal):,.2f}"]
                    ]
                    print(tabulate(stats, headers=["Metric", "Value"], tablefmt="fancy_grid"))
            elif ch=="5":
                break
            if not self.prompt_continue("Employees"):
                break