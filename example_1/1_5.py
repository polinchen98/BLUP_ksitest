"""Предположим, что стандартное отклонение скорости роста (GR) (г/день) до 400 дней в популяции мясного скота
составляло 80 с наследуемостью 0.43. Стандартное отклонение скорости роста мышечной массы (LGR) (г/день) для той же
популяции составило 32 с наследуемостью 0.45. Если генетическая корреляция между обоими признаками составляет 0.95, а
средняя популяционная скорость роста составляет 887 г/день, спрогнозируйте племенную ценность LGR для животного с
GR 945 г/сут."""

import math
import numpy


# data
std_GR = 80
heritability_GR = 0.43
std_LGR = 32
heritability_LGR = 0.45
gen_correlation = 0.95
population_mean_GR = 887
animal_GR = 945

# solution
# для расчета племенной ценности и точности надо расчитать коэффициент b

b = (gen_correlation * heritability_GR * heritability_LGR * std_LGR) / std_GR
breeding_value = b * (animal_GR - population_mean_GR)
accuracy = gen_correlation * (math.sqrt(heritability_GR))

# answer
print(b, "%.1f" % breeding_value, "%.2f" % accuracy)

