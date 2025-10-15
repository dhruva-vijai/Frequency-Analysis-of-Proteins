import requests
from io import StringIO
from Bio import SeqIO

def reader(string):
    lst=string.split()
    print(lst)
    protein_sequences={}
    for i in lst: 
        url = 'https://www.uniprot.org/uniprot/'+i+'.fasta'
        response=requests.get(url)

        try:
            data=StringIO(response.text)
            sequence=SeqIO.read(data,'fasta')
            
            protein_sequences[i]=str(sequence.seq)

        except ValueError:
            pass


    return(protein_sequences)

