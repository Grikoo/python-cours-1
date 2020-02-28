import sys
def ecrire (mon_fichier):
    f=open(mon_fichier,"w")
    f.write(' yanis jeblblbl')
    f.close
    
def lire (mon_fichier):
    f=open(mon_fichier,"r")
    print(f.read())

if __name__ == "__main__":
    mon_fichier = input(sys.argv[0])
    ecrire(mon_fichier)
    lire(mon_fichier)
    print ("This is the name of the script: ", sys.argv[0])
    print ("Number of arguments: ", len(sys.argv))
    print ("The arguments are: " , str(sys.argv))
