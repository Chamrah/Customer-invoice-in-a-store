#Customer invoice in a store
s1=0
s2=0
s3=0
TVA1=0
TVA2=0
TVA3=0
TTC1=0
TTC2=0
TTC3=0
name1=0
name2=0
name3=0
for i in range(1,4):
    n=input(f"Give the customer's first name and last name N{i} : ")
    c=int(input(f"Give the number of items for the customer N{i} : "))
    for j in range(1,c+1):
        p=float(input("Give the price of the item : "))
        if(i==1):
           name1=n
           s1=s1+p
           TVA1=s1*0.15
           TTC1=s1+TVA1-(s1*0.02)
        elif(i==2):
            name2=n
            s2=s2+p
            TVA2=s2*0.15
            TTC2=s2+TVA2-(s2*0.02)
        else:
            name3=n
            s3=s3+p
            TVA3=s3*0.15
            TTC3=s3+TVA3-(s3*0.02)


print(f"The Total to be paid to the customer {name1} is :{TTC1} DH")
print(f"The Total to be paid to the customer {name2} is :{TTC2} DH")
print(f"The Total to be paid to the customer {name3} is :{TTC3} DH")

