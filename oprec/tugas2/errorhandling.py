errors = [
    "Container descent rate failure",
    "Science Payload descent rate failure",
    "Container position failure",
    "Science Payload position failure",
    "Release failure"
]

x = int(input())
binary = format(x, '05b')

a = []
for i in range(5):
    if binary[4 - i] == '1':
        a.append(errors[i])

if a:
    print(", ".join(a))
else:
    print("No error")