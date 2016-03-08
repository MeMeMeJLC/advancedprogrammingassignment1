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

class Model():

    def get_data_header():
        headers = ['id', 'gender', 'age', 'sales', 'bmi', 'income']
        return headers

    def get_data_values():
        data = [[4, 'm', 22, 5000, 22, 50000], [2, 'f', 33, 1000, 50, 30000]]
        return data

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
    pass
    def do_greet(self, person):
        print('hello ' + person)

    def do_show_data(self, header):
        View.display_header(Model.get_data_header())
        View.display_data(Model.get_data_values())

    def do_quit(self, args):
        print('Quitting...')
        raise SystemExit




def main():
    #print('this is the advanced programming assignment 1')
    name = "phil"
    #Controller.do_greet()
    #View.display_header(Model.get_data_header())
    #View.display_data(Model.get_data_values())

if __name__ == '__main__':
    main()
    controller = Controller()
    controller.prompt = '> '
    controller.cmdloop('Starting prompt...')



