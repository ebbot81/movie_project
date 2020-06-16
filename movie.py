import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *


movies_data = pd.read_csv("movie.final-1.csv")

root =tk.Tk()
root.title("My movies")


def get_year():
    selected_years = years.get()
    selected_years = selected_years.split('-')
    return selected_years

def get_genre():
    return genre.get()
    
def get_duration():
    selected_duration = duration.get()
    selected_duration = selected_duration.split('-')
    return selected_duration

def get_high_IMDB():
    return IMDB_high.get()

def get_low_IMDB():
    return IMDB_low.get()

def search_graph():
    selected_years = get_year()
    selected_genre = get_genre()
    selected_duration = get_duration()
    selected_high_IMDB = get_high_IMDB()
    selected_low_IMDB = get_low_IMDB()
    movies  = movies_data.loc[(movies_data.Year.between(int(selected_years[0]),int(selected_years[1]))
    & (movies_data.Duration.between(int(selected_duration[0]),int(selected_duration[1])))
    & (movies_data.IMDB.between(int(selected_low_IMDB),int(selected_high_IMDB)))
    & ((selected_genre == '0') | (movies_data.Genre.str.contains(selected_genre)))
    )]
    
    new_window = tk.Toplevel(root)
    new_window.title("Found " + str(len(movies.index)) + " movies")
    if len(movies.index) == 0:
        new_window.title("No match, please try again")
    
    label_title = tk.Label(new_window, text="Title", font=('times 16 bold italic underline'))
    label_title.grid(row = 0, column=0, sticky=W, pady=10, padx=20)
    label_year = tk.Label(new_window, text="Year", font=('times 16 bold italic underline'))
    label_year.grid(row = 0, column=1, sticky=W, padx=20)
    label_genre = tk.Label(new_window, text="Genre", font=('times 16 bold italic underline'))
    label_genre.grid(row = 0, column=2, sticky=W, padx=20)
    label_director = tk.Label(new_window, text="Director", font=('times 16 bold italic underline'))
    label_director.grid(row = 0, column=3, sticky=W, padx=20)
    label_duration = tk.Label(new_window, text="Duration", font=('times 16 bold italic underline'))
    label_duration.grid(row = 0, column=4, sticky=W, padx=20)
    label_IMDB = tk.Label(new_window, text="IMDB", font=('times 16 bold italic underline'))
    label_IMDB.grid(row = 0, column=5, sticky=W, padx=20)



    for index, row in movies.iterrows():
        label_title = tk.Label(new_window, text=row.Title, font=('times 14'))
        label_title.grid(row = index+1, column=0, sticky=W, pady=3, padx=20)
        label_year = tk.Label(new_window, text=row.Year, font=('times 14'))
        label_year.grid(row = index+1, column=1, sticky=W, padx=20)
        label_genre = tk.Label(new_window, text=row.Genre, font=('times 14'))
        label_genre.grid(row = index+1, column=2, sticky=W, padx=20)
        label_director = tk.Label(new_window, text=row.Director, font=('times 14'))
        label_director.grid(row = index+1, column=3, sticky=W, padx=20)
        label_duration = tk.Label(new_window, text=row.Duration, font=('times 14'))
        label_duration.grid(row = index+1, column=4, padx=20)
        label_IMDB = tk.Label(new_window, text=row.IMDB, font=('times 14'))
        label_IMDB.grid(row = index+1, column=5, padx=20)

        canvas = tk.Canvas(new_window)
        scrollbar = tk.Scrollbar(new_window, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=6, sticky="nsew")
        canvas.configure(yscrollcommand=scrollbar.set)

label_headline=Label(root, text="Pick A Flick For Movienight", font=('times 24 bold italic'))
label_headline.grid(row=15, column=6)

label_year=Label(root, bd=3, text="Choose a Year", bg="light goldenrod1", padx=20)
label_rb=Label()

label_year.grid(row=1, column=0, padx=10, pady=10)
years = StringVar(value="1961-2020")
Radiobutton(root, label_rb, text="Not important", variable= years, value="1961-2020").grid(row=2, column=0)
Radiobutton(root, label_rb, text="1961 - 1966", variable= years, value="1961-1966").grid(row=3, column=0)
Radiobutton(root, label_rb, text="1967 - 1972", variable= years, value="1967-1972").grid(row=4, column=0)
Radiobutton(root, label_rb, text="1973 - 1978", variable= years, value="1973-1978").grid(row=5, column=0)
Radiobutton(root, label_rb, text="1979 - 1984", variable= years, value="1979-1984").grid(row=6, column=0)
Radiobutton(root, label_rb, text="1985 - 1990", variable= years, value="1985-1990").grid(row=7, column=0)
Radiobutton(root, label_rb, text="1991 - 1996", variable= years, value="1991-1996").grid(row=8, column=0)
Radiobutton(root, label_rb, text="1997 - 2002", variable= years, value="1997-2002").grid(row=9, column=0)
Radiobutton(root, label_rb, text="2003 - 2008", variable= years, value="2003-2008").grid(row=10, column=0)
Radiobutton(root, label_rb, text="2009 - 2014", variable= years, value="2009-2014").grid(row=11, column=0)
Radiobutton(root, label_rb, text="2015 - 2020", variable= years, value="2015-2020").grid(row=12, column=0)

label_genre=Label(root, bd=3, text="Choose a Genre", bg="white", padx=20)
label_rbg=Label()

label_genre.grid(row=1, column=1, padx=10, pady=10)
genre = StringVar(value=0)
Radiobutton(root, label_rbg, text="Not important", variable= genre, value=0).grid(row=2, column=1)
Radiobutton(root, label_rbg, text="Action", variable= genre, value="Action").grid(row=3, column=1)
Radiobutton(root, label_rbg, text="Adventure", variable= genre, value="Adventure").grid(row=4, column=1)
Radiobutton(root, label_rbg, text="Biography", variable= genre, value="Biography").grid(row=5, column=1)
Radiobutton(root, label_rbg, text="Comedy", variable= genre, value="Comedy").grid(row=6, column=1)
Radiobutton(root, label_rbg, text="Crime", variable= genre, value="Crime").grid(row=7, column=1)
Radiobutton(root, label_rbg, text="Drama", variable= genre, value="Drama").grid(row=8, column=1)
Radiobutton(root, label_rbg, text="Fantasy", variable= genre, value="Fantasy").grid(row=9, column=1)
Radiobutton(root, label_rbg, text="Horror", variable= genre, value="Horror").grid(row=10, column=1)
Radiobutton(root, label_rbg, text="Sci-Fi", variable= genre, value="Sci-Fi").grid(row=11, column=1)
Radiobutton(root, label_rbg, text="Thriller", variable= genre, value="Thriller").grid(row=12, column=1)

label_duration=Label(root, bd=3, text="Choose duration of the movie", bg="orange red", padx=20)
label_rbd=Label()

label_duration.grid(row=1, column=2, padx=10, pady=10)
duration = StringVar(value="0-300")
Radiobutton(root, label_rbd, text="Not important", variable= duration, value="0-300").grid(row=2, column=2)
Radiobutton(root, label_rbd, text="0 - 30 min", variable= duration, value="0-30").grid(row=3, column=2)
Radiobutton(root, label_rbd, text="31 - 60 min", variable= duration, value="31-60").grid(row=4, column=2)
Radiobutton(root, label_rbd, text="61 - 90 min", variable= duration, value="61-90").grid(row=5, column=2)
Radiobutton(root, label_rbd, text="91 - 120 min", variable= duration, value="91-120").grid(row=6, column=2)
Radiobutton(root, label_rbd, text="121 - 150 min", variable= duration, value="121-150").grid(row=7, column=2)
Radiobutton(root, label_rbd, text="151 - 180 min", variable= duration, value="151-180").grid(row=8, column=2)
Radiobutton(root, label_rbd, text="181 - 210 min", variable= duration, value="181-210").grid(row=9, column=2)
Radiobutton(root, label_rbd, text="211 - 240 min", variable= duration, value="211-240").grid(row=10, column=2)
Radiobutton(root, label_rbd, text="241 - 270 min", variable= duration, value="241-270").grid(row=11, column=2)
Radiobutton(root, label_rbd, text="271 - 300 min", variable= duration, value="271-300").grid(row=12, column=2)

label_low_IMDB=Label(root, bd=3, text="Choose IMDB rating (higher than)", bg="lightgrey", padx=20)
label_rbli=Label()

label_low_IMDB.grid(row=1, column=3, padx=10, pady=10)
IMDB_low = StringVar(value=-1)
Radiobutton(root, label_rbli, text="Not important", variable= IMDB_low, value=-1).grid(row=2, column=3)
Radiobutton(root, label_rbli, text="> = 0", variable= IMDB_low, value=0).grid(row=3, column=3)
Radiobutton(root, label_rbli, text="> = 1", variable= IMDB_low, value=1).grid(row=4, column=3)
Radiobutton(root, label_rbli, text="> = 2", variable= IMDB_low, value=2).grid(row=5, column=3)
Radiobutton(root, label_rbli, text="> = 3", variable= IMDB_low, value=3).grid(row=6, column=3)
Radiobutton(root, label_rbli, text="> = 4", variable= IMDB_low, value=4).grid(row=7, column=3)
Radiobutton(root, label_rbli, text="> = 5", variable= IMDB_low, value=5).grid(row=8, column=3)
Radiobutton(root, label_rbli, text="> = 6", variable= IMDB_low, value=6).grid(row=9, column=3)
Radiobutton(root, label_rbli, text="> = 7", variable= IMDB_low, value=7).grid(row=10, column=3)
Radiobutton(root, label_rbli, text="> = 8", variable= IMDB_low, value=8).grid(row=11, column=3)
Radiobutton(root, label_rbli, text="> = 9", variable= IMDB_low, value=9).grid(row=12, column=3)

label_high_IMDB=Label(root, bd=3, text="Choose IMDB rating (lower than)", bg="grey", padx=20)
label_rbhi=Label()

label_high_IMDB.grid(row=1, column=4, padx=10, pady=10)
IMDB_high = StringVar(value=11)
Radiobutton(root, label_rbhi, text="Not important", variable= IMDB_high, value=11).grid(row=2, column=4)
Radiobutton(root, label_rbhi, text="< = 1", variable= IMDB_high, value=1).grid(row=3, column=4)
Radiobutton(root, label_rbhi, text="< = 2", variable= IMDB_high, value=2).grid(row=4, column=4)
Radiobutton(root, label_rbhi, text="< = 3", variable= IMDB_high, value=3).grid(row=5, column=4)
Radiobutton(root, label_rbhi, text="< = 4", variable= IMDB_high, value=4).grid(row=6, column=4)
Radiobutton(root, label_rbhi, text="< = 5", variable= IMDB_high, value=5).grid(row=7, column=4)
Radiobutton(root, label_rbhi, text="< = 6", variable= IMDB_high, value=6).grid(row=8, column=4)
Radiobutton(root, label_rbhi, text="< = 7", variable= IMDB_high, value=7).grid(row=9, column=4)
Radiobutton(root, label_rbhi, text="< = 8", variable= IMDB_high, value=8).grid(row=10, column=4)
Radiobutton(root, label_rbhi, text="< = 9", variable= IMDB_high, value=9).grid(row=11, column=4)
Radiobutton(root, label_rbhi, text="< = 10", variable= IMDB_high, value=10).grid(row=12, column=4)

button = tk.Button(root, text="Search", font=('Courier', 12), command=lambda:search_graph())
button.grid(row=13, column=5)

background_image = tk.PhotoImage(file='snacks.png')
background_label = tk.Label(root, image=background_image)
background_label.grid(row=14, column=6)

root.mainloop()
