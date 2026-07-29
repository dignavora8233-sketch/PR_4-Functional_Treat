# Functional Treat

print("Welcome to the Data Analyzer and Transformer Program")

summary = {}

# Menu Function
def menu():
    print("\n1. Input Data")
    print("2. Display Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Dataset Statistics")
    print("7. Exit")

# Input Data Function
def input_data():

    print("\n1. 1D Array")
    print("2. 2D Array")

    ch = input("Enter Choice : ")

    if ch == "1":

        data = list(map(int, input("Enter Elements : ").split()))
        return data, "1D"

    elif ch == "2":

        rows = int(input("Enter Rows : "))
        data = []

        for i in range(rows):
            row = list(map(int, input(f"Row {i+1} : ").split()))
            data.append(row)

        return data, "2D"

    else:

        print("Invalid Choice")
        return [], "1D"

# Summary Function
def display_summary(data):

    if len(data) == 0:
        print("No Data Available")
        return

    if array_type == "1D":

        print("\nSummary")
        print("Total Elements :", len(data))
        print("Minimum :", min(data))
        print("Maximum :", max(data))
        print("Sum :", sum(data))
        print("Average :", round(sum(data)/len(data),2))

    else:

        flat = []

        for row in data:
            flat.extend(row)

        print("\nSummary")
        print("Rows :", len(data))
        print("Columns :", len(data[0]))
        print("Total Elements :", len(flat))
        print("Minimum :", min(flat))
        print("Maximum :", max(flat))
        print("Sum :", sum(flat))
        print("Average :", round(sum(flat)/len(flat),2))

# Recursive Function
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

# Lambda Function
def filter_data(data):

    if len(data) == 0:
        print("No Data Available")
        return

    limit = int(input("Enter Threshold : "))

    if array_type == "1D":

        result = list(filter(lambda x: x >= limit, data))
        print("Filtered Data :", result)

    else:

        print("Filtered Data")

        for row in data:

            result = list(filter(lambda x: x >= limit, row))

            if result:
                print(result)

# Sort Function
def sort_data(data):

    if len(data) == 0:
        print("No Data Available")
        return

    print("\n1. Ascending")
    print("2. Descending")

    ch = input("Enter Choice : ")

    if array_type == "1D":

        temp = data.copy()

        if ch == "1":
            temp.sort()
            print("Ascending :", temp)

        elif ch == "2":
            temp.sort(reverse=True)
            print("Descending :", temp)

        else:
            print("Invalid Choice")

    else:

        temp = []

        for row in data:

            if ch == "1":
                temp.append(sorted(row))

            elif ch == "2":
                temp.append(sorted(row, reverse=True))

        if ch == "1":
            print("Ascending Order")
        elif ch == "2":
            print("Descending Order")
        else:
            print("Invalid Choice")
            return

        for row in temp:
            print(row)

# Multiple Return Function
def dataset_statistics(data):

    if len(data) == 0:
        return None, None, None, None

    if array_type == "1D":

        minimum = min(data)
        maximum = max(data)
        total = sum(data)
        average = round(total / len(data), 2)

    else:

        flat = []

        for row in data:
            flat.extend(row)

        minimum = min(flat)
        maximum = max(flat)
        total = sum(flat)
        average = round(total / len(flat), 2)

    return minimum, maximum, total, average

# ---------------- Main Program ----------------

data = []
array_type = "1D"

while True:

    menu()

    choice = input("\nEnter Choice : ")

    if choice == "1":

        data, array_type = input_data()

    elif choice == "2":

        display_summary(data)

    elif choice == "3":

        number = int(input("Enter Number to calulate its factorial: "))
        print("Factorial :", factorial(number))

    elif choice == "4":

        filter_data(data)

    elif choice == "5":

        sort_data(data)

    elif choice == "6":

        minimum, maximum, total, average = dataset_statistics(data)

        if minimum is not None:

            print("\nDataset Statistics")
            print("Minimum :", minimum)
            print("Maximum :", maximum)
            print("Sum :", total)
            print("Average :", average)

        else:

            print("No Data Available")

    elif choice == "7":

        print("\nThank You...")
        break

    else:

        print("Invalid Choice")
