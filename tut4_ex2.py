#exercise2

def parse_int(s: str):
    parsed_int: int | None = None

    try:
        parsed_int = int(s)
    except ValueError:
        return None
    except TypeError:
        return None
    
    return parsed_int
   # is_valid = False 
   # parsed_int = 0

    #while not is_valid:
     #   try:
      #      parsed_int = int(s)
       #     is_valid = True
        #    return parsed_int
        #except ValueError:
         #   print('print a valid number')
        #except TypeError:
         #    print('print a valid number')
    #return parsed_int
        
def get_num_from_user():
    user= input('enter a number or type -9 to quit')
    parsed_input = parse_int(user)

    if parsed_input is None:
        print('enter a number')
        return get_num_from_user()

    return parsed_input


total, count = 0 , 0

parsed_user = get_num_from_user()

while parsed_user != '-9':
    total += parsed_user
    count += 1
    parsed_user= get_num_from_user()

print(total)
print(count)