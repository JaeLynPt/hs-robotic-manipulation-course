def find_grades(grades, students):
    """
    Returns a list containing the grades for students (in the same order)

    Inputs:
        grades (dict): is a dictionary mapping student names (str) to grades (str).
    
        students (list): is a list of student names.

    Returns:
        list: a list of the grades in order by name pf students.

    Examples:
    >>> d = {'Ana': 'B', 'Matt': 'C', 'John': 'B', 'Katy': 'A'}
    >>> find_grades(d, ['Matt', 'Katy'])
    ['C', 'A']
    
    >>> find_grades(d, ['Ana', 'John'])
    ['B', 'B']
    
    >>> find_grades(d, ['John', 'Ana', 'Katy'])
    ['B', 'B', 'A']
    """
    result = [] 
  
    for name in grades:
        if name in students:
            result.append(grades[name])

         

    return result 

def new_dict(input_dict):
    """
    Takes a dictionary and returns a new dictionary where 5 is added to each value.
    
    Inputs:
        input_dict (dict): A dictionary with integer values.

    Returns:
        dict: A new dictionary with each value increased by 5.
    
    Examples:
    >>> new_dict({"item1": 2, "item2": 7, "item3": 20})
    {'item1': 7, 'item2': 12, 'item3': 25}
    """
    new_dict = {}

    for key in input_dict:
        new_dict.update({key: input_dict[key]+5})


    return new_dict

def check_same_values(input_dict):
    """
    Checks if all values in the dictionary are the same.

    Inputs:
        input_dict (dict): A dictionary with values.

    Returns:
        bool: True if all values are the same, False otherwise.
    
    Examples:
    >>> check_same_values({'item1': 'apple', 'item2': 'apple', 'item3': 'apple'})
    True
    >>> check_same_values({'item1': 'apple', 'item2': 'apple', 'item3': 'orange'})
    False
    """
    same = input_dict['item1']
    #iterate through dictionary, compare the values of all the keys 
    for key in input_dict: 
        if input_dict[key] != same:
            return False


    return True 

def combine_dicts(input_dicts):
    """
    Combines a list of dictionaries into a single dictionary by summing the amounts of the same items.
    
    Inputs:
        input_dicts (list): A list of dictionaries with 'item' and 'amount' keys.

    Returns:
        dict: A combined dictionary with summed amounts for each item.
    
    Examples:
    >>> combine_dicts([{'item': 'servos', 'amount': 400}, {'item': 'breadboard', 'amount': 300}, {'item': 'servos', 'amount': 750}])
    {'servos': 1150, 'breadboard': 300}
    """
    new_dict = {}

    for d in input_dicts:
        val = d['item']
        if val not in new_dict:
            new_dict[val] = d['amount'] 
        else: 
            new_dict[val] += d['amount']



    return new_dict 