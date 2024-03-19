#Program to convert Number 2 Word

#Data
numberWords = {
    1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 
    10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
    16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty",
    30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty",
    90:"ninety", 100:"one-Hundred", 200:"two-Hundred", 300:"Three-Hundres", 400:"four-Hundred",
    500:"five-Hundred", 600:"six-Hundred", 700:"seven-Hundred", 800:"eight-Hundred", 
    900: "nine-Hundred", 1000:"One-Thousand", 1001:"One Thousand and one"
}

#User Input convert it into Integer
num = int(input("Enter your Number : "))

if num in numberWords:
        KeyValue = numberWords.get(num) #using get method to get the value for Key
        print(num, " In words is " + KeyValue)

elif num <= 100 :
    remainder = num % 10  
    remainder = numberWords.get(remainder)
    quotient = num // 10
    quotient = quotient * 10
    quotient = numberWords.get(quotient)
    result = quotient + remainder 
    print(num, " In words is : " + result)

elif num > 100:
       # Extract the digits
     ones_digit = num % 10
     ones_digit = numberWords.get(ones_digit) #here getting the value of one's digit
     tens_digit = (num // 10) % 10
     tens_digit = numberWords.get(tens_digit * 10)#here getting 10's digit and * 10 to get value
     hundred_digit = num // 100
     hundred_digit = numberWords.get(hundred_digit * 100)
     result = hundred_digit + " and " + tens_digit + " " + ones_digit
    #  result = hundred_digit + "-hundred and " + tens_digit + " " + ones_digit
     print(num, " In words is " + result)

else:
    print("Number is In-Valid")
 



