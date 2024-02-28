import fitz  # import PyMuPDF
import csv
import re

FOLDER_PATH = "D:\\Developpement\\flightApprovalFillerSmartAviation\\"
SKYDEMON_CSV_NAVLOG = "skydemonFlightLog.csv"
VIRGIN_PDF_NAVLOG_TO_FILL = "Flight approval_ver1.0.pdf"
OUTPUT_FILENAME = "output.pdf"
NB_LINE_PER_SHEET = 9

COLROUTE = 0
COLRADIAL = 1
COLTRACKT = 6
COLTRACKM = 7
COLHDGM = 9
COLDIST = 11
COLGS = 10
COLETE = 12
COLMSA = 3
COLALT = 4

X_COL_ROUTE_RADIAL = 14
Y_COL_ROUTE_RADIAL = 270.5
X_COL_TRACKT = 95
Y_COL_TRACKT = 268
X_COL_TRACKM = 125
Y_COL_TRACKM = 268
X_COL_HDGM = 183
Y_COL_HDGM = 268
X_COL_DIST = 250
Y_COL_DIST = 268
X_COL_GS = 281
Y_COL_GS = 268
X_COL_ETE = 307
Y_COL_ETE = 268
X_COL_MSA = 355
Y_COL_MSA = 268
X_COL_ALT = 390
Y_COL_ALT = 268

OFFSET_BETWEEN_LINES = 29

def parseSkyDemonNavLog():
	myPath = FOLDER_PATH
	filename = myPath+SKYDEMON_CSV_NAVLOG
	
	last_line = 0;
	with open(filename, encoding="utf8") as file_obj: 
	    reader_obj = csv.reader(file_obj) 
	    for row in reader_obj:
	    	if row == [] :
	    		break;
	    	last_line = last_line + 1;
	    last_line = last_line - 1;
	
	with open(filename, encoding="utf8") as file_obj: 
	    reader_obj = csv.reader(file_obj) 
	    i = 0;
	    myPath = FOLDER_PATH;
	    filename = myPath+VIRGIN_PDF_NAVLOG_TO_FILL;
	    doc = fitz.open(filename, filetype="pdf");  # open PDF with PyMuPDF
	    doc.fullcopy_page(0);
	    n_page = 1;
	    page = doc[n_page];

	    x_col1 = X_COL_ROUTE_RADIAL;
	    y_col1 = Y_COL_ROUTE_RADIAL;

	    x_col2 = X_COL_TRACKT;
	    y_col2 = Y_COL_TRACKT;

	    x_col3 = X_COL_TRACKM;
	    y_col3 = Y_COL_TRACKM;

	    x_col4 = X_COL_HDGM;
	    y_col4 = Y_COL_HDGM;

	    x_col5 = X_COL_DIST;
	    y_col5 = Y_COL_DIST;

	    x_col6 = X_COL_GS;
	    y_col6 = Y_COL_GS;

	    x_col7 = X_COL_ETE;
	    y_col7 = Y_COL_ETE;

	    x_col8 = X_COL_MSA;
	    y_col8 = Y_COL_MSA;

	    x_col9 = X_COL_ALT;
	    y_col9 = Y_COL_ALT;
	    
	    iline = 0;
	    for row in reader_obj:
	    	if i>= 2 :
	    		if i<last_line:#last_line:
	    			col_i = 0;
	    			final_col_1 = "";
	    			if iline%NB_LINE_PER_SHEET == 0 and iline != 0:
		    			doc.fullcopy_page(0);
		    			n_page = n_page+1;
		    			page = doc[n_page];
		    			x_col1 = X_COL_ROUTE_RADIAL;
		    			y_col1 = Y_COL_ROUTE_RADIAL;

		    			x_col2 = X_COL_TRACKT;
		    			y_col2 = Y_COL_TRACKT;

		    			x_col3 = X_COL_TRACKM;
		    			y_col3 = Y_COL_TRACKM;

		    			x_col4 = X_COL_HDGM;
		    			y_col4 = Y_COL_HDGM;

		    			x_col5 = X_COL_DIST;
		    			y_col5 = Y_COL_DIST;

		    			x_col6 = X_COL_GS;
		    			y_col6 = Y_COL_GS;

		    			x_col7 = X_COL_ETE;
		    			y_col7 = Y_COL_ETE;

		    			x_col8 = X_COL_MSA;
		    			y_col8 = Y_COL_MSA;

		    			x_col9 = X_COL_ALT;
		    			y_col9 = 268;
	    			for col in row :

	    				if col_i == COLROUTE:
	    					final_col_1 = col;
	    				if col_i == COLRADIAL :
	    					final_col_1 = final_col_1 + "\n" + col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col1,y_col1,x_col1+100,y_col1+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col1 = y_col1 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLTRACKT :
		    				final_col_1 = col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col2,y_col2,x_col2+100,y_col2+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col2 = y_col2 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLTRACKM :
		    				final_col_1 = col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col3,y_col3,x_col3+100,y_col3+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col3 = y_col3 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLHDGM :
		    				final_col_1 = col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col4,y_col4,x_col4+100,y_col4+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col4 = y_col4 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLDIST :
		    				final_col_1 = re.sub(r'\(.+\)', '', col)+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col5,y_col5,x_col5+100,y_col5+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col5 = y_col5 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLGS :
		    				final_col_1 = col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col6,y_col6,x_col6+100,y_col6+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col6 = y_col6 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLETE :
		    				final_col_1 = col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col7,y_col7,x_col7+100,y_col7+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col7 = y_col7 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLMSA :
		    				final_col_1 = col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col8,y_col8,x_col8+100,y_col8+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col8 = y_col8 + OFFSET_BETWEEN_LINES;
		    			if col_i == COLALT :
		    				final_col_1 = col+"\n";
		    				print(final_col_1);
		    				text_rectangle = fitz.Rect(x_col9,y_col9,x_col9+100,y_col9+70)
		    				page.insert_textbox(text_rectangle, f'{final_col_1}');
		    				y_col9 = y_col9 + OFFSET_BETWEEN_LINES;
		    			col_i = col_i+1;
		    		iline = iline + 1;
		    	else:
		    		break;
	    	i = i+1;
	    doc.delete_page(0);
	    doc.save(myPath+OUTPUT_FILENAME);
	    print("Done!");

parseSkyDemonNavLog()
