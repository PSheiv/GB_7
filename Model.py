import json
import xml.etree.ElementTree as ET

# Case 1
def get_Spravochnik():
    file = open("db.json", encoding="utf-8")
    data = file.read()
    file.close()

    tel_spravochnik = json.loads(data)
    return tel_spravochnik

# Case 2
def export_xml_Spravochnik():
    data = get_Spravochnik()
    root = ET.Element("Contacts")
    for i in range(1, (len(data["Contacts"]) + 1)):
        ET.SubElement(ET.SubElement(
            root, f'C{i}'), "FIO").text = data["Contacts"][f'C{i}']["FIO"]
        ET.SubElement(ET.SubElement(
            root, f'C{i}'), "Tel").text = data["Contacts"][f'C{i}']["Tel"]

    tree = ET.ElementTree(root)
    tree.write("contacts.xml")

# Case 3
def new_record():
    fio = input("Введите ФИО: ")
    tel = input("Введите номер телефона: ")
    add_new_record(fio, tel)

def add_new_record(fio, tel):
    data = get_Spravochnik()
    last_elem_index = len(data["Contacts"])
    data["Contacts"][f'C{last_elem_index+1}'] = {"FIO": fio, "Tel": tel}
    print(data)

    with open('db.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
