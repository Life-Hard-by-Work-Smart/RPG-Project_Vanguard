from src.gui_objects.common_gui_elements import *

class Item_slot:

    def update_text(self):
        if not self.stored_item == None:
            self.text = self.stored_item.name
        else:
            self.text = ""

    def __init__(self):
        self.stored_item = None
        self.text = ""

        self.update_text()

class Equipement_slot(Item_slot):

    def update_text(self):
        if not self.stored_item == None:
            self.text = self.stored_item.name
        else:
            self.text = self.equipement_type

    def __init__(self, equipement_type):
        self.equipement_type = equipement_type
        self.stored_item = None
        self.text = ""

        self.update_text()