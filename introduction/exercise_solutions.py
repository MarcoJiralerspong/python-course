# Exercise: Variables and printing
my_name = "Marco"
print(my_name)
my_name = "Mar"
print(my_name)

# Exercise: Object types

num_sequences = 12
is_sequence = True
sequence_1 = "GATC"
sequence_2 = "CCTA"

print(num_sequences)
print(is_sequence)
print(sequence_1)
print(sequence_2)


# Exercise: Collections

# Create both tuples
pair_1 = ("G", "C")
pair_2 = ("T", "A")
pairs = [pair_1, pair_2]  # Set list elements to be the tuples
# or
pairs = []  # Create empty list
pairs.append(pair_1)  # Add tuples to list one at a time
pairs.append(pair_2)

pairs[0][0]  # The first [0] access the first tuple, the second [0] accesses the first element of that tuple

bases = {"A": "Adenine", "G": "Guanine", "C": "Cytosine", "T": "Thymine"}
print(bases["G"])

# Exercise: Math
import math

area = 3 ** 2 * math.pi
print(math.floor(area))

print(23 ** 24)

print(8 * 4 / 2 - (3 * 2) - (16 + 5))

# Exercise: Conditionals
sequence = "ATGCTACGATCGATCG"

if sequence.startswith("A"):
    print("Adenine")
elif sequence.startswith("G"):
    print("Guanine")
elif sequence.startswith("C"):
    print("Cytosine")
else:
    print("Thymine")

if sequence.startswith("G") or sequence.startswith("C"):
    print("GC")

# Exercise: Loops
two = 1

while two < 10000:
    print(two)
    two = two * 2

sequences = {"seq_01": "ATTGCTA", "seq_02": "GCTGATC", "seq_03": "GTACG"}
for seq_id, seq in sequences.items():
    print("Sequence " + seq_id + " starts with " + seq[0] + ".")

# Exercise: Functions
def print_seq_proportions(sequence):
    print(sequence.count("A")/len(sequence))
    print(sequence.count("G")/len(sequence))
    print(sequence.count("T")/len(sequence))
    print(sequence.count("C")/len(sequence))

print_seq_proportions("GATCGATCGATCGATCGATAGC")

# Exercise: Classes
class Sequence:
    def __init__(self, seq_id, sequence_string):
        self.seq_id = seq_id
        self.sequence_string = sequence_string

    def print_proportions(self):
        print(self.sequence_string.count("A")/len(self.sequence_string))
        print(self.sequence_string.count("G")/len(self.sequence_string))
        print(self.sequence_string.count("T")/len(self.sequence_string))
        print(self.sequence_string.count("C")/len(self.sequence_string))

sequence = Sequence("seq_05", "GTACGTAGCTAG")
sequence.print_proportions()

# Exercise: IO
sequence_string = input("Please enter sequence:")
seq_id = input("Please enter sequence ID:")

sequence = Sequence(seq_id, sequence_string)
sequence.print_proportions()

# Exercise: Everything
while True:
    sequence = input("Please enter sequence:")
    print("Proportion of A: " + str(sequence.count("A")/len(sequence)))
    print("Proportion of G: " + str(sequence.count("G")/len(sequence)))
    print("Proportion of T: " + str(sequence.count("T")/len(sequence)))
    print("Proportion of C: " + str(sequence.count("C")/len(sequence)))
