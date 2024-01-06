def arithmetic_arranger(problems, show=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    dashes = ""
    answers = ""

    for problem in problems:
        num1, op, num2 = problem.split()

        if op != "+" and op != "-":
            return "Error: Operator must be '+' or '-'."
        elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not num1.isnumeric() or not num2.isnumeric():
            return "Error: Numbers must only contain digits."

        if len(num1) == max(len(num1), len(num2)):
            dashes += "-" * (2 + len(num1)) + "    "
            line1 += "  " + num1 + "    "
            line2 += op + " " + (len(num1) - len(num2)) * " " + num2 + "    "
            if op == "+":
                answer = int(num1) + int(num2)
            else:
                answer = int(num1) - int(num2)

            answers += " " * (2 + len(num1) - len(str(answer))) + str(answer) + "    "

        elif len(num2) == max(len(num1), len(num2)):
            dashes += "-" * (2 + len(num2)) + "    "
            line1 += "  " + " " * (len(num2) - len(num1)) + num1 + "    "
            line2 += op + " " + num2 + "    "
            if op == "+":
                answer = int(num1) + int(num2)
            else:
                answer = int(num1) - int(num2)

            answers += " " * ((2 + len(num2)) - len(str(answer))) + str(answer) + "    "

    if show:
        arranged_problems = (
            line1.rstrip()
            + "\n"
            + line2.strip()
            + "\n"
            + dashes.rstrip()
            + "\n"
            + answers
        ).rstrip()
    else:
        arranged_problems = (
            line1.rstrip() + "\n" + line2.strip() + "\n" + dashes
        ).rstrip()
    return arranged_problems


print(
    arithmetic_arranger(
        ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True
    )
)
