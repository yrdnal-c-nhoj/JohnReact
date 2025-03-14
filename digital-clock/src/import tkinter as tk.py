import tkinter as tk
import math
from datetime import datetime
from typing import Optional, Tuple

class AnalogClock(tk.Canvas):
    """An analog clock widget"""
    
    def __init__(
        self,
        master,
        radius: int = 150,
        shape: str = 'circle',    # Options : 'circle' or 'rectangle'
        border_width: int = 3,
        border_color: str = '#a6a6a6',
        clock_face_style: str = 'digit', # Options: 'digit or 'roman' or 'tick' or 'none'
        
        fg_color: str = "transparent",
        bg_color: str = "transparent",
        
        font: Tuple[str, int, str] = ('Calibri', 12, 'normal'),
        font_color: str = 'black',
        
        hour_color: str = '#383838',
        minute_color: str = '#454545',
        second_color: str = '#ff3e3e',
        
        hour_hand_width: int = 7,
        minute_hand_width: int = 5,
        second_hand_width: int = 3,
        
        start_time: Optional[str] = None,
        quarter_hour: bool = False,
        quarter_symbol: Optional[str] = None,   # Can be given any letter or symbol in string form
        quarter_symbol_color: Optional[str] = None,
        # **kwargs
        ):

        ###  Parameter variables
        self.master = master
        self.radius = radius
        self.shape = shape
        self.border_width = border_width
        self.border_color = border_color
        self.clock_face_style = clock_face_style

        self.font = font
        self.font_color = font_color
        
        self.hour_color = hour_color
        self.minute_color = minute_color
        self.second_color = second_color
        
        self.hour_hand_width = hour_hand_width
        self.minute_hand_width = minute_hand_width
        self.second_hand_width = second_hand_width
        
        self.start_time = start_time
        self.quarter_hour = quarter_hour
        self.quarter_symbol = quarter_symbol
        self.quarter_symbol_color = quarter_symbol_color
        
        self.fg_color = fg_color
        self.bg_color = bg_color
        
        #  Other Variables
        self.initial_time_set = False
        self.base_time = datetime.now() if not start_time else datetime.strptime(start_time, "%H:%M:%S")
        self.last_update_time = datetime.now()

        # Handling the `fg_color = "transparent"` argument
        if fg_color.lower() == 'transparent':
            try:
                if master.winfo_name().startswith("!ctkframe"):
                    # getting bg_color of customtkinter frames
                    self.fg_color = master._apply_appearance_mode(master.cget("fg_color"))
                else:
                    self.fg_color = master.cget("bg")
            except:  
                self.fg_color = "white"
        else:
            self.fg_color = fg_color

        self.__transparent_bg()
        
        super().__init__(self.master, bg=self.bg_color, width=2 * radius, height=2 * radius, bd=0, highlightthickness=0)


        # Starting the clock update loop
        self.__update_clock()

    def __transparent_bg(self,):
        # Setting the canvas background color to match the parent's background color
        if self.bg_color.lower() == 'transparent':
            try:
                if self.master.winfo_name().startswith("!ctkframe"):
                    # getting bg_color of customtkinter frames
                    self.bg_color = self.master._apply_appearance_mode(self.master.cget("fg_color"))
                else:
                    self.bg_color = self.master.cget("bg")
            except:  
                self.bg_color = "white"
        

    def __update_clock(self):
        """
        Update the clock display with the current time, and schedule the next update.
        """
        now = datetime.now()
        if not self.initial_time_set:
            # Set the initial time based on start_time or the current time
            self.initial_time_set = True
            self.last_update_time = now

        # Calculating the time difference since the last update
        time_difference = now - self.last_update_time
        # Incrementing the base time by this difference
        self.base_time += time_difference
        # Updating the last update time for the next cycle
        self.last_update_time = now

        seconds = self.base_time.second
        minutes = self.base_time.minute
        hours = self.base_time.hour % 12
        
        self.__draw_clock(seconds, minutes, hours)
        self.after(1000, self.__update_clock)

    def __draw_clock(self, seconds, minutes, hours):
        """
        Draw a clock on the canvas based on the given seconds, minutes, and hours.
        Parameters:
            hours (int): The hours component of the time.
            minutes (int): The minutes component of the time.
            seconds (int): The seconds component of the time.
        """
        self.delete("all")

        self.__draw_clock_shape()
       
        # Drawing clock numbers
        if not self.quarter_hour:           ## If `quarter_hour` is False        
            for i in range(1, 13):
                x, y = self.__coordinate_clock_numbers(i)
                self.__assign_clock_face_style(i, x, y)
                # self.create_text(x, y, text=str(i), font=self.font, fill=self.font_color)

        elif self.quarter_hour and not self.quarter_symbol: ## If `quarter_hour` is True and `quarter_symbol` is False
            for i in range(3,13,3):                             ## Only for 3, 6, 9, 12
                x, y = self.__coordinate_clock_numbers(i)
                self.__assign_clock_face_style(i, x, y)
                # self.create_text(x, y, text=str(i), font=self.font, fill=self.font_color)
                
        elif self.quarter_hour and self.quarter_symbol:         ## If `quarter_hour` is True and `quarter_symbol` is True
            for i in range(1, 13):                              ## For all numbers
                x, y = self.__coordinate_clock_numbers(i)
                    
                if i % 3 == 0:                   ## Writing Only 3, 6, 9, 12
                    self.__assign_clock_face_style(i, x, y)
                    # self.create_text(x, y, text=str(i), font=self.font, fill=self.font_color)
                else:                            ## Drawing Symbols on place of numbers not divisible by `3`
                    if self.quarter_symbol_color:   ## Using given color for symbols, If `quarter_symbol_color` is given
                        self.create_text(x, y, text=self.quarter_symbol, font=self.font, fill=self.quarter_symbol_color)
                    else:          ##  If `quarter_symbol_color` is NOT given, using same color as text
                        self.create_text(x, y, text=self.quarter_symbol, font=self.font, fill=self.font_color)
                        

        # Drawing hour hand
        hour_angle = math.radians((hours % 12) * 30 + (minutes / 60) * 30)
        hour_x = self.radius + self.radius * 0.4 * math.sin(hour_angle)
        hour_y = self.radius - self.radius * 0.4 * math.cos(hour_angle)
        self.create_line(
                        self.radius, self.radius,
                        hour_x, hour_y,
                        width=self.hour_hand_width,
                        fill=self.hour_color
                        )

        # Drawing minute hand
        minute_angle = math.radians(minutes * 6 + (seconds / 60) * 6)
        minute_x = self.radius + self.radius * 0.6 * math.sin(minute_angle)
        minute_y = self.radius - self.radius * 0.6 * math.cos(minute_angle)
        self.create_line(
                        self.radius, self.radius, 
                        minute_x, minute_y,
                        width=self.minute_hand_width,
                        fill=self.minute_color
                        )

        # Drawing second hand
        second_angle = math.radians(seconds * 6)
        second_x = self.radius + self.radius * 0.7 * math.sin(second_angle)
        second_y = self.radius - self.radius * 0.7 * math.cos(second_angle)
        self.create_line(
                        self.radius, self.radius,
                        second_x, second_y,
                        width=self.second_hand_width,
                        fill=self.second_color
                        )
    
    
    def __draw_clock_shape(self,):
        # Drawing clock face with a slight padding to not touch the canvas border
        padding = 5
        if self.shape == 'circle':
            self.create_oval(padding, padding, 2 * (self.radius - padding), 2 * (self.radius - padding),
                            width=self.border_width, fill=self.fg_color, outline=self.border_color)
        elif self.shape == 'rectangle':
            side_length = 2 * (self.radius - padding)
            self.create_rectangle(padding, padding, padding + side_length, padding + side_length,
                      width=self.border_width, fill=self.fg_color, outline=self.border_color)
        else:
            raise ValueError("Invalid value for 'shape'. Use 'circle' or 'rectangle'.")

    def __coordinate_clock_numbers(self, i):
        # Getting Coordinates for clock numbers
        x_adjust = 0
        y_adjust = 0
        if self.shape == 'rectangle':
            # Adjusting coordinates for numbers in a rectangle
            x_adjust = 10
            y_adjust = 13

        angle = math.radians(i * 30)
        if i == 2 or i == 4:
            x = self.radius + self.radius * 0.8 * math.sin(angle) + x_adjust
            y = self.radius - self.radius * 0.8 * math.cos(angle)
        elif i == 5:
            x = self.radius + self.radius * 0.8 * math.sin(angle) + 4
            y = self.radius - self.radius * 0.8 * math.cos(angle) + y_adjust
        elif i == 7:
            x = self.radius + self.radius * 0.8 * math.sin(angle) - 4
            y = self.radius - self.radius * 0.8 * math.cos(angle) + y_adjust
        elif i == 8 or i == 10:
            x = self.radius + self.radius * 0.8 * math.sin(angle) - x_adjust
            y = self.radius - self.radius * 0.8 * math.cos(angle)
        elif i == 11:
            x = self.radius + self.radius * 0.8 * math.sin(angle) - 4
            y = self.radius - self.radius * 0.8 * math.cos(angle) - y_adjust
        elif i == 1:
            x = self.radius + self.radius * 0.8 * math.sin(angle) + 4
            y = self.radius - self.radius * 0.8 * math.cos(angle) - y_adjust
        else:
            x = self.radius + self.radius * 0.8 * math.sin(angle)
            y = self.radius - self.radius * 0.8 * math.cos(angle)
            
        return x, y

    def __assign_clock_face_style(self, i, x, y):
        #####   Some constants   #####
        ROMAN_NUMERALS = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
                        7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11: 'XI', 12: 'XII'}
        TICKS = {1: '', 2: '', 3: '―', 4: '', 5: '', 6: '|', 7: '', 8: '', 9: '―', 10: '', 11: '', 12: '|'}
        EMPTY = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: ''}
        if self.clock_face_style == 'digit' or self.clock_face_style == 'DIGIT' or self.clock_face_style == 'Digit':
            self.create_text(x, y, text=str(i), font=self.font, fill=self.font_color)
            
        elif self.clock_face_style == 'roman' or self.clock_face_style == 'ROMAN' or self.clock_face_style == 'Roman':
            self.create_text(x, y, text=ROMAN_NUMERALS[i], font=self.font, fill=self.font_color)

        elif self.clock_face_style == 'tick' or self.clock_face_style == 'TICK' or self.clock_face_style == 'Tick':
            self.create_text(x, y, text=TICKS[i], font=self.font, fill=self.font_color)

        elif self.clock_face_style == None or self.clock_face_style == 'none' or self.clock_face_style == 'None' or self.clock_face_style == 'NONE':
            self.create_text(x, y, text=EMPTY[i], font=self.font, fill=self.font_color)


    ####################        METHODS        ####################
    def get_current_time(self):
        '''
        This method returns the current time of the clock as a datetime object
        '''
        return self.base_time

    def get_current_strftime(self, format_string="%H:%M:%S"):
        ''' 
        This method returns the current time of the clock as a formatted string
        The default format is HH:MM:SS, but you can pass another format if desired
        '''
        return self.base_time.strftime(format_string)

    def configure(self, **kwargs):
        '''
        TO configure some options of the clock
        radius: int = 150,
        shape: str = 'circle',    # Options : 'circle' or 'rectangle'
        border_width: int = 3,
        border_color: str = '#a6a6a6',
        clock_face_style: str = 'digit', # Options: 'digit or 'roman' or 'tick' or 'none'
        
        fg_color: str = "transparent",
        bg_color: str = "transparent",
        
        font: Tuple[str, int, str] = ('Calibri', 12, 'regular'),
        font_color: str = 'black',
        
        hour_color: str = '#383838',
        minute_color: str = '#454545',
        second_color: str = '#ff3e3e',
        
        hour_hand_width: int = 4,
        minute_hand_width: int = 3,
        second_hand_width: int = 1,
        
        start_time: Optional[str] = None,
        quarter_hour: bool = False,
        quarter_symbol: Optional[str] = None,   # Can be given any letter or symbol in string form
        quarter_symbol_color: Optional[str] = None,
        '''
        if 'radius' in kwargs:
            self.radius = kwargs.pop('radius')
            self.config(width=2 * self.radius, height=2 * self.radius)
        
        if 'shape' in kwargs:
            self.shape = kwargs.pop('shape')

        if 'border_width' in kwargs:
            self.border_width = kwargs.pop('border_width')

        if 'border_color' in kwargs:
            self.border_color = kwargs.pop('border_color')
        
        if 'clock_face_style' in kwargs:
            self.clock_face_style = kwargs.pop('clock_face_style')

        if 'fg_color' in kwargs:
            self.fg_color = kwargs.pop('fg_color')

        if 'bg_color' in kwargs:
            self.bg_color = kwargs.pop('bg_color')
            self.__transparent_bg()
            self.config(bg=self.bg_color)
        
        if 'font' in kwargs:
            self.font = kwargs.pop('font')

        if 'font_color' in kwargs:
            self.font_color = kwargs.pop('font_color')

        if 'hour_color' in kwargs:
            self.hour_color = kwargs.pop('hour_color')

        if 'minute_color' in kwargs:
            self.minute_color = kwargs.pop('minute_color')

        if 'second_color' in kwargs:
            self.second_color = kwargs.pop('second_color')

        if 'hour_hand_width' in kwargs:
            self.hour_hand_width = kwargs.pop('hour_hand_width')

        if 'minute_hand_width' in kwargs:
            self.minute_hand_width = kwargs.pop('minute_hand_width')

        if 'second_hand_width' in kwargs:
            self.second_hand_width = kwargs.pop('second_hand_width')

        if 'start_time' in kwargs:
            self.start_time = kwargs.pop('start_time')
            self.base_time = datetime.strptime(self.start_time, "%H:%M:%S")

        if 'quarter_hour' in kwargs:
            self.quarter_hour = kwargs.pop('quarter_hour')

        if 'quarter_symbol' in kwargs:
            self.quarter_symbol = kwargs.pop('quarter_symbol')

        if 'quarter_symbol_color' in kwargs:
            self.quarter_symbol_color = kwargs.pop('quarter_symbol_color')


        # Update the clock appearance
        self.__update_clock()
