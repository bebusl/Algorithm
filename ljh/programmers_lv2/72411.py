from itertools import combinations

def solution(orders, course):
    for order,idx in orders:
        print(order, idx)
        tmp_orders[idx] = tmp_orders.sort()
    print(tmp_orders)


tmp_orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(tmp_orders, course))