# 20. Summary Ranges
![Static Badge](https://img.shields.io/badge/Easy-gray)
![Static Badge](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false

```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.