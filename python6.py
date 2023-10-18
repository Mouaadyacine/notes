a=int(input("entrer le nombre des etudiants"))
tab=[]
s=0
for i in range(0,a):
 b=int(input("entrer la note d'etudiant"))
 tab.append(b)
 s=s+tab[i]
m=s/a
for i in range(0,a):
    if tab[i]>m:
        print(tab[i])