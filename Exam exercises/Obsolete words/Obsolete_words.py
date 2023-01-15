##
#

def main():

    # create dictionary of obsolete words
    with open("obsolete.txt") as obsolete_file:
        lines = [i.split() for i in obsolete_file]
    
    word_sub = {f" {line[0]}": line[1] for line in lines}

    with open("text.txt") as file_text:
        text = file_text.readlines()

    sub_count = {}
    for idx, line in enumerate(text):
        for word in word_sub:

            if word not in line:
                continue
            count = line.count(word)

            if word not in sub_count:
                sub_count.update({word: 1})
            else:
                sub_count[word] += count
            text[idx] = line.replace(word, word_sub[word], count)
    
    print(sub_count)
            
    with open("output.txt", "w") as out_file:
        for line in text:
            out_file.write(line)
    

main()