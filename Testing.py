#python3 -m doctest -v file_name.py >>> doctestleri calistirmaya yariyan kod 
#doctest syntax ornegi::::
"""goal 
add(1+2) #calistirdigimiz fonksyon 
3        #bekledigimiz cikti
"""

def eat_junk_food(food):
    assert food in ("pizza" , "hamburger" "fried patato") , "You need to be eat a funk food"
    return f"I am eatin {food}"

food = input("Enter a food pls ")
print(eat_junk_food(food))


#unit test , setup><><><