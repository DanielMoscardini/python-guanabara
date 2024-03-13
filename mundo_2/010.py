# receba 6 numeros inteiros e some apenas os pares.
nums = []
pares = 0
for i in range(0, 6):
    nums.append(int(input(f'Digite o {i + 1}ª numero: ')))

for i in range(0, len(nums)):
    if nums[i] % 2 == 0:
        pares += nums[i]

print(nums)
print(f'A soma dos numeros pares eh: {pares}')
