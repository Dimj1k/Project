from src.read_data import Data
from src.third.visualization import grapharr, graphdf, colorize
from src.third.methodsVisualization import AndrewsCurve, parallel_coordinates, radviz


def main() -> None:
    file = input("Введите название файла excel с данными: ")
    if file == "quit":
        exit()
    try:
        bata = Data(file)
    except FileExistsError:
        print("Файл не найден")
        return main()
    print("Файл найден")
    method = int(input("Выберите метод (число 1, 2 или любое целое): "))
    print("Чтение данных с файла")

    if method == 1:
        bata.getdftoarrayxlsx(0, 1)
        a = AndrewsCurve()
        grapharr("Диаграмма Эндрюса", bata.Y, a.theta, [i for i in a.curves(bata.X)])
    elif method == 2:
        parallel_coordinates(bata.getdfxlsx(0, 1).df[bata.sheets[0]].join(bata.df[bata.sheets[1]]), bata.Yname,
                             color=colorize(bata.Y, "f"))
        graphdf(bata.Y, "Параллельные координаты")
    else:
        radviz(bata.getdfxlsx(0, 1).df[bata.sheets[0]].join(bata.df[bata.sheets[1]]), bata.Yname,
               color=colorize(bata.Y, "f"))
        graphdf(bata.Y, "RadViz")
    return againli()


def againli() -> None:
    again = input("Выйти из программы? (y/n): ")
    if again.lower() == "n" or again.lower() == "т":
        return main()
    elif again.lower() == "y" or again.lower() == "н":
        exit()
    return againli()


if __name__ == "__main__":
    main()
