##

def main():

    with open("seats.txt") as file_seats, open("answers.txt") as file_answers:
        rows = list(map(str.split, file_seats))
        answers_raw = list(map(str.split, file_answers))
    answers = {line[0]: line[1:] for line in answers_raw}

    for i, row in enumerate(rows):

        for j, student in enumerate(row):

            student_answers = answers[student]
            right_name = row[j + 1] if j != len(row) - 1 else None
            if not right_name: continue

            right_answers = answers[right_name]
            if right_answers and student_answers == right_answers:
                print(f"{student} has the same answers as {right_name}")

            elif right_name:

                if student_answers.count("-") == right_answers.count("-"): continue

                most_unanswered = student if student_answers.count("-") > right_answers.count("-") else right_name
                less_unanswered = student if most_unanswered == right_name else right_name
                comparison = [i for i in answers[less_unanswered]]

                for idx, answer in enumerate(answers[most_unanswered]):
                    if answer == "-" and answers[less_unanswered][idx] != answer:
                        comparison[idx] = answer

                if comparison == answers[most_unanswered]:
                    print(f"{most_unanswered} might have copied from {less_unanswered}")
                    continue


if __name__ == '__main__':
    main()