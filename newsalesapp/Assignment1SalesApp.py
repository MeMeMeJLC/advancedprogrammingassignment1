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
        """
        Check correct data has entered list at correct index.
        Happy day scenario.

        >>> Model.id_list[1]
        'A011'

        >>> Model.gender_list[3]
        'F'
        """
        filename = input("Enter the destination/filename. Eg: D:/data/load_data.txt")
        try:
            with open(filename, 'r') as f:
                for line in f:
                    print("line = " and line)
                    raw_line_data = line
                    i = 0;
                    for element in raw_line_data.split():
                        if i == 0:
                            element = Model.validate_id(element)
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
            print("IO error, not reading file. Try entering the filename again")
            #Do_Get_Data()


    def validate_id(id):
        #id = input('please enter ID no: (format eg: A001 to Z999)')
        """
        Check bad data

        >>> Model.id_list[1] is None
        True
        """
        match_id = re.match('[A-Z][0-9]{3}', id)
        if match_id is None:
            print('id format incorrect: id entered as None')
            id = None
            print(id)
            return(id)
        else:
            return id



class View():
    pass



class Controller():
    pass


def main():
    pass

if __name__ == '__main__':
    main()

Model.get_data()
doctest.testmod()