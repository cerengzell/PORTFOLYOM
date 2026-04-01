import pandas as pd
import matplotlib.pyplot as plt
import os

# CSV'den veriyi okuma
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'veri.csv'))
df = pd.read_csv(data_path)

# Grafik oluşturma
plt.figure(figsize=(10, 6))

# Histogramları çizdirme
plt.hist(df['Degisken1'], bins=30, alpha=0.7, label='Degisken1 (Ort=50, SS=10)', color='blue')
plt.hist(df['Degisken2'], bins=30, alpha=0.7, label='Degisken2 (Ort=100, SS=20)', color='red')

# Grafiğe başlık ve etiket ekleme
plt.title('2 Değişkenli Normal Dağılım (Çan Eğrisi)', fontsize=14)
plt.xlabel('Değer', fontsize=12)
plt.ylabel('Frekans', fontsize=12)
plt.legend(loc='upper right')
plt.grid(axis='y', alpha=0.75)

# Grafiği PNG olarak kaydetme
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'grafik.png'))
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Grafik '{output_path}' konumuna kaydedildi.")
