#Продвинутый метод повышения контрастности. Выравнивание гистограммы
#Для создания идеального контрастного изображения нужно чтобы функция распределения, описыващая гистограмму стремилась к линейной
#f(x) = round((cdf(x) - cdfmin/(kpix-1))*255) преобразует функцию распределения яркости близкой к линейной
