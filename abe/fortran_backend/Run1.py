#!/usr/local/bin/python

import cgi, cgitb, os, string, random, datetime, glob, locale
from string import split,join

def run1(ystime):

  path = './tmp/' + ystime + '/'
  cpCmd = 'cp ' + 'stepl '  + path
  os.system(cpCmd)

  os.chdir(path)

  cpCmd = 'cp ' + 'cligen/pcp.txt '  + '.'
  os.system(cpCmd)

  #----------------------------S myOptPar.pys default-------------------------------------------------------------
  OptPar = open('myOptPar.pys','w')
  for i in range(6) :
    OptPar.write('1.00\n')
  OptPar.close()


  #-----------------------------S Run------------------------------------------------------
  os.system('./stepl')
  #-----------------------------E Run------------------------------------------------------
  rstFile = open( 'myRST.csv','r')
  rst = rstFile.readlines()
  rstFile.close()

  rst[0] = rst[0].split(',')
  for i in range(1,len(rst)) :
    rst[i] = rst[i].replace('\r','')
    rst[i] = rst[i].replace('\n','')
    for j in range(4) :
      rst[i] = rst[i].replace('  ',' ')
    rst[i] = rst[i].split(' ')


  #-------------------S change columns rst >> rst3----------------------------
  rst3 = []


  rst3Str = isStr(rst[0][0]) + ',' 
  rst3Str += isStr(rst[0][1]) + ',' + isStr(rst[0][5]) + ',' + isStr(rst[0][9]) + ',' + isStr(rst[0][13]) + ','
  rst3Str += isStr(rst[0][2]) + ',' + isStr(rst[0][6]) + ',' + isStr(rst[0][10]) + ',' + isStr(rst[0][14]) + ','
  rst3Str += isStr(rst[0][3]) + ',' + isStr(rst[0][7]) + ',' + isStr(rst[0][11]) + ',' + isStr(rst[0][15]) + ','
  rst3Str += isStr(rst[0][4]) + ',' + isStr(rst[0][8]) + ',' + isStr(rst[0][12]) + ',' + isStr(rst[0][16])
  rst3.append(rst3Str)

  for i in range(1,len(rst)) :
    rst3Str = isStr(rst[i][1]) + ',' 
    rst3Str += isStr(rst[i][2]) + ',' + isStr(rst[i][6]) + ',' + isStr(rst[i][10]) + ',' + isStr(rst[i][14]) + ','
    rst3Str += isStr(rst[i][3]) + ',' + isStr(rst[i][7]) + ',' + isStr(rst[i][11]) + ',' + isStr(rst[i][15]) + ','
    rst3Str += isStr(rst[i][4]) + ',' + isStr(rst[i][8]) + ',' + isStr(rst[i][12]) + ',' + isStr(rst[i][16]) + ','
    rst3Str += isStr(rst[i][5]) + ',' + isStr(rst[i][9]) + ',' + isStr(rst[i][13]) + ',' + isStr(rst[i][17]) 
    rst3.append(rst3Str)

    rst3[0] = rst3[0].replace('  ','')

  #-----------------E change columns rst >> rst3----------------------------

  #------------------S Plot-----------------------------------------------

  Narr = []
  Parr = []
  Barr = []
  Sarr = []

  for i in range(1,len(rst)) :
    N_Str1 = 'W' + isStr(i) + '\\n(' + isStr('%.2f'%isFloat(rst[i][14])) + ')\t' + isStr('%.2f'%isFloat(rst[i][2])) + '\t' + isStr('%.2f'%isFloat(rst[i][10]))
    P_Str1 = 'W' + isStr(i) + '\\n(' + isStr('%.2f'%isFloat(rst[i][15])) + ')\t' + isStr('%.2f'%isFloat(rst[i][3])) + '\t' + isStr('%.2f'%isFloat(rst[i][11]))
    B_Str1 = 'W' + isStr(i) + '\\n(' + isStr('%.2f'%isFloat(rst[i][16])) + ')\t' + isStr('%.2f'%isFloat(rst[i][4])) + '\t' + isStr('%.2f'%isFloat(rst[i][12]))
    S_Str1 = 'W' + isStr(i) + '\\n(' + isStr('%.2f'%isFloat(rst[i][17])) + ')\t' + isStr('%.2f'%isFloat(rst[i][5])) + '\t' + isStr('%.2f'%isFloat(rst[i][13]))
    Narr.append(N_Str1)
    Parr.append(P_Str1)
    Barr.append(B_Str1)
    Sarr.append(S_Str1)


  #---last line -> total
  N_Str2 = Narr[-1].split('(')
  Narr[-1] = 'Total\\n(' + N_Str2[1]
  P_Str2 = Parr[-1].split('(')
  Parr[-1] = 'Total\\n(' + P_Str2[1]
  B_Str2 = Barr[-1].split('(')
  Barr[-1] = 'Total\\n(' + B_Str2[1]
  S_Str2 = Sarr[-1].split('(')
  Sarr[-1] = 'Total\\n(' + S_Str2[1]

  datFile(Narr,'N')
  datFile(Parr,'P')
  datFile(Barr,'B')
  datFile(Sarr,'S')

  sctFile('N')
  sctFile('P')
  sctFile('B')
  sctFile('S')


  #-----------------E Plot---------------------------------------------------
  #----S Result File to Download---------------------------------------------

  dwFile = open(  'AnnualLoads.csv','w')
  for i in range(len(rst3)) :
  #  dwFile.write(dwDat[i][1:])
    dwFile.write(rst3[i] + '\n')

  dwFile.write('\n\n----\n')
  dwFile.write('Unit is "ton/year" for sediment and is "lb/year" for the others.\n')
  dwFile.close()

  locale.setlocale(locale.LC_ALL, 'en_US')

  for i in range(len(rst3)) :
    rst3[i] = rst3[i].split(',')
    if ( 0 < i ) :
      for j in range(len(rst3[i])) :
        if ( 0 < j ) :
          rst3[i][j] = isStr(locale.format('%d',isInt(isFloat(rst3[i][j])+0.5),1))

  ch777 = 'chmod 777 *' 
  os.system(ch777)
  #return back to the original dir
  os.chdir("../..")

  return rst3




#----dat files
def datFile(myArr,myName) :
  if ( myName == 'B' ) :
    headerName = 'BOD'
  else :
    headerName = myName
  
  #print '<li>', len(myArr)

  myDat = open( myName + 'gnu.dat','w')
  myDat.write('Watershed\t' + headerName + '_Load_(no_BMP)\t' + headerName + '_Load_(with_BMP)\n')
  if ( len(myArr) < 3 ) :
    myDat.write(myArr[-1] + '\n')
  else :
    for i in range(len(myArr)) :
      myDat.write(myArr[i] + '\n')
  myDat.close()




#----script files
def sctFile(myName) :
  #----define min & max
  maxVal = 0
  myDatFile = open(myName + 'gnu.dat','r')
  myDat = myDatFile.readlines()
  myDatFile.close()
  for i in range(1,len(myDat)) :        # first line is header
    if ( 2 < len(myDat[i]) ) :
      tmpDat = myDat[i].replace('\r','')
      tmpDat = tmpDat.replace('\n','')
      tmpDat = tmpDat.split('\t')
      tmpDat[1] = float(tmpDat[1])
      tmpDat[2] = float(tmpDat[2])
      if ( maxVal <= tmpDat[1] ) :
        maxVal = tmpDat[1]
      if ( maxVal <= tmpDat[2] ) :
        maxVal = tmpDat[2]
      maxVal = maxVal * 1.2
  maxVal = '%.2f'%maxVal
  sctArr = [''] * 40
  sctArr[1] = 'set key top left\n'
  sctArr[2] = 'set terminal jpeg font "Helvetica,10"\n'
  sctArr[4] = 'set xtics border in scale 1,0.5 nomirror rotate by 0  offset character 0, 0.5, -2\n'
  sctArr[6] = 'set yrange[0.00:' + str(maxVal) + ']\n'
  #sctArr[6] = 'set autoscale y\n'
  sctArr[8] = 'set autoscale y2\n'
  sctArr[10] = 'set output "' + myName + '_bar.jpg"\n'
  sctArr[12] = 'set xlabel "Watershed (Reduction, %)"\n'
  if ( myName == 'S' ) :
    sctArr[14] = 'set ylabel "Annual Loads (tons)"\n'
  else :
    sctArr[14] = 'set ylabel "Annual Loads (lbs)"\n'
  #sctArr[16] = 'set y2label "Total Annual Loads (lbs)"\n'
  sctArr[18] = 'set style data histogram\n'
  sctArr[20] = 'set style histogram cluster gap 1\n'
  sctArr[22] = 'set style fill solid border -1\n'
  sctArr[24] = 'set boxwidth 0.9\n'
  sctArr[26] = 'plot "'  + myName + 'gnu.dat' + '" using 2:xtic(1) ti col lt 1, "" u 3 ti col lt 2 \n'

  mySct = open(  myName + 'gnu.script','w')
  for i in range(len(sctArr)) :
    if ( 2 < len(sctArr[i]) ) :
      mySct.write(sctArr[i])
  mySct.close()    
  gnuplotExe = 'gnuplot '  + myName + 'gnu.script'
  os.system(gnuplotExe)


