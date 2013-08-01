
#筛选冒烟用例
import xlrd
import xlwt
from xlutils.copy import copy
import time

try:
	filename='C:\测试用例.xls'
	data=xlrd.open_workbook(filename)
	sheetnames=data.sheet_names()
	#创建一个新的excel
	newfilename=xlwt.Workbook()
	newsheet=newfilename.add_sheet('1')
	newrow=0
	#循环读取被筛选excel的sheet
	for sheetname in sheetnames:
		sheet=data.sheet_by_name(sheetname)
		rows=sheet.nrows
		for row in range(rows):
			value=sheet.row_values(row)
			if value[5]=='P1':  #如果优先级被标为“P1”，则筛选出来               
				newcol=0
				for newvalue in value:
					newsheet.write(newrow,newcol,newvalue)
					newcol=newcol+1
				newrow=newrow+1
		newfilename.save('ok.xls')
finally:
	print('ok')
time.sleep(5)
