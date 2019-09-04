Particle Data in json
==============

This data is taken from [PDG](http://pdg.lbl.gov), transcribed to json format. 

Reference: [M. Tanabashi et al. (Particle Data Group)](http://pdg.lbl.gov/2019/html/authors_2018.html), [Phys. Rev. D 98, 030001 (2018) ](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.98.030001) and 2019 update.


## Idea
List of sub-atomic particles and their properties are unknown to most people, as its complexity and not teaching in school. Taking some research, one can find lot of information online, The most scientific resource probably is [PDG](http://pdg.lbl.gov). The data in the reviews come from numerous researching articles. But the data in the tables are not computer readable, except a [mass_width table](/pdg_summary/mass_width_2019.mcd.txt). With file formats like json, more information can be made to computer-readable. This maybe make some analyzing or visualization easier.

## Which is included?

Only confirmed particle and their properties are include in this data.

## Format

Each json file contents a category of particles. json file is a object with name of the category. Value of category is a list of particle objects.

``` json
{
    "gauge and Higgs bosons":[
        {
            "name":"photon",
            "id":22,
            "alternative names":["gamma","γ"],
            "spin":[0,1],
            "spin-parity":["1","-","-"],
            "mass":{
                "value":0,
                "upper error":1E-27
            },
            "charge":{
                "value":0,
                "upper error":1E-35
            },
            "life":"stable"
        },
        //...
    ]
}
```


### Unit
same unit is used for all particles
| name   | symbol|      explain         |
| ------ | :-----: | ---------------------|
| charge | e | electron charge positive|
| mass | GeV |  |
| life time | s   | second or "stable" |

### About mass and width errors

Mass error and width error may have upper and lower limit, or same error.
