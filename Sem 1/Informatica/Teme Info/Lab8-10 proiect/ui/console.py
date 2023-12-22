from domain.vectors import MyVector
from domain.vectors import VectorRepository

def greet():
    print("Welcome!")
    print("Here are a list of operations to be used:")
    print("0. Stop the program.")
    print("1. Add one vector to the repository.")
    print("2. Get all vectors.")
    print("3. Get a vector at a given index.")
    print("4. Update a vector at an index.")
    print("5. Update a vector by ID.")
    print("6. Delete a vector at an index.")
    print("7. Delete a vector by ID.")
    print("8. Plot all vectors in a chart.")
    
greet()
c = 1


while c !=0:
    c = int(input("Choose your command:"))
    if 0 < c < 15:
        if c == 1:
            id = int(input("id = "))
            colour = str(input("colour = "))
            type = int(input("type = "))
            values = list(input("list = "))
            VectorRepository.addVector( id, colour, type, values)

        elif c == 2:
            VectorRepository.getVectors()

        elif c == 3:
            index = int(input("The position of the vector: "))
            VectorRepository.getAtIndex(index)

        elif c == 4:
            index = int(input("The position of the vector: "))
            id = int(input("id = "))
            colour = str(input("colour = "))
            type = int(input("type = "))
            values = list(input("list = ")) 
            VectorRepository.updateAtIndex(index, id, colour, type, values)

        elif c == 5:
            new_id = int(input("old id = "))
            id = int(input("new id = "))
            colour = str(input("colour = "))
            type = int(input("type = "))
            values = list(input("list = ")) 
            VectorRepository.updateByID(new_id, id, colour, type, values)

        elif c == 6:
            index = int(input("The position of the vector: ")) 
            VectorRepository.deleteAtIndex(index)

        elif c == 7:
            id = int(input("id = "))
            VectorRepository.deleteByID(id)

        elif c == 8:
            VectorRepository.PlotInChart()
    else:
        raise ValueError("The command imputed is not available!")