import json

particle_category =["gauge_and_Higgs_bosons", "quarks", "leptons", "mesons"]

particle_list=[]

for category in particle_category:
    filename = category+".json"
    with open(filename, "r", encoding="utf-8") as f:
        particles = json.load(f)
    category_key=" ".join(category.split('_'))
    particle_list +=particles[category_key]

def life_of(particle):
    life = particle.get('life','unkown life')
    if isinstance(life, dict):
        return "{}s".format(life['value'])
    if isinstance(life, str):
        return life
    else:
        return "{}s".format(life)

def mass_of(particle):
    mass = particle.get('mass','unkown mass')
    if isinstance(mass, dict):
        return "{}GeV".format(mass['value'])
    if isinstance(mass, str):
        return mass
    else:
        return "{}GeV".format(mass)

particle_list = sorted(particle_list, key=lambda x: x["id"])
for par in particle_list:
    print("id:{},{},mass:{},life:{}".format(par['id'],par['name'],mass_of(par), life_of(par)))

# from collections import namedtuple

# for par in particle_list:
#     attrs = ["_".join(key.split(" ")) for key in par.keys()]
#     particle_obj = namedtuple("Particle", attrs)(*par.values())
#     print(f"{particle_obj.id}")


