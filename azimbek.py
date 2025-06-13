from random import randint




print("\t\t\t==== Interaktiv Topshiriqlar ====")
print('''
1. 🎯 Maxfiy sonni toping (Random son o‘yini)
2. 🔄 So‘zni teskari yozish
3. 🔢 Sonlar orasidagi eng kichigini topish
4. 🧮 FizzBuzz o‘yini (1 dan N gacha)
0. ❌ Dasturdan chiqish
=============================================
 ''')
main=int(input("Menyulardan birini tanlang:"))
a=(f"Siz {main} menyuni tanladingiz")

if main==1:
    print(a)
    

    a = randint(1,20)
    print("random son:",a)
    soni=0
    while soni<5:
        soni+=1
        b=int(input("Sonni kiriting: "))
        if b==a:
            print("Sonlar mos keldi")
            break
        else:
            print("Yana urinib ko‘ring")


elif main==2:
    print(a)
    text=input("matn kiriting: ")
    a=len(text)
        # for i in range(a):
        #   print(text[a-i-1])
    b=0
    while b<a:
        a-=1
        print(text[a],end="")

        # while hamda for orqali ishlandi
    

elif main==3:
    print(a)
    
    n=int(input("birinchi sonni kiriting: \n"))
    for a in range(4):
        son=int(input())

        if n>son:
            n=son
        
    print("eng kichik son",n)

elif main==4:
    print(a)
    number=int(input("sonni kiriting: "))
 
    for i in range(1,number):
        if i%3==0 and i%5==0:
            print("Fizzbuzz")
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizz")
        else:
            print(i)

elif main==0:
    print(a)
    a=0
    while True:
        b=int(input("Sonni kiriting: "))

        if b==a:
            print("Dastur yakunlandi.Xayr!")
            break
        else:
            print("Yana urinib ko‘ring")
else:
    print("notug'ri menyu tanladingiz")