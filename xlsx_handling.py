import xlrd, xlsxwriter
import csv
import random

def read_dataset(file_loc):
    workbook = xlrd.open_workbook(file_loc)
    worksheet = workbook.sheet_by_index(0)

    dataset = []
    for row in range(1, worksheet.nrows):
        _row = []
        for col in range(worksheet.ncols):
            _row.append(worksheet.cell_value(row,col))
        dataset.append(_row)
    return dataset

def write_data(file_loc, data):
    # to write tfidf matrix
    workbook = xlsxwriter.Workbook(file_loc)
    worksheet = workbook.add_worksheet()

    # initialize row and col
    row = 1
    col = 1
    for _row in data:
        for _col in _row:
            worksheet.write_number(row, col % len(_row), _col)
            col += 1
        row += 1
    workbook.close()

def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

