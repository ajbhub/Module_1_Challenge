# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

#define variable "loan_count" equal to length of list
loan_count = (len(loan_costs))
#print statement displaying loan count
print(f"There are {loan_count} loans in the list.")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

#define variable "loan_total" equal to sum of all loans in list
loan_total = (sum(loan_costs))
#print statement displaying loan total rounded to 2 decimal places
print(f"The total of all loans in the list is: ${loan_total:.2f}")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

#define variable "avg_loan" equal to "loan_total" divided by "loan_count", which were defined previously on line 23 & 32 respectively
avg_loan = (loan_total/loan_count)
#print statement displaying avg loan, rounded to the second decimal due to it being a dollar amount
print(f"The average loan value in the list is: ${avg_loan:.2f}")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

#created variables for future_value and remianing_months in case needed later in program
future_value = loan.get('future_value')
remaining_months = loan.get('remaining_months')

#print the future value and remaining months with a statement included, put future value in dollars to match rest of program
print(f"The Future Value on this loan is: ${future_value:.2f}")
print(f"The number of Months Remaining on this loan are: {remaining_months}")



# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!

#defined discount_rate variable
discount_rate = .2

#created a variable for fair_value using included formula and printed result
fair_value = future_value / (1 + discount_rate/12) ** remaining_months

print(f"The Fair Value of the loan is: ${fair_value:.2f}")


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

#defined variable for loan_price using get()
loan_price = loan.get('loan_price')

#reused code from split_second_part_2 activity
#Continued to use variable name fair_value to represent my calculated present value and also to differentiate from variables used in next section.
# If fair_value is greater than or equal to cost to buy (loan_price), buy it:
if fair_value >= loan_price:
    print("Buy this one, superior bank boss! It's worth more than it's selling for.")
# Otherwise, take a pass:
elif fair_value < loan_price:
    print("Don't buy this, as it's offered at a price higher than what it's worth.")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!


def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    return present_value



# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

#copied from challenge module as directed by "Your function could then be used as shown in the following example:"
annual_discount_rate = 0.20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)

#chose not to round present_value to two decimals or add dollar sign as this was prewritten in started code 
print(f"The present value of the loan is: ${present_value:.2f}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

#created new list for inexpensive_loans
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

#using for loop, iterated through loans list, calling the "loan_price" value and determining if it is less than or equal to $500
#if the loan_price was less than or equal to $500, appended the dict for that loan to the "inexpensive_loans" list

for dict in loans:
    if dict.get("loan_price") <= 500:
        inexpensive_loans.append(dict)

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

#printed the list of inexpensive loans

print(f"Here is a list of Inexpensive Loans currently available for purchase - {inexpensive_loans}")


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

#reused code from automated equity rounds activity
print("Writing the data to a CSV file...")
# Open the output CSV file path using `with open`
with open(output_path, "w") as csvfile:
    # Create a csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the header to the CSV file
    csvwriter.writerow(header)

    # Write the values of each dictionary inside of `inexpensive_loans`
    # as a row in the CSV file.
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())