a = True
b = False
c = True
print(f"""
a and a,    {a and a}
b and b,    {b and b}
not c,      {not c}
not b,      {not b}
not a,      {not a}
a and b,    {a and b}
b and c,    {b and c}
a or c,     {a or c}
b or c,     {b or c}
c or a,     {c or a}
c or b,     {c or b}
c or c,     {c or c}
b or b,     {b or b}
""")