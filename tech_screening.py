def sort(width, height, length, mass):
    bulky = False
    heavy = False
    dimension = [width, height, length]
    volume = width * height * length
    if volume >= 1000000 or any(dimension) >= 150:
        bulky = True
    
    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return "REJECTED"
    if bulky and not heavy:
        return "SPECIAL"
    if not bulky and heavy:
        return "SPECIAL"
    if not bulky and not heavy:
        return "STANDARD"

test1 = sort(10, 100, 100, 10)
test2 = sort(100,100,100, 10)
test3 = sort(150,100,100, 10)
test4 = sort(100,10,10, 20)
test5 = sort(100,100,100, 20)
test6 = sort(150, 100, 100, 20)

if test1 == "STANDARD":
    print(f"Test 1 passed stacked returned: {test1}")

if test2 == "SPECIAL":
    print(f"Test 2 passed stacked returned: {test2}")

if test3 == "SPECIAL":
    print(f"Test 3 passed stacked returned: {test3}")

if test4 == "SPECIAL":
    print(f"Test 4 passed stacked returned: {test4}")

if test5 == "REJECTED":
    print(f"Test 5 passed stacked returned: {test5}")

if test6 == "REJECTED":
    print(f"Test 6 passed stacked returned: {test6}")