# Part B - Q2: Shallow copy vs Deep copy demonstration

import copy


if __name__ == "__main__":
    nested = [[10, 20], ["x", "y"]]

    shallow_lst = copy.copy(nested)
    deep_lst = copy.deepcopy(nested)

    print("Initial lists:")
    print("  Original:", nested)
    print("  Shallow: ", shallow_lst)
    print("  Deep:    ", deep_lst)

    nested[0][0] = 999
    print("\nAfter changing nested[0][0] = 999:")
    print("  Original:", nested)
    print("  Shallow: ", shallow_lst, "<- changed (shares inner object)")
    print("  Deep:    ", deep_lst, "<- independent")
