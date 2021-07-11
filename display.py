from tkinter import Tk, Button

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

from runSimulation import runSimulation


def display():

    def plotStockGraph():

        # the figure that will contain the plot
        fig = Figure()

        # adding the subplot
        plt = fig.add_subplot(xlabel="Trading Days Simulated",
                              ylabel="Investment Value")

        # plotting the graph
        plt.plot(runSimulation())

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                   master=window)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                       window)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    # The main tkinter window
    window = Tk()

    # setting the title and
    window.title('Stock Simulation')

    # setting the dimensions of
    # the main window
    window.geometry("600x600")

    # button that would displays the plot
    plot_button = Button(master=window,
                         command=plotStockGraph,
                         height=2,
                         width=10,
                         text="Simulate")
    # place the button
    # into the window
    plot_button.pack()

    # run the gui
    window.mainloop()


if __name__ == "__main__":
    display()
