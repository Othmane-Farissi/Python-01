def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    
    bmi = []
    
    try:
        if len(height) != len(weight):
            raise ValueError("bad arguments")
        for i in range(len(height)):
            if not isinstance(height[i],(float,int)) or not isinstance(weight[i],(float,int)):
                raise ValueError("bad arguments")
            bmi.append( weight[i] / (height[i] ** 2) )
        return bmi
         
    except ValueError as e:
        print("error: ", e)
        return []

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    
    result = []
    
    for i in range(len(bmi)):
        if bmi[i] > limit:
            result.append(True)
        else:
            result.append(False)
    return result