# Lesson 5 Independent Challenges

## Challenge 1: `get_numbers_over_50_v1` (8 points)

| Function parameter(s)        | Function return(s)                                                |
|------------------------------|-------------------------------------------------------------------|
| `numbers`, a list of numbers | A list of only those numbers from the input list that are over 50 |

Write a function that takes a list of numbers and returns a list of the numbers from the original list that are over 50.

**Important note:** for version 1 of this function, you should use the `filter` function internally rather than a list comprehension. Your reviewers will check this.

## Challenge 2: `get_numbers_over_50_v2` (8 points)

| Function parameter(s)        | Function return(s)                                                |
|------------------------------|-------------------------------------------------------------------|
| `numbers`, a list of numbers | A list of only those numbers from the input list that are over 50 |

Write a function that takes a list of numbers and returns a list of the numbers from the original list that are over 50.

**Important note:** for version 2 of this function, you should use a list comprehension internally rather than the `filter` function. Your reviewers will check this.

## Challenge 3: `get_words_under_5_characters_v1` (8 points)

| Function parameter(s)      | Function return(s)                                                              |
|----------------------------|---------------------------------------------------------------------------------|
| `words`, a list of strings | A list of only those words from the input list that are under 5 characters long |

Write a function that takes a list of words and returns a list of the numbers from the original list that are under 5 characters long.

**Important note:** for version 1 of this function, you should use the `filter` function internally rather than a list comprehension. Your reviewers will check this.

## Challenge 4: `get_words_under_5_characters_v2` (8 points)

| Function parameter(s)      | Function return(s)                                                              |
|----------------------------|---------------------------------------------------------------------------------|
| `words`, a list of strings | A list of only those words from the input list that are under 5 characters long |

Write a function that takes a list of words and returns a list of the numbers from the original list that are under 5 characters long.

**Important note:** for version 2 of this function, you should use a list comprehension internally rather than the `filter` function. Your reviewers will check this.

## Challenge 5: `get_names_v1` (8 points)

| Function parameter(s)                                | Function return(s)                                    |
|------------------------------------------------------|-------------------------------------------------------|
| `people`, a list of dictionaries representing people | A list of the names of the people from the input list |

Write a function that takes a list of dictionaries representing people and returns a list of the `'name'` keys from each dictionary in the original list.

**Important note:** for version 1 of this function, you should use the `map` function internally rather than a list comprehension. Your reviewers will check this.

## Challenge 6: `get_names_v2` (8 points)

| Function parameter(s)                                | Function return(s)                                    |
|------------------------------------------------------|-------------------------------------------------------|
| `people`, a list of dictionaries representing people | A list of the names of the people from the input list |

Write a function that takes a list of dictionaries representing people and returns a list of the `'name'` keys from each dictionary in the original list.

**Important note:** for version 2 of this function, you should use a list comprehension internally rather than the `map` function. Your reviewers will check this.

## Challenge 7: `double_numbers_v1` (8 points)

| Function parameter(s)        | Function return(s)                                |
|------------------------------|---------------------------------------------------|
| `numbers`, a list of numbers | A list of each number from the input list doubled |

Write a function that takes a list of numbers and returns a list of the numbers from the original list doubled.

**Important note:** for version 1 of this function, you should use the `map` function internally rather than a list comprehension. Your reviewers will check this.

## Challenge 8: `double_numbers_v2` (8 points)

| Function parameter(s)        | Function return(s)                                |
|------------------------------|---------------------------------------------------|
| `numbers`, a list of numbers | A list of each number from the input list doubled |

Write a function that takes a list of numbers and returns a list of the numbers from the original list doubled.

**Important note:** for version 2 of this function, you should use a list comprehension internally rather than the `map` function. Your reviewers will check this.

## Challenge 9: `string_split` (12 points)

| Function parameter(s)                | Function return(s)                         |
|--------------------------------------|--------------------------------------------|
| `string_to_split`, a string to split | A list of individual words from the string |

Write a function that takes a string and separates it into a list of substrings based on the position of the space characters in the original. For example, the string `"One two three"` should be separated into the list of words `['One', 'two', 'three']`.

**Important note:** if you are in any doubt as to the intended behaviour of the function, note that it should mimic the behaviour of the inbuilt string `split` method. You should not use this function as part of your solution. Your reviewers will check this.

## Challenge 10: `string_join` (8 points)

| Function parameter(s)                                                                                | Function return(s)                                                                             |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `separator`, a string to use to separate each string in `strings_to_join`, a list of strings to join | A string containing all the strings in the list of strings to join, separated by the separator |

Write a function that takes a separator string and a list of strings to join, and combines them to form a single string containing each of the strings to join, separated by the separator. For example, the separator string `' AND '` and the list of strings to join `['one', 'two', 'three']` should join to form the string `"one AND two AND three"`.

**Important note:** if you are in any doubt as to the intended behaviour of the function, note that it should mimic the behaviour of the inbuilt string `join` method. You should not use this function as part of your solution. Your reviewers will check this.

## Challenge 11: `list_reverse` (8 points)

| Function parameter(s)    | Function return(s)                          |
|--------------------------|---------------------------------------------|
| `items`, a list of items | A list containing the same items in reverse |

Write a function that takes a list of items and returns another list containing the same items in reverse.

**Important note:** you should not use the inbuilt `reversed` function or the inbuilt list `reverse` method as part of your solution. Your reviewers will check this.

## Challenge 12: `set_intersection` (8 points)

| Function parameter(s)                      | Function return(s)                                      |
|--------------------------------------------|---------------------------------------------------------|
| `items_1` and `items_2`, two sets of items | A set containing the overlap between the two input sets |

Write a function that takes two sets of items and returns another set containing only those items that belong to both of the original sets.

**Important note:** you should not use the inbuilt set `intersection` method or the `&` operator as part of your solution. Your reviewers will check this.
