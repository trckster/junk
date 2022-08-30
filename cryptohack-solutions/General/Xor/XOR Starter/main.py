s = 'label'
result = ''
for c in s:
    result += chr(ord(c) ^ 13)

print(f'crypto{{{result}}}')
