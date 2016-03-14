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
from cmd import Cmd
import pickle
import re

class Model():

    def get_data_header():
        headers = ['id', 'gender', 'age', 'sales', 'bmi', 'income']
        return headers

    def write_id(id):
        match_id = re.match('[A-Z][0-9]{3}', id)
        if match_id == None:
            print('id format incorrect: id entered as X000')
            new_id = 'X000'
            print(new_id)
            return(new_id)
        else:
            return id

    def write_gender(gender):
        match_gender = re.match('(M|F)', gender)
        if match_gender == None:
            print('gender format incorrect:  entered as F')
            gender = 'F'
            return gender
        else:
            return gender

    def write_age(age):
        match_age = re.match('[0-9]{2}', age)
        if match_age == None:
            print('age format incorrect:  entered as 20')
            age = '20'
            return age
        else:
            return age

    def write_sales(sales):
        match_sales = re.match('[0-9]{3}', sales)
        if match_sales == None:
            print('sales format incorrect:  entered as 000')
            sales = '000'
            return sales
        else:
            return sales

    def write_bmi(bmi):
        match_bmi = re.match('(Normal|Overweight|Obesity|Underweight)', bmi)
        if match_bmi == None:
            print('bmi format incorrect:  entered as Normal')
            bmi = 'Normal'
            return bmi
        else:
            return bmi

    def write_income(income):
        match_income = re.match('[0-9]{2,3}', income)
        if match_income == None:
            print('income format incorrect:  entered as 00')
            income = '00'
            return income

class View():
    pass
    def display_header(headers):
        Model.get_data_header()
        for head in headers:
            print(head, end="|")


    def display_data(data):
        Model.get_data_values()
        for item in data:
            i = data.index(item)
            print('', end='\n')
            for item in data[i]:
                print(item, end='   |')

class Controller(Cmd):

    def do_show_data(self, header):
        View.display_header(Model.get_data_header())
        View.display_data(Model.get_data_values())

    def do_write_data(self, args):
        pass
        print('enter the following data')
        id = input('please enter ID no: (format eg: A001 to Z999)')
        id = Model.write_id(id)
        gender = input('please enter gender: (format eg: M or F)')
        gender = Model.write_gender(gender)
        age = input('please enter age: (format eg: 01 to 99)')
        age = Model.write_age(age)
        sales = input('please enter sales: (format eg: 3 numbers only')
        sales = Model.write_sales(sales)
        bmi = input('please enter bmi: (format eg: Underweight, Normal, Overweight or Obesity')
        bmi = Model.write_bmi(bmi)
        income = input('please enter income: (format eg: 2 or 3 digits')
        income = Model.write_income(income)
        array = [id, gender, age, sales, bmi, income]
        print(array)
        with open('datafile.pickle', 'rb') as f:
            data = pickle.load(f)
        with open('datafile.pickle', 'wb') as f: #(w)rite(b)inary
            pickle.dump(str(array) + ', ' + data, f)


    def do_load_data(self, file):
        #Model.load_file()
        with open('datafile.pickle', 'r+b') as f:
            data = pickle.load(f)
            print(data)

    def do_quit(self, args):
        """
        Quit from CMD
        """
        print('Quitting...')
        raise SystemExit

    do_q = do_quit




def main():
    print("Hello, welcome to the SalesPerson Data App")

if __name__ == '__main__': #tells which is main function
    main()
    controller = Controller()
    controller.prompt = ':) '
    controller.cmdloop('Starting prompt...')



