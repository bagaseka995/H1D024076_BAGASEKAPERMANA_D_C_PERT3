import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

info = ctrl.Antecedent(np.arange(0, 101, 1), 'info')
syarat = ctrl.Antecedent(np.arange(0, 101, 1), 'syarat')
petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'sarpras')
kepuasan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan')

for var in [info, syarat, petugas, sarpras]:
    var['Tidak Memuaskan'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['Cukup Memuaskan'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['Memuaskan'] = fuzz.trapmf(var.universe, [75, 90, 100, 100])

kepuasan['Tidak Memuaskan'] = fuzz.trimf(kepuasan.universe, [0, 50, 100])
kepuasan['Kurang Memuaskan'] = fuzz.trimf(kepuasan.universe, [75, 125, 175])
kepuasan['Cukup Memuaskan'] = fuzz.trimf(kepuasan.universe, [150, 200, 250])
kepuasan['Memuaskan'] = fuzz.trimf(kepuasan.universe, [225, 275, 325])
kepuasan['Sangat Memuaskan'] = fuzz.trimf(kepuasan.universe, [300, 350, 400])

rules = [
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Tidak Memuaskan'] & sarpras['Tidak Memuaskan'], kepuasan['Tidak Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Tidak Memuaskan'] & sarpras['Cukup Memuaskan'], kepuasan['Tidak Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Tidak Memuaskan'] & sarpras['Memuaskan'], kepuasan['Tidak Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Cukup Memuaskan'] & sarpras['Tidak Memuaskan'], kepuasan['Tidak Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Cukup Memuaskan'] & sarpras['Cukup Memuaskan'], kepuasan['Tidak Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Cukup Memuaskan'] & sarpras['Memuaskan'], kepuasan['Cukup Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Memuaskan'] & sarpras['Tidak Memuaskan'], kepuasan['Tidak Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Memuaskan'] & sarpras['Cukup Memuaskan'], kepuasan['Cukup Memuaskan']),
    ctrl.Rule(info['Tidak Memuaskan'] & syarat['Tidak Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Cukup Memuaskan']),
    ctrl.Rule(info['Cukup Memuaskan'] & syarat['Cukup Memuaskan'] & petugas['Cukup Memuaskan'] & sarpras['Memuaskan'], kepuasan['Memuaskan']),
    ctrl.Rule(info['Cukup Memuaskan'] & syarat['Cukup Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Memuaskan']),
    ctrl.Rule(info['Cukup Memuaskan'] & syarat['Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Sangat Memuaskan']),
    ctrl.Rule(info['Memuaskan'] & syarat['Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], kepuasan['Sangat Memuaskan']),
    ctrl.Rule(info['Cukup Memuaskan'] & syarat['Tidak Memuaskan'], kepuasan['Cukup Memuaskan'])
]

service_engine = ctrl.ControlSystem(rules)
service_sim = ctrl.ControlSystemSimulation(service_engine)

service_sim.input['info'] = 80
service_sim.input['syarat'] = 60
service_sim.input['petugas'] = 50
service_sim.input['sarpras'] = 90

service_sim.compute()
print(f"Nilai tingkat kepuasan pelayanan: {service_sim.output['kepuasan']:.2f}")
kepuasan.view(sim=service_sim)
plt.show()

input("Tekan ENTER untuk keluar")