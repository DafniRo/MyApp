import matplotlib.pyplot as plt

class Board:
    def __init__(self):
        pass

    def makeBoard(self): 
        fig, ax = plt.subplots()
        for y in range(9):
            ax.axhline(y, color = 'black')
        for x in range(9):
            ax.axvline(x, color = 'black')

        ax.set_xlim(0,8)
        ax.set_ylim(0,8)
        ax.axis('off')

        ax.set_xticks(range(8))
        ax.set_yticks(range(8))
        ax.set_xticklabels(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        ax.set_yticklabels(range(8,0,-1))
        plt.show