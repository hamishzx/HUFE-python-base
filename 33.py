snacks = {'提拉米苏': 15, '芝士蛋糕': 20, '三明治': 10}
drinks = {'红茶': 6, '咖啡': 12, '橙汁': 8}
menus = []
for snack in snacks:
    for drink in drinks:
        menu = (snack,drink, int((snacks[snack] + drinks[drink]) * 0.8))
        menus.append(menu)
        
for menu in menus:
        print(menu)
