import matplotlib.pyplot as plt
from ShellSort import liczylicz

def make_plot(lengths, times):
    """
    W miejscu lengths wpisz liste z długościami list, które chcesz mieć na wykresie,
    a  w miejscu times czasy pomiarów dla kolejno tych długości list.
    """
    plt.plot(lengths, times)
    plt.title('Czas wykonywania programu w zależności od wielkości listy')
    plt.ylabel('czas')
    plt.xlabel('wielkośc listy')
    plt.show()

make_plot([100, 200, 500, 1000, 2500, 5000, 10000, 100000, 1000000], liczylicz())

