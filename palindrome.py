list=[1,2,1]
copy_list=list.copy()
copy_list.reverse()

if copy_list==list:
    print("Palindrome")
else:
    print('Not a Palindrome')