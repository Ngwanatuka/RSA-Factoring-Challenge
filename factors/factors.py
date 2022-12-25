import sys

# Check if a file was provided
if len(sys.argv) < 2:
  print("Error: No file provided")
  sys.exit(1)

# Open the file
with open(sys.argv[1], 'r') as f:
  # Read the file line by line
  for line in f:
    # Try to factorize the number
    n = int(line.strip())
    p = n // 2
    while p >= 2:
      q = n // p
      if p * q == n:
        print(f"{n}={p}*{q}")
      p -= 1
