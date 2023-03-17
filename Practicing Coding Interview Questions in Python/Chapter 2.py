'''
For example, passing the string 'ukulele' to the retrieve_character_indices() function should result in the following output: 
{'e': [4, 6], 'k': [1], 'l': [3, 5], 'u': [0, 2]}.
'''
def character_position(string):                       
    output = dict()
    
    for index, character in enumerate(string):
        if character in output:
            output[character].append(index)
        else:
            output[character] = [index]
            
    return output
