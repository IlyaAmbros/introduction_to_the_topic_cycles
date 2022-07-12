start_n = 1
end_n = 10
print ( "Enter the starting and ending numbers in any sequence : " , start_n , " or " , end_n )
entered_number_1 = int ( input ( "Enter the first value = " ) )
entered_number_2 = int ( input ( "Enter the second value = " ) )
if entered_number_1 == start_n and entered_number_2 == end_n :
        while start_n <= 10:
                print(start_n)
                start_n += 1
if entered_number_1 == end_n and entered_number_2 == start_n :
        while 1 <= end_n:
                print (end_n)
                end_n -= 1
