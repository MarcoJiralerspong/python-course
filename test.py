filename = input("Please input the filename of the fasta file you want to analyze: ")

num_sequences = 0 # Counter variable that keeps track of the number of sequences
sum_gc_content = 0 # Keep track of the total gc content of all strings

with open(filename, "r") as file:
    
    for line in file.readlines():
        if not line.startswith(">"):
            gc_content = (line.count("C") + line.count("G") )/len(line)
            sum_gc_content = sum_gc_content + gc_content
            num_sequences = num_sequences + 1

    print(sum_gc_content/num_sequences)