def get_names():
    name = []
    with open("note.txt", "r+") as fp:
        for line in fp:
            for i in line.split(':'):
                if not i.isdigit():
                    name.append(i)
                    break
    return name


def get_notes():
    notes = []
    with open("note.txt", "r+") as fp:
        for line in fp:
            for i in line.split(":"):
                for a in i.split("\n"):
                    if a.isdigit():
                        notes.append(a)
    return notes


def get_note(name):
    for x in range(len(get_names())):
        if get_names()[x] == name:
            return get_notes()[x]


def has_passed(name):
    if name in get_names():
        if int(get_note(name)) >= 10:
            return True
        else:
            return False
    else:
        return "Ce nom n'est pas dans la base de donnée"
    
def get_average():
    nbr = 0
    for i in get_notes():
        nbr += int(i)
    avg = nbr/len(get_notes())
    return avg

def add_student(name,note):
    element = f"{name}",":",f"{note}"
    with open("note.txt","a") as fp:
        fp.write("\n")
        fp.writelines(element)
        
print(get_note('Yassine'))