import pygame

class Inventory_cell(pygame.Rect):
    common_widht_and_height = 100
    def __init__(self, x, y, name, item):
        self.width = 100
        self.height = 100
        self.x = x
        self.y = y
        self.name = name
        self.item = item


NUMBER_OF_CELLS_IN_INV_GRID = 36
NUMBER_OF_EQUIPEMENT_CELLS = 4
EQUIPEMENT_CELL_NAMES = ["head", "weapon", "chest", "legs"]

def generate_inventory():
    inventory_cells = {}
    for i in range(NUMBER_OF_CELLS_IN_INV_GRID):
        inventory_cells[str(i)] = Inventory_cell(300 + Inventory_cell.common_widht_and_height * (i%6) + 16 * (i%6), 20 + Inventory_cell.common_widht_and_height * (i//6) + 16 * (i//6), str(i), None)
        inventory_cells[str(i)].item = None
    return inventory_cells

def generate_equipement_slots():
    equipement_slots = {}
    for i in range(NUMBER_OF_EQUIPEMENT_CELLS):
        equipement_slots[EQUIPEMENT_CELL_NAMES[i]] = Inventory_cell(100, 136 + Inventory_cell.common_widht_and_height * i + 16 * i, EQUIPEMENT_CELL_NAMES[i], None)
        equipement_slots[EQUIPEMENT_CELL_NAMES[i]].item = None
    return equipement_slots

inventory_cells = generate_inventory()

equipement_cells = generate_equipement_slots()

def transferable(previously_clicked_cell, clicked_cell):
    bool_transferable = True
    print(previously_clicked_cell.name, clicked_cell.name)
    
    if previously_clicked_cell is clicked_cell:
        bool_transferable = False
        print("fail, same cell")
    elif previously_clicked_cell.name in EQUIPEMENT_CELL_NAMES and clicked_cell in EQUIPEMENT_CELL_NAMES:
        bool_transferable = False
        print("fail, both e")
    elif previously_clicked_cell.name not in EQUIPEMENT_CELL_NAMES or clicked_cell not in EQUIPEMENT_CELL_NAMES:
        print(clicked_cell.item)
        if clicked_cell.name in EQUIPEMENT_CELL_NAMES and previously_clicked_cell.item.equipement_type != clicked_cell.name:
            print(previously_clicked_cell.item.equipement_type, clicked_cell.name)
            bool_transferable = False
            print("fail, item not matching e type")
        elif previously_clicked_cell.name in EQUIPEMENT_CELL_NAMES and clicked_cell.item != None and clicked_cell.item.equipement_type != previously_clicked_cell.name:
            bool_transferable = False
            print("fail, 2. item not matching e type")
    print(bool_transferable)
    return bool_transferable

def item_transfare_handler(previously_clicked_cell: Inventory_cell, clicked_cell: Inventory_cell, cells):
    if previously_clicked_cell != None:
        print("cool, ready for transfare")
        if transferable(previously_clicked_cell, clicked_cell):
            print(previously_clicked_cell.item, clicked_cell.item)
            cell_1_name = previously_clicked_cell.name
            cell_2_name = clicked_cell.name
            temp_item = clicked_cell.item
            cells[cell_2_name].item = previously_clicked_cell.item
            print(previously_clicked_cell.item, clicked_cell.item)
            cells[cell_1_name].item = temp_item
            previously_clicked_cell, clicked_cell = None, None
            print(fr"transfered from {cell_2_name} to {cell_1_name} {cells[cell_1_name].item} and from {cell_1_name} to {cell_2_name} {cells[cell_2_name].item}")
            return (previously_clicked_cell, clicked_cell, cells[cell_2_name], cells[cell_1_name])
        else:
            previously_clicked_cell, clicked_cell = None, None


    elif previously_clicked_cell == None and clicked_cell.item != None:
        previously_clicked_cell = clicked_cell
        clicked_cell = None
        print("stored")
    return (previously_clicked_cell, clicked_cell, None, None)