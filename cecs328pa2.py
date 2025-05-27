# Takes input from the user in the form of a string waveform and returns
# the number of 1's and 0's.
def nrz_encoding(nrz_input):
    nrz_str = ''
    nline_bool = False
    zero_counter = 0
    one_counter = 0

    for i, s in enumerate(nrz_input):
        if((nline_bool == False) and (i != 0)):
            if(s == '\n'):
                nline_bool = True
            elif(s == '_'):
                one_counter += 1
                if(one_counter % 3 == 0):
                    nrz_str += '1'
                    one_counter = 0
            elif(s == ' '):
                if(i + 1 != len(nrz_input) and ((nrz_input[i - 1] == '_') or (nrz_input[i + 1] == '_'))):
                    continue
                elif(i + 1 != len(nrz_input)):
                    zero_counter += 1
                    if(zero_counter % 3 == 0):
                        nrz_str += '0'
                        zero_counter = 0

        elif(nline_bool == True):
            if((s == '_') and ('|' not in nrz_input[i:len(nrz_input) - 1])):
                zero_counter += 1
                if(zero_counter % 3 == 0):
                    nrz_str += '0'
                    zero_counter = 0

    return nrz_str