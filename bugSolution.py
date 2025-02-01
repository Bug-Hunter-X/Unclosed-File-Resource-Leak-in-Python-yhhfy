def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("This file is properly closed!")
    except Exception as e:
        print(f"An error occurred: {e}")

function_with_closed_file("my_file.txt")
