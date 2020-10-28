#this is simple Dictionary
a={"Man":"মানুষ","Hand":"হাত","Leg":"পা","Hair":"চুল","Nose":"নাক","Finger":"আঙ্গুল","Knee":"হাঁটু" ,"Eye":"চোখ","Teeth":"দাঁত ","Skin":"চামড়া"}
#user_input
b=input("enter your word\n")
#For_capital and smaller
c=b.capitalize()
#if_function
if c in a:
	print(c,"mean", a[c])
else:
	print("not available")
