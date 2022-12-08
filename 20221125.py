from tkinter import*  #모듈삽입하는부분
import random
from tkinter import messagebox
import pandas as pd
korean=pd.read_csv("c:\한식.csv")       #c드라이브에서 한식 리스트 파일 불러오기
chinese=pd.read_csv("c:\중식.csv")      #c드라이브에서 중식 리스트 파일 불러오기
western=pd.read_csv("c:\양식.csv")      #c드라이브에서 양식 리스트 파일 불러오기
japanese=pd.read_csv("c:\일식.csv")     #c드라이브에서 일식 리스트 파일 불러오기
allrest=pd.read_csv("c:\통합.csv")      #c드라이브에서 통합음식점 리스트 파일 불러오기

window = Tk()           #gui창 만들기
window.title("음식점 추출 프로그램")  #프로그램 제목 삽입
window.geometry("300x150")      #창크기설정
information1=korean[["업소명","대표메뉴(가격)","전화번호","주소"]]  #한식파일에서 불러올 index 매개 변수로 선언하기
information2=chinese[["업소명","대표메뉴(가격)","전화번호","주소"]] #중식파일에서 불러올 index 매개 변수로 선언하기
information3=western[["업소명","대표메뉴(가격)","전화번호","주소"]] #양식파일에서 불러올 index 매개 변수로 선언하기
information4=japanese[["업소명","대표메뉴(가격)","전화번호","주소"]]  #일식파일에서 불러올 index 매개 변수로 선언하기

def random1():    
    messagebox.showinfo("랜덤추천",random.choice(allrest["업소명"]))  #랜덤함수 만들기 -> 버튼을 누르면 통합음식점리스트중에 랜덤으로 업소명이 추출

def eat1():             #한식버튼을 누르면 새 창에 한식리스트가 출력
    global new
    new= Toplevel()
    i=Label(new,text=information1)
    i.pack()

def eat2():             #중식버튼을 누르면 새 창에 한식리스트가 출력
    global new
    new= Toplevel()
    i=Label(new,text=information2)
    i.pack()
  

def eat3():             #양식버튼을 누르면 새 창에 한식리스트가 출력
    global new
    new= Toplevel()
    i=Label(new,text=information3)
    i.pack()

def eat4():             #일식버튼을 누르면 새 창에 한식리스트가 출력
    global new
    new= Toplevel()
    i=Label(new,text=information4)
    i.pack()
    

b1=Button(window,text="한식",command=eat1)      #버튼설정(텍스트는 "한식",클릭시 eat1함수 실행)
b2=Button(window,text="중식",command=eat2)      #버튼설정(텍스트는 "중식",클릭시 eat2함수 실행)
b3=Button(window,text="양식",command=eat3)      #버튼설정(텍스트는 "양식",클릭시 eat3함수 실행)
b4=Button(window,text="일식",command=eat4)      #버튼설정(텍스트는 "일식",클릭시 eat4함수 실행)
b5=Button(window,text="추천받기",command=random1)   #버튼설정(텍스트는 "한식",클릭시 random1함수 실행)

b1.place(x=50, y=40)    #버튼들의 위치조정
b2.place(x=100 ,y=40)
b3.place(x=150 ,y=40)
b4.place(x=200 ,y=40)
b5.place(x=110, y=90)

window.mainloop()   #실행
