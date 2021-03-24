# Домашнее задание 2. Вырожденный графический редактор на tkinter

Ссылка на страницу с заданием: [uneex.org/LecturesCMC/PythonDevelopment2021/05_SshAndSmartWidgents](https://uneex.org/LecturesCMC/PythonDevelopment2021/05_SshAndSmartWidgents)

## Требования к заданию

Имеет два окна — текстовое и графическое
Обязаны присутствовать координаты, ширина границы, цвет границы и цвет заливки

* В графическом окне:
    - Нажатие мышью в пустое место и движение с нажатой кнопкой создаёт овал и меняет его размер
    - Нажатие на существующий овал и движение с нажатой кнопкой перемещает этот овал
    - В текстовом окне параллельно формируется описание картинки на некотором языке. Синтаксис языка придумайте сами, можно взять из семинара.

* При изменении текста
    - Если в нём нет ошибок, рисуются все фигуры
    - Если ошибки есть, ошибочные строчки раскрашиваются в красный цвет
    - Допустимо для обновления одного окна из другого использовать две кнопки
 
 ## Реализованные дополнительные функции
 * перемещение по скроллу мыши (вериткальное и горизонтальное через shift)
 * перемещение фигур по щелчку на фигуре
 * удаление фигуры по щелчку правой кнопкой мыши
  
 ## Пример работы приложения

<img src='https://github.com/dronperminov/PythonDevelopment2021/blob/main/05_SshAndSmartWidgents/examples/ellipse_drawer.gif' />

## Скриншоты работы приложения

<table>
  <tr>
    <td width='33%'><img src='https://github.com/dronperminov/PythonDevelopment2021/blob/main/05_SshAndSmartWidgents/examples/example_init.png' /></td>
    <td width='33%'><img src='https://github.com/dronperminov/PythonDevelopment2021/blob/main/05_SshAndSmartWidgents/examples/example_drawed.png' /></td>
    <td width='33%'><img src='https://github.com/dronperminov/PythonDevelopment2021/blob/main/05_SshAndSmartWidgents/examples/example_error.png' /></td>
  </tr>
</table>