#Корреляция и свертка. Корреляция размывает изображение. Данная операция принимает два изображения: исходное и ядро. Все элементы ядра равны 1/9, значит сумма элементов ядра равна единице, а значит яркость изображения не поменяется. Поэлементно умножаем два изображения.
#Корреляция и свертка - одно и то же, но в операции свертки ядро зеркалится.
#Нужно научиться накладывать ядро на углы, чтобы операция свертки не выполнялась для краев изображение. Первый - заполнить нулями края изображения( расширить массив). Второй  - продублировать значения на крае изображения за границы изображения.Третий - зеркалирование границы( отражаем  массив за его границу). Для быстрого выполнения операции свертки нужно прибегнутьк  интегральному изображению. Это изображение, по размерам равное исходному, но в каждом пикселе записана сумма всех пикселей от левого верхнего угла до угла, соответствующего данному пикселю. С помощью интегрального выражения находим сумму окресности и накалдываем фильтр