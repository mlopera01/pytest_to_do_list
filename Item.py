class Item:
    def __init__(self, id_item, description, priority, assigned_to):
        self.id_item = id_item #argumento 1 de la clase
        self.description = description
        self.priority = priority
        self.assigned_to =assigned_to

    def get_id(self):
        return self.id_item

    def set_id(self, id_item):
        self.id_item=id_item

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def get_assigned_to(self):
        return self.assigned_to

    def set_assigned_to(self, user):
        self.assigned_to = user            

