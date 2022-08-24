#import os
#import ftplib 

#login=input(" les valeurs sont :")
#if login == "bonjour":
    #print(" ok")
    #choix_zic=input("quelle musique : ")
    #os.system("ftp jmy@localhost ")
    #host = "localhost" # adresse du serveur FTP
    #user = "jmy" # votre identifiant
    #password = "1234" # votre mot de passe
    #m=connect = ftplib.ftplib(host,user,password) # on se connecte
    #fichier = "C:\Python_exercices\ftp.py"
    #file = open(fichier, 'rb') # ici, j'ouvre le fichier ftp.py 
    #connect.storbinary('STOR '+fichier, file) # ici (où connect est encore la variable de la connexion), j'indique le fichier à envoyer
    #file.close() # on ferme le fichier# Example Python program to upload a file to an FTP server

    # in binary mode

#Création des variables et importation des modules

from ftplib import FTP
import os, sys, subprocess, time

verdad=0
musique=""
musiqueok=""
#    login=sys.argv[1]
#    passwd=sys.argv[2]

#Etapes avant boucle

login=input("Quel est votre login ?")
passwd=input("Quel est votre password ?")
server=input("Quel est le serveur sur lequel il faut se connecter ?")
boucle=True

#Boucle main du streaming

while boucle:
    
    isIn=0
    cmd="lftp {0}:{1}@{2} -e 'cls;quit'".format(login,passwd,server)
    list_music=os.popen(cmd).read().split("\n")
    print(list_music)
    test_zic=input(" Quelle musique voulez vous ecouter :")

# Vérification si la musique demandée est sur le serveur FTP ou pas 

    for i in list_music:
        if test_zic in i:
            musique=i
            isIn=1
            musiqueok=musique.replace(" ","_")
            print(musiqueok)
            cmd="lftp {0}:{1}@{2} -e 'get {3};quit'".format(login,passwd,server,musique)
            os.popen(cmd)
            time.sleep(1)
            try:
                print("Entrée dans le try")
                os.mkdir("Musics/")
                print("Dossier Musics créé")
                time.sleep(1)
                proc=subprocess.Popen([f"mv",f"{musiqueok}",f"Musics/{musiqueok}"])
                proc=subprocess.Popen(["vlc",f"Musics/{musiqueok}"])
                proc.communicate()
            except:
                proc=subprocess.Popen([f"mv",f"{musiqueok}",f"Musics/{musiqueok}"])
                proc=subprocess.Popen(["vlc",f"Musics/{musiqueok}"])
                proc.communicate()
            
    if isIn == 0:
        list_music=os.popen("ls Musics/").read().split("\n")
        print(list_music)
        test_zic=test_zic.replace(" ","_")
        print(test_zic)
        flag=0
        for i in list_music:
            if test_zic.upper() in i.upper():                
                flag=1                     
                musique=i
                print(musique)
                break        
        
        if flag == 0:
            test_zic.replace("_"," ")
            proc=subprocess.Popen(["youtube-dl","-x","ytsearch1:{0}".format(test_zic)])
            proc.communicate()
            list_music=os.popen("ls")
            list_music=os.popen("ls").read().split("\n")
            for i in list_music:
                if test_zic.upper() in i.upper():                                     
                    musique=i
                    print(musique)
                    break
        
        musiqueok=musique.replace(" ","_")
        proc=subprocess.Popen([f"mv",f"{musique}",f"{musiqueok}"])
        cmd=f"lftp {login}:{passwd}@{server} -e 'put {musiqueok};quit'"
        os.popen(cmd)
        time.sleep(1)
        try:
            os.mkdir("Musics/")
        except:
            proc=subprocess.Popen([f"mv",f"{musiqueok}",f"Musics/{musiqueok}"])
            proc.communicate()
            proc=subprocess.Popen(["vlc",f"Musics/{musiqueok}"])
            proc.communicate()
            
    reponse=input("Voulez-vous continuer ? (O/n)").upper()
    if reponse == "N" or reponse == "NON" or reponse == "NO":
        boucle = False
                #proc=subprocess.Popen(["mkdir","Musics"]) 
                #proc.communicate()
#cmd="lftp {0}:{1} -e 'cls;quit'".format(login,passwd)
#list_music=os.popen(cmd).read().split("\n")

    #youtube-dl https://www.youtube.com/user/lyndapodcast ytsearch1:'David Booth'
    #cmd="vlc {0}".format(musique_tele)
    #los.popen(cmd)


# Create an FTP object and connect to the server

# as anonymous user

#ftpObject = FTP(host="localhost");
#'put {2};quit'
#print(ftpObject.getwelcome());

      

# Login to the server

#ftpResponseMessage = ftpObject.login(user='jmy',passwd='1234');

#print(ftpResponseMessage);

       

# Change to the required working directory

#ftpResponseMessage = ftpObject.cwd("/home/jmy/Music");

#print(ftpResponseMessage);

 #       'put {2};quit'

# Open the file in binary mode

#fileObject = open("mdm.py", "rb");

#file2BeSavedAs = "sujets.py"

          

#ftpCommand = "STOR %s"%file2BeSavedAs;

           

# Transfer the file in binary mode

#ftpResponseMessage = ftpObject.storbinary(ftpCommand, fp=fileObject);

#print(ftpResponseMessage);
    #os.sytem("pwd")
    #print(m)
#else:
#print("erreur")

