###
## Plotter class is used to create graphical analysis report.
## Uses matplotlib for plotting the graph
## Author Delhi Durai
###


import matplotlib.pyplot as plt

class plotter:
    # Variable declaration
    txt_size =[]
    pat_size = []
    time = []
    memory = []

    def __init__(self):
        self.txt_size =[]
        self.pat_size = []
        self.time = []
        self.memory = []
    def clear(self):
        self.txt_size =[]
        self.pat_size = []
        self.time = []
        self.memory = []

    # Setter function that takes input text as a parameter
    def add_txt(self, txt):
        self.txt_size.append(len(txt))
    # Setter function that takes pattern as a parameter
    def add_pattern(self, patt):
        self.pat_size.append(len(patt))
    # Setter function that takes time as a parameter
    def add_time(self, time):
        self.time.append(time)
    # Setter function that takes memory usage as a parameter
    def add_usage(self, memory):
        self.memory.append(memory)
    # plot function to plot graph between textsize  and time in ms
    def plot_txt_time(self):
        self.plot_graph("Text Size","Time in ms",self.txt_size,self.time,"Text size vs Time graph")
    # plot function to plot graph between patternsize and time in ms
    def plot_pat_time(self):
        self.plot_graph("Pattern Size", "Time in ms",self.pat_size,self.time,"Pattern size vs Time graph")
    # plot function to plot graph between textsize  and Memory usage in mb
    def plot_txt_size(self):
        self.plot_graph("Text Size","Memory Usage MB",self.txt_size,self.memory,"Text Size vs Mem Usage  graph")
    # plot function to plot graph between patternsize  and Memory usage in mb
    def plot_pat_size(self):
        self.plot_graph("Pattern Size","Memory Usage MB",self.pat_size,self.memory,"Text Size vs Mem Usage  graph")

    #  function to plot x, y graph
    def plot_graph(self, x_label, y_label, x_value, y_value, title):

        # plotting the points
        plt.plot(x_value, y_value, 'o-')

        # naming the x axis
        plt.xlabel(x_label)
        # naming the y axis
        plt.ylabel(y_label)

        # giving a title to my graph
        plt.title(title)

        # function to show the plot
        plt.show()