python 3.11.0

The aim of this program is to autofill the lognav of SmartAviation flight Approval in order to gain some time
such avoiding to fill all the navlog by hand.
(It can be adjusted to any kind of navlog, some adjustements will be however needed, see "Note" at the bottom of this document)

It requires the following libraries :
fitz
csv
re

You have to 

1) Export the flight log of skydemon as a csv, using the columns : 
"Show RNAV vectors, Show cruise speed, Cumulative distances, Show position, Show magnetic track, perform wind calculations"
If you don't have these columns ticked, you will have to adapt slightly the code in order to mke it work

2) In your folder, put :
your virgin pdf Flight Approval (navlog) with the folowing name : Flight approval_ver1.0.pdf
the skydemon csv navlog with the following name : skydemonFlightLog.csv
(you can change the name of these file in the pdfFiller.py, line 7/6)
pdfFiller.py

3) In pdfFiller.py set the number of lines per sheet your navlog need

3) Go to your python folder and Execute the following command:
python ../path/to/your/folder/pdfFiller.py
(you have to change the name of the path to your folder in pdfFiller.py : line 5)

4)The script will generate a file called output.pdf with all the lines filled. If there are more lines to fill than
your navlog is able to handle, a new page in the pdf will be added with the lines completed!
(you can change the name of the output file in pdfFiller.py line 8)

You just have to print it and enjoy


Note : 
If the lines doesn't fit very well your navlog, it may be because of your screen size.
You may have to adjust the pdfFiller.py and play with the values of
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

In order to make it fit well.


-If you want to fill an other type of navlog, it's totally doable,

You will only have to adjust the value of each columns.


-If you didn't export the good columns from the skydemon navlog you will not have the great lines filled
You can make the program adjust to the configuration of your skydemon navlog csv, by enter the proper column
by modifying the following parameters : 

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