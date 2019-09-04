import json



file_gauges_name = 'gauge_and_Higgs_bosons.json'
file_gauges = open(file_gauges_name, 'r', encoding='utf-8')
gauges = json.load(file_gauges)
file_gauges.close()

file_quarks_name = 'quarks.json'
file_quarks = open(file_quarks_name, 'r', encoding='utf-8')
quarks = json.load(file_quarks)
file_quarks.close()

particle_list= gauges['gauge and Higgs bosons'] + quarks['quarks']

def take_mass_from_dict(mass):
    if isinstance(mass, dict):
        return mass['value']
    else:
        return mass

for par in particle_list:
    print("id:{},{},mass:{}GeV".format(par['id'],par['name'],take_mass_from_dict(par['mass'])))
