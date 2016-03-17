#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jeremy
#
# Created:     17/03/2016
# Copyright:   (c) jeremy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cmd
import pickle
import re
import doctest

class Model():
    id_list = list()
    gender_list = list()
    age_list = list()
    sales_list = list()
    bmi_list = list()
    income_list = list()

    def get_data():
        try:
            with open('loadData_Good.txt', 'r') as f:
                for line in f:
                    raw_line_data = f.readline()
                    print(raw_line_data)
                    i = 0;
                    for element in raw_line_data.split():
                        if i == 0:
                            Model.id_list.append(element)
                            print(Model.id_list)
                        elif i == 1:
                            Model.gender_list.append(element)
                            print(Model.gender_list)
                        elif i == 2:
                            Model.age_list.append(element)
                            print(Model.age_list)
                        elif i == 3:
                            Model.sales_list.append(element)
                            print(Model.sales_list)
                        elif i == 4:
                            Model.bmi_list.append(element)
                            print(Model.bmi_list)
                        elif i == 5:
                            Model.income_list.append(element)
                            print(Model.income_list)
                        else:
                            print("error in get_data() raw_line_data")
                        i += 1


        except IOError:
            print("IO error, not reading file")



class View():
    pass



class Controller():
    pass


def main():
    pass

if __name__ == '__main__':
    main()

Model.get_data()