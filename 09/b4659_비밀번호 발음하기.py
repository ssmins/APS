
while True: 
    strr = input()
    if strr == 'end': 
        break

    mo = 'aeiou'
    mo_count = 0 
    ja_count = 0 

    mo_1_state = False
    in_a_row_state = True 
    same_char_state = True
    result = True

    for i in range(len(strr)): 

        # 조건 1 
        if strr[i] in mo: 
            mo_1_state = True
        
        # 조건 2 
        if strr[i] not in mo: 
            mo_count = 0 
            ja_count += 1 
        
        if strr[i] in mo: 
            ja_count = 0 
            mo_count += 1 
    
        # 조건 3-1 
        if 0 < i <= len(strr) - 1: # 범위는 항상 견제하자. 내가 틀렸을 확률이 좀 높아 
            if strr[i] == strr[i-1]: 
                same_char_state = False

            # 조건 3-2 
            if strr[i] == 'e': 
                if strr[i-1] == 'e': 
                    same_char_state = True        

            elif strr[i] == 'o': 
                if strr[i-1] ==  'o': 
                    same_char_state = True 

        # 판정 
        if same_char_state == False : 
            result = False
            break
                
        # 판정 
        if mo_count >= 3 or ja_count >= 3: 
            in_a_row_state = False
            result = False
            break

    if mo_1_state == False: 
        result = False
    
    if result == False: 
        print(f'<{strr}> is not acceptable.')
    elif result == True: 
        print(f'<{strr}> is acceptable.')
        