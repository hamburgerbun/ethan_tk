# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:47:23 2013

@author: joshua
"""
from Tkinter import Tk, Frame, Entry, StringVar, Label, Button, Message, \
    Toplevel, TOP, LEFT, IntVar, Checkbutton
import random

MAX_PLAYERS_IN_ROW = 10
MAX_PLAYER_COUNT = 30
MIN_PLAYER_COUNT = 2
GAME_WINDOW_WIDTH = 1024
GAME_WINDOW_HEIGHT = 768
INIT_WINDOW_WIDTH = 220
INIT_WINDOW_HEIGHT = 220
X_POS = 10
Y_POS = 10

# subfunction for initiating the main Tk widget
def init_main_window( main_window, ethan_eyes ):
    title_string = "pyETHAN ALLENthon"
    if ethan_eyes:
        title_string = "%s - %s" % (title_string, "ETHAN EYES ON")
    main_window.wm_title(string=title_string)
    main_window.wm_resizable( width=False, height=False )
    main_window.geometry("%dx%d+%d+%d" % 
        (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT, X_POS, Y_POS))

class Ethan:
    # attributes here, we'll need these for the callbacks
    main_window = None
    player_name_list = list()
    player_frame_list = list()
    player_strvars = list()
    current_turn = None
    player_turn = None
    dice1_strvar = None
    dice2_strvar = None
    ethan_strvar = None
    ethan_eyes = None
    
    def __init__(self, main_window, player_num, ethan_eyes):
        #three part frame division
        #first frame stuff, just ethan
        # TODO: find a picture of ethan and put it in here
        title_frame = Frame(main_window);
        title_frame.pack(side=TOP);
        title_label = Label(title_frame,  \
                            text="TIME FOR ETHAN", \
                            fg="blue", \
                            font=("Arial", 36), \
                            pady=30);
        title_label.pack(side=LEFT);
        ethan_strvar = StringVar();
        ethan_score = Entry(title_frame, \
                            textvariable=ethan_strvar, \
                            font=("Arial", 36), \
                            width=3, \
                            state='readonly');
        ethan_strvar.set("0");
        ethan_score.pack(side=LEFT);
        #second frame, die rolling        
        dice_frame = Frame(main_window);
        dice_frame.pack(side=TOP);
        self.dice1_strvar = StringVar()
        self.dice2_strvar = StringVar()
        self.dice1_strvar.set("2")
        self.dice2_strvar.set("2")
        dice1 = Label( dice_frame, \
                        textvariable=self.dice1_strvar, \
                        fg="black", \
                        font=("Arial", 24), \
                        borderwidth=2, \
                        relief='raised', \
                        pady=20, \
                        padx=40 )
        dice1.pack()
        dice2 = Label( dice_frame, \
                        textvariable=self.dice2_strvar, \
                        fg="black", \
                        font=("Arial", 24), \
                        borderwidth=2, \
                        relief='raised', \
                        pady=20, \
                        padx=40);    
        dice2.pack();
        #third frame, scores and players
        scores_frame = Frame(main_window, pady=30);
        scores_frame.pack(side=TOP);
        #find how many rows, and how many left over
        rows = int(player_num/MAX_PLAYERS_IN_ROW)
        last_row_amt = int(player_num - MAX_PLAYERS_IN_ROW*rows)
        if last_row_amt > 0:
            rows = rows + 1
        elif last_row_amt == 0:
            last_row_amt = 10
        #make the number of subframes we need for this
        frame_list = list();
        player_name_frame_list = list();
        player_name_list = list();
        player_frame_list = list();
        player_score_list = list();
        player_strvars = list();
        for frame_ind in xrange(0, rows):
            #first frame, let's just make textboxes for names
            frame_list.append(Frame(scores_frame))
            frame_list[2*frame_ind].pack(side=TOP);
            frame_list.append(Frame(scores_frame, pady=10));
            frame_list[2*frame_ind+1].pack(side=TOP);
            #now generate the smaller frames for each button and number count
            if frame_ind < (rows-1):
                make_this_amount = 10;
            else:
                make_this_amount = last_row_amt;
            for player_ind in xrange(0, make_this_amount):
                actual_player_ind = player_ind + frame_ind*MAX_PLAYERS_IN_ROW
                # player name textbox
                player_name_frame_list.append(Frame(frame_list[2*frame_ind]))
                player_name_frame_list[actual_player_ind].pack(side=LEFT)
                player_name_list.append(Entry(player_name_frame_list[actual_player_ind], \
                      font=("Arial", 12), \
                      width=10))
                player_name_list[actual_player_ind].pack(side=LEFT)
                # score box
                player_frame_list.append(Frame(frame_list[2*frame_ind+1]))
                player_frame_list[actual_player_ind].pack(side=LEFT);
                player_strvars.append(StringVar());
                player_score_list.append(Entry(player_frame_list[actual_player_ind], \
                                                state="readonly", \
                                                font=("Arial", 24), \
                                                width=5, \
                                                textvariable=player_strvars[actual_player_ind]));
                player_strvars[actual_player_ind].set("5");                          
                player_score_list[actual_player_ind].pack(side=LEFT);
        #raise the first guy, we can change it with each turn
        player_frame_list[0].config(relief='raised', borderwidth=2);     
        # need to also create a roll button
        roll_button = Button( scores_frame, text="Roll Dice", \
            command=lambda: Ethan.do_a_turn(self) );
        roll_button.pack();
        self.main_window = main_window
        self.player_strvars = player_strvars
        self.player_name_list = player_name_list
        self.player_frame_list = player_frame_list
        self.current_turn = 1
        self.player_turn = 0
        self.ethan_strvar = ethan_strvar
        self.ethan_eyes = ethan_eyes
        return; 
            
    #subfunction for each turn
    def do_a_turn(self):
        # roll die
        die1_val = random.randint(1,6)
        die2_val = random.randint(1,6)
        # TODO: potentially simulate die motion like in matlab version
        # change die values on screen
        self.dice1_strvar.set(str(die1_val))
        self.dice2_strvar.set(str(die2_val))
        
        # check dice conditions
        ethan_val = int(self.ethan_strvar.get())
        player_val = int(self.player_strvars[self.player_turn].get())
        if (die1_val+die2_val == 4):
            # player gets ethan's stuff
            player_val = player_val + ethan_val
            ethan_val = 0
        elif (die1_val+die2_val == 2) and self.ethan_eyes:
            # player loses it all to ethan
            ethan_val = player_val + ethan_val
            player_val = 0
        else:
            # player loses one chip to ethan
            ethan_val = ethan_val + 1
            player_val = player_val - 1
        self.ethan_strvar.set(str(ethan_val))
        self.player_strvars[self.player_turn].set(str(player_val))
        # check for the lose condition
        total_chips = 0
        num_players_positive = 0
        for x in self.player_strvars:
            if int(x.get()) > 0:
                num_players_positive = num_players_positive + 1
            total_chips = total_chips + int(x.get())
        if total_chips == 0:
            # everybody loses
            error_dlg = Toplevel(master=self.main_window)
            error_dlg.geometry("%dx%d+%d+%d" % 
                (INIT_WINDOW_WIDTH, INIT_WINDOW_HEIGHT, X_POS, Y_POS))
            error_dlg.title( "LOSERS" );
            error_dlg.grab_set();
            error_msg = Message(error_dlg, aspect=300, text="EVERYBODY LOSES, AE2015")
            error_msg.pack();
            error_button = Button(error_dlg, text="OK", \
                                command=lambda: self.destroy_all(error_dlg));
            error_button.pack();
            error_dlg.update();
        elif (num_players_positive == 1) and (player_val > ethan_val):
            #win condition, only for player who just moved
            player_name = self.player_name_list[self.player_turn].get();
            error_dlg = Toplevel(master=self.main_window)
            error_dlg.geometry("%dx%d+%d+%d" % 
                (INIT_WINDOW_WIDTH, INIT_WINDOW_HEIGHT, X_POS, Y_POS))
            error_dlg.title( "WINNER" );
            error_dlg.grab_set();
            error_msg = Message(error_dlg, aspect=300, text="GOOD JOB %s, YOU BEAT ETHAN" % (player_name) )
            error_msg.pack();
            error_button = Button(error_dlg, text="OK", \
                                    command=error_dlg.destroy);
            error_button.pack();
            error_dlg.update();
        else:
            # game isn't over, increment turn to next positive player
            self.player_frame_list[self.player_turn].config(relief='flat', \
                borderwidth=0)
            num_players = len(self.player_strvars)
            found_next = 0
            self.current_turn = self.current_turn + 1
            while (found_next == 0):
                self.player_turn = (self.player_turn + 1) % num_players
                if int(self.player_strvars[self.player_turn].get()) > 0:
                    found_next = 1
            self.player_frame_list[self.player_turn].config(relief='raised', \
                borderwidth=2)    
        return
    
    def destroy_all(self, error_dlg):
        error_dlg.destroy()
        self.main_window.destroy()

# helper startup stuff here

def make_error_dialog(player_dlg):
    error_dlg = Toplevel(master=player_dlg);
    error_dlg.title( "Error" );
    error_dlg.grab_set();
    error_msg = Message(error_dlg, aspect=300, text="Player count must be between %d and %d" % (MIN_PLAYER_COUNT, MAX_PLAYER_COUNT) )
    error_msg.pack();
    error_button = Button(error_dlg, text="OK", \
                            command=error_dlg.destroy);
    error_button.pack();
    error_dlg.update();
    return

def generate_main(player_dlg, player_count, ethan_eyes_var ):
    s = player_count.get();
    if s != "":
        try:
            player_num = int(s);
        except:
            player_num = 9999
    if (player_num > MAX_PLAYER_COUNT) or (player_num < MIN_PLAYER_COUNT):
        make_error_dialog(player_dlg)
        return;
    else:
        ethan_eyes = ethan_eyes_var.get()
        player_dlg.destroy();
        root = Tk();
        init_main_window(root, ethan_eyes);
        app = Ethan(root, player_num, ethan_eyes);
        root.mainloop();
    return
    
#start program with dialog box, which will lead to either just terminating
#or making a game box
if __name__ == "__main__":
    player_dlg = Tk();
    player_dlg.geometry("%dx%d+%d+%d" % 
        (INIT_WINDOW_WIDTH, INIT_WINDOW_HEIGHT, X_POS, Y_POS))
    # TODO: make dialog box show up in the middle of the screen based on
    # screen resolution
    player_dlg.title("How many players?")
    msg = Message(player_dlg, text="How many players will be playing this time?");
    msg.pack()
    player_count = Entry(player_dlg)
    player_count.pack()
    ethan_eyes_var = IntVar()
    ethan_eyes_check = Checkbutton(player_dlg, \
                                   text="enable Ethan Eyes", \
                                   var=ethan_eyes_var)
    ethan_eyes_check.pack()
    confirm_button = Button(player_dlg, text="OK", \
                            command=lambda: generate_main(player_dlg, \
                                                          player_count, \
                                                          ethan_eyes_var) );
    confirm_button.pack();
    cancle_button = Button(player_dlg, text="Cancel", \
                            command=lambda: player_dlg.quit() );
    cancle_button.pack();
    player_dlg.mainloop();



    