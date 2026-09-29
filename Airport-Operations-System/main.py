"Entry point and session controller for Airport Management System."
import sys
from core import Authenticator, AirportManager
def main():
    auth=Authenticator()
    if not auth.authenticate():
        print("ACCESS DENIED. SESSION TERMINATED.")
        sys.exit()
    app=AirportManager()
    while True:
        print("\n" + "=" * 45)
        print("      AIRPORT MANAGEMENT SYSTEM (AMS)")
        print("=" * 45)
        print("1. Airline Management")
        print("2. Flight Dispatch Board")
        print("3. Passenger Manifest")
        print("4. Staff & Payroll Analytics")
        print("5. Exit System")
        print("-" * 45)
        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            app.manage_airlines()
        elif choice == "2":
            app.manage_flights()
        elif choice == "3":
            app.manage_passengers()
        elif choice == "4":
            app.manage_employees()
        elif choice == "5":
            print("\nSession ended. Goodbye.")
            sys.exit()
        else:
            print("Invalid input. Select a number from 1 to 5.")
if __name__=="__main__":
    main()