import pandas as pd

data = {
    'Mahasiswa': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma': [90, 50, 65],
    'Bumerik': [80, 60, 70]
}
df = pd.DataFrame(data)
average_kuliah = df[['Algoritma', 'Bumerik']].mean()
average_mahasiswa = df[['Algoritma', 'Bumerik']].mean(axis=1)

print("Rata-rata nilai kuliah:\n", average_kuliah)
print("\nRata-rata nilai setiap mahasiswa:\n", average_mahasiswa)
