from Osztaly import Osztaly

def fajlbeolvas():
        
        f= open("auto.txt","r",encoding="UTF-8")
        f.readline()
        fbol_sorok=f.readlines()
        print(fbol_sorok)
        f.close()

        A_Lista=[]
        for i in range(0,len(fbol_sorok),1):
                elem=fbol_sorok[i]
                lista=elem.strip().split(";")
                print(lista)
                nev:str=str(lista[0])
                datum:str=str(lista[1])
                auto=A_Lista(nev,datum)
                A_Lista.append(auto)

        return A_Lista



def tabla():
        