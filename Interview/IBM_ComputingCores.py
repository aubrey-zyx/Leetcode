def getMinCost(n, k, plans):
    def get_available_plans(day, plans):
        available = []
        for plan in plans:
            l, r = plan[0], plan[1]
            if l <= day <= r:
                available.append(plan[2:])
        available.sort(key=lambda x: x[1])
        return available

    def calculate_cost(available, k):
        cost = 0
        remain = k
        i = 0
        while remain > 0 and i < len(available):
            c, p = available[i][0], available[i][1]
            if c >= remain:
                cost += remain * p
                break
            cost += c * p
            remain -= c
            i += 1
        return cost

    min_cost = 0
    for day in range(n):
        available = get_available_plans(day + 1, plans)
        today_cost = calculate_cost(available, k)
        print("Day {}: {}".format(day + 1, today_cost))
        min_cost += today_cost

    return min_cost

n = 5
k = 7
plans = [[1, 3, 5, 2], [1, 4, 5, 3], [2, 5, 10, 1]]

print(getMinCost(n, k, plans))