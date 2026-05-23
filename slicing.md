
# Python Slicing Notes

## 1. Slicing kya hoti hai?

Slicing ka use string, list, tuple etc. ke kisi specific part ko access karne ke liye hota hai.

Syntax:

object[start : stop : step]

- start → kahan se shuru karna hai
- stop → kahan tak jana hai (ye include nahi hota)
- step → kitne gap se move karna hai

---

## 2. Indexing

Python indexing 0 se start hoti hai.

Example:

text = "PYTHON"

| Character | P | Y | T | H | O | N |
|------------|---|---|---|---|---|---|
| Index      | 0 | 1 | 2 | 3 | 4 | 5 |

Examples:

text[0] → P
text[2] → T
text[5] → N

---

## 3. Negative Indexing

Negative indexing end se start hoti hai.

| Character | P | Y | T | H | O | N |
|------------|---|---|---|---|---|---|
| Index      |-6 |-5 |-4 |-3 |-2 |-1 |

Examples:

text[-1] → N
text[-2] → O
text[-6] → P

---

## 4. Basic Slicing

Example:

text = "PYTHON"

text[0:3]

Output:

PYT

Explanation:

- start = 0
- stop = 3
- 3 include nahi hoga

---

text[2:5]

Output:

THO

---

## 5. Empty Start and Stop

Start empty:

text[:4]

Output:

PYTH

Meaning:
Start automatically beginning se hoga

Stop empty:

text[2:]

Output:

THON

Meaning:
End tak jayega

Both empty:

text[:]

Output:

PYTHON

Meaning:
Pure object copy

---

## 6. Step Value

Example:

text[0:6:2]

Output:

PTO

Explanation:

Har 2nd element select hoga

---

text[::2]

Output:

PTO

---

## 7. Reverse Slicing

Reverse ke liye negative step use karte hain.

text[::-1]

Output:

NOHTYP

Meaning:
String reverse ho gayi

---

## 8. Negative Slicing

text[-5:-2]

Output:

YTH

Explanation:

- Start = -5
- Stop = -2
- Stop include nahi hoga

---

## 9. Important Rules

1. Stop index kabhi include nahi hota

2. Positive step:
   Left → Right move karta hai

3. Negative step:
   Right → Left move karta hai

4. Wrong direction dene par empty output aa sakta hai

Example:

text[4:2]

Output:

''

Reason:
Python left se right move kar raha hai but start > stop

---

## 10. Most Important Examples

text="PYTHON"

text[1:4]   → YTH

text[:3]    → PYT

text[2:]    → THON

text[-3:]   → HON

text[::2]   → PTO

text[::-1]  → NOHTYP

text[-4:-1] → THO