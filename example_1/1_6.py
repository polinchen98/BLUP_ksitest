"""Предположим, что следующие параметры были получены для среднесуточного привеса (ADG) от рождения до 400 дней и
процента постного мяса (LP) в том же возрасте в группе телят:
ADG (g/day) Heritability = 0.43; Standard deviation = 80.0
LP (%) Heritability = 0.30; Standard deviation = 7.2
Генетические и фенотипические корреляции (rg и rp) между ADG и LP составляют 0,30 и -0,10 соответственно.
Постройте индекс для улучшения скорости роста телят. ADG - признак 1 и LP - признак 2"""

# data
heritability_ADG = 0.43
heritability_LP = 0.30
standard_deviation_ADG = 80.0
standard_deviation_LP = 7.2
rg = 0.3
rp = -0.10

# solution

import numpy as np
import math

# search data for matrix
p_11 = standard_deviation_ADG ** 2
p_22 = standard_deviation_LP ** 2
p_21 = rp * math.sqrt(p_11 * p_22)
p_12 = rp * math.sqrt(p_11 * p_22)

g_11 = heritability_ADG * p_11
g_22 = heritability_LP * p_22
g_21 = rg * math.sqrt(g_11 * g_22)

# phenotype matrix
p = np.matrix([[p_11, p_12], [p_21, p_22]])
p_inv = np.linalg.inv(p)
# genotype matrix
g = np.matrix([[g_11], [g_21]])
# p x g
b = p_inv.dot(g)
# the solutions b1 and b2
b_1 = np.around(b[0], decimals=3)
b_2 = np.around(b[1], decimals=3)
# using Eqn 1.21 (book)
r = math.sqrt(((b_1 * g_11) + (b_2 * g_21)) / g_11)
print(np.around(r, decimals=3))

