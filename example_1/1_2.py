"""Предположим, что средний удой коровы за первую и вторую лактации составляет 8000 кг. Если фенотипическое
стандартное отклонение и наследуемость надоев молока в первые две лактации составляют 600 кг и 0.30 соответственно,
а корреляция между надоями первой и второй лактации составляет 0.5, спрогнозируйте племенную ценность коровы по надоям
за первые две лактации и его точность. Предположим, что средний удой за первую и вторую лактации составляет 6000 кг."""

import math

# data
average_milk_yield_cow = 8000
average_milk_yield = 6000
records_on_animal = 2
st_dev_phen = 600
heritability = 0.3
correlation = 0.5

# solution
# для расчета племенной ценности и точности надо расчитать коэффициент b
b = (records_on_animal * heritability) / (1 + (records_on_animal - 1) * correlation)
breeding_value = b * (average_milk_yield_cow - average_milk_yield)
accuracy = math.sqrt(b)

# answer
print("%.1f" % breeding_value, "%.3f" % accuracy)




