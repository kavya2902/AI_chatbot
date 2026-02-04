from vector_db import add_data

with open("data.txt") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    add_data(line.strip(), f"doc{i}")

print("Data Loaded!")
