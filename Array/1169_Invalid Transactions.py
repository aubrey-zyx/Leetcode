class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ht = {}
        invalid = set()
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            if int(amount) > 1000:
                invalid.add(i)
            if name not in ht:
                ht[name] = []
            else:
                prev = ht[name]
                for j in range(len(prev)):
                    prev_name, prev_time, prev_amount, prev_city = transactions[prev[j]].split(",")
                    if abs(int(time) - int(prev_time)) <= 60 and city != prev_city:
                        invalid.add(i)
                        invalid.add(prev[j])
            ht[name].append(i)
        return [transactions[i] for i in invalid]


class Solution2:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        ht = defaultdict(dict)
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            if name not in ht[time]:
                ht[time][name] = {city}
            else:
                ht[time][name].add(city)

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            if int(amount) > 1000:
                invalid.append(transaction)
                continue
            for inv_time in range(time - 60, time + 61):
                if inv_time in ht and name in ht[inv_time]:
                    city_set = ht[inv_time][name]
                    if city not in city_set or len(city_set) > 1:
                        invalid.append(transaction)
                        break
        return invalid