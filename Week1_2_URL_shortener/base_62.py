base_62_list = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base_62_encoder(number):
    if number == 0: 
        return number
    
    result = []
    while number > 0: 
        remainder = base_62_list[number % 62]
        result.append(str(remainder))
        number = number // 62

    result_inverse = result[len(result): : -1]
    return "".join(result_inverse)


# For reference
'''
def base_62_decoder(string): 
    power = 0
    result = 0
    while len(string) >= 1: 
        if len(string) == 1: 
            result += int(base_62_list.find(string[-1]) * (62 ** power))
            return result
        
        last = base_62_list.find(string[-1]) * (62 ** power)
        power += 1
        result += last
        string = string[0: len(string)-1]
    return result
'''
