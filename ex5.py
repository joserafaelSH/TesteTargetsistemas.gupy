def reverseString(str_: list, start:int, end:int) -> list:

    if start < end:
        if start == end:
            return str_
        
        else:
            str_[start],str_[end] = str_[end],str_[start]
            return reverseString(str_, start+1,end-1)
    
    else:
        return str_


    

def main():
    assert("".join(reverseString(list("Cat"),0,len("Cat")-1))) == "taC"
    assert("".join(reverseString(list("civic"),0,len("civic")-1))) == "civic"
   
if __name__ == "__main__":
    main()
