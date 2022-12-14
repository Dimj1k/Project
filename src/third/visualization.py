import matplotlib.pyplot as plt
from numpy import array, unique, empty, int32, linspace, append


def lenhex(hexcol: hex) -> str:
    return "#" + "0" * (5 - len(hexcol)) + hexcol[2:]


def tohexcolor(labels: array, alpha: str) -> list:
    lens = len(labels)
    a = [lens // 3, (lens - lens // 3) // 2 + (lens - lens // 3) % 2, (lens - lens // 3) // 2] \
        if lens != 1 else [0, 0, 1]
    return [lenhex(hex(i)) + alpha for i in append(append(linspace(0x00f, 0x0f8, a[0], dtype=int32),
                                                          append(linspace(0x0fa, 0x60f, a[1] // 2, dtype=int32),
                                                                 linspace(0x70f, 0xa50, a[1] // 2 + a[1] % 2,
                                                                          dtype=int32))),
                                                   linspace(0xfe0, 0xd00, a[2], dtype=int32))]


def colorize(y: array, alpha: str) -> list:
    return tohexcolor(unique(y), alpha)


def grapharr(method: str, legend: array, x: array, fx: list,
             name: str = "Figure", alpha: str = "f") -> None:
    plt.xlim(x.min(), x.max())
    plt.title(method)
    plt.get_current_fig_manager().canvas.set_window_title(name)
    colors = colorize(legend, alpha)
    colorlegends = empty(len(legend), dtype=object)
    for i, el in enumerate(unique(legend)):
        colorlegends[legend == el] = colors[i]
    del colors
    uniq = list()
    if legend.dtype == "object":
        for i, el in enumerate(fx):
            plt.plot(x, el, c=colorlegends[i],
                     label=legend[i] if legend[i] not in uniq else "")
            None if legend[i] in uniq else uniq.append(legend[i])
        plt.legend(loc=0)
    else:
        [plt.plot(x, el, c=colorlegends[i]) for i, el in enumerate(fx)]
    plt.show()


def graphdf(Y, method: str, name: str = "Figure") -> None:
    plt.title(method)
    plt.get_current_fig_manager().canvas.set_window_title(name)
    plt.gca().legend_.remove() if Y.dtype != "object" else None
    plt.show()
