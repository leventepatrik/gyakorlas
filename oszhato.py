import random

def lista():
    print("2.feladat")
    lista=[]
    for i in range(50):
        szamok=random.randint(1,100)
        lista.append(szamok)
        print(szamok)
    return lista   



def ottel_oszthato(szamok):
    szamlalo=0
    for i in range(0,len(szamok),1):
        if szamok[i]%7==0:
            szamlalo+=1
        i+=1
    print(f"A héttel osztható számok száma:{szamlalo}")
    return szamlalo