# Существует список чисел, представляющих собой дневные температуры 
# (в градусах Цельсия) в течение одного месяца (30 дней). 
# Ваша задача - реализовать несколько функций, которые выполняют следующие операции 
# с этим списком температур:

from random import randint 
from input_output import input_lst_temperature, output_temperature_lst
from search_day_temp import search_index_day_gt, search_index_day_lt
from crud_operations import append_new_temp, extend_union_lst, del_temp_lst
from dop_funcs import count_day_temperature, selsia_in_farangeit




def main():
    lst_temp = input_lst_temperature()

    output_temperature_lst(lst_temp)

    # print("Задание №1")
    # index_gt = search_index_day_gt(lst_temp)
    # print(f"Индекс первого дня, когда температура превысила заданное значение: {index_gt}")


    # print("Задание №2")
    # index_lt = search_index_day_lt(lst_temp)
    # print(f"Индекс первого дня, когда температура превысила заданное значение: {index_lt}")
    

    # print("Задание №3")
    # count_day = count_day_temperature(lst_temp)
    # print(f"Подсчитать количество дней, когда температура была ниже заданного значения.: {count_day}")


    # print("Задание №4")
    # lst_temp_copy = append_new_temp(lst_temp)
    # print(f"Добавить в список температур еще один список температур за последние несколько дней месяца.")
    # output_temperature_lst(lst_temp_copy)
    # print("Исходный список для сравнения:")
    # output_temperature_lst(lst_temp)


    # print("Задание №5")
    # lst_temp_copy = del_temp_lst(lst_temp)
    # print(f"Добавить в список температур еще один список температур за последние несколько дней месяца.")
    # output_temperature_lst(lst_temp_copy)
    # print("Исходный список для сравнения:")
    # output_temperature_lst(lst_temp)


    # print("Задание №6")
    # extend_lst = extend_union_lst()
    # output_temperature_lst(extend_lst)

    print("Задание №6")

    farangeit_lst_temp = selsia_in_farangeit(lst_temp)
    output_temperature_lst(farangeit_lst_temp)





main()


