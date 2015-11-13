
def genCLIGEN(myFile, stateN,countyN,stationN,ystime):

    myFile = myFile.replace(' ','')
    dirName = myFile[:2].lower()

    path = '../tmp/' + str(ystime) + '/'
    mkdirPath = 'mkdir ' + path  + 'cligen'
    os.system(mkdirPath)
    path = path + 'cligen/'
    cpCLIGEN = 'cp ./cligen_exe ' + path + '/.'
    os.system(cpCLIGEN)
    myFilePath = 'cp ./parFiles/' + dirName + '/' + myFile + ' ' + path + 'rawPcp.txt'
    os.system(myFilePath)
    chmod777 = 'chmod 777 ' + path + '/*'
    os.system(chmod777)

    os.chdir(path)
    
    #print '<li>', os.getcwd()
    os.system('./cligen_exe -b1 -y100 -irawPcp.txt -orawOut.txt -F >> tmp.txt')

    #----------------------S Read CLIGEN Output and Write pcp.txt----------------------
    #print '<li> Writing Precipitation File..'
    rawDataPath = open('./rawOut.txt','r')
    rawData = rawDataPath.readlines()
    rawDataPath.close()

    sttLine = 0 
    myData = []
    for i in range(len(rawData)) :
      rawData[i] = rawData[i].split()
      if ( 5 < len(rawData[i]) and str(rawData[i][0]) == '1' and str(rawData[i][1]) == '1' and str(rawData[i][2]) == '1' and sttLine < 1 ) : 
        sttLine = i
      if ( sttLine != 0 and 5 < len(rawData[i]) ) :
        tmpStr = str('%04i'%int(rawData[i][2])) + str('%02i'%int(rawData[i][1])) + str('%02i'%int(rawData[i][0])) + '\t' + str(rawData[i][3])
        myData.append(tmpStr)

    pcp = open('./pcp.txt','w')
    for i in range(len(myData)) :
      pcp.write(str(myData[i]) + '\n')
    pcp.close()

    chmod777 = 'chmod 777 ./*.txt'
    os.system(chmod777)
    #return back to the original dir
    os.chdir("../../..")
    #--------------------E Read CLIGEN Output and Write pcp.txt----------------------


    #---------------------S Read CLIGEN Output and Write stainfo.txt----------------------
    stainfo = open('./stainfo.txt', 'w')
    stainfo.write("Station:\t" + str(stationN) + '\n' )
    stainfo.write("State:\t" + str(stateN) + '\n')
    stainfo.write("County:\t" + str(countyN) )
    stainfo.close()

    chmod777 = 'chmod 777 ./*.txt'
    os.system(chmod777)

