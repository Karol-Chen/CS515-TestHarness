# CS515-TestHarness

# Project Submission - CS515 Test Harness

## Author

- **Name:**Daixuan Chen
- **Stevens Login:** 20015422

## GitHub Repository

- **URL:**https://github.com/Karol-Chen/CS515-TestHarness

## Time Spent

- I spent approximately 20 hours on this project. About 10 of those hours I spent writing gron and ungron, and about 2 hours of the other 10 hours consulting the documentation.

## Testing Approach

- I tested my code using a combination of unit tests and integration tests.
- For unit tests, I used Python's built-in `unittest` module to test individual functions.
- For integration tests, I created a test harness (`test.py`) to automate the execution of various test cases.

## Bugs or Issues

- I encountered tons of bugs in gron.py, such as stack overflows due to recursive repeat calls, and overcalls in processing json files.
- The main problems I'm having with test.py are inaccessible files and subprocess handling issues. The former I solved by modifying relative paths, the latter I did in hardcode form.

## Difficult Issue

- The most challenging issue I encountered was related to the inability to locate files when running tests in the GitHub Actions environment. The root cause of this problem lies in the difference between the working directory in the GitHub Actions environment and the one set locally, causing file paths to be resolved incorrectly.

## Implemented Extensions

1. **More advanced wc: multiple files**

   - Description: This extension allows the `wc` program to handle multiple files. The test cases include scenarios with multiple input files, and the output should display individual counts as well as a total count.
   - Evaluation: To test this extension, create test cases with multiple input files and check if the output correctly displays individual and total counts.

2. **Flags to control output**

   - Description: The `wc` program now supports flags to control the information shown. For example, `-l` counts only lines, `-w` counts only words, and `-c` counts only characters. Multiple flags can be combined.
   - Evaluation: Test different combinations of flags with various input files and ensure that the output matches the expected counts.

3. **Expected STDERR**
   - Description: Introduce the ability to specify the expected output on STDERR using a PROG.NAME.err file. If the STDERR of the actual command doesn’t match, fail the test case. Also, consider creating PROG.NAME.arg.err for running on arguments.
   - Evaluation: Write tests with both empty and non-empty STDERR and PROG.NAME.err files, ensuring that the test case fails when STDERR doesn't match the expected output.
