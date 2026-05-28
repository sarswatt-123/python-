# Python String Methods Notes

## Introduction
In Python, a string is a sequence of characters. Python provides many built-in string methods to perform operations such as searching, formatting, checking, and modifying text.

---

# String Case Conversion Methods

### `capitalize()`
Converts the first character to uppercase.

Example:
```python
"hello".capitalize()
# Output: Hello
```

### `casefold()`
Converts text to lowercase in a stronger way than `lower()`.

```python
"HELLO".casefold()
# Output: hello
```

### `lower()`
Converts all characters to lowercase.

```python
"HELLO".lower()
# Output: hello
```

### `upper()`
Converts all characters to uppercase.

```python
"hello".upper()
# Output: HELLO
```

### `swapcase()`
Changes uppercase to lowercase and lowercase to uppercase.

```python
"Hello".swapcase()
# Output: hELLO
```

### `title()`
Converts the first letter of each word to uppercase.

```python
"hello world".title()
# Output: Hello World
```

---

# Searching Methods

### `find()`
Returns the index of the first occurrence.

```python
"hello".find("l")
# Output: 2
```

### `rfind()`
Searches from the right side.

```python
"hello".rfind("l")
# Output: 3
```

### `index()`
Same as `find()` but gives an error if not found.

```python
"hello".index("e")
# Output: 1
```

### `rindex()`
Searches from the right and returns index.

```python
"hello".rindex("l")
# Output: 3
```

### `count()`
Counts occurrences of a substring.

```python
"hello".count("l")
# Output: 2
```

---

# Checking Methods

### `isalnum()`
Checks if string contains only letters and numbers.

### `isalpha()`
Checks if string contains only letters.

### `isascii()`
Checks if characters are ASCII.

### `isdecimal()`
Checks for decimal characters.

### `isdigit()`
Checks if string contains digits.

### `isnumeric()`
Checks if string contains numeric values.

### `islower()`
Checks if all letters are lowercase.

### `isupper()`
Checks if all letters are uppercase.

### `isspace()`
Checks if string contains only spaces.

### `istitle()`
Checks if string follows title case.

### `isidentifier()`
Checks if string is a valid Python variable name.

### `isprintable()`
Checks if characters can be printed.

Example:

```python
"Hello123".isalnum()
# Output: True
```

---

# Removing Spaces and Characters

### `strip()`
Removes spaces from both sides.

```python
" hello ".strip()
# Output: hello
```

### `lstrip()`
Removes spaces from the left side.

```python
" hello".lstrip()
```

### `rstrip()`
Removes spaces from the right side.

```python
"hello ".rstrip()
```

### `removeprefix()`
Removes a given prefix.

```python
"Mr.John".removeprefix("Mr.")
# Output: John
```

### `removesuffix()`
Removes a given suffix.

```python
"file.txt".removesuffix(".txt")
# Output: file
```

---

# Splitting and Joining Methods

### `split()`
Splits a string into a list.

```python
"a b c".split()
# Output: ['a','b','c']
```

### `rsplit()`
Splits from the right side.

### `splitlines()`
Splits text by lines.

```python
"Hi\nHello".splitlines()
```

### `join()`
Joins elements together.

```python
"-".join(["a","b","c"])
# Output: a-b-c
```

---

# Replacement Methods

### `replace()`
Replaces one value with another.

```python
"hello".replace("l","x")
# Output: hexxo
```

### `translate()`
Replaces characters using a translation table.

### `maketrans()`
Creates a translation table.

---

# Alignment Methods

### `center()`
Aligns text in the center.

```python
"Hi".center(10)
```

### `ljust()`
Aligns text to the left.

### `rjust()`
Aligns text to the right.

### `zfill()`
Adds zeros at the beginning.

```python
"45".zfill(5)
# Output: 00045
```

---

# Formatting Methods

### `format()`
Formats strings.

```python
"Hello {}".format("John")
# Output: Hello John
```

### `format_map()`
Formats using dictionary values.

---

# Partition Methods

### `partition()`
Splits string into three parts.

```python
"a-b-c".partition("-")
```

### `rpartition()`
Splits from the right side.

---

# Other Methods

### `startswith()`
Checks whether string starts with a value.

```python
"hello".startswith("he")
# Output: True
```

### `endswith()`
Checks whether string ends with a value.

```python
"hello".endswith("lo")
# Output: True
```

### `expandtabs()`
Converts tabs into spaces.

### `encode()`
Converts string into bytes.

---

# String Operators

### Concatenation (`+`)

```python
"Hello" + " World"
# Output: Hello World
```

### Repetition (`*`)

```python
"Hi"*3
# Output: HiHiHi
```

### Membership (`in`)

```python
"a" in "apple"
# Output: True
```

### Length (`len()`)

```python
len("hello")
# Output: 5
```

---

# Summary

Python string methods help in:

- Modifying text
- Searching data
- Validating values
- Formatting strings
- Splitting and joining text
- Removing spaces
- Performing text operations efficiently