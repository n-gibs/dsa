def lcp(input_str):
	solutions = []

	fill_blanks(0, [], input_str, solutions) # Root manager call

	return solutions
#slate = partial solution
def fill_blanks(idx_subproblem, slate, input_str, solutions):

    def p(comment):
        print(idx_subproblem, comment, slate, solutions)
    # Base case
    if idx_subproblem == len(input_str):
        #create string from array
        solutions.append("".join(slate))

        return

    # Recursive case
    if input_str[idx_subproblem].isdigit():
        slate.append(input_str[idx_subproblem])
        fill_blanks(idx_subproblem + 1, slate, input_str, solutions)
        #remove last element when going back up the tree
        slate.pop()

    else:
        slate.append(input_str[idx_subproblem].lower())
        fill_blanks(idx_subproblem + 1, slate, input_str, solutions)       #remove last element when going back up the tree
        slate.pop()

        slate.append(input_str[idx_subproblem].upper())
        fill_blanks(idx_subproblem + 1, slate, input_str, solutions)
        #remove last element when going back up the tree
        slate.pop()


prob = "a1b2"



res = lcp(prob)

print(res)