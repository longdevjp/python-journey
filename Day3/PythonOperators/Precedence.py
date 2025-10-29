# Dấu ngoặc đơn có mức độ ưu tiên cao nhất, nghĩa là các biểu thức bên trong dấu ngoặc đơn phải được đánh giá trước
print((6 + 3) - (6 + 3))

# Phép nhân *có mức độ ưu tiên cao hơn phép cộng +, do đó phép nhân được thực hiện trước phép cộng:
print(6 + 3 * 2)

'''
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
'''
# Nếu hai toán tử có cùng độ ưu tiên, biểu thức sẽ được đánh giá từ trái sang phải.
print(5 + 4 - 7 + 3)