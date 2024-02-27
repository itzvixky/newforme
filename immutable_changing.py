def spell_correction(string,position,character):
    
    corrected = string[:position] + character + string[position+1:]
    
    return corrected

string = 'vizky' #input() also possible
position = 2     #int(input())
character = 'c'  #input()

vk = spell_correction(string,position,character)

print(vk)