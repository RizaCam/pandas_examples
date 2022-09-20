####################
# pandas series

import pandas as pd
s= pd.Series([10, 77, 12, 4, 5])

s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3) # 0 ,1,2 indexleini getirir
s.tail(3)

########### VERİ OKUMA #######

#  df = pd.read_csv("dosyanın yolunu kopyala " dosya üstüne sağ tık yap copy path de ")
# başka bir veri dosyası açmak için
# pd ifadesine ctrl ye basarak tıkla
# ctrl f de. arama yerine read_ yaz