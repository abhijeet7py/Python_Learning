my_shoppig_list = ["Bread", "Milk", "Butter"]

print(my_shoppig_list[0])
print(len(my_shoppig_list))

#  To remove the duplicate from the list --> set -- data
def bring_food(my_shoppig_list):
    more_item = input("Enter the item:")
    my_shoppig_list.append(more_item)
    # my_shoppig_list.remove(more_item)
    my_shoppig_list.insert(0,more_item)
    return my_shoppig_list

l = bring_food(my_shoppig_list)
print(l)