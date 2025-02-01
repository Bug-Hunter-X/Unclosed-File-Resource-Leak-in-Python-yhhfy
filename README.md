# Unclosed File Resource Leak

This repository demonstrates a common, yet often overlooked, error in Python: failing to close a file after opening it. This can lead to resource leaks and potential data corruption. The `bug.py` file contains the erroneous code, while `bugSolution.py` presents a corrected version using context managers.