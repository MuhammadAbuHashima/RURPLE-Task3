nums = []*10
output = []
N = 3

print("Enter any 10 integer numbers to determine which of them are divisible by 3", "\n")

while len(nums) < 10:
    x = int(input())
    nums.append(x)

def mod(a, b):
    for ctr in a:
        if ctr % b == 0:
            output.append(ctr)

mod(nums, N)

print("\n")
print("The numbers in", nums, "which are divisible by", N, "are:")
print(output, "\n")