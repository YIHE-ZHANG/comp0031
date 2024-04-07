from parser31 import parse_to_latex

# Examples 1
B_1 = [('KEYWORD', 'B')]

premises_1 = [
    ('KEYWORD', 'path'), ('VARIABLE', 'X'), ('VARIABLE', 'Y'), 
    ('PUNCTUATION', '::'), ('KEYWORD', 'adj'), ('VARIABLE', 'X'),
    ('VARIABLE', 'Z'), ('PUNCTUATION', '::'), ('KEYWORD', 'path'),
    ('VARIABLE', 'Z'), ('VARIABLE', 'Y'), ('PUNCTUATION', '::'),
    ('KEYWORD', 'L'), ('KEYWORD', 'arrowseq'), ('KEYWORD', 'arrowseq'), ('IDENTIFIER', 'B')
]

gamma_1 = [
    ('KEYWORD', 'adj'), ('VARIABLE', 'X'), ('VARIABLE', 'Z'),
    ('PUNCTUATION', '::'), ('KEYWORD', 'path'), ('VARIABLE', 'Z'),
    ('VARIABLE', 'Y'), ('PUNCTUATION', '::'), ('KEYWORD', 'L')
]

# Example 2
B_2 = [('KEYWORD', 'path'), ('VARIABLE', 'X'), ('VARIABLE', 'Z') ]

premises_2 = [
     ('IDENTIFIER', 'Gamma'), ('KEYWORD', 'arrowseq'), ('KEYWORD', 'adj'), 
     ('VARIABLE', 'X'), ('VARIABLE', 'Y'), ('IDENTIFIER', 'Gamma'), 
     ('KEYWORD', 'arrowseq'), ('KEYWORD', 'path') , ('VARIABLE', 'Y'), ('VARIABLE', 'Z')
]

gamma_2 =[('KEYWORD', 'Gamma')]

# Parse and print the LaTeX representation 1
latex_representation = parse_to_latex(B_1, premises_1, gamma_1)
latex_representation

# Parse and print the LaTeX representation 2
latex_representation_2 = parse_to_latex(B_2, premises_2, gamma_2)
print(latex_representation_2)