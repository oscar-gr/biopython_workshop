from Bio import SeqIO
#filename = "NC_000913.faa"
filename = "PGSC_DM_v3.4_pep_representative.fasta"
no_star = 0
with_star = 0
print("Checking " + filename + " for terminal stop codons")
for record in SeqIO.parse(filename, "fasta"):
    if record.seq.endswith("*"):
        with_star = with_star + 1
    else:
        no_star = no_star + 1
print(str(with_star) + " with terminal stop, " + str(no_star) + " without terminal stop")

