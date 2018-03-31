from read_xl import reading_data, reading_doc_header, reading_cell
from layout import pdf_creator, sheet_title, table_header_epic, table_line_epic, table_footer_epic, sheet_footer
from fpdf import FPDF
from in_words import num_in_words
  
"""loadig data from excel"""    
REF, REF_CUST, DESC, CMMF, EAN, QTY, AMOUNT =[], [], [], [], [], [], []
del_note  = '2515910440'
reading_data(REF, REF_CUST, DESC, CMMF, EAN, QTY, AMOUNT, del_note)

GSU_HEADER, DOC_HEADER, CLIENT_LIST = [], [], []
client = 'Epicentr' # make GUI input or in mention in docs
reading_doc_header(GSU_HEADER, DOC_HEADER, CLIENT_LIST,client)
order_n = reading_cell (2,60,del_note) # make GUI input or in mention in docs

sum = 345677.38
vat = str(round (sum / 6, 2)) + ' грн.'
result = ""
sum_in_word = num_in_words (sum)

"""creating pdf file"""
pdf = FPDF('L','mm','A4')
pdf_creator (pdf)
sheet_title (GSU_HEADER, DOC_HEADER, order_n, pdf)
table_header_epic (pdf)
for i in range (len(CMMF)):
    ref = str(REF[i])
    ref_cust = str(REF_CUST[i])
    num = str(i + 1)
    ean = str(EAN[i])
    qty = QTY[i]
    amount = AMOUNT[i]
    desc = str(DESC[i])
    table_line_epic (ref, ref_cust, num, ean, qty, desc, amount, pdf)
table_footer_epic (pdf)

pdf.cell(275, 3, '',0,1,'L') # empty line

pdf.cell(30, 4, 'Всього на суму із ПДВ:',0,0,'R')
pdf.cell(250, 4, sum_in_word ,0 ,1 ,'L')
pdf.cell(30, 4, 'ПДВ:',0,0,'R')
pdf.cell(30, 4, vat ,0 ,1 ,'L')

pdf.cell(70, 2, '',0,1,'L') # empty line

sheet_footer (pdf)

# y = pdf.get_y()
# print (y)

pdf.output('Outputs\Layout2.pdf', 'F')