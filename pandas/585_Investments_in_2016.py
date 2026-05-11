# Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

# have the same tiv_2015 value as one or more other policyholders, and
# are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Insurance table:
# +-----+----------+----------+-----+-----+
# | pid | tiv_2015 | tiv_2016 | lat | lon |
# +-----+----------+----------+-----+-----+
# | 1   | 10       | 5        | 10  | 10  |
# | 2   | 20       | 20       | 20  | 20  |
# | 3   | 10       | 30       | 20  | 20  |
# | 4   | 10       | 40       | 40  | 40  |
# +-----+----------+----------+-----+-----+
# Output: 
# +----------+
# | tiv_2016 |
# +----------+
# | 45.00    |
# +----------+
# Explanation: 
# The first record in the table, like the last record, meets both of the two criteria.
# The tiv_2015 value 10 is the same as the third and fourth records, and its location is unique.

# The second record does not meet any of the two criteria. Its tiv_2015 is not like any other policyholders and its location is the same as the third record, which makes the third record fail, too.
# So, the result is the sum of tiv_2016 of the first and last record, which is 45.


# Solution:

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # 1. Identify rows where tiv_2015 is NOT unique (count > 1)
    is_dup_tiv = insurance.groupby('tiv_2015')['tiv_2015'].transform('count') > 1
    
    # 2. Identify rows where (lat, lon) IS unique (count == 1)
    is_unique_loc = insurance.groupby(['lat', 'lon'])['lat'].transform('count') == 1
    
    # 3. Filter rows meeting BOTH criteria
    filtered_df = insurance[is_dup_tiv & is_unique_loc]
    
    # 4. Sum and round the result
    total_tiv_2016 = round(filtered_df['tiv_2016'].sum(), 2)
    
    return pd.DataFrame({'tiv_2016': [total_tiv_2016]})
