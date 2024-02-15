from collections import deque

def is_palindrome(str):
    d= deque()
    
    new_s = ''.join(c.lower() for c in str if c.isalpha())
    d.extend(new_s)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True
    # reversed_d = deque(reversed(d))
    # if d == reversed_d:
    #     return True
    # return False
    
    
    
print(is_palindrome("Я несу гусеня"))
print(is_palindrome("Козак з казок."))
print(is_palindrome("Уже лисі ліси... Лежу."))
print(is_palindrome("І що сало? Ласощі..."))
print(is_palindrome("A man, a plan, a canal, Panama!"))

    