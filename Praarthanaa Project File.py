# Initialize an empty dictionary to store the gene data
gene_dict = {}

# Open the gene data file for reading
with open('sequence_file.txt', 'r') as gene_file:

    # Read the contents of the file line by line
    for line in gene_file:

        # Check if the line starts with '>'
        if line.startswith('>'):
            
            # Extract the gene ID and remove any trailing whitespace
            gene_id = line.split()[0][1:].strip()
            
            # Read the next line to get the gene details
            gene_details = next(gene_file).strip()
            if(gene_details.startswith('>')):
              break

           # Add the gene ID and details to the dictionary
            gene_dict[gene_id] = gene_details

# Function to retrieve gene details given a gene ID
def get_gene_details(gene_id):
    if gene_id in gene_dict:
        return gene_dict[gene_id]
    else:
        return "Gene ID not found in dictionary"

# Function to retrieve gene details given a list of gene IDs
def get_gene_details_list(gene_id_list):
    # Sort the gene ID list alphabetically
    gene_id_list.sort()
    
    # Create an empty list to store the gene details
    gene_details_list = []
    
    # Iterate over the gene ID list and retrieve the gene details for each ID
    for gene_id in gene_id_list:
        if gene_id in gene_dict:
            gene_details_list.append(gene_dict[gene_id])
        else:
            gene_details_list.append("Gene ID not found in dictionary")
    
    # Return the list of gene details
    return gene_details_list

# Retrieve the gene details for a list of gene IDs
a= input("How many gene IDs do you want to locate: ")
gene_id_list = []
i=0
for i in range(int(a)):
    gene_id = input("Enter Gene ID: ")
    gene_id_list.append(gene_id)
gene_details_list = get_gene_details_list(gene_id_list)
print("\n")
for gene_id, gene_details in zip(gene_id_list, gene_details_list):
    print(f"Gene ID: {gene_id}\nGene Details: {gene_details}\n")
