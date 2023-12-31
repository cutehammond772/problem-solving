import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
MAX = int(1e6)

def primes(N):
	check = [True] * (N + 1)
	check[0] = check[1] = False

	for num in range(2, int(N ** 0.5) + 1):
		if not check[num]:
			continue

		for next in range(num * 2, N + 1, num):
			check[next] = False

	nums = [x for x in range(2, N + 1) if check[x]]

	return check, nums

if __name__ == '__main__':
	T = int(input())
	check, nums = primes(MAX)

	for i in range(1, T + 1):
		N, M = map(int, input().split())

		A = [*map(int, input().split())]
		B = [*map(int, input().split())]

		# +: 분자, -: 분모
		memo = defaultdict(int)

		for num in A:
			current, end = num, int(num ** 0.5)

			for x in range(len(nums)):
				if current == 1:
					break

				if nums[x] > end or check[current]:
					memo[current] += 1
					break

				while not (current % nums[x]):
					memo[nums[x]] += 1
					current //= nums[x]

		for num in B:
			current, end = num, int(num ** 0.5)

			for x in range(len(nums)):
				if current == 1:
					break

				if nums[x] > end or check[current]:
					memo[current] -= 1
					break

				while not (current % nums[x]):
					memo[nums[x]] -= 1
					current //= nums[x]

		a, b = 1, 1

		for x in memo:
			if memo[x] > 0:
				a *= x ** memo[x]

			if memo[x] < 0:
				b *= x ** -memo[x]

		print(f"Case #{i}: {a} / {b}")
