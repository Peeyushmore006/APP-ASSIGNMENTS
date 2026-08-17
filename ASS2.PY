# ============================================================
# DYNAMIC REPORT GENERATOR
# ============================================================
# This program creates dynamic reports using:
#
# 1. Decorators
# 2. Class methods
# 3. Static methods
# 4. Magic methods
# 5. Dynamic templates
# 6. Object-oriented programming
#
# The user can:
# - Create a report
# - Add data
# - Apply formatting
# - Generate the final report
# ============================================================

from typing import Dict, Any, Callable
from functools import wraps


# ============================================================
# DECORATOR 1: LOGGING DECORATOR
# ============================================================

def log_function(func: Callable) -> Callable:
    """
    Decorator that prints a message whenever a function is called.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"[LOG] Executing: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] Completed: {func.__name__}")

        return result

    return wrapper


# ============================================================
# DECORATOR 2: UPPERCASE DECORATOR
# ============================================================

def uppercase_report(func: Callable) -> Callable:
    """
    Converts generated report text to uppercase.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


# ============================================================
# REPORT CLASS
# ============================================================

class Report:
    """
    Represents a customizable report.
    """

    # Default templates
    templates = {
        "simple": "Name: {name}\nMarks: {marks}\nGrade: {grade}",

        "detailed": (
            "===== STUDENT REPORT =====\n"
            "Name   : {name}\n"
            "Marks  : {marks}\n"
            "Grade  : {grade}\n"
            "Status : {status}"
        )
    }

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------

    def __init__(self, title: str, template: str = "simple"):

        self.title = title
        self.template = self.templates.get(
            template,
            template
        )

        self.data: Dict[str, Any] = {}

    # --------------------------------------------------------
    # CLASS METHOD
    # --------------------------------------------------------

    @classmethod
    def create_detailed_report(cls, title: str):
        """
        Alternative constructor using classmethod.
        """

        return cls(title, "detailed")

    # --------------------------------------------------------
    # ADD DATA
    # --------------------------------------------------------

    @log_function
    def add_data(self, **kwargs) -> None:
        """
        Accepts unlimited keyword arguments dynamically.
        """

        self.data.update(kwargs)

    # --------------------------------------------------------
    # CHANGE TEMPLATE
    # --------------------------------------------------------

    @log_function
    def set_template(self, template: str) -> None:

        self.template = template

    # --------------------------------------------------------
    # GENERATE REPORT
    # --------------------------------------------------------

    @log_function
    def generate(self) -> str:

        try:

            return self.template.format(**self.data)

        except KeyError as error:

            return f"Missing data field: {error}"

    # --------------------------------------------------------
    # MAGIC METHOD: __str__
    # --------------------------------------------------------

    def __str__(self):

        return self.generate()

    # --------------------------------------------------------
    # MAGIC METHOD: __len__
    # --------------------------------------------------------

    def __len__(self):

        return len(self.data)

    # --------------------------------------------------------
    # MAGIC METHOD: __call__
    # --------------------------------------------------------

    def __call__(self):

        return self.generate()

    # --------------------------------------------------------
    # STATIC METHOD
    # --------------------------------------------------------

    @staticmethod
    def calculate_grade(marks: float) -> str:
        """
        Calculates grade without requiring object data.
        """

        if marks >= 90:
            return "A+"

        elif marks >= 80:
            return "A"

        elif marks >= 70:
            return "B"

        elif marks >= 60:
            return "C"

        elif marks >= 50:
            return "D"

        return "F"


# ============================================================
# SPECIAL DECORATED REPORT CLASS
# ============================================================

class UpperCaseReport(Report):
    """
    Child class demonstrating inheritance and decorators.
    """

    @uppercase_report
    def generate(self) -> str:

        return super().generate()


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n========================================")
    print("       DYNAMIC REPORT GENERATOR")
    print("========================================")

    # --------------------------------------------------------
    # CREATE REPORT USING CLASS METHOD
    # --------------------------------------------------------

    report = Report.create_detailed_report(
        "Student Performance"
    )

    # --------------------------------------------------------
    # CALCULATE GRADE
    # --------------------------------------------------------

    marks = 87

    grade = Report.calculate_grade(marks)

    # --------------------------------------------------------
    # ADD DATA DYNAMICALLY
    # --------------------------------------------------------

    report.add_data(
        name="Peeyush",
        marks=marks,
        grade=grade,
        status="PASS"
    )

    # --------------------------------------------------------
    # GENERATE REPORT
    # --------------------------------------------------------

    print("\nGenerated Report:\n")

    print(report)

    # --------------------------------------------------------
    # __len__ MAGIC METHOD
    # --------------------------------------------------------

    print("\nNumber of data fields:", len(report))

    # --------------------------------------------------------
    # __call__ MAGIC METHOD
    # --------------------------------------------------------

    print("\nCalling report object directly:")

    print(report())

    # --------------------------------------------------------
    # CUSTOM TEMPLATE
    # --------------------------------------------------------

    custom_template = """
---------------------------------
       STUDENT SUMMARY
---------------------------------
Student : {name}
Marks   : {marks}
Grade   : {grade}
Result  : {status}
---------------------------------
"""

    report.set_template(custom_template)

    print("\nCustom Report:\n")

    print(report)

    # --------------------------------------------------------
    # DECORATOR DEMONSTRATION
    # --------------------------------------------------------

    upper_report = UpperCaseReport(
        "Upper Case Report",
        custom_template
    )

    upper_report.add_data(
        name="Rahul",
        marks=92,
        grade=Report.calculate_grade(92),
        status="PASS"
    )

    print("\nDecorated Uppercase Report:\n")

    print(upper_report)


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()