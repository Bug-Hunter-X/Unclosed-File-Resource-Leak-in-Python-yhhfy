def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    f.write("This file will remain open!")
    # Missing f.close() call

function_with_unclosed_file("my_file.txt")