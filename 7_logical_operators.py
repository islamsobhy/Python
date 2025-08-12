is_hungry = True
has_money = True
resturant_open = True
meeting_friends = False

if is_hungry and  resturant_open and has_money or meeting_friends:
    #ordering is very important, test using the below:
    #if is_hungry and  resturant_open and or meeting_friends and has_money:
    print ("I want food")
else : 
    print ("I can't buy food")