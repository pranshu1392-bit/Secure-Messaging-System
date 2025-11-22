q=["Q1. Name of the national fruit of India?\n", "Q2. Which is the longest river in India?\n", "Q3. National animal of India?\n", "Q4. National tree of india\n", "Q5. Current Prime Minister of India\n", "Q6. How many states are there in India?\n", "Q7. How many hours are there in 1 day?\n", "Q8. How many seconds in 1 hour?\n"]
opt=["(a)Apple            (b)Mango\n (c)Banana           (d)Grapes", "(a)Ganga                (b)Brahamaputra\n (c)Narmada              (d)Nile", "(a)Lion                   (b)Elephant\n (c)Tiger                     (d)Giraffe", "(a)Mango Tree                         (b)Banana Tree\n (c)Apple Tree                       (d)Banayan Tree", "(a)Mr. Narendra Modi                         (b)Mr. Donald Trump\n (c)Mr.Vladimir Putin                        (d)Mr. Xi Jingping", "(a)27                      (b)28\n (c)29                      (d)26", "(a)23                          (b)24\n (c)25                           (d)26", "(a)3500                          (b)3600\n (c)3700                           (d)3800"]
ans=["b", "a", "c", "d", "a", "c", "b", "b"]
points=["5000rs", "15000rs", "50000rs", "100000rs", "200000rs", "400000rs", "800000rs", "1600000rs"]
for i in range(8):
    print(q[i], opt[i])
    input("")
    answer=input("Enter the answer : ")
    if(answer==ans[i]):
        print("Correct Answer")
        print("Money earned : ", points[i])
    else:
        print("Wrong answer")
        print("Game Over")
        break