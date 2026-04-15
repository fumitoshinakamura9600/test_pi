#Tkinterを使う
import tkinter

#キャプションを変更
def changeCaption( text , val ):
    root.title( text + "(" + str( val ) + ")")

#ボタンクリック時の振る舞い
def onClickButton():
    changeCaption( textbox.get(), slider.get() )

#スライダー変更時の振る舞い
def onChangeSlider( event ):
    changeCaption( textbox.get(), slider.get() )

# メインウィンドウ
root = tkinter.Tk()
root.title("Hello World from Tkinter")

#ボタンをメインウィンドウの（30，10）に配置
#ボタンがクリックされたときにonClickButton関数を呼び出す
button = tkinter.Button( root, text = "Press Me!", command = onClickButton)
button.place( x=30, y=10 )

#テキスト入力欄（Entry)を追加
textbox = tkinter.Entry( root )
textbox.place( x=120, y=10 )

#スライダー(Scale)を追加
slider = tkinter.Scale(
    root, 
    orient = tkinter.HORIZONTAL,
    from_ = -100, to=100,
    resolution = 10,
    length = 250,
    width = 15,
    command = onChangeSlider
)

slider.set(20);
slider.place(x=30, y=50)


root.mainloop()
