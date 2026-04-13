import csv
import os

USERS = {
    "admin": "admin123"
}

FILENAME = "campus_data.csv"

class Facility:
    def __init__(self, fid, name, ftype, location, status, usage):
        self.fid = fid
        self.name = name
        self.ftype = ftype
        self.location = location
        self.status = status
        self.usage = usage

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if USERS.get(username) == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid login!\n")
        return False

def add_facility(data):
    fid = input("Facility ID: ")
    name = input("Name: ")
    ftype = input("Type (classroom/lab/library/washroom): ")
    location = input("Location: ")
    status = input("Status (available/busy/maintenance): ")
    usage = int(input("Usage count: "))

    data[fid] = Facility(fid, name, ftype, location, status, usage)
    print("Facility added successfully")

def view_facilities(data):
    if not data:
        print("No facilities found")
        return

    print("\n{:<8} {:<15} {:<15} {:<15} {:<15} {:<10}".format(
        "FID", "Name", "Type", "Location", "Status", "Usage"))
    print("-" * 80)
    for f in data.values():
        print("{:<8} {:<15} {:<15} {:<15} {:<15} {:<10}".format(
            f.fid, f.name, f.ftype, f.location, f.status, f.usage))

def update_facility(data):
    fid = input("Enter Facility ID: ")
    if fid not in data:
        print("Facility not found")
        return
    data[fid].status = input("New Status: ")
    data[fid].usage = int(input("New Usage Count: "))
    print("Facility updated successfully")

def delete_facility(data):
    fid = input("Enter Facility ID: ")
    if fid in data:
        del data[fid]
        print("Facility deleted")
    else:
        print("Facility not found")

def search_by_id(data):
    fid = input("Facility ID: ")
    f = data.get(fid)
    if f:
        print(vars(f))
    else:
        print("Facility not found")

def search_by_name(data):
    name = input("Name: ").lower()
    found = False
    for f in data.values():
        if f.name.lower() == name:
            print(vars(f))
            found = True
    if not found:
        print("Facility not found")

def usage_report(data):
    if not data:
        print("No facilities available")
        return
    total = 0
    for f in data.values():
        total += f.usage
    print("Total Usage:", total)

def maintenance_report(data):
    found = False
    for f in data.values():
        if f.status.lower() == "maintenance":
            print(f.fid, f.name, f.location)
            found = True
    if not found:
        print("No facilities in maintenance")

def save_to_csv(data):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["fid", "name", "ftype", "location", "status", "usage"])
        for f in data.values():
            writer.writerow([f.fid, f.name, f.ftype, f.location, f.status, f.usage])
    print("Data saved to CSV.")

def load_from_csv(data):
    if not os.path.exists(FILENAME):
        print("CSV file not found.")
        return
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row["fid"]] = Facility(
                row["fid"], row["name"], row["ftype"],
                row["location"], row["status"], int(row["usage"])
            )
    print("Data loaded from CSV.")

def main():
    data = {}
    if login():
        load_from_csv(data)
        while True:
            print("""
--- Smart Campus Navigation, Facility Monitoring & Resource Analytics System ---
1. Add Facility
2. View Facilities
3. Update Facility
4. Delete Facility
5. Search by ID
6. Search by Name
7. Usage Report
8. Maintenance Report
9. Save to CSV
10. Load from CSV
0. Exit
""")
            choice = input("Enter choice: ")

            if choice == "1":
                add_facility(data)
            elif choice == "2":
                view_facilities(data)
            elif choice == "3":
                update_facility(data)
            elif choice == "4":
                delete_facility(data)
            elif choice == "5":
                search_by_id(data)
            elif choice == "6":
                search_by_name(data)
            elif choice == "7":
                usage_report(data)
            elif choice == "8":
                maintenance_report(data)
            elif choice == "9":
                save_to_csv(data)
            elif choice == "10":
                load_from_csv(data)
            elif choice == "0":
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    main()