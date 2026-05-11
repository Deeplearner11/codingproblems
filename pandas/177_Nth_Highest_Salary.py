# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

# Solution :

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    dist = employee['salary'].drop_duplicates()
    
    sort_dist = dist.sort_values(ascending =False)
    
    if N> len(sort_dist) or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    nth_highest = sort_dist.iloc[N-1]

    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
