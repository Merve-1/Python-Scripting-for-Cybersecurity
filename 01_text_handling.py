line = "Name: Ada Burak "
name = "Ada"
print(line.strip())
print('-' * 40)

print(line.strip().split(": ")) 
print('-' * 40)

print(line.lower())
print('-' * 40)

print(line.replace("Ada", "Grace"))
print('-' * 40)


print(",".join(['a','b','c']))
print('-' * 40)

print("a,b,c".split(","))

price = 19.5
f"{price:.2f}" 
f"{1234567:,}"
print('-' * 40)

message= f"""
Dear {name},
Thanks for signing up 
"""
print(message)