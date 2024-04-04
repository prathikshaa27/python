def to_divide_numbers(first_number, second_number):
    import pdb; pdb.set_trace()
    if second_number == 0:
        print("Error: You cannot divide the number by zero")
        return None
    return first_number / second_number

final_result = to_divide_numbers(100, 0)
if final_result is not None:
    print("The division of two numbers will be :", final_result)
