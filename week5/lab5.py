import sys
 #for part C
 #Part B
#1
def trimmed_max(xs, y):
    xs.sort(reverse=True)
    for value in xs:
        if value < y:
            return value
    return None
#2
def normalize_spaces(text):
    return ' '.join(seq for seq in text.split(' ') if len(seq) >0)
    
#3
t = ['Nr', '37', ':', 'So', 'excited', '!', ':','!','!', 'The', 'Pointer', 'Sisters'," ", '','i21!']
def alphanum_tokens(t):
    i=0
    while i < len(t):
        if not t[i].isalnum():
            t.remove(t[i])
        else:
            i+=1
    print(t)
#Part C
def sticks_triangles():
    if(len(sys.argv) > 4):
        print("You provided more than 3 arguments")
        return
    elif(len( sys.argv) ==1 ):
        len_stick1 = int(input("please Enter lengths of stick1 "))
        len_stick2 = int(input("please Enter lengths of stick2 "))
        len_stick3 = int(input("please Enter lengths of stick3 "))
    elif (len(sys.argv) == 2):
        len_stick1 = int (sys.argv[1])
        len_stick2 = int(input("please Enter lengths of stick2 "))
        len_stick3 = int(input("please Enter lengths of stick3 "))
    elif (len(sys.argv) == 3):
        len_stick1 = int (sys.argv[1])
        len_stick2 = int (sys.argv[2])
        len_stick3 = int(input("please Enter lengths of stick3 "))
    elif (len(sys.argv) == 4):
        len_stick1 = int (sys.argv[1])
        len_stick2 = int (sys.argv[2])
        len_stick3 = int (sys.argv[3])  

    if len_stick1 > len_stick2+len_stick3 or len_stick2 > len_stick1+len_stick3 or len_stick3 > len_stick1+len_stick2:
        print("No")
    if len_stick1 == len_stick2+len_stick3 or len_stick2 == len_stick1+len_stick3 or len_stick3 == len_stick1+len_stick2:
        print("They form a degenerate triangle")
    else:
        print("Yes")
#Main function                
def main():
    print(trimmed_max([-3,5,-0.1,-100,1,5000],0))  #1
    print(normalize_spaces("        what           is this              What's  up   ")) #2
    alphanum_tokens(t) #3
    sticks_triangles() #partc

if __name__ == '__main__':
    main()