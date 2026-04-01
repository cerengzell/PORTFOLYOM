import numpy as np
import pandas as pd
import os

# Rastgelelik için seed ayarı (tekrar üretilebilir olması için)
np.random.seed(42)

# En az 500 satır veri oluşturma (Normal Dağılım / Çan Eğrisi)
# Değişken 1: Ortalama=50, Standart Sapma=10
var1 = np.random.normal(loc=50, scale=10, size=500)

# Değişken 2: Ortalama=100, Standart Sapma=20
var2 = np.random.normal(loc=100, scale=20, size=500)

# DataFrame oluşturma
df = pd.DataFrame({
    'Degisken1': var1,
    'Degisken2': var2
})

# Veriyi CSV olarak kaydetme
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'veri.csv'))
df.to_csv(output_path, index=False)
print(f"Veri '{output_path}' konumuna kaydedildi.")
