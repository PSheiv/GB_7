import Model
import View

def start_program():
    View.user_menu()
    choice()
       
def choice():
    choice = input("Введите номер: ")
    next_step(choice)    

def next_step(choice):
    match choice:
        case "1":
           print(Model.get_Spravochnik())
        case "2":
            Model.export_xml_Spravochnik()
        case "3":
            Model.new_record()
        case _:
            start_program()