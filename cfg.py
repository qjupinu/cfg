# L(G) is a^n b^n, with n >= 0
NON_TERMINALS = {'S'}
TERMINALS = {'a', 'b'}
START_SYMBOL = 'S'
PRODUCTIONS = {'S': ['aSb', '']} # '' = epsilon

import random

# Task 1: CFG definition
def cfg_init():
    """Display the CFG definition"""
    print("CFG Definition:")
    print(f"Non-terminals: {NON_TERMINALS}")
    print(f"Terminals: {TERMINALS}")
    print(f"Start symbol: {START_SYMBOL}")
    print(f"Productions: S -> aSb | epsilon")

# Task 2: random strings
def generate_strings(total, max_length):
    strings = []
    
    for _ in range(total):
        # begin with with start symbol
        current = START_SYMBOL
        steps = 0
        
        while any(c in NON_TERMINALS for c in current) and steps < max_length:
            # find leftmost non-terminal
            for i, char in enumerate(current):
                if char in NON_TERMINALS:
                    # choose random production rule
                    rule = random.choice(PRODUCTIONS[char])
                    # replace NT with rule
                    current = current[:i] + rule + current[i+1:]
                    break
            steps += 1
        
        if (all(c in TERMINALS or c == '' for c in current) and len(current) <= max_length):
            strings.append(current)
    
    return list(set(strings))

# Task 3: show derivation steps. Target must be a^n b^n
def derive_string(target):
    if not is_member(target):
        return None
    
    derivation = ['S']
    current = 'S'
    
    # empty string case
    if target == '':
        derivation.append('epsilon')
        return derivation
    
    # count needed 'a's and apply S -> aSb rule that many times
    n = target.count('a')
    for cnti in range(n):
        current = current.replace('S', 'aSb', 1)
        derivation.append(current)
    
    # now apply S -> epsilon rule
    current = current.replace("S", "epsilon")
    if "epsilon" in current:
        current = current.replace("epsilon", "")
    derivation.append(current)
    
    return derivation

# Task 4: Check if string belongs to L(G)
def is_member(string):
    if string == '':
        return True

    # check for equal number of a's and b's
    # all a's before all b's
    # nothing else allowed
    
    if not all(char in TERMINALS for char in string):
        return False

    a_total = string.count('a')
    b_total = string.count('b')
    if a_total != b_total:
        return False
    
    try:
        first_b_id = string.index('b')
        return 'a' not in string[first_b_id:]
    except ValueError:
        return string == ''



def main():
    print("======== Context-Free Grammar ========\n")
    print("Task 1 - CFG Definition:")
    cfg_init()  

    print("\nTask 2 - Generated Strings:")
    generated_strings = generate_strings(10, 10)
    for str in generated_strings:
        print(f"  {str if str else 'epsilon'}")
    
    print("\nTask 3 - Derivations:")
    for str in generated_strings:
        print(f"Derivation for '{str}':")
        derivation = derive_string(str)
        if derivation:
            for step in derivation:
                display_step = step if step else 'epsilon'
                print(f"  {display_step}")
        else:
            print("No derivations.")
    
    # Task 4: Test membership
    # test_strings = ['aaabbb', 'aabb', 'abab', 'aaaabbbb', 'aabbb', 'bbaaa', 'abc', '']
    print("\nTask 4 - Membership Check:")
    for str in generated_strings:
        print(f"  OK: '{str}' is {'a member' if is_member(str) else 'not a member'} of L(G).")

if __name__ == "__main__":
    main()