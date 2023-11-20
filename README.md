# CS515-TestHarness

# Project Submission - CS515 Test Harness

## Author

- **Name:**Daixuan Chen
- **Stevens Login:** 20015422

## GitHub Repository

- **URL:**https://github.com/Karol-Chen/CS515-TestHarness

## Time Spent

- I spent approximately 20 hours on this project.

## Testing Approach

- I tested my code using a combination of unit tests and integration tests.
- For unit tests, I used Python's built-in `unittest` module to test individual functions.
- For integration tests, I created a test harness (`test.py`) to automate the execution of various test cases.

## Bugs or Issues

-

## Difficult Issue

- One challenging issue was related to handling

## Implemented Extensions

1. **More advanced wc: multiple files**

   - Description: This extension allows the `wc` program to handle multiple files. The test cases include scenarios with multiple input files, and the output should display individual counts as well as a total count.
   - Evaluation: To test this extension, create test cases with multiple input files and check if the output correctly displays individual and total counts.

2. **Flags to control output**

   - Description: The `wc` program now supports flags to control the information shown. For example, `-l` counts only lines, `-w` counts only words, and `-c` counts only characters. Multiple flags can be combined.
   - Evaluation: Test different combinations of flags with various input files and ensure that the output matches the expected counts.

3. **Expected exit status**
   - Description: Each test case now includes a `PROG.NAME.status` file that contains a valid exit status (0 through 255). The test harness checks if the actual exit status matches the expected one.
   - Evaluation: Create test cases with various exit statuses and verify that the program correctly exits with the expected status.
