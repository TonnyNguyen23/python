"""
Program: case_study_incometax_page_38.py
Author: Nguyen Xuan Tung
Date: 13/07/2021
Compute a person’s income tax.
1. Significant constants
 tax rate
 standard deduction
 deduction per dependent
2. The inputs are
 gross income
 number of dependents
3. Computations:
 taxable income = gross income - the standard
 deduction - a deduction for each dependent
 income tax = is a fixed percentage of the taxable income
4. The outputs are
 the income tax
"""

# Khởi tạo hằng số
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Yêu cầu nhập đầu vào
grossIncome = float(input("Nhập tổng thu nhập: "))
numDependents = int(input("Nhập số người phụ thuộc: "))

# Tính thuế thu nhập
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

# Hiển thị thuế thu nhập
print("Thuế thu nhập là: $" + str(incomeTax))