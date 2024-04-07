# Parser
def parse_to_latex(B, premises, gamma):
    # Helper function to convert a single tuple to a LaTeX string
    def tuple_to_latex(t, is_after_arrowseq=False):
        if t[0] == 'KEYWORD':
            if t[1] == 'arrowseq':
                if not is_after_arrowseq:  # Only add \vdash if the previous wasn't an arrowseq
                    return r'\vdash ', True
                else:
                    return '', True  # Skip this arrowseq
            elif t[1] == 'Gamma':
              return r'\Gamma ', False
            else:
                return t[1] + ' ', False
        elif t[0] == 'VARIABLE':
            return t[1] + ' ', False
        elif t[0] == 'IDENTIFIER' and t[1] == 'B':
            return B[0][1], False
        elif t[0] == 'IDENTIFIER' and t[1] == 'Gamma':
          return r'\Gamma', False
        elif t[0] == 'PUNCTUATION' and t[1] == '::':
            return ',', False
        return '', False

    # Convert the tuples into LaTeX strings, handling consecutive 'arrowseq' keywords correctly
    is_after_arrowseq = False
    premises_latex_parts = []
    gamma_latex_parts = []

    gamma_and = False
    first_premise = True

    for t in premises:
        latex_part, is_after_arrowseq = tuple_to_latex(t, is_after_arrowseq)
        if latex_part == '\Gamma' and gamma_and == False:
          gamma_and = True
        if gamma_and == True and latex_part == '\Gamma' and not first_premise:
          latex_part = '& ' + latex_part
        premises_latex_parts.append(latex_part)
        first_premise = False

    is_after_arrowseq = False  # Reset for gamma processing
    for t in gamma:
        latex_part, is_after_arrowseq = tuple_to_latex(t, is_after_arrowseq)
        gamma_latex_parts.append(latex_part)

    premises_latex = ''.join(premises_latex_parts).rstrip()
    gamma_latex = ''.join(gamma_latex_parts).rstrip()

  
    # Constructing the final LaTeX inference rule
    if len(B) == 1:
      B_identifier = B[0][1]
    else:
      join_list = [j[1] for j in B]
      B_identifier = ' '.join(join_list)
    latex = r"\[" + r"\infer{" + f"{gamma_latex}" + r"\vdash " + f"{B_identifier}" + r"}{" + f"{premises_latex}" + r"}" + r"\]"
    return latex