from tkinter import *
from random import shuffle 


#-------------------------partie declaration---------------------------

nb_lig=4
nb_col=5
nb_carte=nb_col*nb_lig//2
dim=128 #dimension de l'image
pad=5 #panding
side=dim+pad*2 #une seul coté
l=nb_col*side
h=nb_lig*side

#---------------------------------creation du canvas---------------------------------------

#-----------------------------------------convertir une image-----------------------

x0=y0=side/2 #coor de la centre de l'image



#---------------------------------------------------------------------
def Melange_grille():
    carte=list(range(nb_carte))*2  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    shuffle(carte) #melanger le contenu de la carte
    p=[]
    i=0
    for k in range(nb_lig):
        l=[]
        for j in range(nb_col):
            l.append(carte[i])
            i=i+1
        p.append(l)    
    return p






 #----------------------------------------------------------creation d'une liste d'image--------------- 
 
liste=['achiv','choy','daifuku','gas','kiwi','popsicle','python','sound','thumb','truck']
def creation_logos():        
    icones=[]
    for lang in liste:
        fichier="./image/"+lang+".png"
        icon=PhotoImage(file=fichier)
        icones.append(icon)
    return icones
   



    
 #affichage de la grille ---------------------------- placement des images-----------
def remplissage(plat):
    nb_l=4
    nb_c=5
    ids_imgs=[]
    for ligne in range(nb_l):
        id=[]
        for col in range(nb_c):
            centre=(col*side+x0,ligne*side+y0)
            print(col,"+", x0,"=",col*side+x0)
            nr=plat[ligne][col]
            icon=icones[nr]
            cnv.create_image(centre,image=icon)
            id_im= cnv.create_image(centre,image=logo)
            id.append(id_im)
        ids_imgs.append(id)  
    return ids_imgs    
          


def clic(event):
    if move[1] is not None:
        return
    x=event.x
    y=event.y
    col=x//side
    lig=y//side
    if (plat[lig][col]!=-1):
        traite_clic(lig,col)
        



def traite_clic(lig,col):
    global cpt
    item=ids_imgs[lig][col]
    cnv.delete(item)
    if move[0] is None:
        move[0]=(lig,col)
    else:
        if move[0]==(lig,col):       #meme clic 
            return
        cpt=cpt-1           #traitement du compteur
        lbl['text']=cpt     # --
        move[1]=(lig,col)    
        i,j=move[0]
        if plat[i][j]==plat[lig][col]:
             plat[i][j]=plat[lig][col]=-1
             move[0]=move[1]=None
                 
        else:
            cnv.after(400,cacher,i,j,lig,col)     
            
  
  
  
  
  
            
def cacher(i,j,lig,col):
    centre=(j*side+x0,side*i+y0)
    ids_imgs[i][j]= cnv.create_image(centre,image=logo)
    centre=(col*side+x0,lig*side+y0)
    ids_imgs[lig][col]= cnv.create_image(centre,image=logo)
    move[0]=move[1]=None
    
    
    
    
                
def init():
    global plat,ids_imgs,move,icones,logo ,cpt,lbl
    icones= creation_logos() 
    logo=PhotoImage(file="flag.png")  
    plat=Melange_grille()  
    ids_imgs=remplissage(plat)   
    move=[None,None]
    cpt=500
    lbl['text']=500
         
    
    
root=Tk()
#----------------------tittre

root.title("jeu")
root.resizable(False,False)
#-----------------------------Label1-------------
lab=Label(root,text="jeu de mémoire",font="courier 20 bold")
lab.pack()
#--------------------------------------------creation du canvas
cnv=Canvas(root,width=l,height=h,bg="ivory")

cnv.pack(side=LEFT)


#--------------------------ajout  d'un compteur----------------------
score=Label(root,text="Score : ",font="courier 15 bold")
score.pack(pady=13)
lbl=Label(root,text=500,font="courier 20 bold")
lbl.pack(pady=5)
#----------------------------app du jeu
init()
#------------------------le button de l'event principal  -----------------
cnv.bind("<Button>",clic)

#------------------------------ ajout du button 'Réinstaller' -------------------------
b=Button(root,text="   --  Réinstaller   --",command=init)
b.pack(pady=10)

print(plat)










  
#--------------------***********************    Menu     ********* 
      
principale = Menu(root)                                #principale m --> principale
partie1 = Menu(root)
partie2  = Menu(root)
principale.add_cascade (label = "Fichier", menu = partie1 )
principale.add_cascade (label = "Help", menu = partie2)


nb = 1 ##-------------- compteur pour blocker les buttons


o=  Label(root)

def print_file () : 
    global o ,nb
    o.configure(text="Un jeu de cartes mémoire.\n Ce jeu consiste généralement \n en un ensemble de cartes avec des images \n ou des motifs assortis par paires.\n Objectif du jeu :\n Le but du jeu est de trouver toutes\n les paires correspondantes de cartes en\n les retournant deux par deux.  ")
    o.pack()
  
    
         
   
    

    
  
def ajoute_bouton () :
    global nb,o
    b= Button (text = "how to play" ,command=print_file)
    if(nb==1):
        b.pack(pady=100)
    nb=nb+1
    
  
   
   

  
   
partie1 .add_command (label = "Quitter", command = root.destroy)
partie2.add_command (label = "ajoute_bouton", command = ajoute_bouton)

root.config(menu = principale, width = 200)




        








root.mainloop()