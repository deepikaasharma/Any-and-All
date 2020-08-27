numbers = [0, 1, 2, 3]
are_any_truthy = any(numbers)

print(are_any_truthy)
# In the above example, all the non-zero values are "truthy" so the result of applying the any() function evaluates to True.

numbers = [0, False, 0, False]
are_any_truthy = any(numbers)

print(are_any_truthy)

# Because none of the values in the above code snippet are "truthy," the above code will evaluate to False.

bool_list = [True, False, True, True, False]
print(any(bool_list))

a = 10
n = 20

num_list = list(range(a, n))
print(any(num_list))

"""All the values are non-zero and, therefore, "truthy", so the code below will print True."""

numbers = [1, 2, 3, 4]
all_are_truthy = all(numbers)

print(all_are_truthy)

# The numbers list contains a 0, which is not "truthy," so the result of the all() function will be False.

numbers = [0, 1, 2, 3]
some_are_truthy = all(numbers)

print(some_are_truthy)


bool_list = [True, False, True, True, False]
print(all(bool_list))

a = 10
n = 20

num_list = list(range(a, n))
print(all(num_list))

num_list[0] = 0
print(all(num_list))


# Given the following code, what would print to the console?

str_list = ['a', 'b', 'c', '']
print(any(str_list))


# Given the following code, what would print to the console?

str_list = ['a', 'b', 'c', '']
print(all(str_list))



