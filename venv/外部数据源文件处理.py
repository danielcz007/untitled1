#http://www.python-excel.org/
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
#实例化对象
wb = Workbook()
#创建表格
dest_filename = 'empty_book.xlsx'
#实例化一个对象接收文件
ws1 = wb.active
#对象title，sheet页的名称
ws1.title = "range names"
#row=行 创建一个39行，从第一行到40行。每行有600列
for row in range(1, 40):
    ws1.append(range(600))
#创建一个新的sheet页，P
ws2 = wb.create_sheet(title="Pi")
#输出sheet页Pi中，第F列，第5行的值
ws2['F5'] = 3.14
#创建sheet3Data，
ws3 = wb.create_sheet(title="Data")
for row in range(10, 20):
    for col in range(27, 54):
        #cell方法，column=列，row=行，value=单元格对应值，{0}和format（）格式化输出，get_column_letter(col)获取对应列的值
        _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
print(ws3['AA10'].value)

ws4 = wb.create_sheet(title="Daniel")
for i in range(1,30):
    for j in range(1,30):
        #自我拓展，把每个单元格的值改成列+行，首先对单元格的值进行赋值，get_column_letter(j)拼接上行号i，由于是字符串行所以需要对行号i进行转换格式str（）
        columnraow = get_column_letter(j)+str(i)
        ws4.cell(column=j,row=i,value=columnraow)i
print(ws4['F10'].value)

wb.save(filename=dest_filename)