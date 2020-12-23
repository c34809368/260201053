"""
A script for automatically grading Python assignments.
This is the student copy which is slightly different than the instructor copy.
version 27.11.2020 by Ersin Çine
"""

import os
import subprocess


def ends_with_newline(path):
    file = open(path)
    content = file.read()
    file.close()
    return len(content) > 0 and content[-1] == "\n"
    # TODO: Is this okay on Windows?
    # Will we be in trouble if their line separator is CRLF (\r\n)?
    # We also do this in other places.
    # Probably don't be lazy and do it properly!!!


def read_text_file(path):
    file = open(path)
    content = file.read()
    file.close()
    return content


homework_no = input("Enter homework no:")
student_id = input("Enter student id:")

submission_filename = f"ceng113_hw{homework_no}_{student_id}.py"
directory = os.path.dirname(os.path.realpath(__file__))
print(f"I am looking for a file named {submission_filename} in {directory}.")
files = os.listdir()
if submission_filename in files:
    print("Yes, I found the file. Good.")
else:
    print("ERROR! There is no such file.")
    exit()

print("-" * 100)
print("These are the examples in the same directory:")

examples = set()
for file in files:
    example = None
    if file.endswith(".txt"):
        if file.startswith("inputs_"):
            example = file[len("inputs_"):-len(".txt")]
        elif file.startswith("outputs_"):
            example = file[len("outputs_"):-len(".txt")]
        if example is not None:
            inputs_filename = f"inputs_{example}.txt"
            outputs_filename = f"outputs_{example}.txt"
            if inputs_filename in files and outputs_filename in files:
                examples.add(example)
            elif inputs_filename in files:
                print(f"There is {inputs_filename} but not {outputs_filename} !!! (Create this file.)")
            elif outputs_filename in files:
                print(f"There is {outputs_filename} but not {inputs_filename} !!! (Create this file.)")

proper_examples = set()
for example in sorted(examples):
    print(example)
    inputs_filename = f"inputs_{example}.txt"
    outputs_filename = f"outputs_{example}.txt"
    inputs_ends_with_newline = ends_with_newline(inputs_filename)
    outputs_ends_with_newline = ends_with_newline(outputs_filename)
    if inputs_ends_with_newline and outputs_ends_with_newline:
        proper_examples.add(example)
    else:
        if not inputs_ends_with_newline:
            print(f"{inputs_filename} does not end with a newline !!! (Add an empty line at the end.)")
        if not outputs_ends_with_newline:
            print(f"{outputs_filename} does not end with a newline !!! (Add an empty line at the end.)")

if len(proper_examples) == 0:
    print("ERROR! There is no example. Create inputs_1.txt and outputs_1.txt.")
    exit()

example = input("Enter an example:")

while example not in proper_examples:
    print("This example is not available!")
    example = input("Enter an example:")

# submission_filename
inputs_filename = f"inputs_{example}.txt"
outputs_filename = f"outputs_{example}.txt"

print("-" * 100)
print("Okay we start to compare the outputs...")
print("-" * 100)
correct_outputs = read_text_file(outputs_filename)
with open(inputs_filename) as inputs:
    submission_outputs = subprocess.run(["python", submission_filename], stdin=inputs, stdout=subprocess.PIPE).stdout.decode("utf-8")
    # TODO: use the named argument: timeout

    submission_lines = submission_outputs.splitlines()
    correct_lines = correct_outputs.splitlines()

    if len(submission_lines) == len(correct_lines):
        print(f"Both your output and correct output have {len(submission_lines)} lines. Very good.")
    else:
        print(f"Correct output has {len(correct_lines)} lines.")
        print(f"But your solution has {len(submission_lines)} lines. Not good!!!")
        print(f"I will display the first {min(len(correct_lines), len(submission_lines))} lines:")

    print("-" * 100)

    score = 0
    line_no = 0
    for submission, correct in zip(submission_lines, correct_lines):
        if submission == correct:
            print(f"{line_no:3}|{submission}")
            score += 1
        else:
            print()
            print(f"Error in line {line_no}!")
            print("You displayed this:")
            print(submission)
            print("But the correct output is this:")
            print(correct)
            print()
        line_no += 1

    print("-" * 100)
    print(f"Score: {score} out of {len(correct_lines)}.")
