my_dict = {"Name":"Ram", "Address":"Urlabari"}

#Reverse of key and value pair using dictionary comprehension
#Syntax {k:v for vars in iterable}

reverse_of_key_value_pair = {k:v for (v, k) in my_dict.items()}
print(reverse_of_key_value_pair)