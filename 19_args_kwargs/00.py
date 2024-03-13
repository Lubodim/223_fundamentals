def my_function(param1, param2, *args, **kwargs):
    return f"{kwargs} from {param1} and {param2} have {args} grades"


print(my_function("UKTC", 223, 2, 3, 4, 5, 6, 2, 2, 3, 4, f_name="Спиридон", l_name="Стаматов"))


# def my_func(param1, param2, *args):
#     a = args[0]
#     return a
#
#
# my_func(3, 4, 5, 6, True, 8, "Gosho", 10, [11, 12, 69], 12, 13, 14, 15, 16, 17)
