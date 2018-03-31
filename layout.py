from fpdf import FPDF

W = (10, 17, 65, 17, 25, 10, 10, 10, 10, 12, 20, 20, 10, 20, 20)
print ('table len = ',sum(W))

def pdf_creator(pdf):# creation of pdf layout, loading fonts, add one page
    #pdf = FPDF('L','mm','A4')
    pdf.add_page()
    pdf.add_font('Arial2', '', './fonts/arial.ttf', uni=True) 
    pdf.add_font('Arial2', 'I', './fonts/ariali.ttf', uni=True) 
    pdf.add_font('Arial2', 'B', './fonts/arialbd.ttf', uni=True) 
    pdf.set_font('Arial2', '', 8) # fpdf.set_font(family, style = '', size = 0)
    
def sheet_title (GSU_HEADER, DOC_HEADER, order_n, pdf): # 275 x 69mm
    pdf.cell(200, 5, 'Товариство з обмеженою відповідальністю Груп СЕБ Україна 02121, '
    'Київ, ул. Харьківське  шоссе 201\\203. тел 044-300-11-03',0,1,'L') 

    pdf.cell(70, 3, '',0,1,'L')
    
    pdf.set_font('Arial2', 'B', 8)
    pdf.cell(40, 5, 'Покупець',0,0,'R') 

    pdf.cell(200, 5, DOC_HEADER[0],0,2,'L') 
    
    pdf.set_font('Arial2', '', 8)
    pdf.cell(200, 5, DOC_HEADER[1],0,2,'L') 
    pdf.cell(200, 5, DOC_HEADER[2],0,2,'L') 
    
    pdf.set_font('Arial2', 'B', 8)
    pdf.cell(30, 5, 'Місце доставки: ',0,0,'L')
    pdf.cell(200, 5, DOC_HEADER[3],0,2,'L') 

    pdf.cell(70, 3, '',0,1,'L')
    pdf.cell(40, 5, 'Постачальник:',0,0,'R')
    pdf.cell(200, 5, GSU_HEADER[0],0,2,'L') 
    pdf.set_font('Arial2', '', 8)
    pdf.cell(200, 5, GSU_HEADER[1],0,2,'L')
    pdf.cell(150, 5, GSU_HEADER[2],0,0,'L')
    pdf.cell(50, 5, 'Місце складання :м. Київ, Харківське шоссе 201/203 ',0,1,'L')

    pdf.cell(70, 3, '',0,1,'L')

    pdf.set_font('Arial2', 'B', 8)
    pdf.cell (40, 5, 'Пiдстава: Договiр № ',0,0,'R')
    pdf.cell (50, 5, str(DOC_HEADER[4])    ,'B',0,'L') 
    pdf.cell (50, 5, '',0,0,'L') 
    pdf.set_font('Arial2', '', 8)
    pdf.cell (50, 5, 'Номер замовлення: '  ,0,0,'R')
    pdf.cell (50, 5, str(order_n)         ,'B',1,'L')

    pdf.cell(70, 3, '',0,1,'L')
  
def table_header_epic(pdf):  #шапка таблицы 275 x 20mm
    """Первая строка"""
    pdf.cell(W[0], 4, '','TLR',0,'C') # 1:10
    pdf.cell(W[1] + W[2] + W[3] + W[4], 4, 'Товар', 1, 0, 'C') # 2:115
    pdf.cell(W[5], 4, 'Оди-', 'TLR', 0, 'C')  # 3:125
    pdf.cell(W[6] + W[7], 4, 'Кількість', 1, 0, 'C')  # 4:145
    pdf.cell(W[8], 4, 'Оди-', 'TLR', 0, 'C')  # 4:155
    pdf.cell(W[9], 4, '', 'TLR', 0, 'C')  # 6:170
    pdf.cell(W[10], 4, '', 'TLR', 0, 'C')  # 7:190
    pdf.cell(W[11], 4, 'Сума без', 'TLR', 0, 'C')  # 8:215
    pdf.cell(W[12] + W[13], 4, 'ПДВ', 1, 0, 'C')  # 9:250
    pdf.cell(W[14], 4, 'Сума з', 'TLR', 1, 'C')  # 10:275
    """Вторая строка"""
    pdf.cell(W[0], 4, 'Номер','LR',0,'C') # 1:10
    pdf.cell(W[1], 4, 'Артикул', 'LR', 0, 'C') # 2:25
    pdf.cell(W[2], 4, 'Найменування, харакетиристики,', 'LR', 0, 'C') # 3:85
    pdf.cell(W[3], 4, 'Код', 'LR', 0, 'C')  # 4:100
    pdf.cell(W[4], 4, 'Штрих-код', 'LR', 0, 'C')  # 4:115
    pdf.cell(W[5], 4, 'ниця', 'LR', 0, 'C')  # 6:125
    pdf.cell(W[6], 4, '', 'LR', 0, 'C')  # 7:135
    pdf.cell(W[7], 4, 'в одно-', 'LR', 0, 'C')  # 8:145
    pdf.cell(W[8], 4, 'ниця', 'LR', 0, 'C')  # 9:155
    pdf.cell(W[9], 4, 'Кількість', 'LR', 0, 'C')  # 10:170
    pdf.cell(W[10], 4, 'Ціна,', 'LR', 0, 'C')  # 11:190
    pdf.cell(W[11], 4, 'урахування', 'LR', 0, 'C')  # 12:215
    pdf.cell(W[12], 4, 'ставка,', 'LR', 0, 'C')  # 13:225
    pdf.cell(W[13], 4, 'сума', 'LR', 0, 'C')  # 14:250
    pdf.cell(W[14], 4, 'урахуванням', 'LR', 1, 'C')  # 15:275
    """Третья строка"""
    pdf.cell(W[0], 4, 'п/п','LR',0,'C') # 1:10
    pdf.cell(W[1], 4, '', 'LR', 0, 'C') # 2:25
    pdf.cell(W[2], 4, 'сорт артикулу,', 'LR', 0, 'C') # 3:85
    pdf.cell(W[3], 4, 'артикулу', 'LR', 0, 'C')  # 4:100
    pdf.cell(W[4], 4, '', 'LR', 0, 'C')  # 4:115
    pdf.cell(W[5], 4, 'вимі-', 'LR', 0, 'C')  # 6:125
    pdf.cell(W[6], 4, 'місць', 'LR', 0, 'C')  # 7:135
    pdf.cell(W[7], 4, 'му', 'LR', 0, 'C')  # 8:145
    pdf.cell(W[8], 4, 'вимі-', 'LR', 0, 'C')  # 9:155
    pdf.cell(W[9], 4, '', 'LR', 0, 'C')  # 10:170
    pdf.cell(W[10], 4, 'грн.коп', 'LR', 0, 'C')  # 11:190
    pdf.cell(W[11], 4, 'ПДВ,', 'LR', 0, 'C')  # 12:215
    pdf.cell(W[12], 4, '%,', 'LR', 0, 'C')  # 13:225
    pdf.cell(W[13], 4, 'грн.коп', 'LR', 0, 'C')  # 14:250
    pdf.cell(W[14], 4, 'ПДВ,', 'LR', 1, 'C')  # 15:275
    """Четвертая строка"""
    pdf.cell(W[0], 4, '','LR',0,'C') # 1:10
    pdf.cell(W[1], 4, '', 'LR', 0, 'C') # 2:25
    pdf.cell(W[2], 4, '', 'LR', 0, 'C') # 3:85
    pdf.cell(W[3], 4, '', 'LR', 0, 'C')  # 4:100
    pdf.cell(W[4], 4, '', 'LR', 0, 'C')  # 4:115
    pdf.cell(W[5], 4, 'ру', 'LR', 0, 'C')  # 6:125
    pdf.cell(W[6], 4, '', 'LR', 0, 'C')  # 7:135
    pdf.cell(W[7], 4, 'місці', 'LR', 0, 'C')  # 8:145
    pdf.cell(W[8], 4, 'ру', 'LR', 0, 'C')  # 9:155
    pdf.cell(W[9], 4, '', 'LR', 0, 'C')  # 10:170
    pdf.cell(W[10], 4, '', 'LR', 0, 'C')  # 11:190
    pdf.cell(W[11], 4, 'грн.коп', 'LR', 0, 'C')  # 12:215
    pdf.cell(W[12], 4, '', 'LR', 0, 'C')  # 13:225
    pdf.cell(W[13], 4, '', 'LR', 0, 'C')  # 14:250
    pdf.cell(W[14], 4, 'грн.коп', 'LR', 1, 'C')  # 15:275
    """Пятая строка"""
    pdf.cell(W[0], 4, '1',1,0,'C') # 1:10
    pdf.cell(W[1], 4, '2', 1, 0, 'C') # 2:25
    pdf.cell(W[2], 4, '3', 1, 0, 'C') # 3:85
    pdf.cell(W[3], 4, '4', 1, 0, 'C')  # 4:100
    pdf.cell(W[4], 4, '5', 1, 0, 'C')  # 4:115
    pdf.cell(W[5], 4, '6', 1, 0, 'C')  # 6:125
    pdf.cell(W[6], 4, '7', 1, 0, 'C')  # 7:135
    pdf.cell(W[7], 4, '8', 1, 0, 'C')  # 8:145
    pdf.cell(W[8], 4, '9', 1, 0, 'C')  # 9:155
    pdf.cell(W[9], 4, '10', 1, 0, 'C')  # 10:170
    pdf.cell(W[10], 4, '11', 1, 0, 'C')  # 11:190
    pdf.cell(W[11], 4, '12', 1, 0, 'C')  # 12:215
    pdf.cell(W[12], 4, '13', 1, 0, 'C')  # 13:225
    pdf.cell(W[13], 4, '14', 1, 0, 'C')  # 14:250
    pdf.cell(W[14], 4, '15', 1, 1, 'C')  # 15:275

def table_line_epic(ref, ref_cust, num, ean, qty, desc, amount, box, pdf):
    pdf.cell (W[0],  4, num                                          , 'LR',0,'C') # 1:10 / Номер пп
    pdf.cell (W[1],  4, ref_cust                                     , 'LR', 0, 'C') # 2:25 / Артикул
    pdf.cell (W[2],  4, desc                                         , 'LR', 0, 'L') # 3:85 / Наименование
    pdf.cell (W[3],  4, ref                                          , 'LR', 0, 'C')  # 4:100 / код артикула
    pdf.cell (W[4],  4, ean                                          , 'LR', 0, 'C')  # 4:115 / EAN
    pdf.cell (W[5],  4, 'кор.'                                       , 'LR', 0, 'C')  # 6:125 / одиниця виміру
    pdf.cell (W[6],  4, str(format(box,',d')) + ' '                  , 'LR', 0, 'C')  # 7:135 / місць
    pdf.cell (W[7],  4, str(format(qty//box,',d')) + ' '             , 'LR', 0, 'C')  # 8:145 / в одному місці
    pdf.cell (W[8],  4, 'шт.'                                        , 'LR', 0, 'C')  # 9:155 / одиниця виміру
    pdf.cell (W[9],  4, str(format(qty,',d')) + ' '                  , 'LR', 0, 'R')  # 10:170 / кількість
    pdf.cell (W[10], 4, str(format(round(amount/qty,2),',.2f')) + ' ', 'LR', 0, 'R')  # 11:190 / ціна
    pdf.cell (W[11], 4, str(format(amount, ',.2f')) + ' '            , 'LR', 0, 'R')  # 12:215 / сума без ПДВ
    pdf.cell (W[12], 4, '20%'                                        , 'LR', 0, 'C')  # 13:225 / ставка
    pdf.cell (W[13], 4, str(format(round(amount/5,2),',.2f')) + ' '  , 'LR', 0, 'R')  # 14:250 / сума ПДВ
    pdf.cell (W[14], 4, str(format(round(amount*1.2),',.2f')) + ' '  , 'LR', 1, 'R')  # 15:275 / сума з ПДВ
   
def table_header_line(pdf): # 275 x 4 mm
    pdf.cell(W[0], 4, '1',1,0,'C') # 1:10
    pdf.cell(W[1], 4, '2', 1, 0, 'C') # 2:25
    pdf.cell(W[2], 4, '3', 1, 0, 'C') # 3:85
    pdf.cell(W[3], 4, '4', 1, 0, 'C')  # 4:100
    pdf.cell(W[4], 4, '5', 1, 0, 'C')  # 4:115
    pdf.cell(W[5], 4, '6', 1, 0, 'C')  # 6:125
    pdf.cell(W[6], 4, '7', 1, 0, 'C')  # 7:135
    pdf.cell(W[7], 4, '8', 1, 0, 'C')  # 8:145
    pdf.cell(W[8], 4, '9', 1, 0, 'C')  # 9:155
    pdf.cell(W[9], 4, '10', 1, 0, 'C')  # 10:170
    pdf.cell(W[10], 4, '11', 1, 0, 'C')  # 11:190
    pdf.cell(W[11], 4, '12', 1, 0, 'C')  # 12:215
    pdf.cell(W[12], 4, '13', 1, 0, 'C')  # 13:225
    pdf.cell(W[13], 4, '14', 1, 0, 'C')  # 14:250
    pdf.cell(W[14], 4, '15', 1, 1, 'C')  # 15:275

def table_footer (sum_qty, sum_amount, pdf): # 275 x 4 mm
    pdf.cell(W[0] + W[1] + W[2] + W[3] + W[4], 4, 'Всього:',1,0,'C') 
    pdf.cell(W[5], 4, '', 1, 0, 'C')
    pdf.cell(W[6], 4, '', 1, 0, 'C')  
    pdf.cell(W[7], 4, '', 1, 0, 'C')  
    pdf.cell(W[8], 4, '', 1, 0, 'C')  
    pdf.cell(W[9], 4, str(format(sum_qty,',d')) + ' ', 1, 0, 'R')  
    pdf.cell(W[10], 4, '', 1, 0, 'C')  
    pdf.cell(W[11], 4, str(format(sum_amount,',.2f')) + ' ', 1, 0, 'R')  
    pdf.cell(W[12], 4, '', 1, 0, 'C')  
    pdf.cell(W[13], 4, str(format(round(sum_amount/5,2),',.2f') + ' '), 1, 0, 'R')  
    pdf.cell(W[14], 4, str(format(round(sum_amount*1.2,2),',.2f') + ' '), 1, 1, 'R')  

def sheet_footer (pdf): # 274 x 86 mm
    pdf.cell(137, 7, '',0,0,'L')
    pdf.cell(137, 7, 'За дорученням № ___________________ від "______" _________________________ ___________  р.',0,1,'L')
    pdf.cell(137, 7, '',0,0,'L')
    pdf.cell(137, 7, 'Виданої: _____________________________________________________________________________',0,1,'L')
    pdf.cell(137, 7, '',0,0,'L')
    pdf.cell(137, 7, '______________________________________________________________________________________',0,1,'L')
    pdf.cell(137, 7, 'Вiдпуск дозволив: _________________________  _______________________  __________________',0,0,'L')
    pdf.cell(137, 7, 'Вантаж прийняв: ___________________________  _______________________  __________________',0,1,'L')
    pdf.cell(137, 7, 'Відвантажив:    ___________________________  _______________________  __________________',0,0,'L')
    pdf.cell(137, 7, 'Одержувач ванажу: _________________________  _______________________  __________________',0,1,'L')
    pdf.cell(137, 7, 'М.П.',0,0,'C')
    pdf.cell(137, 7, 'М.П',0,1,'L')

def up_table_line (del_note, doc_date, pdf):
    pdf.cell(275, 3, '', 0, 1, 'L') # empty line
    pdf.set_font('Arial2', 'B', 12)
    pdf.cell(137, 7, 'Видаткова накладна № ', 0, 0, 'R')
    pdf.cell(50, 7, str(del_note) , 0, 0, 'L')
    pdf.cell(50, 7, '    від    ' + str(doc_date) + '   р.' , 0, 1, 'L')
    pdf.set_font('Arial2', '', 8)
    pdf.cell(275, 3, '', 0, 1, 'L') # empty line




# sheet_title()
# table_header_epic()
# for i in range (5):
#     table_line_epic()
# table_footer_epic()

# pdf.output('Outputs\Layout.pdf', 'F')

