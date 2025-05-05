def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:  # Base case: if there's only one disk, move it directly from source to target
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move the top (n-1) disks from source to auxiliary peg
    tower_of_hanoi(n-1, source, auxiliary, target)
    
    # Move the nth disk (largest disk) from source to target peg
    print(f"Move disk {n} from {source} to {target}")
    
    # Move the (n-1) disks from auxiliary peg to target peg
    tower_of_hanoi(n-1, auxiliary, target, source)

# Driver Code
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'C', 'B')
