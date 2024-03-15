#!/usr/bin/python3

# Exercise 1
test_string = "Test string Hello"
test_number = 666
test_list = ['one', 'two', 'three']
test_bool = True

# Exercise 2
test_string_grab = test_string[:3]

# Exercise 3
test_list_grab_first = test_list[0]

# Exercise 4
test_number_add = test_number + 10

# Exercise 5
test_list_grab_last = test_list[-1]

# Exercise 6
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')

# Exercise 7
test_string_word_first = test_string.split()[0]
test_string_words_other = test_string.split(test_string_word_first, maxsplit=1)[1]
test_string_exer_7 = test_string_word_first.upper() + test_string_words_other

# Exercise 8
print(str(test_number))

# Exercise 9
print("hello world")

# Exercise "add"
print(test_string.find("Hello"))
test_string_replace = test_string.replace("Hello", "Good bye")
