"""
Actualice este archivo para implementar los siguientes métodos ya declarados:
- add_member: Debe agregar un miembro a la lista self._members
- delete_member: Debe eliminar un miembro de la lista self._members
- get_member: Debe devolver un miembro de la lista self._members
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1, 2, 3]
            }
        ]

    # Este método genera un ID incremental único
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## Debes implementar este método
        ## Agrega el miembro a la lista de _miembros
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name

        self._members.append(member)
        
        return member

    def delete_member(self, id):
        ## Debes implementar este método
        ## Recorre la lista y elimina el miembro con el ID especificado
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return True
        ## Si no se encuentra el miembro, devuelve False
        return False

    def get_member(self, id):
        ## Debes implementar este método
        ## Loop todos los miembros y devuelve el que tiene esa ID
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    


if __name__ == "__main__":
    familia = FamilyStructure("Jackson")
    print("Miembros iniciales:", familia.get_all_members())
    resultado = familia.delete_member(1)  # Intenta eliminar el miembro con id 1
    print("¿Eliminado?", resultado)
    print("Miembros después de eliminar:", familia.get_all_members())
    # Output esperado:
    # Miembros iniciales: [{'id': 1, 'first_name': 'John