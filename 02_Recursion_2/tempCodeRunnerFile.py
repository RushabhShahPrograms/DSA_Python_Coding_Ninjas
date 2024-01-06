
a c
b a
b c
a c
'''

def tower_of_hanoi(n, source_rod, destination_rod, auxiliary_rod):
    if n == 1:
        print(source_rod, destination_rod)