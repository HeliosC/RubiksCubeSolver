import random  
import time  
#import matplotlib.pyplot as plt  
  
def init():  
    "Intailise le patron du cube par un cube résolu"  
    return(['B','B','B','B','B','B','B','B','B','W','W','W','W','W','W','W','W','W','O','O','O','O','O','O','O','O','O','V','V','V','V','V','V','V','V','V','R','R','R','R','R','R','R','R','R','J','J','J','J','J','J','J','J','J',])  
  
  
    # Fonctions relatives aux mouvements légaux des faces du cube :  
      
def F1():  
    c[2],c[5],c[8],c[7],c[6],c[3],c[0],c[1]=c[0],c[1],c[2],c[5],c[8],c[7],c[6],c[3]  
    c[18],c[21],c[24],c[47],c[46],c[45],c[44],c[41],c[38],c[15],c[16],c[17]=c[15],c[16],c[17],c[18],c[21],c[24],c[47],c[46],c[45],c[44],c[41],c[38]  
def Fp():  
    c[0],c[1],c[2],c[5],c[8],c[7],c[6],c[3]=c[2],c[5],c[8],c[7],c[6],c[3],c[0],c[1]  
    c[15],c[16],c[17],c[18],c[21],c[24],c[47],c[46],c[45],c[44],c[41],c[38]=c[18],c[21],c[24],c[47],c[46],c[45],c[44],c[41],c[38],c[15],c[16],c[17]  
def F2():  
    c[2],c[5],c[8],c[7],c[6],c[3],c[0],c[1]=c[6],c[3],c[0],c[1],c[2],c[5],c[8],c[7]  
    c[15],c[16],c[17],c[18],c[21],c[24],c[47],c[46],c[45],c[44],c[41],c[38]=c[47],c[46],c[45],c[44],c[41],c[38],c[15],c[16],c[17],c[18],c[21],c[24]  
def U1():  
    c[9],c[10],c[11],c[14],c[17],c[16],c[15],c[12]=c[15],c[12],c[9],c[10],c[11],c[14],c[17],c[16]  
    c[38],c[37],c[36],c[29],c[28],c[27],c[20],c[19],c[18],c[2],c[1],c[0]=c[2],c[1],c[0],c[38],c[37],c[36],c[29],c[28],c[27],c[20],c[19],c[18]  
def Up():  
    c[15],c[12],c[9],c[10],c[11],c[14],c[17],c[16]=c[9],c[10],c[11],c[14],c[17],c[16],c[15],c[12]  
    c[2],c[1],c[0],c[38],c[37],c[36],c[29],c[28],c[27],c[20],c[19],c[18]=c[38],c[37],c[36],c[29],c[28],c[27],c[20],c[19],c[18],c[2],c[1],c[0]  
def U2():  
    c[15],c[12],c[9],c[10],c[11],c[14],c[17],c[16]=c[11],c[14],c[17],c[16],c[15],c[12],c[9],c[10]  
    c[20],c[19],c[18],c[2],c[1],c[0],c[38],c[37],c[36],c[29],c[28],c[27]=c[38],c[37],c[36],c[29],c[28],c[27],c[20],c[19],c[18],c[2],c[1],c[0]  
def R1():  
    c[18],c[19],c[20],c[23],c[26],c[25],c[24],c[21]=c[24],c[21],c[18],c[19],c[20],c[23],c[26],c[25]  
    c[17],c[14],c[11],c[27],c[30],c[33],c[53],c[50],c[47],c[8],c[5],c[2]=c[8],c[5],c[2],c[17],c[14],c[11],c[27],c[30],c[33],c[53],c[50],c[47]  
def Rp():  
    c[24],c[21],c[18],c[19],c[20],c[23],c[26],c[25]=c[18],c[19],c[20],c[23],c[26],c[25],c[24],c[21]  
    c[8],c[5],c[2],c[17],c[14],c[11],c[27],c[30],c[33],c[53],c[50],c[47]=c[17],c[14],c[11],c[27],c[30],c[33],c[53],c[50],c[47],c[8],c[5],c[2]  
def R2():  
    c[24],c[21],c[18],c[19],c[20],c[23],c[26],c[25]=c[20],c[23],c[26],c[25],c[24],c[21],c[18],c[19]  
    c[8],c[5],c[2],c[17],c[14],c[11],c[27],c[30],c[33],c[53],c[50],c[47]=c[27],c[30],c[33],c[53],c[50],c[47],c[8],c[5],c[2],c[17],c[14],c[11]  
def B1():  
    c[27],c[28],c[29],c[32],c[35],c[34],c[33],c[30]=c[33],c[30],c[27],c[28],c[29],c[32],c[35],c[34]  
    c[11],c[10],c[9],c[36],c[39],c[42],c[51],c[52],c[53],c[26],c[23],c[20]=c[26],c[23],c[20],c[11],c[10],c[9],c[36],c[39],c[42],c[51],c[52],c[53]  
def Bp():  
    c[33],c[30],c[27],c[28],c[29],c[32],c[35],c[34]=c[27],c[28],c[29],c[32],c[35],c[34],c[33],c[30]  
    c[26],c[23],c[20],c[11],c[10],c[9],c[36],c[39],c[42],c[51],c[52],c[53]=c[11],c[10],c[9],c[36],c[39],c[42],c[51],c[52],c[53],c[26],c[23],c[20]  
def B2():  
    c[33],c[30],c[27],c[28],c[29],c[32],c[35],c[34]=c[29],c[32],c[35],c[34],c[33],c[30],c[27],c[28]  
    c[26],c[23],c[20],c[11],c[10],c[9],c[36],c[39],c[42],c[51],c[52],c[53]=c[36],c[39],c[42],c[51],c[52],c[53],c[26],c[23],c[20],c[11],c[10],c[9]  
def L1():  
    c[36],c[37],c[38],c[41],c[44],c[43],c[42],c[39]=c[42],c[39],c[36],c[37],c[38],c[41],c[44],c[43]  
    c[9],c[12],c[15],c[0],c[3],c[6],c[45],c[48],c[51],c[35],c[32],c[29]=c[35],c[32],c[29],c[9],c[12],c[15],c[0],c[3],c[6],c[45],c[48],c[51]  
def Lp():  
    c[42],c[39],c[36],c[37],c[38],c[41],c[44],c[43]=c[36],c[37],c[38],c[41],c[44],c[43],c[42],c[39]  
    c[35],c[32],c[29],c[9],c[12],c[15],c[0],c[3],c[6],c[45],c[48],c[51]=c[9],c[12],c[15],c[0],c[3],c[6],c[45],c[48],c[51],c[35],c[32],c[29]  
def L2():  
    c[42],c[39],c[36],c[37],c[38],c[41],c[44],c[43]=c[38],c[41],c[44],c[43],c[42],c[39],c[36],c[37]  
    c[35],c[32],c[29],c[9],c[12],c[15],c[0],c[3],c[6],c[45],c[48],c[51]=c[0],c[3],c[6],c[45],c[48],c[51],c[35],c[32],c[29],c[9],c[12],c[15]  
def D1():  
    c[45],c[46],c[47],c[50],c[53],c[52],c[51],c[48]=c[51],c[48],c[45],c[46],c[47],c[50],c[53],c[52]  
    c[6],c[7],c[8],c[24],c[25],c[26],c[33],c[34],c[35],c[42],c[43],c[44]=c[42],c[43],c[44],c[6],c[7],c[8],c[24],c[25],c[26],c[33],c[34],c[35]  
def Dp():  
    c[51],c[48],c[45],c[46],c[47],c[50],c[53],c[52]=c[45],c[46],c[47],c[50],c[53],c[52],c[51],c[48]  
    c[42],c[43],c[44],c[6],c[7],c[8],c[24],c[25],c[26],c[33],c[34],c[35]=c[6],c[7],c[8],c[24],c[25],c[26],c[33],c[34],c[35],c[42],c[43],c[44]  
def D2():  
    c[51],c[48],c[45],c[46],c[47],c[50],c[53],c[52]=c[47],c[50],c[53],c[52],c[51],c[48],c[45],c[46]  
    c[42],c[43],c[44],c[6],c[7],c[8],c[24],c[25],c[26],c[33],c[34],c[35]=c[24],c[25],c[26],c[33],c[34],c[35],c[42],c[43],c[44],c[6],c[7],c[8]  
  
    # Fonctions de rotation du cube entier :  
      
def X():  
    F1(),Bp()  
    c[19],c[22],c[25],c[50],c[49],c[48],c[43],c[40],c[37],c[12],c[13],c[14]=c[12],c[13],c[14],c[19],c[22],c[25],c[50],c[49],c[48],c[43],c[40],c[37]  
def Y():  
    Lp(),R1()  
    c[7],c[4],c[1],c[16],c[13],c[10],c[28],c[31],c[34],c[52],c[49],c[46]=c[52],c[49],c[46],c[7],c[4],c[1],c[16],c[13],c[10],c[28],c[31],c[34]  
def Z():  
    U1(),Dp()  
    c[3],c[4],c[5],c[21],c[22],c[23],c[30],c[31],c[32],c[39],c[40],c[41]=c[21],c[22],c[23],c[30],c[31],c[32],c[39],c[40],c[41],c[3],c[4],c[5]  
  
def aff():  
    "affiche l'état du cube sous forme de patron"  
    print(c[9],c[10],c[11])  
    print(c[12],c[13],c[14])  
    print(c[15],c[16],c[17])  
    print(c[0],c[1],c[2],c[18],c[19],c[20],c[27],c[28],c[29],c[36],c[37],c[38])  
    print(c[3],c[4],c[5],c[21],c[22],c[23],c[30],c[31],c[32],c[39],c[40],c[41])  
    print(c[6],c[7],c[8],c[24],c[25],c[26],c[33],c[34],c[35],c[42],c[43],c[44])  
    print(c[45],c[46],c[47])  
    print(c[48],c[49],c[50])  
    print(c[51],c[52],c[53])  
  

    #Paramètres    
nb_mig        = 10000  
nb_gen        = 20  
  
nb_indiv      = 100  
taille_indiv  = 15  
  
nb_suppr      = 3  
#p_crois       /  
#p_muta       /    différents pour chaque ilots      
vie           = 10  
  
courbe_ent=[]  
  
mooves=['F1()','Fp()','F2()','U1()','Up()','U2()','R1()','Rp()','R2()','B1()','Bp()','B2()','L1()','Lp()','L2()','D1()','Dp()','D2()']  
  
def scramble():  
    "mélange le cube avec un mÉlange donnÉ"  
    L2(), Up(), R1(), B2(), R2(), Bp(), Rp(), B1(), F2(), D1()  
  
  
      
def creer_pop():  
    "crÉÉ la population initiale"  
    global mooves,taille_indiv,nb_indiv  
    pop=[]  
    for i in range (nb_indiv):  
        pop.append([])  
        for j in range (taille_indiv):  
            pop[i].append(mooves[random.randint(0,17)])  
        pop[i].append(0)  
    return(pop)  
  
  
  
def neguentropie_2x2x3():  
    "compte les paires du parallÉlÉpipède"  
    neguneguentropie=0  
      
    #centre-arètes  
    neguneguentropie+=int(     (c[3]==c[4])   + (c[4]==c[7])  
                     + (c[31]==c[32]) + (c[31]==c[34])   
                     + (c[40]==c[39]) + (c[40]==c[41]) + (c[40]==c[43])  
                     + (c[49]==c[46]) + (c[49]==c[48]) + (c[49]==c[52])   )  
      
    #coin-arètes  
    neguneguentropie+=int(     (c[3]==c[6])*(c[41]==c[44])   + (c[6]==c[7])*(c[45]==c[46])  
                     + (c[32]==c[35])*(c[39]==c[42]) + (c[34]==c[35])*(c[51]==c[52])  
                     + (c[42]==c[43])*(c[51]==c[48]) + (c[43]==c[44])*(c[48]==c[45])   )  
          
    return(neguneguentropie)  
  
  
  
def fitness(pop,k):  
    "assigne Ã  chaque individu sa fitness"  
    liste_neguentropie=[]  
    global nb_indiv, taille_indiv,c,courbe_ent  
    fitnessmax=0  
    for indiv in range(10):  
        c=init()  
        scramble()  
        fitmax=-100  
        for moove in range(taille_indiv):  
            eval(pop[indiv][moove])  
            fit=neguentropie_2x2x3()  
            if fit>fitmax:  
                fitmax=fit  
                n=moove  
        fitnessm=10*fitmax**1-n  
        liste_neguentropie.append(fitnessm)  
        if fitnessm>fitnessmax:  
            fitnessmax=fitnessm  
            N=n  
        courbe_ent.append(fitnessmax)  
      
    return(liste_neguentropie)  
  
  
	  
	  
def classe(pop,liste_neguentropie):  
    "classe la population par fitness dÉcroissante"  
    global nb_indiv  
    pop2=[[]]*(10)  
    triee=sorted(liste_neguentropie)  
    for indiv in range(10):  
        indice=triee.index(liste_neguentropie[indiv])  
        pop2[indice]=pop[indiv]  
        triee[indice]=-1000  
    return(pop2)  
          
	              
	  
	  
def mutation(pop,p_muta,ilot):  
    "opÃ¨re les mutations"  
    for indiv in range(nb_suppr ,10-1):  
        for moove in range(taille_indiv):  
            if random.random()<p_muta:  
                pop[indiv][moove]=mooves[random.randint(0,17)]  
                  
        if pop[indiv][taille_indiv]>vie-1:  
            for moove in range(taille_indiv):  
                pop[indiv][moove]=mooves[random.randint(0,17)]  
            pop[indiv][taille_indiv]=0  
        else:  
            pop[indiv][taille_indiv]+=1  
	              
    return(pop)  
  
	  
	  
	  
def croisement2(pop,indiv1,indiv2,enfant):  
    "croise 2 individus"  
    global                             p_crois
    for moove in range(taille_indiv):  
        if random.random()<p_crois:  
	              
            if random.randint(0,1):  
                pop[enfant][moove]=pop[indiv1][moove]  
            else:  
                pop[enfant][moove]=pop[indiv2][moove]  
  
        else:  
            pop[enfant][moove]=mooves[random.randint(0,17)]  
    pop[enfant][taille_indiv]=0  
          
  
  
	  
def generation(pop,liste_neguentropie,ilot):  
    "Éffectue une 'boucle' de gÉnÉration"  
    global taille_indiv,nb_indiv,p_crois,p_muta,nb_suppr,vie  
	      
    for new in range(ilot*10,ilot*10 + nb_suppr):  
	          
	          
        tot=sum(liste_neguentropie[nb_suppr:nb_indiv])  
        a=random.randint(1,tot)  
        k=10  
        while a<=tot:  
            k-=1  
            tot-=liste_neguentropie[k]  
        indiv1=k +10*ilot  
  
        indiv2=-1  
        booleen=True  
        while booleen or indiv1==indiv2:  
            tot=sum(liste_neguentropie[nb_suppr:nb_indiv])  
            b=random.randint(1,tot)  
            k=10  
            while b<=tot:  
                k-=1  
                tot-=liste_neguentropie[k]  
            indiv2=k +10*ilot  
            booleen=False  
        croisement2(pop, indiv1 , indiv2 , new)  
	  
	            
def main():  
    "prgramme principal"  
    global p_muta,nb_gen,nb_mig,nb_indiv         ,p_crois
    t1=time.time()  
	  
    c=init()  
    pop=creer_pop()  
	  
    for k in range(nb_mig):  
        
        print(k)
	  
        #Évolution des ilots de taille 1/10 de la population  
        for ilot in range(nb_indiv//10):  
  
             #paramÉtrage des ilots  
            p_crois=0.4*(ilot//5 +1)  
            p_muta=0.1*(ilot%5  +1)  
  
  
	  
            for gen in range(nb_gen):  
	              
                liste_neguentropie=fitness(pop[ilot*10:(ilot+1)*10],gen)  
                pop[ilot*10:(ilot+1)*10]=classe(pop[ilot*10:(ilot+1)*10],liste_neguentropie)  
                  
                generation(pop,liste_neguentropie,ilot)  
                pop[ilot*10:(ilot+1)*10]=mutation(pop[ilot*10:(ilot+1)*10],p_muta,ilot)  
  
	  
       
        #migrations  
        pop_migr=pop[0:3]  
        for ilot in range(nb_indiv//10-1):  
            pop[ilot*10:ilot*10 +3]=pop[(ilot+1)*10:(ilot+1)*10 +3]  
        pop[nb_indiv-10:nb_indiv-7]=pop_migr  
  
	  
	  
    #affiche les ilots un Ã  un Ã  la fin"  
    maxs=[]  
    for ilot in range(nb_indiv//10):  
        liste_neguentropie=fitness(pop[ilot*10:(ilot+1)*10],1)  
        pop[ilot*10:(ilot+1)*10]=classe(pop[ilot*10:(ilot+1)*10],liste_neguentropie)  
        liste_neguentropie=fitness(pop[ilot*10:(ilot+1)*10],1)  
        print(ilot,liste_neguentropie)  
        maxs.append(liste_neguentropie[9])  

        print(pop[ilot*10:(ilot+1)*10])    
    print(maxs)  
    print("t= ",time.time()-t1)       

main()