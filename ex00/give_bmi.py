def checkType(element):
    """
    Check if the input is a list of numbers (int or float).

    Args:
        element (any): The object to check.

    Returns:
        bool: True if element is a list containing only int or
        float, False otherwise.
    """
    if not isinstance(element, list):
        return False
    for x in element:
        if not isinstance(x, (int, float)):
            return False
    return True


def give_bmi(height: list[int | float], weight: list[int | float]):
    """
    Calculate Body Mass Index (BMI) for lists of heights and weights.

    BMI formula: BMI = weight / (height ** 2)

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[float]: List of BMI values corresponding to each
        height/weight pair.
    """
    result = []
    try:
        if not checkType(height) or not checkType(weight):
            raise AssertionError("Values must be type of int or float")
        elif len(height) != len(weight):
            raise AssertionError("Lists must be same size")

        for i in range(len(height)):
            result.append(weight[i] / (height[i] ** 2))

    except AssertionError as e:
        print(f"ERROR: {e}")
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to BMI values to indicate if each exceeds the threshold.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Threshold value to compare against.

    Returns:
        list[bool]: List of boolean values; True if BMI exceeds limit,
        else False.
    """
    result = []
    try:
        if not checkType(bmi):
            raise AssertionError("Values must be type of int or float")
        elif not isinstance(limit, int):
            raise AssertionError("Limit must be an integer")

        for i in range(len(bmi)):
            result.append(bmi[i] > limit)
    except AssertionError as e:
        print(f"ERROR: {e}")

    return result

# tester.py:

# from give_bmi import give_bmi, apply_limit
# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
