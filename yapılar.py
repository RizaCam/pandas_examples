"""
 print("Hello")
    num = [1,2,3,4,5]
for i in num:
    print(i)
dir(str)
"""
############# VERİ YAPILARI ###########
######  LISTELER  #########
notes=[1,2,3,4]
type(notes)
names=["a","b","v","d"]

#eleman erişimi
not_nam=[1,2,3,"a","b",True,[11,22,33]]
not_nam[0]
not_nam[6][1]
type(not_nam[6][1])              #int

#Eleman değişimi
not_nam[0]=99
not_nam

# LİSTE METODLARI
notes = [1, 2, 3, 4]
dir(notes)    #kullanabileceğin metodları gösterir

len(notes)    #eleman sayısı

notes.append(100)     #[1,2,3,4,100]
notes.insert(2, 99)
notes

############## DICTİONARY ##############

dictionary = {"reg": "Regression",
              "log": "lojistic Regression",
              "cart": "clasification and reg"}
dictionary["reg"]

dictionary = {"reg": ["Re",10],
              "log": ["l",20],
              "cart": ["c",30]}
dictionary["reg"]   #dictionary.get("reg")
dictionary["reg"][1]

"reg" in dictionary    #true

# Value Değiştirme
dictionary["reg"] = ["rza",97]
dictionary

dictionary.keys()
dictionary.values()
dictionary.items()   # keys and values

dictionary.update({"reg": 876})  # update mevcuk key i değiştirir. mevcutta değilse ekler

dictionary.update({"rf" : 111})
dictionary.items()

########## DEMET (TUPLE)  ##############
#Değiştirilemez
#Sıralı
#kapsayıcı

t = ("riza", " mert" ,1,2)
type(t)
t[0]    #  "riza"
t[0:3]

t= list(t)       #tuple turn to list

################# SET ###############

# değiştirilebilir
# sırasız + eşsiz
# kapsayıcı

set1 = set([1 ,5 , 3 ])

set2 = set([1 ,2 , 3 ])
set1.difference(set2)  # 5
set2.difference(set1)  # 2

set1.symmetric_difference(set2)   # 5 ve 2  iki küme içinde birbirinde olmayan elemanlar
set1.union(set2)  # ikisinin birleşimi

set1.isdisjoint(set2)   # iki kümenin kesişimi boş mu?

set11 = set([1 ,5 , 3 ])

set22 = set([1 ,2 , 3 , 5])
set11.issuperset(set22)
set22.issuperset(set11)


