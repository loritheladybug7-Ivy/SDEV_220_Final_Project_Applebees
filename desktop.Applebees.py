# Define a class representing a Recipe
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    
    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}\n"

# Main function to demonstrate the usage
def main():
    # Dictionary to store recipes
    recipes = {}

    # Creating recipe instances and adding them to the dictionary
    recipe1 = Recipe("Chicken Fettucini Alfredo",
                     ["fettucini", "heavy whipping cream", "parmesan", "salt", "black pepper", "garlic powder", "butter"],
                     "\n1. Cook fettucini until al dente, and place chicken strips into oven at 375 deg F.\n2. In a separate pan, melt butter then add whipping cream and heat.\n3. Once heated, add in salt, pepper, and garlic powder, and stir in well.\n4. While continuing to stir, add in parmesan and turn off heat.\5. Drain fettucini and add to alfredo sauce and combine.\6. Plate, adding chicken in strips on top.")
    recipes["Chicken Fettucini Alfredo"] = recipe1

    recipe2 = Recipe("Margarita",
                     ["Margarita Mix", "Tequila (well unless specified)", "rim salt", "lime juice", "lime wedge"],
                     "\n1. Taking a 2 piece mixing cups, fill with ice, tequila, lime juice, and mix.\n2. Hold tightly and shake.\n3. Take the lime wedge and wet the edges of a 32 oz glass, and rub the top of the glass on the rim salt.\n 4. Pour the margarita into the glass, garnish with another lime wedge, and serve.")
    recipes["Margarita"] = recipe2

    recipe3 = Recipe("Tiramisu",
                     ["ladyfingers", "mascarpone cheese", "eggs", "sugar", "coffee", "cocoa powder"],
                     "\n1. Dip ladyfingers in coffee.\n2. Layer soaked ladyfingers and mascarpone mixture.\n3. Repeat layers and refrigerate.\n4. Dust with cocoa powder before serving.")
    recipes["Tiramisu"] = recipe3

    # Displaying all recipes
    print("Restaurant Recipes:")
    for recipe_name, recipe in recipes.items():
        print(recipe)

if __name__ == "__main__":
    main()
