name = "Islam"      #string
age = 32            #int
money = 22.3        #float 
Happy =  True       #Boolean (True, False)

print (name)  
print (age)
print (money)
print (Happy)


print ("Name: " + name)  #string concatination 
#print ("Age: "+ age)     #This will bring an error because u can only concatenate str (not "int") to str and to override
#you can use built-in function called str() which converts int/float/bool into a string 

print ("Age: " + str(age))