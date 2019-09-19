#!/usr/bin/python

import math

# do the ingredients exist to make at lease one?
# yes - devide ingredients by recipe
# no  - return 0


def recipe_batches(recipe, ingredients):
	hasIngredients = True
	total = 0
	for key in recipe:
		if (key not in ingredients.keys()) or (ingredients[key] < recipe[key]):
				hasIngredients = False

	if hasIngredients:
		canMake = []
		for key in recipe:
			canMake.append(int(ingredients[key]/recipe[key]))
		total = min(canMake)

	return total


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))