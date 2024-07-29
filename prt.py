def greeting():
    fname = input("what is your first name? ").title().strip()
    sname = input("what is your surname? ").title().strip()
    sex = input("what is your gender? ")
    if sex == "male" :
        print(f"hello, welcome Mr. {sname} {fname}")
    elif sex == "female" :
        print(f"hello, welcome Mrs. {sname} {fname}")
    else:
        print(f"enter a valid gender ")
        
greeting()
    