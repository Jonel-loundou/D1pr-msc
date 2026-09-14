
def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")
def sandwich(nombre,vegetarian=0):
    
    for i in range(nombre):

        if vegetarian == 1:
           bread()
           lettuce()
           tomato()
           lettuce()
           tomato()
           bread()
        else:
           bread()
           lettuce()
           tomato()
           ham()
           ham()
           bread()

nombre = int(input("Combien de sandwichs voulez-vous ? "))
vegetarian = int(input("Quel sandwich voulez-vous ? végétarien (1) ou normal (0) ? "))
sandwich(2)    #Sandwich normal
sandwich (2,1) #Sandwich végétarien



    
#        print("I can't do this")
#nombre = int(input ("Combien de sandwichs voudriez vous? "))
#sandwich(nombre)



    
#    if vegetarian == 1:
#       print("This is a vegetarian sandwich")
#    else:
#        print("This is a regular sandwich")