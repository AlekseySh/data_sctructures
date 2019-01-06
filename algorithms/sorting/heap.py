from algorithms.sorting.test import test
from structures.bin_heap import BinHeap

__all__ = ['heap_sort']


def heap_sort(x):
    bin_heap = BinHeap(x)
    bin_heap.build_heap()
    bin_heap.inplace_sort()


def main():
    test(sort_func=heap_sort)
    print('Heap-sort passed tests!')


if __name__ == '__main__':
    main()
