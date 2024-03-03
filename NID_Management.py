
NID_SOTORE = {}

def add_NID_number():
   
    name = input("Adding Enter the name: ")
    NID = input("Adding Enter the NID number: ")

    if name in NID_SOTORE:
        NID_SOTORE[name].append(NID)

    else:
        NID_SOTORE[name] = [NID]

def delete_NID_number():

    name = input("Delete Enter the name: ")
    NID = input("Delete Enter the NID number: ")

    if name in NID_SOTORE:
        if NID in NID_SOTORE[name]:
            NID_SOTORE[name].remove(NID)

def update_NID_number():

    name = input("Update Enter the name: ")
    old_NID = input("Enter the old NID number: ")
    new_NID = input("Enter the new NID number: ")

    if name in NID_SOTORE and old_NID in NID_SOTORE[name]:

        NID_SOTORE[name][NID_SOTORE[name].index(old_NID)] = new_NID

def search_NID_number():

    name = input("Search Enter the name: ")

    if name in NID_SOTORE:
        return NID_SOTORE[name]

    else:
        return "Name not found"


if __name__=='__main__':

    add_NID_number()

    add_NID_number()
 
    print(search_NID_number())  
    print(delete_NID_number())

    print(search_NID_number())
    update_NID_number()
    print(search_NID_number()) 