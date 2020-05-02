from menu_item import MenuItem


menu_item1 = MenuItem('sandwich',3,)
menu_item2 = MenuItem('choclate',4)
menu_item3 = MenuItem('pizza',5)
menu_item4 = MenuItem('cake',2)

menu_items = [menu_item1,menu_item2,menu_item3,menu_item4]
index=0
for menu_item in menu_items:
    print(str(index)+ ' ' + menu_item.info())
    index+=1


order = int(input("enter item number"))

selected_menu = menu_items[order]

print('seleceted_item is ' + ' : ' + selected_menu.name )

count = int(input("enter quantity of item(10% off more then 3)"))
result = selected_menu.get_total_price(count)
print('your total is ' + str(result))

