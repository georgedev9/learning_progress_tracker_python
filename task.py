import re

class LearningTracker:
    students_count = 0
    students_dict = {}

    def find_student(self, student_id):
        while True:
            student_record = {}

            if student_id == 'back':
                break

            for key in self.students_dict.values():
                if key.get(int(student_id)):
                    student_record = key.get(int(student_id))

            if student_record:
                record = (f"Python={student_record['python']}; DSA={student_record['dsa']}; "
                          f"Databases={student_record['databases']}; Flask={student_record['flask']}")

                print(f"id points: {record}")
            else:
                print(f"No student is found for id={student_id}")

            student_id = input()


    def show_students(self):
        if self.students_dict:
            print("Students:")
            for key, first, last in self.students_dict.values():
                print(key)
        else:
            print("No students found")

    def add_student(self, email, first, last):
        student_id = 24_000 + self.students_count

        self.students_dict[email] = {
            student_id: {'python': 0, 'dsa': 0, 'databases': 0, 'flask': 0}, 'first_name': first, 'last_name': last}
        self.students_count += 1

        print("The student has been added.")

    def update_record(self, record):

        while True:
            record_lst = record.split()

            if len(record_lst) > 0 and record_lst[0] == 'back':
                break

            elif len(record_lst) != 5:
                print("Incorrect points format")

            else:
                student_id = int(record_lst[0])
                python_score = record_lst[1]
                dsa_score = record_lst[2]
                databases_score = record_lst[3]
                flask_score = record_lst[4]

                student_record = {}

                for key in self.students_dict.values():
                    if key.get(student_id):
                        student_record = key.get(student_id)

                scores_match = f"{python_score} {dsa_score} {databases_score} {flask_score}"

                if student_record:
                    if re.fullmatch(r"[0-9]* [0-9]* [0-9]* [0-9]*", scores_match):
                        student_record.update(
                            python=python_score,
                            dsa=dsa_score,
                            databases=databases_score,
                            flask=flask_score
                        )
                        print("Points updated")
                    else:
                        print("Incorrect points format")
                else:
                    print(f"No student is found for id={student_id}")

            record = input()

    def is_there_student(self, email):
        return self.students_dict.get(email)

    def verify_name(self, name):
        return re.fullmatch(r"^[^-'](?!.*--)(?!.*'')(?!.*-')(?!.*'-)[A-Za-z'-]*[^-']$", name)

    def verify_email(self, email):
        return re.fullmatch(r"[^@]+@[^@]+\..+$", email)

    def verify_credentials(self, credentials):

        while True:
            credentials_lst = credentials.split()

            if len(credentials_lst) > 0 and credentials_lst[0] == 'back':
                print(f"Total {self.students_count} students have been added.")
                break

            elif len(credentials_lst) < 3:
                print("Incorrect credentials.")

            else:

                first_name = credentials_lst[0]
                last_name = ""
                email_address = credentials_lst[-1]

                for i in range(1, len(credentials_lst) - 1):
                    last_name += credentials_lst[i]

                first = self.verify_name(first_name)
                last = self.verify_name(last_name)
                email = self.verify_email(email_address)

                if first and last and email:
                    if self.is_there_student(email.string):
                        print("This email is already taken.")
                    else:
                        self.add_student(email.string, first.string, last.string)

                elif not first:
                    print("Incorrect first name")
                elif not last:
                    print("Incorrect last name")
                elif not email:
                    print("Incorrect email")

            credentials = input()

    def start_tracker(self):
        print("Learning progress tracker")

        while True:
            user_input = input()

            if user_input == "exit":
                print("Bye!")
                break
            elif user_input.strip() == "":
                print("No input")
            elif user_input == 'back':
                print("Enter 'exit' to exit the program.")

            elif user_input == 'add students':
                print("Enter student credentials or 'back' to return: ")
                credentials = input()
                if credentials == 'back':
                    print(f"Total {self.students_count} students have been added.")
                else:
                    self.verify_credentials(credentials)

            elif user_input == 'list':
                self.show_students()

            elif user_input == 'add points':
                print("Enter an id and points or 'back' to return")
                points = input()
                if points != 'back':
                    self.update_record(points)

            elif user_input == 'find':
                print("Enter an id or 'back' to return")
                student_id = input()
                if student_id != 'back':
                    self.find_student(student_id)

            else:
                print("Unknown command!")


def main():
    lp_tracker = LearningTracker()
    lp_tracker.start_tracker()


if __name__ == "__main__":
    main()
