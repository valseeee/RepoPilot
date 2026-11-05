def count_labels(lines):
    return sum(1 for line in lines if line.strip())
