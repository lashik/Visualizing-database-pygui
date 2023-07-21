from tkinter import *
import tksvg 
from mprmls import *
from PIL import Image, ImageTk
#basic setup
main_window=Tk()
ml=LinkedList
main_window.title("MPR Python")
main_window.config(bg='#1E1E1E')
main_window.geometry("1300x715")
menu_img=PhotoImage(file='truemenu.png')
#basic setup end
#functions used in the program
class AnimatedGif:
    def __init__(self, master, filename,gif_width,gif_height):
        self.master = master
        self.filename = filename
        self.gif = Image.open(filename)
        self.gif_frames = []
        try:
            while True:
                self.gif_frames.append(ImageTk.PhotoImage(self.gif))
                self.gif.seek(len(self.gif_frames))
        except EOFError:
            pass
        self.current_frame = 0
        self.canvas = Canvas(master, width=gif_width, height=gif_height)
        self.canvas.pack()
        x=self.gif_frames[0]
        self.canvas.create_image(0,0,anchor='nw', image=x)
        self.animate()

    def animate(self):
        self.current_frame += 1
        if self.current_frame == len(self.gif_frames):
            self.canvas.destroy()
        self.canvas.itemconfig(1, image=self.gif_frames[self.current_frame])
        self.master.after(75, self.animate)

def roundPolygon(x, y, sharpness, **kwargs):
    if sharpness < 2:
        sharpness = 2
    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness
    points = []
    for i in range(len(x)):
    
        points.append(x[i])
        points.append(y[i])
        if i != (len(x) - 1):
            points.append((ratioMultiplier*x[i] + x[i + 1])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[i + 1])/ratioDividend)
            points.append((ratioMultiplier*x[i + 1] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[i + 1] + y[i])/ratioDividend)
        else:
            
            points.append((ratioMultiplier*x[i] + x[0])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[0])/ratioDividend)
            points.append((ratioMultiplier*x[0] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[0] + y[i])/ratioDividend)
           
            points.append(x[0])
            points.append(y[0])
    return main_canvas.create_polygon(points, **kwargs, smooth=TRUE)
eh,lh,el,ll,eb,lb,em,lm=0,0,0,0,0,0,0,0
def close_win(e):
   main_window.destroy()

def enter_hash(e):
    main_canvas.delete(lh)
    eh=roundPolygon([61.6, 272.6, 272.6, 61.6], [198, 198, 505, 505], 8 , width=8, outline="white",fill="#1E1E1E")
def left_hash(e):
   main_canvas.delete(eh)
   lh=roundPolygon([61.6, 272.6, 272.6, 61.6], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
   

def enter_ls(e):
    main_canvas.delete(ll)
    el=roundPolygon([292.2, 598.2, 598.2, 292.2], [198, 198, 505, 505], 8 , width=8, outline="white",fill="#1E1E1E")   
def left_ls(e):
   main_canvas.delete(el)
   ll=roundPolygon([292.2, 598.2, 598.2, 292.2], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
   

def enter_bst(e):
    main_canvas.delete(lb)
    eb=roundPolygon([637.8, 924.8, 924.8, 637.8], [198, 198, 505, 505], 8 , width=8, outline="white",fill="#1E1E1E")      
def left_bst(e):
    main_canvas.delete(eb)
    lb=roundPolygon([637.8, 924.8, 924.8, 637.8], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")


def enter_mls(e):
    main_canvas.delete(lm)
    em=roundPolygon([966.4,1253.4,1253.4,966.4], [198, 198, 505, 505], 8 , width=8, outline='white',fill="#1E1E1E")
    
def left_mls(e):
   main_canvas.delete(em)
   lm=roundPolygon([966.4,1253.4,1253.4,966.4], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
            
#function used in the program end

#configuration for buttons
y=25

main_canvas = Canvas(
    main_window,
    bg='#1E1E1E',
    height= 715,
    width=1300,
    bd=0,
    highlightthickness=0,
    relief='ridge',
)
main_canvas.place(x=0,y=0)
bg=tksvg.SvgImage(file='blob-scene-haikei (1).svg')
main_canvas.create_image(0,0,anchor='nw',image=bg)
main_canvas.create_text(
    300.5,
    30,
    anchor='nw',
    text='Visualizing Data Structures',
    fill='#000000',
    font=('Poppins',46)
)

main_canvas.create_text(
    300.5,
    20,
    anchor='nw',
    text="Visualizing Data Structures",
    fill='#FFFFFF',
    font=('Poppins',46)
)


menu_but=Button(main_canvas, #0
    text='',
    image=menu_img,
    borderwidth=0,
    bg='#1E1E1E',
    activebackground='#1E1E1E',
    activeforeground='#1E1E1E',
    relief='sunken'
)

hash_but=Button(
    text='    Hash Table   \n\n\n\n\n',
    borderwidth=0,
    bg='#1E1E1E',
    activebackground='#1E1E1E',
    activeforeground='#1E1E1E',
    relief='sunken',
    font=("Poppins",y*-1),
    fg='white',
    command=lambda :hash_win()
)
hash_descript=Label(
    text='In a Hash table, keys\nare mapped to array \npositions by a hash \nfunction.',
    background="#1E1E1E",
    border=0,
    font=('Poppins Bold',16*-1),
    fg="white",
    justify=LEFT
)
bst_but=Button(main_canvas,
    text='Binary Search Tree   \n\n\n\n\n',
    borderwidth=0,
    bg='#1E1E1E',
    activebackground='#1E1E1E',
    activeforeground='#1E1E1E',
    relief='sunken',
    font=("Poppins",y*-1),
    fg='white',
    command=lambda :bst_win()
)
bst_descript=Label(
    text='In a binary search tree, the \nnodes are arranged in an \nefficient order.',
    background="#1E1E1E",
    border=0,
    font=('Poppins Bold',18*-1),
    fg="white",
    justify=LEFT
)

ls_but=Button(main_canvas,
    text='    Sequential Search    \n\n\n\n\n',
    borderwidth=0,
    bg='#1E1E1E',
    activebackground='#1E1E1E',
    activeforeground='#1E1E1E',
    relief='sunken',
    font=("Poppins",y*-1),
    fg='white',
    command=lambda :ls_win()
)
ls_descript=Label(
    text='In Indexed Sequential Search \nrecords are mapped to a \nprimary key by an index value.',
    background="#1E1E1E",
    border=0,
    font=('Poppins Bold',18*-1),
    fg="white",
    justify=LEFT
)
mls_but=Button(main_canvas,
    text='Multi-Level Search   \n\n\n\n\n',
    borderwidth=0,
    bg='#1E1E1E',
    activebackground='#1E1E1E',   
    activeforeground='#1E1E1E',
    relief='sunken',
    font=("Poppins",y*-1),
    fg='white',
    command=lambda :mls_win()
)
mls_descript=Label(
    text='Multilevel Search is a 2D data \nstructure in which each node \nhas a next and child pointer.',
    background="#1E1E1E",
    border=0,
    font=('Poppins Bold',18*-1),
    fg="white",
    justify=LEFT
)



#configuration for buttons end
butpack_x=20
butpack_y=114
def win_enter_hash(e):
    x=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="white",fill="#1E1E1E")
def win_left_hash(e):
    x=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")

def win_enter_ls(e):
    a1=butpack_y+93+17.75
    x=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="white",fill="#1E1E1E")   
def win_left_ls(e):
    a1=butpack_y+93+17.75
    x=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")

def win_enter_bst(e):
    a1=butpack_y+(93*2)+(17.75*2)
    x=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="white",fill="#1E1E1E")      
def win_left_bst(e):
    a1=butpack_y+(93*2)+(17.75*2)
    x=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")

def win_enter_mls(e):
    a1=butpack_y+(93*3)+(17.75*3)
    x=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="white",fill="#1E1E1E")
def win_left_mls(e):
    a1=butpack_y+(93*3)+(17.75*3)
    x=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")




def hash_win(): 
        
        win_canvas=Canvas(
                bg='#1E1E1E',
                height= 443,
                width=931,
                bd=0,
                highlightthickness=0,
                relief='ridge',
        )
        win_canvas.place(x=326,y=114)  
            
        global selected_option
        selected_option=0     
        def ins_active():
            global selected_option
            selected_option=1
            active_photo1.configure(file='active.svg')
            insert_check.configure(command=ins_inactive)
            print(selected_option)
            
        def ins_inactive():
            global selected_option
            selected_option=-1
            active_photo1.configure(file='inactive.svg')
            insert_check.configure(command=ins_active)
            print(selected_option)
            
        def ups_active():
            global selected_option
            selected_option=2
            active_photo2.configure(file='active.svg')
            update_check.configure(command=ups_inactive)
            print(selected_option)
            
        def ups_inactive():
            global selected_option
            selected_option=-1
            active_photo2.configure(file='inactive.svg')
            update_check.configure(command=ups_active)
            print(selected_option)
            
        def dels_active():
            global selected_option
            selected_option=3
            active_photo3.configure(file='active.svg')
            delete_check.configure(command=dels_inactive)
            print(selected_option)
            
        def dels_inactive():
            global selected_option
            selected_option =-1
            active_photo3.configure(file='inactive.svg')
            delete_check.configure(command=dels_active)
            print(selected_option)

        insert_check = Button(
            win_canvas,
            image=active_photo1,
            command=ins_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        insc_text = Label(
            win_canvas,
            text="Append",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        update_check = Button(
            win_canvas,
            image=active_photo2,
            command=ups_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        upc_text = Label(
            win_canvas,
            text="Update",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        delete_check = Button(
            win_canvas,
            image=active_photo3,
            command=dels_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        delc_text = Label(
            win_canvas,
            text="Delete",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        et_key=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_wei=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_qua=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_pri=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_name=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )  
        lb_wei=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Weight",
        )
        lb_name=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Name"
        )
        lb_key=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Key"
        )
        lb_pri=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Price"
        )
        lb_qua=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Quality",
        )   

        disp_canvas=Canvas(
             bg='#1E1E1E',
                        height= 180,
                        width=701,
                        bd=0,
                        highlightthickness=0,
                        relief='ridge',
                        
                        )
        has_animation=AnimatedGif(disp_canvas,'hashin.gif',628,280)
        disp_canvas.configure(height=180)
        def submit():
            global selected_option
            #result=StringVar(disp_canvas)
            with open('randomnum.txt') as f:
                for line in f.readlines():
                    x=line.split()
                    #print("iweadifasdi",x[4:len(x)])
                    x1=x[4:len(x)]
                    pname = ' '.join([str(elem) for elem in x1])
                    
                    #result.setresult+x[1]+" "+x[3]+" "+x[2]+" "+pname+" "+x[0]+"\n"
            #print(result)
            print(selected_option)
            if selected_option==1:
                        #result=et_wei.get()+" "+et_qua.get()+" "+et_pri.get()+" "+et_name.get()+" "+et_key.get()+"\n"
                        et_wei.delete(0,END)
                        et_qua.delete(0,END)
                        et_pri.delete(0,END)
                        et_name.delete(0,END)
                        et_key.delete(0,END)
                        disp_canvas.create_text(50,50,justify=LEFT,text="""101001 20 54.95 15 TELEPHOTO POCKET CAMERA 
                                                                            101002 12 24.95 15 MINI POCKET CAMERA 
                                                                            102001 20 49.95 10 POL. ONE-STEP CAMERA 
                                                                            102002 13 189.95 12 SONAR 1-STEP CAMERA 
                                                                            102003 15 74.95 5 PRONTO CAMERA 
                                                                            103002 15 310.55 10 SOUND/ZOOM 8MM CAMERA 
                                                                            104001 10 389.00 12 35MM SLR XG-7 MINO. CAM. 
                                                                            104002 11 349.95 12 35MM SLR AE-1 PENT. CAM. 
                                                                            104003 20 319.90 12 35MM SLR ME CAN. CAM. 
                                                                            104101 13 119.95 12 35MM HI-MATIC CAMERA 
                                                                            104102 20 89.99 12 35MM COMPACT CAMERA 
                                                                            151001 7 129.95 5 ZOOM MOVIE PROJECTOR 
                                                                            151002 9 239.99 5 ZOOM-SOUND PROJECTOR 
                                                                            152001 10 219.99 5 AUTO CAROUSEL PROJECTOR 
                                                                            152002 4 114.95 5 CAR. SLIDE PROJECTOR
                                                                            201001 4 14.95 5 POCKET STROBE
                                                                            201002 12 48.55 10 STROBE SX-10
                                                                            201003 10 28.99 15 ELEC. FLASH SX-10
                                                                            301001 13 32.99 15 TELE CONVERTER 14 2100508
                                                                            301002 14 97.99 15 28MM WIDE-ANGLE LENS 
                                                                            301003 13 87.95 15 135MM TELEPHOTO LENS 
                                                                            301004 8 267.95 5 35-105 MM ZOOM LENS 
                                                                            301005 7 257.95 5 80-200 MM ZOOM LENS 
                                                                            311001 4 67.50 5 HEAVY-DUTY TRIPOD 21 2006GB
                                                                            311002 10 19.95 5 LIGHTWEIGHT TRIPOD T2200568 
                                                                            351001 10 159.99 5 35MM ENLARGER KIT
                                                                            401001 4 35.98 5 40X40 DELUXE SCREEN 
                                                                            401002 10 44.98 5 50X50 DELUXE SCREENS 
                                                                            501001 17 4.29 25 120-SLIDE TRAY
                                                                            501002 33 2.95 25 100-SLIDE TRAY
                                                                            502001 12 6.25 15 SLIDE VIEWER
                                                                            503001 12 55.95 10 MOVIE EDITOR
                                                                            601001 10 59.95 5 CONDENSER MICROPHONE 
                                                                            611001 80 0.89 100 AA ALKALINE BATTERY 
                                                                            701001 19 19.79 20 GADGET BAG 
                                                                            801001 45 1.49 50 135-24 COLOR FILM 
                                                                            802001 60 0.99 50 110-12 COLOR FILM 
                                                                            802002 42 1.45 50 110-24 COLOR FILM""",fill="white")
            elif selected_option==2:
                        if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                        else:
                            x1.update(et_wei.get(),et_qua.get(),et_pri.get(),et_name.get(),et_key.get())
            else:
                    if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                    else:
                            x1.delete(et_key.get())        
        hashwin_sub=Button(
            win_canvas,
            text='Submit',
            borderwidth=0,
            bg='#1E1E1E',
            activebackground='#1E1E1E',
            activeforeground='#1E1E1E',
            relief='sunken',
            font=("Poppins",25*-1),
            fg='#376ebc',
            command=submit
        )
        #x2=roundPolygon([1135,1250,1250, 1135], [409,409,492,492], 20 , width=4, outline="#376ebc",fill="#1E1E1E")
        x1=roundPolygon([61.6, 272.6, 272.6, 61.6], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
        
        hash_but.configure(
        text='Hash Table\t'
        )
        bst_but.configure(
            text='Binary Search Tree'
        )

        ls_but.configure(
            text='Indexed Search\t'
        )
        mls_but.configure(
            text='Multi-Level Search'
        )
        butpack_x=20
        butpack_y=114
        hash_but.place(x=butpack_x,y=butpack_y+10)
        ls_but.place(x=butpack_x,y=butpack_y+10+93+17.75)
        bst_but.place(x=butpack_x,y=butpack_y+(93*2)+(17.75*2)+10)
        mls_but.place(x=butpack_x,y=butpack_y+(93*3)+(17.75*3)+10)
        
        x=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="white",fill="#1E1E1E")
        hash_but.bind("<Enter>",win_enter_hash)
        hash_but.unbind("<Leave>")
        ls_but.bind("<Enter>",win_enter_ls)
        ls_but.bind("<Leave>",win_left_ls)
        bst_but.bind("<Enter>",win_enter_bst)
        bst_but.bind("<Leave>",win_left_bst)
        mls_but.bind("<Enter>",win_enter_mls)
        mls_but.bind("<Leave>",win_left_mls)
        delc_text.place(x=680,y=26)
        insert_check.place(x=280,y=30)
        delete_check.place(x=650,y=30)
        upc_text.place(x=495,y=26)
        update_check.place(x=465,y=30)
        insc_text.place(x=310,y=26)
        et_key.place(x=300,y=90)
        lb_key.place(x=250,y=90)
        lb_name.place(x=560,y=90)
        et_name.place(x=640,y=90)
        lb_pri.place(x=238,y=130)
        lb_qua.place(x=546,y=130)
        et_pri.place(x=300,y=130)
        et_qua.place(x=640,y=130)
        et_wei.place(x=300,y=170)
        lb_wei.place(x=216,y=170)
        hash_descript.place(x=600,y=355)
        ls_descript.place(x=600,y=355)
        hashwin_sub.place(x=700,y=165)
        disp_canvas.place(x=480,y=355)
        def win_destroyed(e):
            disp_canvas.destroy()
            hashwin_sub.destroy()
            delc_text.destroy()
            insert_check.destroy()
            delete_check.destroy()
            upc_text.destroy()
            update_check.destroy()
            insc_text.destroy()
            et_key.destroy()
            lb_key.destroy()
            lb_name.destroy()
            et_name.destroy()
            lb_pri.destroy()
            lb_qua.destroy()
            et_pri.destroy()
            et_qua.destroy()
            et_wei.destroy()
            lb_wei.destroy()
            win_canvas.destroy()
            x=205
            a1=butpack_y+(93*2)+(17.75*2)
            x1=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            x2=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            hash_but.place(x=68.6,y=x)
            hash_descript.place(x=68.6,y=x+70)
            ls_but.place(x=299.2,y=x)
            ls_descript.place(x=299.2,y=x+70)
            bst_but.place(x=644.8,y=x)
            main_canvas.tag_raise(main_window)
            mls_but.place(x=973.4,y=x)
            hash_but.bind("<Enter>",enter_hash)
            hash_but.bind("<Leave>",left_hash)
            ls_but.bind("<Enter>",enter_ls)
            ls_but.bind("<Leave>",left_ls)
            bst_but.bind("<Enter>",enter_bst)
            bst_but.bind("<Leave>",left_bst)
            mls_but.bind("<Enter>",enter_mls)
            mls_but.bind("<Leave>",left_mls)
            hash_but.configure(
                
                text='    Hash Table   \n\n\n\n\n'
            )
            bst_but.configure(
                text='Binary Search Tree   \n\n\n\n\n',
            )

            ls_but.configure(
                text='    Sequential Search    \n\n\n\n\n'
            )
            mls_but.configure(
                
                text='Multi-Level Search   \n\n\n\n\n'
            )
        main_window.bind('<BackSpace>',lambda e:win_destroyed(e))

def ls_win():  
        x2=roundPolygon([292.2, 598.2, 598.2, 292.2], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
        win_canvas=Canvas(
                bg='#1E1E1E',
                height= 443,
                width=931,
                bd=0,
                highlightthickness=0,
                relief='ridge',
        )        
        global selected_option
        selected_option=0     
        def ins_active():
            global selected_option
            selected_option=1
            active_photo1.configure(file='active.svg')
            insert_check.configure(command=ins_inactive)
            print(selected_option)
            
        def ins_inactive():
            global selected_option
            selected_option=-1
            active_photo1.configure(file='inactive.svg')
            insert_check.configure(command=ins_active)
            print(selected_option)
            
        def ups_active():
            global selected_option
            selected_option=2
            active_photo2.configure(file='active.svg')
            update_check.configure(command=ups_inactive)
            print(selected_option)
            
        def ups_inactive():
            global selected_option
            selected_option=-1
            active_photo2.configure(file='inactive.svg')
            update_check.configure(command=ups_active)
            print(selected_option)
            
        def dels_active():
            global selected_option
            selected_option=3
            active_photo3.configure(file='active.svg')
            delete_check.configure(command=dels_inactive)
            print(selected_option)
            
        def dels_inactive():
            global selected_option
            selected_option =-1
            active_photo3.configure(file='inactive.svg')
            delete_check.configure(command=dels_active)
            print(selected_option)

        insert_check = Button(
            win_canvas,
            image=active_photo1,
            command=ins_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        insc_text = Label(
            win_canvas,
            text="Append",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        update_check = Button(
            win_canvas,
            image=active_photo2,
            command=ups_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        upc_text = Label(
            win_canvas,
            text="Update",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        delete_check = Button(
            win_canvas,
            image=active_photo3,
            command=dels_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        delc_text = Label(
            win_canvas,
            text="Delete",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        et_key=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_wei=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_qua=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_pri=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_name=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )  
        lb_wei=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Weight",
        )
        lb_name=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Name"
        )
        lb_key=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Key"
        )
        lb_pri=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Price"
        )
        lb_qua=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Quality",
        )   

        disp_canvas=Canvas(bg='white',
                        height= 180,
                        width=701,
                        bd=0,
                        highlightthickness=0,
                        relief='ridge',
                        )
        def submit():
            global selected_option
            x1=LinkedList()
            print(selected_option)
            if selected_option==1:
                        x1.insert(et_wei.get(),et_qua.get(),et_pri.get(),et_name.get(),et_key.get())
                        et_wei.delete(0,END)
                        et_qua.delete(0,END)
                        et_pri.delete(0,END)
                        et_name.delete(0,END)
                        et_key.delete(0,END)
            elif selected_option==2:
                        if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                        else:
                            x1.update(et_wei.get(),et_qua.get(),et_pri.get(),et_name.get(),et_key.get())
            else:
                    if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                    else:
                            x1.delete(et_key.get())       
        hashwin_sub=Button(
            win_canvas,
            text='Submit',
            borderwidth=0,
            bg='#1E1E1E',
            activebackground='#1E1E1E',
            activeforeground='#1E1E1E',
            relief='sunken',
            font=("Poppins",25*-1),
            fg='#376ebc',
            command=submit
        )
        hashwin_sub=Button(
            win_canvas,
            text='Submit',
            borderwidth=0,
            bg='#1E1E1E',
            activebackground='#1E1E1E',
            activeforeground='#1E1E1E',
            relief='sunken',
            font=("Poppins",25*-1),
            fg='#376ebc',
            command=submit
        )
        #x2=roundPolygon([1135,1250,1250, 1135], [409,409,492,492], 20 , width=4, outline="#376ebc",fill="#1E1E1E")
        win_canvas.place(x=326,y=114)
        x1=roundPolygon([61.6, 272.6, 272.6, 61.6], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
        
        hash_but.configure(
        text='Hash Table\t'
        )
        bst_but.configure(
            text='Binary Search Tree'
        )

        ls_but.configure(
            text='Indexed Search\t'
        )
        mls_but.configure(
            text='Multi-Level Search'
        )
        butpack_x=20
        butpack_y=114
        hash_but.place(x=butpack_x,y=butpack_y+10)
        ls_but.place(x=butpack_x,y=butpack_y+10+93+17.75)
        bst_but.place(x=butpack_x,y=butpack_y+(93*2)+(17.75*2)+10)
        mls_but.place(x=butpack_x,y=butpack_y+(93*3)+(17.75*3)+10)
         
        x=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="white",fill="#1E1E1E")
        hash_but.bind("<Enter>",win_enter_hash)
        hash_but.unbind("<Leave>")
        ls_but.bind("<Enter>",win_enter_ls)
        ls_but.bind("<Leave>",win_left_ls)
        bst_but.bind("<Enter>",win_enter_bst)
        bst_but.bind("<Leave>",win_left_bst)
        mls_but.bind("<Enter>",win_enter_mls)
        mls_but.bind("<Leave>",win_left_mls)
        delc_text.place(x=680,y=26)
        insert_check.place(x=280,y=30)
        delete_check.place(x=650,y=30)
        upc_text.place(x=495,y=26)
        update_check.place(x=465,y=30)
        insc_text.place(x=310,y=26)
        et_key.place(x=300,y=90)
        lb_key.place(x=250,y=90)
        lb_name.place(x=560,y=90)
        et_name.place(x=640,y=90)
        lb_pri.place(x=238,y=130)
        lb_qua.place(x=546,y=130)
        et_pri.place(x=300,y=130)
        et_qua.place(x=640,y=130)
        et_wei.place(x=300,y=170)
        lb_wei.place(x=216,y=170)
        hashwin_sub.place(x=700,y=165)
        disp_canvas.place(x=480,y=355)
        def win_destroyed(e):
            disp_canvas.destroy()
            hashwin_sub.destroy()
            delc_text.destroy()
            insert_check.destroy()
            delete_check.destroy()
            upc_text.destroy()
            update_check.destroy()
            insc_text.destroy()
            et_key.destroy()
            lb_key.destroy()
            lb_name.destroy()
            et_name.destroy()
            lb_pri.destroy()
            lb_qua.destroy()
            et_pri.destroy()
            et_qua.destroy()
            et_wei.destroy()
            lb_wei.destroy()
            win_canvas.destroy()
            x=205
            a1=butpack_y+(93*2)+(17.75*2)
            x1=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            x2=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            hash_but.place(x=68.6,y=x)
            ls_but.place(x=299.2,y=x)
            bst_but.place(x=644.8,y=x)
            main_canvas.tag_raise(main_window)
            mls_but.place(x=973.4,y=x)
            hash_but.bind("<Enter>",enter_hash)
            hash_but.bind("<Leave>",left_hash)
            ls_but.bind("<Enter>",enter_ls)
            ls_but.bind("<Leave>",left_ls)
            bst_but.bind("<Enter>",enter_bst)
            bst_but.bind("<Leave>",left_bst)
            mls_but.bind("<Enter>",enter_mls)
            mls_but.bind("<Leave>",left_mls)
            hash_but.configure(
            text='    Hash Table   \n\n\n\n\n'
            )
            bst_but.configure(
                text='Binary Search Tree   \n\n\n\n\n'
            )

            ls_but.configure(
                text='    Sequential Search    \n\n\n\n\n'
            )
            mls_but.configure(
                text='Multi-Level Search   \n\n\n\n\n'
            )
        main_window.bind('<BackSpace>',lambda e:win_destroyed(e))

def mls_win():    
        x4=roundPolygon([966.4,1253.4,1253.4,966.4], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
        win_canvas=Canvas(
                bg='#1E1E1E',
                height= 443,
                width=931,
                bd=0,
                highlightthickness=0,
                relief='ridge',
        )      
        global selected_option
        selected_option=0     
        def ins_active():
            global selected_option
            selected_option=1
            active_photo1.configure(file='active.svg')
            insert_check.configure(command=ins_inactive)
            print(selected_option)
            
        def ins_inactive():
            global selected_option
            selected_option=-1
            active_photo1.configure(file='inactive.svg')
            insert_check.configure(command=ins_active)
            print(selected_option)
            
        def ups_active():
            global selected_option
            selected_option=2
            active_photo2.configure(file='active.svg')
            update_check.configure(command=ups_inactive)
            print(selected_option)
            
        def ups_inactive():
            global selected_option
            selected_option=-1
            active_photo2.configure(file='inactive.svg')
            update_check.configure(command=ups_active)
            print(selected_option)
            
        def dels_active():
            global selected_option
            selected_option=3
            active_photo3.configure(file='active.svg')
            delete_check.configure(command=dels_inactive)
            print(selected_option)
            
        def dels_inactive():
            global selected_option
            selected_option =-1
            active_photo3.configure(file='inactive.svg')
            delete_check.configure(command=dels_active)
            print(selected_option)

        insert_check = Button(
            win_canvas,
            image=active_photo1,
            command=ins_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        insc_text = Label(
            win_canvas,
            text="Append",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        update_check = Button(
            win_canvas,
            image=active_photo2,
            command=ups_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        upc_text = Label(
            win_canvas,
            text="Update",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        delete_check = Button(
            win_canvas,
            image=active_photo3,
            command=dels_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        delc_text = Label(
            win_canvas,
            text="Delete",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        et_key=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_wei=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_qua=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_pri=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_name=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )  
        lb_wei=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Weight",
        )
        lb_name=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Name"
        )
        lb_key=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Key"
        )
        lb_pri=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Price"
        )
        lb_qua=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Quality",
        )   

        disp_canvas=Canvas(bg='white',
                        height= 180,
                        width=701,
                        bd=0,
                        highlightthickness=0,
                        relief='ridge',
                        )
        def submit():
            global selected_option
            x1=LinkedList()
            print(selected_option)
            if selected_option==1:
                        x1.insert(et_wei.get(),et_qua.get(),et_pri.get(),et_name.get(),et_key.get())
                        et_wei.delete(0,END)
                        et_qua.delete(0,END)
                        et_pri.delete(0,END)
                        et_name.delete(0,END)
                        et_key.delete(0,END)
            elif selected_option==2:
                        if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                        else:
                            x1.update(et_wei.get(),et_qua.get(),et_pri.get(),et_name.get(),et_key.get())
            else:
                    if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                    else:
                            x1.delete(et_key.get())
        hashwin_sub=Button(
            win_canvas,
            text='Submit',
            borderwidth=0,
            bg='#1E1E1E',
            activebackground='#1E1E1E',
            activeforeground='#1E1E1E',
            relief='sunken',
            font=("Poppins",25*-1),
            fg='#376ebc',
            command=submit
        )
        hashwin_sub=Button(
            win_canvas,
            text='Submit',
            borderwidth=0,
            bg='#1E1E1E',
            activebackground='#1E1E1E',
            activeforeground='#1E1E1E',
            relief='sunken',
            font=("Poppins",25*-1),
            fg='#376ebc',
            command=submit
        )
        #x2=roundPolygon([1135,1250,1250, 1135], [409,409,492,492], 20 , width=4, outline="#376ebc",fill="#1E1E1E")
        win_canvas.place(x=326,y=114)
        x1=roundPolygon([61.6, 272.6, 272.6, 61.6], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
        
        hash_but.configure(
        text='Hash Table\t'
        )
        bst_but.configure(
            text='Binary Search Tree'
        )

        ls_but.configure(
            text='Indexed Search\t'
        )
        mls_but.configure(
            text='Multi-Level Search'
        )
        butpack_x=20
        butpack_y=114
        hash_but.place(x=butpack_x,y=butpack_y+10)
        ls_but.place(x=butpack_x,y=butpack_y+10+93+17.75)
        bst_but.place(x=butpack_x,y=butpack_y+(93*2)+(17.75*2)+10)
        mls_but.place(x=butpack_x,y=butpack_y+(93*3)+(17.75*3)+10)
         
        x=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="white",fill="#1E1E1E")
        hash_but.bind("<Enter>",win_enter_hash)
        hash_but.unbind("<Leave>")
        ls_but.bind("<Enter>",win_enter_ls)
        ls_but.bind("<Leave>",win_left_ls)
        bst_but.bind("<Enter>",win_enter_bst)
        bst_but.bind("<Leave>",win_left_bst)
        mls_but.bind("<Enter>",win_enter_mls)
        mls_but.bind("<Leave>",win_left_mls)
        delc_text.place(x=680,y=26)
        insert_check.place(x=280,y=30)
        delete_check.place(x=650,y=30)
        upc_text.place(x=495,y=26)
        update_check.place(x=465,y=30)
        insc_text.place(x=310,y=26)
        et_key.place(x=300,y=90)
        lb_key.place(x=250,y=90)
        lb_name.place(x=560,y=90)
        et_name.place(x=640,y=90)
        lb_pri.place(x=238,y=130)
        lb_qua.place(x=546,y=130)
        et_pri.place(x=300,y=130)
        et_qua.place(x=640,y=130)
        et_wei.place(x=300,y=170)
        lb_wei.place(x=216,y=170)
        hashwin_sub.place(x=700,y=165)
        disp_canvas.place(x=480,y=355)
        def win_destroyed(e):
            disp_canvas.destroy()
            hashwin_sub.destroy()
            delc_text.destroy()
            insert_check.destroy()
            delete_check.destroy()
            upc_text.destroy()
            update_check.destroy()
            insc_text.destroy()
            et_key.destroy()
            lb_key.destroy()
            lb_name.destroy()
            et_name.destroy()
            lb_pri.destroy()
            lb_qua.destroy()
            et_pri.destroy()
            et_qua.destroy()
            et_wei.destroy()
            lb_wei.destroy()
            win_canvas.destroy()
            x=205
            a1=butpack_y+(93*2)+(17.75*2)
            x1=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            x2=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            hash_but.place(x=68.6,y=x)
            ls_but.place(x=299.2,y=x)
            bst_but.place(x=644.8,y=x)
            main_canvas.tag_raise(main_window)
            mls_but.place(x=973.4,y=x)
            hash_but.bind("<Enter>",enter_hash)
            hash_but.bind("<Leave>",left_hash)
            ls_but.bind("<Enter>",enter_ls)
            ls_but.bind("<Leave>",left_ls)
            bst_but.bind("<Enter>",enter_bst)
            bst_but.bind("<Leave>",left_bst)
            mls_but.bind("<Enter>",enter_mls)
            mls_but.bind("<Leave>",left_mls)
            hash_but.configure(
            text='    Hash Table   \n\n\n\n\n'
            )
            bst_but.configure(
                text='Binary Search Tree   \n\n\n\n\n'
            )

            ls_but.configure(
                text='    Sequential Search    \n\n\n\n\n'
            )
            mls_but.configure(
                text='Multi-Level Search   \n\n\n\n\n'
            )
        main_window.bind('<BackSpace>',lambda e:win_destroyed(e))     

def bst_win():  
        x3=roundPolygon([637.8, 924.8, 924.8, 637.8], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E") 
        win_canvas=Canvas(
                bg='#1E1E1E',
                height= 443,
                width=931,
                bd=0,
                highlightthickness=0,
                relief='ridge',
        )
        global selected_option
        selected_option=0     
        def ins_active():
            global selected_option
            selected_option=1
            active_photo1.configure(file='active.svg')
            insert_check.configure(command=ins_inactive)
            print(selected_option)
            
        def ins_inactive():
            global selected_option
            selected_option=-1
            active_photo1.configure(file='inactive.svg')
            insert_check.configure(command=ins_active)
            print(selected_option)
            
        def ups_active():
            global selected_option
            selected_option=2
            active_photo2.configure(file='active.svg')
            update_check.configure(command=ups_inactive)
            print(selected_option)
            
        def ups_inactive():
            global selected_option
            selected_option=-1
            active_photo2.configure(file='inactive.svg')
            update_check.configure(command=ups_active)
            print(selected_option)
            
        def dels_active():
            global selected_option
            selected_option=3
            active_photo3.configure(file='active.svg')
            delete_check.configure(command=dels_inactive)
            print(selected_option)
            
        def dels_inactive():
            global selected_option
            selected_option =-1
            active_photo3.configure(file='inactive.svg')
            delete_check.configure(command=dels_active)
            print(selected_option)

        insert_check = Button(
            win_canvas,
            image=active_photo1,
            command=ins_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        insc_text = Label(
            win_canvas,
            text="Append",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        update_check = Button(
            win_canvas,
            image=active_photo2,
            command=ups_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        upc_text = Label(
            win_canvas,
            text="Update",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        delete_check = Button(
            win_canvas,
            image=active_photo3,
            command=dels_active,
            border=0,
            background="#1E1E1E",
            activebackground="#1E1E1E"
            )
        delc_text = Label(
            win_canvas,
            text="Delete",
            background="#1E1E1E",
            border=0,
            font=('Poppins Bold',18*-1),
            fg="white"
            )
        et_key=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_wei=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_qua=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )
        et_pri=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            
            width=10
            )
        et_name=Entry(
            win_canvas,
            font=('Poppins Light',18*-1),
            bg="white",
            relief="flat",
            width=10
            )  
        lb_wei=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Weight",
        )
        lb_name=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Name"
        )
        lb_key=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Key"
        )
        lb_pri=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Price"
        )
        lb_qua=Label(
            win_canvas,
            fg="White",
            background="#1E1E1E",
            font=("Poppins bold",20*-1),
            text="Quality",
        )   

        disp_canvas=Canvas(bg='white',
                        height= 180,
                        width=701,
                        bd=0,
                        highlightthickness=0,
                        relief='ridge',
                        )
        def submit():
            global selected_option
            x1=LinkedList()
            print(selected_option)
            if selected_option==1:
                        x1.insert(et_wei.get(),et_qua.get(),et_pri.get(),et_name.get(),et_key.get())
                        et_wei.delete(0,END)
                        et_qua.delete(0,END)
                        et_pri.delete(0,END)
                        et_name.delete(0,END)
                        et_key.delete(0,END)
            elif selected_option==2:
                        if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                        else:
                            x1.update(et_wei.get(),et_qua.get(),et_pri.get(),et_name.get(),et_key.get())
            else:
                    if et_key.get()=="":
                            disp_canvas.create_text(100,100,text="Key cannot be empty")
                    else:
                            x1.delete(et_key.get())
        hashwin_sub=Button(
            win_canvas,
            text='Submit',
            borderwidth=0,
            bg='#1E1E1E',
            activebackground='#1E1E1E',
            activeforeground='#1E1E1E',
            relief='sunken',
            font=("Poppins",25*-1),
            fg='#376ebc',
            command=submit
        )
        x2=roundPolygon([1135,1250,1250, 1135], [409,409,492,492], 20 , width=4, outline="#1E1E1E",fill="#1E1E1E")
        win_canvas.place(x=326,y=114)
        #x1=roundPolygon([61.6, 272.6, 272.6, 61.6], [198, 198, 505, 505], 8 , width=8, outline="#1E1E1E",fill="#1E1E1E")
        
        hash_but.configure(
        text='Hash Table\t'
        )
        bst_but.configure(
            text='Binary'
        )

        ls_but.configure(
            text='Indexed Search\t'
        )
        mls_but.configure(
            text='Multi-Level Search'
        )
        butpack_x=20
        butpack_y=114
        hash_but.place(x=butpack_x,y=butpack_y+10)
        ls_but.place(x=butpack_x,y=butpack_y+10+93+17.75)
        bst_but.place(x=butpack_x,y=butpack_y+(93*2)+(17.75*2)+10)
        mls_but.place(x=butpack_x,y=butpack_y+(93*3)+(17.75*3)+10)
         
        hash_but.bind("<Enter>",win_enter_hash)
        hash_but.bind("<Leave>",win_left_hash)
        ls_but.bind("<Enter>",win_enter_ls)
        ls_but.bind("<Leave>",win_left_ls)
        a1=butpack_y+(93*2)+(17.75*2)
        x=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="white",fill="#1E1E1E")
        bst_but.bind("<Enter>",win_enter_bst)
        bst_but.unbind("<Leave>")
        mls_but.bind("<Enter>",win_enter_mls)
        mls_but.bind("<Leave>",win_left_mls)
        delc_text.place(x=680,y=26)
        insert_check.place(x=280,y=30)
        delete_check.place(x=650,y=30)
        upc_text.place(x=495,y=26)
        update_check.place(x=465,y=30)
        insc_text.place(x=310,y=26)
        et_key.place(x=300,y=90)
        lb_key.place(x=250,y=90)
        lb_name.place(x=560,y=90)
        et_name.place(x=640,y=90)
        lb_pri.place(x=238,y=130)
        lb_qua.place(x=546,y=130)
        et_pri.place(x=300,y=130)
        et_qua.place(x=640,y=130)
        et_wei.place(x=300,y=170)
        lb_wei.place(x=216,y=170)
        hashwin_sub.place(x=700,y=165)
        disp_canvas.place(x=480,y=355)
        def win_destroyed(e):
            disp_canvas.destroy()
            hashwin_sub.destroy()
            delc_text.destroy()
            insert_check.destroy()
            delete_check.destroy()
            upc_text.destroy()
            update_check.destroy()
            insc_text.destroy()
            et_key.destroy()
            lb_key.destroy()
            lb_name.destroy()
            et_name.destroy()
            lb_pri.destroy()
            lb_qua.destroy()
            et_pri.destroy()
            et_qua.destroy()
            et_wei.destroy()
            lb_wei.destroy()
            win_canvas.destroy()
            x=205
            a1=butpack_y+(93*2)+(17.75*2)
            x1=roundPolygon([10,307,307,10], [butpack_y,butpack_y,207,207], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            x2=roundPolygon([10,307,307,10], [a1,a1,a1+93,a1+93], 20 , width=6, outline="#1E1E1E",fill="#1E1E1E")
            hash_but.place(x=68.6,y=x)
            ls_but.place(x=299.2,y=x)
            bst_but.place(x=644.8,y=x)
            main_canvas.tag_raise(main_window)
            mls_but.place(x=973.4,y=x)
            hash_but.bind("<Enter>",enter_hash)
            hash_but.bind("<Leave>",left_hash)
            ls_but.bind("<Enter>",enter_ls)
            ls_but.bind("<Leave>",left_ls)
            bst_but.bind("<Enter>",enter_bst)
            bst_but.bind("<Leave>",left_bst)
            mls_but.bind("<Enter>",enter_mls)
            mls_but.bind("<Leave>",left_mls)
            hash_but.configure(
                text='    Hash Table   \n\n\n\n\n',
                command=hash_win
            )
            bst_but.configure(
                text='Binary Search Tree   \n\n\n\n\n',
                command=bst_win
            )

            ls_but.configure(
                text='    Sequential Search    \n\n\n\n\n',
                command=ls_win
            )
            mls_but.configure(
                text='Multi-Level Search   \n\n\n\n\n',
                command=mls_win
            )
        main_window.bind('<BackSpace>',lambda e:win_destroyed(e))
       



active_photo1  = tksvg.SvgImage(file='inactive.svg')
active_photo2 = tksvg.SvgImage(file='inactive.svg')
active_photo3  = tksvg.SvgImage(file='inactive.svg')


    
#packing


#packing end
#Binding


main_window.resizable(False,False)
x=250
hash_but.place(x=68.6,y=x)
hash_descript.place(x=68.6,y=x+70)
#q__m.place(x=0,y=0)
ls_but.place(x=299.2,y=x)
ls_descript.place(x=299.2,y=x+70)
bst_but.place(x=644.8,y=x)
bst_descript.place(x=644.8,y=x+70)
mls_but.place(x=973.4,y=x)
mls_descript.place(x=973.4,y=x+70)
menu_but.place(x=10,y=10,width=19,height=14)
main_window.bind('<Escape>', lambda e: close_win(e))
hash_but.bind("<Enter>",enter_hash)
hash_but.bind("<Leave>",left_hash)
ls_but.bind("<Enter>",enter_ls)
ls_but.bind("<Leave>",left_ls)
bst_but.bind("<Enter>",enter_bst)
bst_but.bind("<Leave>",left_bst)
mls_but.bind("<Enter>",enter_mls)
mls_but.bind("<Leave>",left_mls)
main_canvas.tag_raise(main_window)


#loading animation 

#loading animation end

#x=AnimatedGif(main_window,'loading.gif',1300,715)
#main_window.after_idle(x)
mainloop()
#Binding ends
