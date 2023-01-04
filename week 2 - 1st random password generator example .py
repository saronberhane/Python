import random #this makes it a random generator 

choices = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" #this is the letters and symboles of choice for the password
passlen = 8 #the required length of the password
password = "".join(random.sample(choices, passlen)) #variable of what our password will be
print (password)