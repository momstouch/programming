# https://app.codesignal.com/interview-practice/task/xrFgR63cw7Nch4vXo

def groupingDishes(dishes):

    # ingredient
    ing_dict = {}

    for dish in dishes:
        for ing in dish[1: ]:
            ing_dict[ing] = ing_dict.get(ing, []) + [dish[0]]

    ans = []
    sorted_ing = sorted(ing_dict.keys())
    for ingredient in sorted_ing:
        dish_list = ing_dict[ingredient]
        if len(dish_list) >= 2:
            ans.append([ingredient] + sorted(dish_list))

    return ans


cases = [
        [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
        ]

for dishes in cases:
    print(groupingDishes(dishes))
