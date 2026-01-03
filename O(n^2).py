def OnSquareTime(n):
    iteration = 0 

    for i in range(0 , n):
        for j in range(0 , n):
            iteration = iteration + 1

        print("")

    print("\n when n is" , n , "Iterations = " , iteration)

OnSquareTime(5)
OnSquareTime(4)
OnSquareTime(3)