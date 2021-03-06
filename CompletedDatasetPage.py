from tkinter import *
from tkinter.ttk import *
from HashtagFilter import *
import time

LARGE_FONT = ("Verdana", 12)


class CompletedDatasetPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Dataset Generation Complete!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        generate_new_dataset_btn = Button(self, text="Generate Another Dataset",
                            command=lambda: controller.restart())
        generate_new_dataset_btn.pack()

    def showData(self, dataset, hashtag):
        # TODO make this display more than one hashtag/dataset item
        sample_data = Label(self, text=dataset[0][0], font=LARGE_FONT)
        sample_data.pack()

        lbl_hashtags = Label(self, text=dataset[0][1])
        lbl_hashtags.pack()

        for ht in dataset[0][1]:
            #feedback_btn = Button(self, text=txt, command=lambda: HashtagFilter.user_feedback([hashtag, ht], False))
            Button(self, text="#" + ht + " Not Relevant",
                   command=lambda: HashtagFilter.user_feedback([hashtag, ht], False)).pack(side=LEFT)

