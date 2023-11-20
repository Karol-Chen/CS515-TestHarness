# import os
# import subprocess
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# def run_test(program, test_name):
#     input_file = f"test/{program}.{test_name}.in"
#     print(input_file)
#     expected_output_file = f"test/{program}.{test_name}.out"
#     expected_arg_output_file = f"test/{program}.{test_name}.arg.out"
#     args=None
#     if(program=="gron"):
#         args=f"python prog/{program}.py -f {input_file}"
#     if(program=="wc"):
#         args=f"python prog/{program}.py -l -w -c {input_file}"
#     if(program=="csv_sum"):
#         args=f"python prog/{program}.py {input_file} age,salary"
#     try:
#         with open(input_file, 'r') as f:
#             input_data = f.read()
#         process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         output, _ = process.communicate(input=input_data)
#         exit_code = process.returncode

#         if os.path.exists(expected_output_file):
#             with open(expected_output_file, 'r') as f:
#                 expected_output = f.read()
#                 assert output == expected_output, "OutputMismatch"

#         if os.path.exists(expected_arg_output_file):
#             process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#             arg_output, _ = process.communicate()
#             exit_code_arg = process.returncode
#             with open(expected_arg_output_file, 'r') as f:
#                 expected_arg_output = f.read()
#                 assert arg_output == expected_arg_output, "OutputMismatch"

#         assert exit_code == 0, "NonZeroExitCode"

#         assert exit_code_arg == 0, "NonZeroExitCode_Arg"

#         print(f"OK: {program} {test_name}")

#     except Exception as e:
#         print(f"FAIL: {program} {test_name} ({e})")
#             # print(f"FAIL: {program} {test_name} ({e})")
#         print(f"Command: {args}")
#         print(f"Output: {output}")
#         print(f"Exit Code: {exit_code}")
#     # finally:
#     #     os.chdir("..") 

# def run_tests(program):
#     test_files = [f for f in os.listdir("./test") if f.startswith(f"{program}.") and f.endswith(".in")]

#     print(test_files)
#     for test_file in test_files:
#         test_name = test_file[len(program) + 1:-3]
#         run_test(program, test_name) 

# if __name__ == "__main__":
#     program_name = "gron"
#     run_tests(program_name)
#     run_tests("csv_sum")
#     run_tests("wc")

import os
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def run_test(program, test_name):
    input_file = os.path.join("test", f"{program}.{test_name}.in")
    print(input_file)
    expected_output_file = os.path.join("test", f"{program}.{test_name}.out")
    expected_arg_output_file = os.path.join("test", f"{program}.{test_name}.arg.out")
    
    args = None
    if program == "gron":
        args = f"python prog/{program}.py -f {input_file}"
    elif program == "wc":
        args = f"python prog/{program}.py -l -w -c {input_file}"
    elif program == "csv_sum":
        args = f"python prog/{program}.py {input_file} age,salary"
    
    try:
        with open(input_file, 'r') as f:
            input_data = f.read()
        process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, _ = process.communicate(input=input_data)
        exit_code = process.returncode

        if os.path.exists(expected_output_file):
            with open(expected_output_file, 'r') as f:
                expected_output = f.read()
                assert output == expected_output, "OutputMismatch"

        if os.path.exists(expected_arg_output_file):
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            arg_output, _ = process.communicate()
            exit_code_arg = process.returncode
            with open(expected_arg_output_file, 'r') as f:
                expected_arg_output = f.read()
                assert arg_output == expected_arg_output, "OutputMismatch"

        assert exit_code == 0, "NonZeroExitCode"
        assert exit_code_arg == 0, "NonZeroExitCode_Arg"

        print(f"OK: {program} {test_name}")

    except Exception as e:
        print(f"FAIL: {program} {test_name} ({e})")
        print(f"Command: {args}")
        print(f"Output: {output}")
        print(f"Exit Code: {exit_code}")

def run_tests(program):
    test_files = [f for f in os.listdir("./test") if f.startswith(f"{program}.") and f.endswith(".in")]

    print(test_files)
    for test_file in test_files:
        test_name = test_file[len(program) + 1:-3]
        run_test(program, test_name)

if __name__ == "__main__":
    program_name = "gron"
    run_tests(program_name)
    run_tests("csv_sum")
    run_tests("wc")
