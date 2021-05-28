"""Учитывая, что вес годовалой телки составляет 320 кг в стаде со средним значением 250 кг,
спрогнозируйте ее племенную ценность и ее точность, если наследуемость веса годовалой телки составляет 0,45."""

import math


# data
weight_heifer = 320
mean_herd = 250
heritability = 0.45

# solution
breeding_value = heritability * (weight_heifer - mean_herd)
accuracy = math.sqrt(heritability)

# answer
print(breeding_value, accuracy)
