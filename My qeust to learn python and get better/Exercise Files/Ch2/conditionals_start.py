#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if (x > y) :
        st = "x is greater than Y"
    elif (x==y):
        st = "x the same to Y"
    else:
        st = "Y is greater than x"
    
    print(st)    
    
    st = "x is greater than y" if(x>y) else "Y is greater than x"
    
    print(st)

    # conditional statements let you use "a if C else b"


if __name__ == "__main__":
    main()
