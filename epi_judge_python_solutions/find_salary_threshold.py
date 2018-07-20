from test_framework import generic_test


def find_salary_cap_brute(target_payroll, current_salaries):
    current_salaries.sort()
    if sum(current_salaries) == target_payroll:
        return current_salaries[-1]
    if sum(current_salaries) < target_payroll:
        return -1
    print("Current: " + str(target_payroll) + ", Sum: " + str(sum(current_salaries)) + ", Target: " + str(target_payroll))
    current_cap = 1
    while(current_cap <= target_payroll):
        temp_salaries = []
        for val in current_salaries:
            if val > current_cap:
                temp_salaries.append(current_cap)
            else:
                temp_salaries.append(val)
        print(sum(temp_salaries))
        if sum(temp_salaries) >= target_payroll:
            return current_cap
        else:
            current_cap += 1
            #print("Bumping up current cap to: " + str(current_cap))
    return current_cap



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap_brute))
