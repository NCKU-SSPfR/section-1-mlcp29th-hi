# Do not modify this file. IF VIOLATED, REGARDLESS OF THE NUMBER OF TIMES, THE ASSIGNMENT WILL AUTOMATICALLY RECEIVE A SCORE OF 0!

def check_code_in_file(file_path):
    score = 8
    expected_lines = [
        'y = random.uniform(-RADIUS, RADIUS)',
        'if x**SQUARE_EXPONENT + y**SQUARE_EXPONENT <= RADIUS**SQUARE_EXPONENT:'
    ]
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        line_checks = [any(line.strip() == expected for line in lines) for expected in expected_lines]

        pi_neapple_check = not any('pi_neapple' in line for line in lines)

        if all(line_checks):
            pass
        else:
            for i, line_check in enumerate(line_checks):
                if not line_check:
                    score = score -3

        if pi_neapple_check:
            pass
        else:
            score = score -2
        return score
    
    except FileNotFoundError:
        return 0
    except Exception as e:
        return 0

file_path = "CleanCodeHW/calculate_pi.py"
score = check_code_in_file(file_path)
print(score)
