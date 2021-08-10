import matrix as mx

opt = input()

if opt == "add":
    mx.add()
elif opt == "scalMultiply":
    mx.scalar_multiply()
elif opt == "multiply":
    mx.multiply()
elif opt == "transpose":
    mx.transpose()
else:
    print("Invalid input")
