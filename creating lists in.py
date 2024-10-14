a_list_with_values = [1,2,3,4,'joemama',6,'alucard']

mutipled_list = a_list_with_values * 2
print(mutipled_list)

the_multiplied_list_is_not_multiplied_anymore = mutipled_list[::-1]
print(the_multiplied_list_is_not_multiplied_anymore)

for item in the_multiplied_list_is_not_multiplied_anymore:
    print(item,end="")