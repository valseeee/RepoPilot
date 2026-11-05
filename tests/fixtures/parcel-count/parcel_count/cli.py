import sys

from .labels import count_labels


def main():
    print(count_labels(sys.stdin))
