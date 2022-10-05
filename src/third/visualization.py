import matplotlib.pyplot as plt
from numpy import array, unique, empty, int32, linspace, append


def lenhex(hexcol: hex) -> str:
    return "#" + "0" * (4 - len(hexcol)) + hexcol[2:]


def strtohexcolor(labels: array, alpha: str) -> list:
    return [lenhex(hex(i)) + alpha for i in append(linspace(0x008, 0xf8c,
                                                            len(labels) // 2 + len(labels) % 2, dtype=int32),
                                                   linspace(0x0be, 0xf00,
                                                            len(labels) // 2,
                                                            dtype=int32))]


def inttohexcolor(labels: array, alpha: str) -> list:
    b = list(zip([lenhex(hex(i)) + alpha for i in append(linspace(0x008, 0xf8c,
                                                                  len(labels) // 2 + len(labels) % 2, dtype=int32),
                                                         linspace(0x0be, 0xf00,
                                                                  len(labels) // 2,
                                                                  dtype=int32))], labels))
    b.sort(key=lambda x: x[1])
    return list(zip(*b))[0]


def colorize(y: array, alpha: str) -> list:
    return strtohexcolor(unique(y), alpha) if y.dtype == "object" else inttohexcolor(unique(y), alpha)


def grapharr(method: str, legend: array, x: array, fx: list,
             name: str = "Figure", alpha: str = "f", width: float = 1.5) -> None:
    plt.xlim(x.min(), x.max())
    plt.title(method)
    plt.get_current_fig_manager().canvas.set_window_title(name)
    uniquelegend = unique(legend)
    colors = colorize(uniquelegend, alpha)
    colorlegends = empty(len(legend), dtype=object)
    for i, el in enumerate(uniquelegend):
        colorlegends[legend == el] = colors[i]
    print(list(zip(uniquelegend, colors)))
    del colors, uniquelegend
    uniq = list()
    if legend.dtype == "object" or legend.dtype == "int64":
        for i, el in enumerate(fx):
            plt.plot(x, el, c=colorlegends[i], linewidth=width,
                     label=legend[i] if legend[i] not in uniq else "")
            None if legend[i] in uniq else uniq.append(legend[i])
        plt.legend(loc=0)
    else:
        [plt.plot(x, el, c=colorlegends[i], linewidth=width) for i, el in enumerate(fx)]
    plt.show()


def graphdf(Y, method: str, name: str = "Figure") -> None:
    plt.title(method)
    plt.get_current_fig_manager().canvas.set_window_title(name)
    plt.gca().legend_.remove() if Y.dtype != "object" else None
    plt.show()
