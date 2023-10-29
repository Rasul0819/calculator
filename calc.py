import tkinter

window = tkinter.Tk()
window.geometry('500x700')
window.title('Calculator')
window.config(bg='black')

def create_btn(symbol,fgcolor='black',bgcolor='white'):
	return tkinter.Button(
		text=symbol,
		font='Impact 16',
		fg =fgcolor,
		bg=bgcolor,
		border=0
		 )	
entryfield = tkinter.Entry(
	font='Impact 25',

	)
entryfield.pack(pady=20)

clear_btn = create_btn(symbol='C',fgcolor='lime',bgcolor='#0a0a14')
clear_btn.place(x=10,y=100,width=50,height=50)

window.mainloop()