# Functional Treat

print("Welcome to the Data Analyzer and Transformer Program")

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

    while True:

        print("\n1. 1D Array")
        print("2. 2D Array")

        ch = input("Enter Choice : ")

        if ch == "1":

            data = list(map(int, input("Enter Elements : ").split()))

            if len(data) == 0:
                print("Data cannot be empty.")
                continue

            return data, "1D"

        elif ch == "2":

            rows = int(input("Enter Rows : "))

            if rows <= 0:
                print("Rows must be greater than 0.")
                continue

            data = []

            for i in range(rows):

                row = list(map(int, input(f"Row {i+1} : ").split()))

                if len(row) == 0:
                    print("Empty Row is not allowed.")
                    return [], "2D"

                data.append(row)

            columns = len(data[0])

            for row in data:

                if len(row) != columns:
                    print("All rows must have equal columns.")
                    return [], "2D"

            return data, "2D"

        else:

            print("Invalid Choice! Please Enter 1 or 2.")


# Summary Function

def display_summary(data, array_type):

    if len(data) == 0:
        return None

    summary = {}

    if array_type == "1D":

        summary["Total Elements"] = len(data)
        summary["Minimum"] = min(data)
        summary["Maximum"] = max(data)
        summary["Sum"] = sum(data)
        summary["Average"] = round(sum(data) / len(data), 2)

    else:

        flat = []

        for row in data:
            flat.extend(row)

        summary["Rows"] = len(data)
        summary["Columns"] = len(data[0])
        summary["Total Elements"] = len(flat)
        summary["Minimum"] = min(flat)
        summary["Maximum"] = max(flat)
        summary["Sum"] = sum(flat)
        summary["Average"] = round(sum(flat) / len(flat), 2)

    return summary


# **kwargs Function

def print_summary(**kwargs):

    print("\nSummary")

    for key, value in kwargs.items():
        print(key, ":", value)

# Recursive Function

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


# Lambda Function

def filter_data(data, array_type):

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

def sort_data(data, array_type):

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

def dataset_statistics(data, array_type):

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


# *args Function

def print_statistics(*args):

    labels = ["Minimum", "Maximum", "Sum", "Average"]

    print("\nDataset Statistics")

    for label, value in zip(labels, args):
        print(label, ":", value)

# ---------------- Main Program ----------------

data = []
array_type = "1D"

while True:

    menu()

    choice = input("\nEnter Choice : ")

    if choice == "1":

        data, array_type = input_data()

    elif choice == "2":

        summary = display_summary(data, array_type)

        if summary:

            print_summary(**summary)

        else:

            print("No Data Available")

    elif choice == "3":

        number = int(input("Enter Number to calculate its Factorial : "))

        if number < 0:

            print("Factorial is not defined for Negative Numbers.")

        else:

            print("Factorial :", factorial(number))

    elif choice == "4":

        filter_data(data, array_type)

    elif choice == "5":

        sort_data(data, array_type)

    elif choice == "6":

        minimum, maximum, total, average = dataset_statistics(data, array_type)

        if minimum is not None:

            print_statistics(minimum, maximum, total, average)

        else:

            print("No Data Available")

    elif choice == "7":

        print("\nThank You for using the Data Analyzer and Transformer Program.")
        print("Goodbye!")
        break

    else:

        print("Invalid Choice")
