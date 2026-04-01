import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# --- Langkah 4: Menyiapkan himpunan Fuzzy ---
# Semesta pembicaraan berdasarkan definisi kasus [cite: 322]
biaya = ctrl.Antecedent(np.arange(0, 1001), 'biaya')
permintaan = ctrl.Antecedent(np.arange(0, 61), 'permintaan') # Skala 0-60 (puluh ribu) [cite: 322]
produksi = ctrl.Consequent(np.arange(0, 101), 'produksi')  # Skala 0-100 (puluh ribu) [cite: 322]

# Definisi Fungsi Keanggotaan Biaya Produksi [cite: 324, 325]
biaya['Rendah'] = fuzz.zmf(biaya.universe, 0, 500)
biaya['Standar'] = fuzz.pimf(biaya.universe, 0, 500, 500, 1000)
biaya['Tinggi'] = fuzz.smf(biaya.universe, 500, 1000)

# Definisi Fungsi Keanggotaan Permintaan [cite: 327, 329]
permintaan['Turun'] = fuzz.trapmf(permintaan.universe, [0, 0, 10, 30])
permintaan['Biasa'] = fuzz.trimf(permintaan.universe, [10, 30, 50])
permintaan['Naik'] = fuzz.trapmf(permintaan.universe, [30, 50, 60, 60])

# Definisi Fungsi Keanggotaan Produksi Barang [cite: 331]
produksi['Berkurang'] = fuzz.trapmf(produksi.universe, [0, 0, 10, 50])
produksi['Normal'] = fuzz.trimf(produksi.universe, [30, 50, 70])
produksi['Bertambah'] = fuzz.trapmf(produksi.universe, [50, 90, 100, 100])

# --- Langkah 7: Membuat Aturan-aturan Fuzzy [cite: 376, 377] ---
aturan1 = ctrl.Rule(biaya['Rendah'] & permintaan['Naik'], produksi['Bertambah'])
aturan2 = ctrl.Rule(biaya['Standar'], produksi['Normal'])
aturan3 = ctrl.Rule(biaya['Tinggi'] & permintaan['Turun'], produksi['Berkurang'])

# --- Langkah 8: Membuat Inference Engine [cite: 379] ---
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)

# --- Langkah 9: Pengujian Input [cite: 383, 384, 385] ---
# Input: Biaya Produksi 500, Permintaan 30
system.input['biaya'] = 500
system.input['permintaan'] = 30

# Perhitungan [cite: 386]
system.compute()

# Output ke terminal [cite: 387]
print(f"Jumlah Produksi Barang: {system.output['produksi']}")

# --- Langkah 10: Visualisasi [cite: 388] ---
produksi.view(sim=system)

input("Tekan ENTER untuk keluar")