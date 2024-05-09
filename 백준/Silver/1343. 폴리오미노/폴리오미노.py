S = input()

def t(S):
    result = ''
    if S.find('.') != -1:
        while S.find('.') != -1:
            c = S.find('.')
            if c % 2:
                return -1
            else:
                cA = c // 4
                cB = (c % 4) // 2
                result += cA * 'AAAA' + cB * 'BB' + '.'
                S = S[c+1:]

    if len(S) % 2:
        return -1
    else:
        cA = len(S) // 4
        cB = (len(S) % 4) // 2
        result += cA * 'AAAA' + cB * 'BB'
        return result

print(t(S))