import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga')
profit = ctrl.Antecedent(np.arange(0, 4000001, 1), 'profit')
stok = ctrl.Consequent(np.arange(0, 1001, 1), 'stok')

terjual['Rendah'] = fuzz.trimf(terjual.universe, [0, 20, 40])
terjual['Sedang'] = fuzz.trimf(terjual.universe, [30, 50, 70])
terjual['Tinggi'] = fuzz.trimf(terjual.universe, [60, 80, 100])

permintaan['Rendah'] = fuzz.trimf(permintaan.universe, [0, 50, 100])
permintaan['Sedang'] = fuzz.trimf(permintaan.universe, [75, 150, 225])
permintaan['Tinggi'] = fuzz.trimf(permintaan.universe, [200, 250, 300])

harga['Murah'] = fuzz.trimf(harga.universe, [0, 20000, 40000])
harga['Sedang'] = fuzz.trimf(harga.universe, [30000, 50000, 70000])
harga['Mahal'] = fuzz.trimf(harga.universe, [60000, 80000, 100000])

profit['Rendah'] = fuzz.trimf(profit.universe, [0, 1000000, 2000000])
profit['Sedang'] = fuzz.trimf(profit.universe, [1500000, 2500000, 3500000])
profit['Tinggi'] = fuzz.trimf(profit.universe, [3000000, 3500000, 4000000])

stok['Sedikit'] = fuzz.trimf(stok.universe, [0, 250, 500])
stok['Sedang'] = fuzz.trimf(stok.universe, [400, 600, 800])
stok['Banyak'] = fuzz.trimf(stok.universe, [700, 850, 1000])

rule1 = ctrl.Rule(terjual['Tinggi'] & permintaan['Tinggi'] & harga['Murah'] & profit['Tinggi'], stok['Banyak'])
rule2 = ctrl.Rule(terjual['Tinggi'] & permintaan['Tinggi'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
rule3 = ctrl.Rule(terjual['Tinggi'] & permintaan['Sedang'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
rule4 = ctrl.Rule(terjual['Sedang'] & permintaan['Tinggi'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
rule5 = ctrl.Rule(terjual['Sedang'] & permintaan['Tinggi'] & harga['Murah'] & profit['Tinggi'], stok['Banyak'])
rule6 = ctrl.Rule(terjual['Rendah'] & permintaan['Rendah'] & harga['Sedang'] & profit['Sedang'], stok['Sedang'])

toko_engine = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
pet_shop = ctrl.ControlSystemSimulation(toko_engine)

pet_shop.input['terjual'] = 80
pet_shop.input['permintaan'] = 255
pet_shop.input['harga'] = 25000
pet_shop.input['profit'] = 3500000

pet_shop.compute()
print(f"Jumlah optimal stok makanan: {pet_shop.output['stok']:.2f}")
stok.view(sim=pet_shop)

input("Tekan ENTER untuk keluar")