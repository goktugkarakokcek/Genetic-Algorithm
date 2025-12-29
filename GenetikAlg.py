import random

def gen_uret():
    
    alfabe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z']

    yeni_gen = []

    for i in range(8):
        
        secilen = random.choice(alfabe)
        
        yeni_gen.append(secilen)

    return yeni_gen

def pop_uret(birey_sayisi):
    
    pop = []

    for i in range(birey_sayisi):
        
        birey = gen_uret()
        
        pop.append(birey)
        
    return pop

def fitness(birey):
    
    fitness_score = 0
    
    target = 'AHMETGOK'
    
    for j in range(8):
        
        if birey[j] == target[j]:
            
            fitness_score += 1
  
    return fitness_score            

def selection(guncel_populasyon):
    
    fitness_scores = []
    
    for kisi in guncel_populasyon:
        
        kisi_fitness = fitness(kisi)
        fitness_scores.append(kisi_fitness)
        
    puanlı_liste=[]
    for i in range(len(guncel_populasyon)):
        
        birlesik=[fitness_scores[i],guncel_populasyon[i]]
        puanlı_liste.append(birlesik)

    puanlı_liste.sort(reverse=1)

    yasayacak_sayisi=len(puanlı_liste)//2
    
    en_iyi_skor=puanlı_liste[0][0]
    en_iyi_birey=puanlı_liste[0][1]

    
    mating_pop=puanlı_liste[:yasayacak_sayisi]
    
    print("En yüksek fitness değerine sahip bireyler: ",mating_pop)
    
    return mating_pop,en_iyi_skor,en_iyi_birey

def crossover(gelen_pool,hedef_sayi):
    
    yeni_nesil=[]
    ebeveyn_sayisi=len(gelen_pool)
    gereken_cocuk=hedef_sayi-ebeveyn_sayisi
    
    for i in range(gereken_cocuk):
        
        cift=random.sample(gelen_pool,2)
        baba_puanlı=cift[0]
        anne_puanlı=cift[1]

        baba_gen=baba_puanlı[1]
        anne_gen=anne_puanlı[1]

        caprazlama_noktası=random.randint(1,7)

        cocuk=baba_gen[:caprazlama_noktası]+anne_gen[caprazlama_noktası:]
        
        yeni_nesil.append(cocuk)
        
    for j in gelen_pool:
        
        gen=j[1]
        
        yeni_nesil.append(gen)
        
    print("-"*20)
    
    print("Oluşan yeni nesil: ",yeni_nesil)
    
    return yeni_nesil,gereken_cocuk
        
def mutation(populasyon,cocuk_sayisi):

    mutasyon_yuzdesi=0.05

    alfabe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z']

    for i in range(cocuk_sayisi):
        
        for j in range(8):
            
            if random.random() < mutasyon_yuzdesi:

                eski_harf=populasyon[i][j]
                
                yeni_harf=random.choice(alfabe)
                
                populasyon[i][j]=yeni_harf

                print(f"Mutasyon:{i+1}. Çocuğun,{j+1}. Geni değişti.({eski_harf}->{yeni_harf})")
           
    return populasyon            

pop_sayisi=int(input('Popülasyon Kaç Bireyden Oluşsun?: '))

populasyon = pop_uret(pop_sayisi)

jenerasyon=1

while True:

    gelen_pool,best_score,best_dna=selection(populasyon)

    print(f"\nJenerasyon: {jenerasyon} | En İyi Puan: {best_score} | En İyi Birey: {best_dna}")

    if best_score==8:
        
        print(f"Hedef Kelime: {best_dna}")
        
        print(f"Toplam Jenerasyon: {jenerasyon}")
        
        break
    
    sonraki_nesil,yeni_cocuklar=crossover(gelen_pool,pop_sayisi)

    mutasyonlu_nesil=mutation(sonraki_nesil,yeni_cocuklar)

    populasyon=mutasyonlu_nesil

    jenerasyon+=1
        



    
