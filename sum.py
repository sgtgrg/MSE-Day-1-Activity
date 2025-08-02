def sum_even_odd():
    number = input("Please put a positive integer number:")
    n = int(number)
    
    if n < 1:
        return "More a number greater than 0"
    
    else:
     sum_even = 0
     sum_odd = 0
     
     print("\n These are the even numbers:")
     i = 2
     while i <= n:
        print(",",i)
        sum_even = sum_even + i
        i += 2
     print("Sum of even numbers:", sum_even)
   
    print("\nThese are Odd numbers:")
    j = 1
    while j <= n:
        print(",", j)
        sum_odd = sum_odd + j
        j += 2
    print("Sum of odd numbers:", sum_odd)
    
    total = sum_even + sum_odd
    return total

if __name__ == "__main__":
    ans = sum_even_odd()
    print("\n Total Sum:", ans)
   