"""
The test file for part 1. The grader will use this file to test whether your system gives the right answer.
It should run with the following command `python3 test1.py` from the *root directory* of the assignment.
"""

import csv
from part1.code import *

input_dir = 'part1/input/'
output_dir = 'part1/output/'

def read_file(filename):
  """Read the csv file at the given path"""
  with open(filename, mode='r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    test = [row for row in csv_reader]
  return test


def s2t(string):
  """Convert a keyword string to the appropriate type"""
  if string == 'True':
    return True
  elif string == 'False':
    return False
  elif string == 'None':
    return None
  else:
    return string


def run_tests(inputs, ans_test, ans_gold):
  """Compares test answers to gold answers and prints number correct"""
  n = 0
  m = 1
  for (i, t, g) in zip(inputs, ans_test, ans_gold):
    if t == g:
      s = 'SUCCESS'
      n = n+1
    else:
      s = 'FAILURE'
    print('%d: %s\n  in:   %s\n  test: %s\n  gold: %s' % (m, s, i, t, g))
    m += 1
  print('NUMBER CORRECT: %s / %s\n' % (n, len(ans_gold)))


def test_check_subsumption():
  """Test 'check_subsumption' function"""
  in_raw = read_file(input_dir + 'input.txt')
  out_raw = read_file(output_dir + 'output.txt')
  ans_test = [check_subsumption(*x) for x in in_raw]
  ans_gold = [(s2t(x[0]), s2t(x[1])) for x in out_raw]
  print('\n\nTesting function \'check_subsumption\':')
  run_tests(in_raw, ans_test, ans_gold)


def main():
  test_check_subsumption()
  

if __name__== "__main__":
  main()
