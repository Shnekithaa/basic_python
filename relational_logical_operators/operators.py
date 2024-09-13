# Relational Operators
# - Equals to `==`
# - Not equals to `!=`
# - Greater than `>`
# - Lesser than `<`
# - Greater than or equal to `>=`
# - Lesser than or equal to `<=`

value_1 = "A"
value_2 = "B"
print(value_1 > value_2)

# Logical Operators
# - and
# - or
# - not

# | A   | B   | A AND B |
# |-----|-----|---------|
# |  0  |  0  |    0    |
# |  0  |  1  |    0    |
# |  1  |  0  |    0    |
# |  1  |  1  |    1    |


# | A   | B   | A OR B  |
# |-----|-----|---------|
# |  0  |  0  |    0    |
# |  0  |  1  |    1    |
# |  1  |  0  |    1    |
# |  1  |  1  |    1    |


# | A   | NOT A |
# |-----|-------|
# |  0  |   1   |
# |  1  |   0   |

print(True and False)
print(True or False)
print(not(True))