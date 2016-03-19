import cmd
import pickle
import re
import doctest
import matplotlib.pyplot as plt
import numpy as np

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
        loadData_Bad.txt scenario.

        >>> Model.id_list[3] is None
        True

        >>> Model.gender_list[3]
        'F'
        """
        filename = input("Enter the destination/filename. Eg: D:/data/load_data.txt")
        try:
            with open(filename, 'r') as f:
                for line in f:
                    #print("line = " and line)
                    raw_line_data = line
                    i = 0;
                    for element in raw_line_data.split():
                        if i == 0:
                            element = Model.validate_id(element)
                            Model.id_list.append(element)
                            #print(Model.id_list)
                        elif i == 1:
                            element = Model.validate_gender(element)
                            Model.gender_list.append(element)
                            #print(Model.gender_list)
                        elif i == 2:
                            element = Model.validate_age(element)
                            Model.age_list.append(element)
                            #print(Model.age_list)
                        elif i == 3:
                            element = Model.validate_sales(element)
                            Model.sales_list.append(element)
                            #print(Model.sales_list)
                        elif i == 4:
                            element = Model.validate_bmi(element)
                            Model.bmi_list.append(element)
                            #print(Model.bmi_list)
                        elif i == 5:
                            element = Model.validate_income(element)
                            Model.income_list.append(element)
                            #print(Model.income_list)
                        else:
                            print("error in get_data() raw_line_data")
                        i += 1


        except IOError:
            print("IO error, not reading file. Try entering the filename again")
            #Do_Get_Data()


    def validate_id(id):
        """
        test using loadData_Bad.txt.
        #Raw input is "a0111", should return None
        because the input is too long to be valid.

        >>> Model.id_list[1] is None
        True

        #Raw input is "c234", should return None because
        the input has a lower case first char.

        >>> Model.id_list[3] is None
        True

        #Raw input is "E30", should return None because
        the input is not long enough.

        >>> Model.id_list[5] is None
        True

        #Raw input is "F456", should return "F456" because
        the input is in correct format.
        >>> Model.id_list[6]
        'F456'
        """
        match_id = re.match('[A-Z][0-9]{3}', id)
        if match_id is None or len(id) is not 4:
            print('id format incorrect: id entered as None')
            id = None
            print(id)
            return(id)
        else:
            return id



    def validate_gender(gender):
        """
        #Raw input is "?", should return None because not a valid input.
        >>> Model.gender_list[1] is None
        True

        #Raw input is " ", should return None because not a valid input.
        >>> Model.gender_list[6] is None
        True

        #Raw input is "F", should return "F" because it is valid input.
        >>> Model.gender_list[3]
        'F'
        """
        match_gender = re.match('(M|F)', gender)
        if match_gender is None:
            print('gender format incorrect:  entered as None')
            gender = None
            return gender
        else:
            return gender

    def validate_age(age):
        """
        #Raw input is "2", should return None as input is in
        invalid format.

        >>> Model.age_list[0] is None
        True

        #Raw input is "1S", should return None as input has a
        non-int character in it.

        >>> Model.age_list[7] is None
        True

        #Raw input is "60", should return "60" as it is valid.

        >>> Model.age_list[9]
        '60'
        """
        match_age = re.match('[0-9]{2}', age)
        if match_age is None or len(age) is not 2:
            print('age format incorrect:  entered as None')
            age = None
            return age
        else:
            return age

    def validate_sales(sales):
        """
        #Raw input is "54", should return None, because input in
        incorrect format.

        >>> Model.sales_list[6] is None
        True

        #Raw input is "5554", should return None, because input is in
        incorrect format, too long

        >>> Model.sales_list[7] is None
        True

        #Raw input is "222", should return "222" as it's correct format

        >>> Model.sales_list[0]
        '222'
        """
        match_sales = re.match('[0-9]{3}', sales)
        if match_sales is None or len(sales) is not 3:
            print('sales format incorrect:  entered as None')
            sales = None
            return sales
        else:
            return sales

    def validate_bmi(bmi):
        """
        #Raw input is "underweight", should return None as first char
        is lowercase

        >>> Model.bmi_list[1] is None
        True

        #Raw input is " ", should return None as field is empty

        >>> Model.bmi_list[4] is None
        True

        #Raw input is "Normal", should return "Normal" as is correct format

        >>> Model.bmi_list[0]
        'Overweight'
        """
        match_bmi = re.match('(Normal|Overweight|Obesity|Underweight)', bmi)
        if match_bmi is None:
            print('bmi format incorrect:  entered as None')
            bmi = None
            return bmi
        else:
            return bmi

    def validate_income(income):
        """
        #Raw input is "8", should return None, incorrect format, only 1 number

        >>> Model.income_list[2] is None
        True

        #Raw input is " ", should return None as it is an empty field

        >>> Model.income_list[3] is None
        True

        #Raw input is "999", should return "999" as is in correct format
        >>> Model.income_list[0]
        '999'

        #Raw input is "87", should return "87" because it is correct format
        >>> Model.income_list[1]
        '87'

        """
        match_income = re.match('[0-9]{2,3}', income)
        if match_income is None or len(income) > 3:
            print('income format incorrect:  entered as None')
            income = None
            return income
        else:
            return income

class View():
    pass

    def bar_graph(x, y):

        arrayX = np.array(x)
        arrayY = np.array(y)

        plt.plot(x, y, label="loaded from file")

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Interesting graph\nCheck it out')
        plt.legend()
        plt.show()


class Controller():
    pass


def main():
    pass

if __name__ == '__main__':
    main()

Model.get_data()
#doctest.testmod()
View.bar_graph([1,2,3,4], [5,22,33,450])