from Item import Item
from User import User
from Cell import Cell

class To_do_list:
    def __init__(self):
        self.items= [] #el constructor
        
    def add_item(self, item):
        self.items.append(item)

    def delete_item(self, id_item):
        for i in self.items:
            if (i.get_id() == id_item):
                items.remove(i)

    def get_item(self, id_item):
        for i in self.items:
            if (i.get_id() == id_item):
                print ("id :" + i.id_item)
                print ("description :" + i.description)
                print ("priority :" + i.priority)
                print ("user name :" + i.assigned_to.name)
                print ("user last name :" + i.assigned_to.last_name)

    def show_item(self):
        for i in self.items:
            print("id :" + i.id_item)
            print("description : " + i.description)
            print("priority : " + i.priority)
            print("user name : " + i.assigned_to.name)
            print("user last_name : " + i.assigned_to.last_name)
          
def main():
#    print("soy linda jajaja")
    cell = Cell("Desarrollo", "Marce", "2022-06-16")
    user = User("CC", "43103973", "Marce", "Hernandez", cell)
    item = Item("1", "Afiliar", "1", user)
    to_do_list = To_do_list()
    to_do_list.add_item(item) #envía la variable que acabo de declarar en el main
    to_do_list.show_item()
    

if __name__ == "__main__":
    main()

