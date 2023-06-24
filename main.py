def total_expenses_by_category(filename: str):
    res = {}
    with open(filename, encoding='utf-8') as file:
        for line in file:
            *_, money, category = line.strip().split()
            money = float(money.replace('$', ''))
            if category in res:
                res[category] += money
            else:
                res[category] = money
    return res
def total_expenses(filename: str):
    res = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            *_, money, category = line.strip().split()
            money = float(money.replace('$', ''))
            res += money
    return res



if __name__ == '__main__':
    print(total_expenses_by_category('hw_10_test.txt'))
    print(total_expenses('hw_10_test.txt'))