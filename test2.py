"""
The test file for part 2. The grader will use this file to test whether your system gives the right answer.
It should run with the following command `python3 test2.py` from the *root directory* of the assignment.
"""

import csv
from part2.code import *

input_dir = 'part2/input/'
output_dir = 'part2/output/'

def read_file(filename):
  """Read the csv file at the given path"""
  with open(filename, mode='r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    test = [row for row in csv_reader]
  return test


def is_number(x):
  """Check if x is a number or number-like string (including floats)"""
  if not x:
    return False
  elif not isinstance(x, str):
    return True
  split = x.split('.')
  return x.isnumeric() or (len(split) == 2 and split[0].isnumeric() and split[1].isnumeric())


def compare(t, g):
  """Compares test answer to gold answer, allowing for some small variation with numerical answers"""
  if is_number(t) and is_number(g):
    t_f, g_f = float(t), float(g)
    return True if abs(t_f - g_f) <= 1e-4 else False
  else:
    return t == g


def run_tests(inputs, ans_test, ans_gold):
  """Compares test answers to gold answers and prints number correct"""
  n = 0
  m = 1
  for (i, t, g) in zip(inputs, ans_test, ans_gold):
    if compare(t, g):
      s = 'SUCCESS'
      n = n+1
    else:
      s = 'FAILURE'
    print('%d: %s\n  in:   %s\n  test: %s\n  gold: %s' % (m, s, i, t, g))
    m += 1
  print('NUMBER CORRECT: %s / %s\n' % (n, len(ans_gold)))
  return n


def test_similarity_path_dist(N, T):
  """Test 'similarity_path_dist' function"""
  in_raw = read_file(input_dir + 'path_distance.txt')
  out_raw = read_file(output_dir + 'path_distance.txt')
  ans_test = [similarity_path_dist(*x) for x in in_raw]
  ans_gold = [x[0] for x in out_raw]
  print('\n\nTesting function \'similarity_path_dist\':')
  return (N+run_tests(in_raw, ans_test, ans_gold), T+len(ans_gold))


def test_similarity_wu_palmer(N, T):
  """Test 'similarity_wu_palmer' function"""
  in_raw = read_file(input_dir + 'wu_palmer.txt')
  out_raw = read_file(output_dir + 'wu_palmer.txt')
  ans_test = [similarity_wu_palmer(*x) for x in in_raw]
  ans_gold = [x[0] for x in out_raw]
  print('\n\nTesting function \'similarity_wu_palmer\':')
  return (N+run_tests(in_raw, ans_test, ans_gold), T+len(ans_gold))


def test_most_similar_type(N, T):
  """Test 'most_similar_type' function"""
  in_raw = read_file(input_dir + 'similar_type.txt')
  out_raw = read_file(output_dir + 'similar_type.txt')
  ans_test = [most_similar_type(*x) for x in in_raw]
  ans_gold = [x[0] for x in out_raw]
  print('\n\nTesting function \'most_similar_type\':')
  return (N+run_tests(in_raw, ans_test, ans_gold), T+len(ans_gold))


def test_disambiguate_conjunction(N, T):
  """Test 'disambiguate_conjunction' function"""
  in_raw = read_file(input_dir + 'disambiguation.txt')
  out_raw = read_file(output_dir + 'disambiguation.txt')
  ans_test = [disambiguate_conjunction(*x) for x in in_raw]
  ans_gold = [x[0] for x in out_raw]
  print('\n\nTesting function \'disambiguate_conjunction\':')
  return (N+run_tests(in_raw, ans_test, ans_gold), T+len(ans_gold))


def main():
  N, T = 0, 0
  N, T = test_similarity_path_dist(N, T)
  N, T = test_similarity_wu_palmer(N, T)
  N, T = test_most_similar_type(N, T)
  N, T = test_disambiguate_conjunction(N, T)
  print('\nOVERALL CORRECT: %s / %s\n' % (N, T))


if __name__== "__main__":
  main()
