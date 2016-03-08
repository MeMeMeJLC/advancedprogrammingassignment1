#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jeremy
#
# Created:     08/03/2016
# Copyright:   (c) jeremy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
class SalesPersonData():
    data = [111, 'm', 22, 5000, 22, 50000, 222, 'f', 33, 1000, 5, 30000]
    #id, gender, age, sales, bmi, income

    def get_data():
        for item in data:
            return item
"""

def main():
    print('hello world, this is the advanced programming assignment 1')

    data = [111, 'm', 22, 5000, 22, 50000, 222, 'f', 33, 1000, 5, 30000]

    variables = ['id', 'gender', 'age', 'sales', 'bmi', 'income']

    new_list = []

    for item in data:
        var_index = data.index(item)
        if var_index > 5:
            var_index = var_index % 5
        var = variables[var_index]
        new_list.append(var)
        new_list.append(item)

    print(new_list)


if __name__ == '__main__':
    main()



