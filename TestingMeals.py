from CoreFunctions import *
from Scripts.CoreFunctions import join_string, rangin_printing, create_base64, get_vegmeals
from Meals import *
from Scripts.Meals import count_ingredients

#Get a list of the 8 most used ingredients in vegetarian meals
#strCategory =
#   "idCategory": "12",
#  "strCategory": "Vegetarian",
# find all the meals that are vegeies
#Get all the ingredients
# add them th dictionary with key as ingredient
# sort in desc and pull first 8 out

meals = get_meals("Vegetarian")
#print(meals)
i=1
ingredients_list = []
for meal in meals:
    #if (i >5):break;
    i=i+1
    ingredients=get_ingredients(meal['idMeal'])
    ingredients_list.append(ingredients)

#print(count_ingredients(ingredients_list))
ingredient_count =count_ingredients(ingredients_list)

print("Ingredient usage count:")
for ingredient, count in ingredient_count.most_common():
    print(f"{ingredient}: {count}")

