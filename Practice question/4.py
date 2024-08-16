row1=['#','#','#']
row2=['#','#','#']
row3=['#','#','#']
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}" )
position=input("Enter the position where you want to hide :")
row=int(position[0])
coloum=int(position[1])
roww_selected=matrix[row-1]
roww_selected[coloum-1]='x'
print(f"{row1}\n{row2}\n{row3}" )