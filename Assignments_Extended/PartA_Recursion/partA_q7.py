# Part A - Q7: Recursive Tower of Hanoi


def solve_hanoi(disks, source, target, aux, counter=[0]):
    if disks == 1:
        counter[0] += 1
        print(f"Move {counter[0]}: Disk 1 from {source} -> {target}")
        return

    solve_hanoi(disks - 1, source, aux, target, counter)
    counter[0] += 1
    print(f"Move {counter[0]}: Disk {disks} from {source} -> {target}")
    solve_hanoi(disks - 1, aux, target, source, counter)


if __name__ == "__main__":
    print("Solving Tower of Hanoi for 3 disks:")
    solve_hanoi(3, "A", "C", "B")
