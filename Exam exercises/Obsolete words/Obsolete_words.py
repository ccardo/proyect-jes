##
#

def main():

    # create dictionary of obsolete words
    with open("obsolete.txt") as obsolete_file:
        lines = [i.split() for i in obsolete_file]
    
    word_sub = {line[0]: line[1] for line in lines}

    with open("text.txt") as file_text:
        text = file_text.readlines()
    
    for index, line in enumerate(text):
        
        if any(word in word_sub for word in line):
            
            for obsolete_word in word_sub:
                
                text[index] = line.replace(obsolete_word, word_sub[obsolete_word])
    
    with open("output.txt", "w") as output:

        for line in text:
            output.write(line)

main()