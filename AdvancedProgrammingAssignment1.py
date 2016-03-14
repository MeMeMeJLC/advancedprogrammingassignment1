from cmd import Cmd
import pickle
import re
import doctest

class Model():

    def get_data_header():
        headers = ['id', 'gender', 'age', 'sales', 'bmi', 'income']
        return headers

    def get_data_values():
        file = input('Enter file name:')
        print('file name choosen is: ' + file)
        try:
            with open(file + '.pickle', 'r+b') as f:
                data = pickle.load(f)
            raise file_error('File name not valid')
        finally:
            return data

    def validate_id(id):
        #id = input('please enter ID no: (format eg: A001 to Z999)')
        match_id = re.match('[A-Z][0-9]{3}', id)
        if match_id is None:
            print('id format incorrect: id entered as X000')
            new_id = 'X000'
            print(new_id)
            return(new_id)
        else:
            return id

    def validate_gender(gender):
        match_gender = re.match('(M|F)', gender)
        if match_gender is None:
            print('gender format incorrect:  entered as F')
            gender = 'F'
            return gender
        else:
            return gender

    def validate_age(age):
        match_age = re.match('[0-9]{2}', age)
        if match_age is None:
            print('age format incorrect:  entered as 20')
            age = '20'
            return age
        else:
            return age

    def validate_sales(sales):
        match_sales = re.match('[0-9]{3}', sales)
        if match_sales is None:
            print('sales format incorrect:  entered as 000')
            sales = '000'
            return sales
        else:
            return sales

    def validate_bmi(bmi):
        match_bmi = re.match('(Normal|Overweight|Obesity|Underweight)', bmi)
        if match_bmi is None:
            print('bmi format incorrect:  entered as Normal')
            bmi = 'Normal'
            return bmi
        else:
            return bmi

    def validate_income(income):
        match_income = re.match('[0-9]{2,3}', income)
        if match_income is None:
            print('income format incorrect:  entered as 00')
            income = '00'
            return income


class View():

    def display_header(headers):
        Model.get_data_header()
        for head in headers:
            print(head, end="|")

    def display_data(data):
        Model.get_data_values()
        print(data)
        """for item in data:
            i = data.index(item)
            print('', end='\n')
            for item in data[i]:
                print(item, end='   |')"""


class Controller(Cmd):

    def do_show_data(self, header):
        """
        method do_show_data
        :param self:
        :param header:
        :return The column names, and the rows of values in raw form:
        """
        View.display_header(Model.get_data_header())
        View.display_data(Model.get_data_values())

    def do_write_data(self, args):
        """
        method docstring
        :param self:
        :param args:
        :Where you create and serialise the input data :
        """

        id = input("enter id")
        gender = input("gender")
        age = input("age")
        sales = input("sales")
        bmi = input("bmi")
        income = input("income")
        filename = input("filename")

        id = Model.validate_id(id)
        gender = Model.validate_gender(gender)
        age = Model.validate_age(age)
        sales = Model.validate_sales(sales)
        bmi = Model.validate_bmi(bmi)
        income = Model.validate_income(income)
        array = [id, gender, age, sales, bmi, income]
        print(array)

        try:
            print('file name choosen is: ' + filename)
            with open(filename + '.pickle', 'rb') as f:
                data = pickle.load(f)
            with open(filename + '.pickle', 'wb') as f:
                pickle.dump(str(array) + ', ' + data, f)
        except NameError:
            print("file name not found")
            with open(filename + '.pickle', 'wb') as f:
                pickle.dump(str(array), f)


    def do_delete_data(self, args):
        """
        method do_delete_data
        :param self:
        :param args:
        :Deletes all data in the file:
        """
        file = input('Enter file name:')
        print('file name choosen is: ' + file)
        with open(file + '.pickle', 'wb') as f:
            pickle.dump("", f)
            print("data deleted")

    def do_load_data(self, file):
        """
        method do_delete_data
        :param self:
        :param args:
        :Deletes all data in the file:
        """
        file = file
        print('file name choosen is: ' + file)
        with open(file + '.pickle', 'r+b') as f:
            data = pickle.load(f)
            print(data)

    def do_hello(self, person):
        print('hello ' + person)

    def do_quit(self, args):
        """
        Quit from CMD
        """
        print('Quitting...')
        raise SystemExit

    do_q = do_quit


def main():
    print("Hello, welcome to the SalesPerson Data App")

if __name__ == '__main__':
    main()

    controller = Controller()
    controller.prompt = ':) '
    controller.cmdloop('Starting prompt...')
