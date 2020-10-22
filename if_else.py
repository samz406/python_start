def p_out(name):
    print("Hi {0}".format(name))


def age_type(age):
    if age < 10:
        print('you are little son')
    elif age <= 20:
        print('You are yong son')
    elif age <= 30:
        print ("you are qingnian son")
    elif age <= 45:
        print ("you are middle son")
    else:
        print ("you enter error ")


def f():
    for a in ["a","b","c"]:
        print a

def dic():
    d = {"name": "lilin", "age": 10, "sex": "male"}
    print(d)
    print (d["name"])
    del d["name"]
    print (d["age"])

if __name__ == '__main__':
    # p_out("samz")
    # age_type(10)
    # age_type(19)
    # age_type(22)
    # age_type(31)
    # age_type(50)
    f()