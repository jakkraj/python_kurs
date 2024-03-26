# Zadanie nr 1
# Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu i pokonanego dystansu (prędkość = dystans / czas)
# i umieść ją w jednym pliku.

# W drugim pliku zaimportuj moduł, wczytaj informacje od użytkownika i wywołaj funkcję - oblicz prędkość średnią.

# import calculations.avg_velocity
#
# user_distance = float(input('Podaj przebiegnięty dystans w kilometrach: '))
# user_time = float(input('Podaj czas biegu w godzinach: '))
#
# avg_velocity = calculations.avg_velocity.calculate_avg_velocity(user_distance, user_time)
#
# print(f'Twoja średnia prędkość biegu to {avg_velocity} km/h.')



# Zadanie nr 2
# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na podstawie otrzymanych długości przyprostokątnych.
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:

#   - sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
#   - pow(x, y) - podnosi x do potęgi y

# import math
#
# def calculate_hypotenuse(a, b):
#     c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
#     return c
#
# a_length = float(input('Podaj długość boku a: '))
# b_length = float(input('Podaj długość boku b: '))
#
# c_length = calculate_hypotenuse(a_length, b_length)
#
# print(f'Dłogość przeciwprostokątnej: {c_length}.')



# Zadanie nr 3
# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.
# Wczytaj od użytkownika informacje o:

# - Początkowym kapitale (wpłaconej kwocie)
# - Oprocentowaniu
# - Okresie trwania inwestycji (w latach)

# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations, a wczytanie danych i uruchomienie obliczeń w pliku
# powyżej pakietu.
# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat

import calculations.investment

start = int(input('Podaj początkową kwotę inwestycji: '))
per = int(input('Podaj oprocentowanie lokaty: '))
time = int(input('Podaj czas trwania inwestycji w latach: '))

end_value = calculations.investment.calculate_investment(start, per, time)

print(f'Końcowa wartość inwestycji: {end_value}.')
