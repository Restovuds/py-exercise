def fibonacci():
    results = [0, 1,]

    def get_n(n):
        if n <= len(results):
            return results[n-1]

        for i in range(len(results), n):
            next_number = results[i - 1] + results[i - 2]
            results.append(next_number)

        return results[n-1]
    return get_n


fibo = fibonacci()
for i in range(1, 100):
    print(fibo(i))
