# cfg
Homework 3: Context-Free Grammar - Formal Languages and Automata Theory

## Overview
This project implements a Context-Free Grammar (CFG) parser for the grammar:
```
S → aSb | ε
```
This grammar generates the language L(G) = {aⁿbⁿ | n ≥ 0}

## Tasks
- **CFG Definition**
- **String Generation**
- **String Derivation**
- **Membership Testing**

## Running the program
```bash
python3 cfg.py
```

## Sample output
```
======== Context-Free Grammar ========

Task 1 - CFG Definition:
CFG Definition:
Non-terminals: {'S'}
Terminals: {'b', 'a'}
Start symbol: S
Productions: S -> aSb | epsilon

Task 2 - Generated Strings:
  epsilon
  aaabbb
  aaaabbbb
  ab
  aabb

Task 3 - Derivations:
Derivation for '':
  S
  epsilon
Derivation for 'aaabbb':
  S
  aSb
  aaSbb
  aaaSbbb
  aaabbb
Derivation for 'aaaabbbb':
  S
  aSb
  aaSbb
  aaaSbbb
  aaaaSbbbb
  aaaabbbb
Derivation for 'ab':
  S
  aSb
  ab
Derivation for 'aabb':
  S
  aSb
  aaSbb
  aabb

Task 4 - Membership Check:
  OK: '' is a member of L(G).
  OK: 'aaabbb' is a member of L(G).
  OK: 'aaaabbbb' is a member of L(G).
  OK: 'ab' is a member of L(G).
  OK: 'aabb' is a member of L(G).
```