nums = [i for i in range(0, 11, 1)]
print(nums)
search = tuple(filter(lambda x: x % 2 == 1, nums))
print(search)
looking = list(filter(lambda x: x > 5, nums))
print(looking)
purifing = list(filter(lambda x: 2 < x < 8, nums))
print(purifing)

