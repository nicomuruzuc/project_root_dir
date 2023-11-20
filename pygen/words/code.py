import re #package regex (regular expression, for pattern mathcing)

#step 1: words

def read_words(file):
    result = [] # 
    f = open(file, "r") # 
    Lines = f.read().splitlines()
    for line in Lines:
        if len(line) >= 3:
            result.append(line.upper())

    return result


#print file content
#file = open("proteome_fasta",'r')
#print (file.read())

#step 2: dictionnary
def read_sequence(file):
    fasta_file = open(file, "r")
    sections = re.split(r'>sp\|([A-Z0-9]*)\|', fasta_file.read().replace('\n', ''))
    dictionary = {}
    print(sections)

    i=1

    while i < len(sections)-1:
        key = sections[i]
        dictionary[key] = sections[i+1]
        i += 2

    for key, value in dictionary.items():
        if key == 'O95139':
            print(f"Key: {key}")
            print(f"Section content:")
            print(value)
            print("\n")

    return dictionary

def main():
    #dictionary = read_sequence('proteome_fasta.txt')
    result = read_words('words_file.txt')
    print(result)

if __name__ =='__main__':
    main()

