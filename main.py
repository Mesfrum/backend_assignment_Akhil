import json
from datetime import datetime
from tabulate import tabulate


# function to load data from JSON
def read_json_file():
    try:
        with open("AttendanceRegister.json") as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        print(f"File not found: {e}.")
        return None


# function to parse jsoin file and convert the data to a dictionary
def parse_json_file(data):
    search_result = {}

    for entry in data:
        employee_name = entry["employeName"].lower()
        entry_details = [
            entry["employeName"],
            entry["checkinTime"],
            entry["checkouttime"],
            entry["date"],
            entry["dept"],
            str(
                int(entry["checkouttime"].split(":")[0])
                - int(entry["checkinTime"].split(":")[0])
            ),
        ]
        if employee_name not in search_result:
            search_result[employee_name] = [entry_details]
        else:
            search_result[employee_name].append(entry_details)

    return search_result


def main(test_inputs, data):
    if data is None:
        return

    parsed_json = parse_json_file(data)

    for person_name in test_inputs:
        # try block to detect invalid user input
        try:
            cleaned_person_name = person_name.lower().strip()
        except Exception as e:
            print(f"Invalid input format for input: {person_name}, Error: {e}\n")
            continue

        try:
            output_table = []

            # get schedul details for person_name from parsed_json
            output_table.extend(parsed_json[cleaned_person_name])

            # output formating
            headers = [
                "Employee Name",
                "Date",
                "Check-in Time",
                "Checkout Time",
                "Department",
                "Working Hours per day",
            ]

            print(f"* Office schedule for {person_name}:")
            print(tabulate(output_table, headers=headers, tablefmt="grid"))
            print(f"Found {len(parsed_json[cleaned_person_name])} entries for {person_name}.\n")

        except Exception as e:
            print(f"* No data found for {person_name}:\n")


if __name__ == "__main__":
    data = read_json_file()

    # person_name = input("Enter person's name: ")
    # main([person_name], data)

    test_inputs = [
        " ",
        "",
        " test1",
        "test ",
        "Test1",
        "TEST4 ",
        "Akhil",
        123,
        "1234",
        "TesT2",
        "test 2",
    ]

    main(test_inputs, data)
