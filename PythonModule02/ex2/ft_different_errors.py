def garden_operations(operations_number):
    if operations_number == 0:
        value = int("abc")
    elif operations_number == 1:
        value = 10 / 0
    elif operations_number == 2:
        missing_file = '/non/existent/file'
        with open(missing_file) as file:
            print(file)
    elif operations_number == 3:
        value = "abc" + 3
    elif operations_number == 4:
        print("Operation completed successfully")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    for num in [0, 1, 2, 3, 4]:
        print(f"Testing operation {num}...")
        try:
            garden_operations(num)
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("All error types tested successfully!")

test_error_types()