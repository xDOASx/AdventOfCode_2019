# 1202_program_alarm.py

def continue_program(code):
    if (code == 99):
        print("Code <99> encountered. Ending program")
        return False
    elif (code != 1 and code != 2):
        print("Error!")
        print("Unrecognized code: <" + str(code) + "> encountered. Ending program.")
        return False
    return True

def run_intcode(i_code):
    position = 0

    while continue_program(i_code[position]):
        opt_code = i_code[position]

        if (opt_code == 1):
            print("Opt code is: " + str(opt_code))
            sum = i_code[i_code[(position + 1)]] + i_code[i_code[(position + 2)]]
            i_code[i_code[position + 3]] = sum
        elif (opt_code == 2):
            print("Opt code is: " + str(opt_code))
            product = i_code[i_code[(position + 1)]] * i_code[i_code[(position + 2)]]
            i_code[i_code[position + 3]] = product
        
        position += 4
        
    print(i_code)

Final_Intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0]

Intcode = [2,4,4,5,99,0]

run_intcode(Intcode)