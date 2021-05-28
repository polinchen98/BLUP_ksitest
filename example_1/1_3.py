"""Предположим, что выход жира 25 полусибских потомков быка составил в среднем 250 кг за первую лактацию.
Предполагая наследуемость 0.30 и среднее значение по стаду 200 кг, спрогнозируйте племенную ценность быка по выходу
жира и его точности. Также спрогнозируйте показатели будущей дочери этого быка по удоям жира в этом стаде."""

import math


# data
number_bulls = 25
fat_yield = 250
herd_mean = 200
heritability = 0.3

# solution
# для расчета племенной ценности и точности надо расчитать коэффициент b
b = 2 * number_bulls / (number_bulls + (4 - heritability) / heritability)
breeding_value_bull = b * (fat_yield - herd_mean)

# для расчета точности нужно найти коэффициент k
k = (4 - heritability) / heritability
accuracy = math.sqrt(number_bulls / (number_bulls + k))
performance_of_future_daughter = 0.5 * breeding_value_bull + herd_mean

# answer
print("%.1f" % breeding_value_bull, "%.2f" % accuracy, "%.1f" % performance_of_future_daughter)
