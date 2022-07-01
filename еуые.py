from openpyxl.styles.numbers import BUILTIN_FORMATS

for key, val in BUILTIN_FORMATS.items():
    print(f'{key}: {val}')
