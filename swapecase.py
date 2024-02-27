def swape_case(s):
    
    nk = ''
    for i in s:
        if i.isupper() == True:
            nk += i.lower()
        else:
            nk +=i.upper()
            
    return nk


vk = swape_case('vIGnESh')

print(vk)