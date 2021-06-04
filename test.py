from mixed_model_equations import constructing_mixed_model_equations

pedigree = {1: {'sex': None, 'sire': None, 'dam': None, 'WWG': None},
            2: {'sex': None, 'sire': None, 'dam': None, 'WWG': None},
            3: {'sex': None, 'sire': None, 'dam': None, 'WWG': None},
            4: {'sex': 1, 'sire': 1, 'dam': None, 'WWG': 4.5},
            5: {'sex': 0, 'sire': 3, 'dam': 2, 'WWG': 2.9},
            6: {'sex': 0, 'sire': 1, 'dam': 2, 'WWG': 3.9},
            7: {'sex': 1, 'sire': 4, 'dam': 5, 'WWG': 3.5},
            8: {'sex': 1, 'sire': 3, 'dam': 6, 'WWG': 5.0}}

solutions = constructing_mixed_model_equations(pedigree)
print(solutions)
