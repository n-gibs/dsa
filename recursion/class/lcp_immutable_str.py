def subordinate(input_str, idx_subproblem, partial_solution, result):
	if idx_subproblem == len(input_str):
		result.append(partial_solution)
		return

	if input_str[idx_subproblem].isdigit():
		subordinate(
            input_str,
            idx_subproblem + 1,
            partial_solution +
            input_str[idx_subproblem],
            result
        )
	else:
		subordinate(
            input_str,
            idx_subproblem + 1,
            #creating new string (copy)
            # o(n)
            partial_solution + input_str[idx_subproblem].upper(),
            result
        )
		subordinate(
            input_str,
            idx_subproblem + 1,
            partial_solution + input_str[idx_subproblem].lower(),
            result
        )

def root_manager(input_str):
	result = []

	subordinate(input_str, 0, "", result)

	return result

print(root_manager('a1b2'))