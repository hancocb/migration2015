#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

# to jump, 'Java' , 'Step5'

#----S input----------------------------------------------------------------------------------------------------
numWSD = int(form.getvalue('numWSD'))
#----E input----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL WEB</title>'
print '</head>'
print '<body onLoad="init()">'
print '<form name=optMain><br>'

#----Step5
print '  <hr><b><font color=blue>Step 5. Select average soil hydrologic group (SHG), SHG A = highest infiltration and SHG D = lowest infiltration </font></b><br>'
print '  <center>'
print '  <table border=1>'
print '    <tr>'
print '      <td align=center>Watershed</td>'
print '      <td align=center>SHG</td>'
print '      <td align=center>Soil N Conc. %</td>'
print '      <td align=center>Soil P Conc. %</td>'
print '      <td align=center>Soil BOD Conc. %</td>'
print '    </tr>'

for i in range(1,numWSD+1) :
  print '  <tr>'
  print '    <td align=cneter>W', i,'</td>'
  tmpStr = '      <td align=center><select name=HSG_' + str('%02i'%i) + '><option value="1">A<option value="2">B<option value="3">C<option value="4">D</select></td>'
  print tmpStr
  tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=SoilN_' + str('%02i'%i) + ' value=0.080></td>' 
  print tmpStr
  tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=SoilP_' + str('%02i'%i) + ' value=0.080></td>'
  print tmpStr
  tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=SoilB_' + str('%02i'%i) + ' value=0.080></td>'
  print tmpStr
  print '  </tr>'
print '</table></center>'

#----Step6
print '  <hr><b><font color=blue>Step 6. Reference runoff curve number</font></b><br>'
print '  <center>'
print '  <table border=1>'
print '    <tr>'
print '      <td align=center>Landuse</td>'
print '      <td align=center>SHG A</td>'
print '      <td align=center>SHG B</td>'
print '      <td align=center>SHG C</td>'
print '      <td align=center>SHG D</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Urban</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_A value=83></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_B value=89></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_C value=92></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Cropland</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_A value=67></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_B value=78></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_C value=85></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_D value=89></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Pastureland</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_A value=49></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_B value=69></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_C value=79></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_D value=84></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Forest</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_A value=39></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_B value=60></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_C value=73></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_D value=79></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>User Defined</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_A value=50></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_B value=70></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_C value=80></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_D value=85></td>'
print '    </tr>'
print '  </table>'
print '  </center>'


#----Step6a
print '  <hr><b><font color=blue>Step 6a. Detailed urban reference runoff curve number</font></b><br>'
print '  <center>'
print '  <table border=1>'
print '    <tr>'
print '      <td align=center>Urban</td>'
print '      <td align=center>SHG A</td>'
print '      <td align=center>SHG B</td>'
print '      <td align=center>SHG C</td>'
print '      <td align=center>SHG D</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Commercial</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_A value=89></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_B value=92></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_C value=94></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_D value=95></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Industrial</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Institutional</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Transportation</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Multi-Family</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Single-Family</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Urban-Cultivated</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Vacant-Developed</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>Open Space</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_A value=81></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_B value=88></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_C value=91></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_D value=93></td>'
print '    </tr>'
print '  </table>'
print '  </center>'


#----Step7
print '  <hr><b><font color=blue>7. Nutrient concentration in runoff (mg/l)</font></b><br>'
print '  <center>'
print '  <table border=1>'
print '    <tr>'
print '          <td align=center>Landuse</td>'
print '          <td align=center>N</td>'
print '          <td align=center>P</td>'
print '          <td align=center>BOD</td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>L-Cropland</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_1_N value=1.9></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_1_P value=0.3></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_1_B value=4.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>L-Cropland w/ manure</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_2_N value=8.1></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_2_P value=2.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_2_B value=12.3></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>M-Cropland</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_1_N value=2.9></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_1_P value=0.4></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_1_B value=6.1></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>M-Cropland w/ manure</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_2_N value=12.2></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_2_P value=3.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_2_B value=18.5></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>H-Cropland</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_1_N value=4.4></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_1_P value=0.5></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_1_B value=9.2></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>H-Cropland w/ manure</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_2_N value=18.3></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_2_P value=4.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_2_B value=24.6></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>Pastureland</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntPast_N value=4.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntPast_P value=0.3></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntPast_B value=13.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>Forest</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntFrst_N value=0.2></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntFrst_P value=0.1></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntFrst_B value=0.5></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>User Defined</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntUser_N value=0.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntUser_P value=0.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntUser_B value=0.0></td>'
print '        </tr>'
print '  </table>'
print '  </center>'


#----Step7a
print '  <hr><b><font color=blue>7a. Nutrient concentration in shallow groundwater (mg/l)</font></b><br>'
print '  <center>'
print '  <table border=1>'
print '    <tr>'
print '          <td align=center>Landuse</td>'
print '          <td align=center>N</td>'
print '          <td align=center>P</td>'
print '          <td align=center>BOD</td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>Urban</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUrbn_N value=1.5></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUrbn_P value=0.063></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUrbn_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>Cropland</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntCrop_N value=1.44></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntCrop_P value=0.063></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntCrop_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>Pastureland</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntPast_N value=1.44></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntPast_P value=0.063></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntPast_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>Forest</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFrst_N value=0.11></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFrst_P value=0.009></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFrst_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>Feedlot</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFeed_N value=6.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFeed_P value=0.007></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFeed_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td align=center>User-Defined</td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUser_N value=0.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUser_P value=0.0></td>'
print '          <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUser_B value=0.0></td>'
print '        </tr>'
print '  </table>'
print '  </center>'


#----Step8
print '  <hr><b><font color=blue>8. Input or modify urban land use distribution</font></b><br>'
print '  <center>'
print '  <table border=1>'
print '    <tr>'
print '      <td align=center>Watershed</td>'
print '          <td align=center>Urban Area (ac)</td>'
print '          <td align=center>Commercial %</td>'
print '          <td align=center>Industrial %</td>'
print '          <td align=center>Institutional %</td>'
print '          <td align=center>Transportation %</td>'
print '          <td align=center>Multi-Family %</td>'
print '          <td align=center>Single-Family %</td>'
print '          <td align=center>Urban-Cultivated %</td>'
print '          <td align=center>Vacant (developed) %</td>'
print '          <td align=center>Open Space %</td>'
print '      <td align=center>Total % Area</td>'
print '    </tr>'

for i in range(1,numWSD+1) :
  print '  <tr>'
  print '    <td align=center>W', i,'</td>'
  tmpStr = '    <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=UrbanArea_' + str('%02i'%i) + ' readonly></td>'
  print tmpStr
  for j in range(1,10) :
    print '    <td align=center>'
    tmpStr = '    <input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=dist_' + str(j) + str('%02i'%i)
    tmpStr = tmpStr + ' onChange="javascript:UrbanTotal_' + str('%02i'%i) + '()" value=0.0></td>'
    print tmpStr
  tmpStr = '    <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=TotalUrban_' + str('%02i'%i) + ' readonly></td>'
  print tmpStr
  print '  </tr>'
print '  </table>'
print '  </center>'


#----Step9
print '  <hr><b><font color=blue>9. Input irrigation area (ac) and irrigation amount (in)</font></b><br>'
print '  <center>'
print '  <table border=1>'
print '    <tr>'
print '          <td align=center>Watershed</td>'
print '          <td align=center>Total Cropland (ac)</td>'
print '          <td align=center>Cropland: Acres Irrigated</td>'
print '          <td align=center>Water Depth (in) per Irrigation - Before BMP</td>'
print '          <td align=center>Water Depth (in) per Irrigation - After BMP</td>'
print '          <td align=center>Irrigation Frequency (#/Year)</td>'
print '        </tr>'

for i in range(1,numWSD+1) :
  print '  <tr>'
  print '    <td align=center>W',i,'</td>'
  tmpStr = '    <td align=center><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CropTotArea_' + str('%02i'%i) + ' readonly></td>'
  print tmpStr
  for j in range(1,5) :
    tmpStr = '    <td align=center>'
    tmpStr = tmpStr + '<input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=IrrVal_' + str(j) + str('%02i'%i) + ' value=0></td>' 
    print tmpStr
  print '  </tr>'
print '  </table>'

print '  <br><br>'
print '  <input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Update" onClick="javascript:returnVal()"><br><br>'


print '</form>'
print '</body>'

print '<script language="JavaScript">'						#--------------------Java
print '  function init() {'
for i in range(1,numWSD+1) :
  tmpStr = '    document.optMain.HSG_' + str('%02i'%i) + '.value = opener.document.inputMain.HSG_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    document.optMain.SoilN_' + str('%02i'%i) + '.value = opener.document.inputMain.SoilN_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    document.optMain.SoilP_' + str('%02i'%i) + '.value = opener.document.inputMain.SoilP_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    document.optMain.SoilB_' + str('%02i'%i) + '.value = opener.document.inputMain.SoilB_' + str('%02i'%i) + '.value ;'
  print tmpStr

#----Step6, Step6a, Step7, Step7a
print '    document.optMain.CN_urban_A.value = opener.document.inputMain.CN_urban_A.value ;'
print '    document.optMain.CN_urban_B.value = opener.document.inputMain.CN_urban_B.value ;'
print '    document.optMain.CN_urban_C.value = opener.document.inputMain.CN_urban_C.value ;'
print '    document.optMain.CN_urban_D.value = opener.document.inputMain.CN_urban_D.value ;'
print '    document.optMain.CN_crop_A.value = opener.document.inputMain.CN_crop_A.value ;'
print '    document.optMain.CN_crop_B.value = opener.document.inputMain.CN_crop_B.value ;'
print '    document.optMain.CN_crop_C.value = opener.document.inputMain.CN_crop_C.value ;'
print '    document.optMain.CN_crop_D.value = opener.document.inputMain.CN_crop_D.value ;'
print '    document.optMain.CN_past_A.value = opener.document.inputMain.CN_past_A.value ;'
print '    document.optMain.CN_past_B.value = opener.document.inputMain.CN_past_B.value ;'
print '    document.optMain.CN_past_C.value = opener.document.inputMain.CN_past_C.value ;'
print '    document.optMain.CN_past_D.value = opener.document.inputMain.CN_past_D.value ;'
print '    document.optMain.CN_frst_A.value = opener.document.inputMain.CN_frst_A.value ;'
print '    document.optMain.CN_frst_B.value = opener.document.inputMain.CN_frst_B.value ;'
print '    document.optMain.CN_frst_C.value = opener.document.inputMain.CN_frst_C.value ;'
print '    document.optMain.CN_frst_D.value = opener.document.inputMain.CN_frst_D.value ;'
print '    document.optMain.CN_user_A.value = opener.document.inputMain.CN_user_A.value ;'
print '    document.optMain.CN_user_B.value = opener.document.inputMain.CN_user_B.value ;'
print '    document.optMain.CN_user_C.value = opener.document.inputMain.CN_user_C.value ;'
print '    document.optMain.CN_user_D.value = opener.document.inputMain.CN_user_D.value ;'

print '    document.optMain.CN_comm_A.value = opener.document.inputMain.CN_comm_A.value ;'
print '    document.optMain.CN_comm_B.value = opener.document.inputMain.CN_comm_B.value ;'
print '    document.optMain.CN_comm_C.value = opener.document.inputMain.CN_comm_C.value ;'
print '    document.optMain.CN_comm_D.value = opener.document.inputMain.CN_comm_D.value ;'
print '    document.optMain.CN_indu_A.value = opener.document.inputMain.CN_indu_A.value ;'
print '    document.optMain.CN_indu_B.value = opener.document.inputMain.CN_indu_B.value ;'
print '    document.optMain.CN_indu_C.value = opener.document.inputMain.CN_indu_C.value ;'
print '    document.optMain.CN_indu_D.value = opener.document.inputMain.CN_indu_D.value ;'
print '    document.optMain.CN_inst_A.value = opener.document.inputMain.CN_inst_A.value ;'
print '    document.optMain.CN_inst_B.value = opener.document.inputMain.CN_inst_B.value ;'
print '    document.optMain.CN_inst_C.value = opener.document.inputMain.CN_inst_C.value ;'
print '    document.optMain.CN_inst_D.value = opener.document.inputMain.CN_inst_D.value ;'
print '    document.optMain.CN_tran_A.value = opener.document.inputMain.CN_tran_A.value ;'
print '    document.optMain.CN_tran_B.value = opener.document.inputMain.CN_tran_B.value ;'
print '    document.optMain.CN_tran_C.value = opener.document.inputMain.CN_tran_C.value ;'
print '    document.optMain.CN_tran_D.value = opener.document.inputMain.CN_tran_D.value ;'
print '    document.optMain.CN_mult_A.value = opener.document.inputMain.CN_mult_A.value ;'
print '    document.optMain.CN_mult_B.value = opener.document.inputMain.CN_mult_B.value ;'
print '    document.optMain.CN_mult_C.value = opener.document.inputMain.CN_mult_C.value ;'
print '    document.optMain.CN_mult_D.value = opener.document.inputMain.CN_mult_D.value ;'
print '    document.optMain.CN_sing_A.value = opener.document.inputMain.CN_sing_A.value ;'
print '    document.optMain.CN_sing_B.value = opener.document.inputMain.CN_sing_B.value ;'
print '    document.optMain.CN_sing_C.value = opener.document.inputMain.CN_sing_C.value ;'
print '    document.optMain.CN_sing_D.value = opener.document.inputMain.CN_sing_D.value ;'
print '    document.optMain.CN_urcu_A.value = opener.document.inputMain.CN_urcu_A.value ;'
print '    document.optMain.CN_urcu_B.value = opener.document.inputMain.CN_urcu_B.value ;'
print '    document.optMain.CN_urcu_C.value = opener.document.inputMain.CN_urcu_C.value ;'
print '    document.optMain.CN_urcu_D.value = opener.document.inputMain.CN_urcu_D.value ;'
print '    document.optMain.CN_vade_A.value = opener.document.inputMain.CN_vade_A.value ;'
print '    document.optMain.CN_vade_B.value = opener.document.inputMain.CN_vade_B.value ;'
print '    document.optMain.CN_vade_C.value = opener.document.inputMain.CN_vade_C.value ;'
print '    document.optMain.CN_vade_D.value = opener.document.inputMain.CN_vade_D.value ;'
print '    document.optMain.CN_open_A.value = opener.document.inputMain.CN_open_A.value ;'
print '    document.optMain.CN_open_B.value = opener.document.inputMain.CN_open_B.value ;'
print '    document.optMain.CN_open_C.value = opener.document.inputMain.CN_open_C.value ;'
print '    document.optMain.CN_open_D.value = opener.document.inputMain.CN_open_D.value ;'

print '    document.optMain.ntLcrop_1_N.value = opener.document.inputMain.ntLcrop_1_N.value ;'
print '    document.optMain.ntLcrop_1_P.value = opener.document.inputMain.ntLcrop_1_P.value ;'
print '    document.optMain.ntLcrop_1_B.value = opener.document.inputMain.ntLcrop_1_B.value ;'
print '    document.optMain.ntLcrop_2_N.value = opener.document.inputMain.ntLcrop_2_N.value ;'
print '    document.optMain.ntLcrop_2_P.value = opener.document.inputMain.ntLcrop_2_P.value ;'
print '    document.optMain.ntLcrop_2_B.value = opener.document.inputMain.ntLcrop_2_B.value ;'
print '    document.optMain.ntMcrop_1_N.value = opener.document.inputMain.ntMcrop_1_N.value ;'
print '    document.optMain.ntMcrop_1_P.value = opener.document.inputMain.ntMcrop_1_P.value ;'
print '    document.optMain.ntMcrop_1_B.value = opener.document.inputMain.ntMcrop_1_B.value ;'
print '    document.optMain.ntMcrop_2_N.value = opener.document.inputMain.ntMcrop_2_N.value ;'
print '    document.optMain.ntMcrop_2_P.value = opener.document.inputMain.ntMcrop_2_P.value ;'
print '    document.optMain.ntMcrop_2_B.value = opener.document.inputMain.ntMcrop_2_B.value ;'
print '    document.optMain.ntHcrop_1_N.value = opener.document.inputMain.ntHcrop_1_N.value ;'
print '    document.optMain.ntHcrop_1_P.value = opener.document.inputMain.ntHcrop_1_P.value ;'
print '    document.optMain.ntHcrop_1_B.value = opener.document.inputMain.ntHcrop_1_B.value ;'
print '    document.optMain.ntHcrop_2_N.value = opener.document.inputMain.ntHcrop_2_N.value ;'
print '    document.optMain.ntHcrop_2_P.value = opener.document.inputMain.ntHcrop_2_P.value ;'
print '    document.optMain.ntHcrop_2_B.value = opener.document.inputMain.ntHcrop_2_B.value ;'
print '    document.optMain.ntPast_N.value = opener.document.inputMain.ntPast_N.value ;'
print '    document.optMain.ntPast_P.value = opener.document.inputMain.ntPast_P.value ;'
print '    document.optMain.ntPast_B.value = opener.document.inputMain.ntPast_B.value ;'
print '    document.optMain.ntFrst_N.value = opener.document.inputMain.ntFrst_N.value ;'
print '    document.optMain.ntFrst_P.value = opener.document.inputMain.ntFrst_P.value ;'
print '    document.optMain.ntFrst_B.value = opener.document.inputMain.ntFrst_B.value ;'
print '    document.optMain.ntUser_N.value = opener.document.inputMain.ntUser_N.value ;'
print '    document.optMain.ntUser_P.value = opener.document.inputMain.ntUser_P.value ;'
print '    document.optMain.ntUser_B.value = opener.document.inputMain.ntUser_B.value ;'

print '    document.optMain.GntUrbn_N.value = opener.document.inputMain.GntUrbn_N.value ;'
print '    document.optMain.GntUrbn_P.value = opener.document.inputMain.GntUrbn_P.value ;'
print '    document.optMain.GntUrbn_B.value = opener.document.inputMain.GntUrbn_B.value ;'
print '    document.optMain.GntCrop_N.value = opener.document.inputMain.GntCrop_N.value ;'
print '    document.optMain.GntCrop_P.value = opener.document.inputMain.GntCrop_P.value ;'
print '    document.optMain.GntCrop_B.value = opener.document.inputMain.GntCrop_B.value ;'
print '    document.optMain.GntPast_N.value = opener.document.inputMain.GntPast_N.value ;'
print '    document.optMain.GntPast_P.value = opener.document.inputMain.GntPast_P.value ;'
print '    document.optMain.GntPast_B.value = opener.document.inputMain.GntPast_B.value ;'
print '    document.optMain.GntFrst_N.value = opener.document.inputMain.GntFrst_N.value ;'
print '    document.optMain.GntFrst_P.value = opener.document.inputMain.GntFrst_P.value ;'
print '    document.optMain.GntFrst_B.value = opener.document.inputMain.GntFrst_B.value ;'
print '    document.optMain.GntFeed_N.value = opener.document.inputMain.GntFeed_N.value ;'
print '    document.optMain.GntFeed_P.value = opener.document.inputMain.GntFeed_P.value ;'
print '    document.optMain.GntFeed_B.value = opener.document.inputMain.GntFeed_B.value ;'
print '    document.optMain.GntUser_N.value = opener.document.inputMain.GntUser_N.value ;'
print '    document.optMain.GntUser_P.value = opener.document.inputMain.GntUser_P.value ;'
print '    document.optMain.GntUser_B.value = opener.document.inputMain.GntUser_B.value ;'

#----Step8
for i in range(1,numWSD+1) :
  for j in range(1,10) :
    tmpStr = '    document.optMain.dist_' + str(j) + str('%02i'%i) + '.value = opener.document.inputMain.dist_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

#----Step9
for i in range(1,numWSD+1) :
  for j in range(1,5) :
    tmpStr = '    document.optMain.IrrVal_' + str(j) + str('%02i'%i) + '.value = opener.document.inputMain.IrrVal_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

#----Step8,9  Total Area
for i in range(1,numWSD+1) :
  tmpStr = '    document.optMain.UrbanArea_' + str('%02i'%i) + '.value = opener.document.inputMain.LuseAreaWSD_1' + str('%02i'%i) + '.value ;' 
  print tmpStr
  tmpStr = '    document.optMain.CropTotArea_' + str('%02i'%i) + '.value = opener.document.inputMain.LuseAreaWSD_2' + str('%02i'%i) + '.value ;'
  print tmpStr

print '  }'				# init

#----Step8, UrbanTotal
for i in range(1,numWSD+1) :
  tmpStr = '  function UrbanTotal_' + str('%02i'%i) + '() {'
  print tmpStr
  for j in range(1,10) :
    tmpStr = '    var area' + str(j) + ' = document.optMain.dist_' + str(j) + str('%02i'%i) + '.value * 1.0 ;'
    print tmpStr
  print '    var totArea = area1 + area2 + area3 + area4 + area5 + area6 + area7 + area8 + area9 ;' 
  tmpStr = '    document.optMain.TotalUrban_' + str('%02i'%i) + '.value = totArea ;'
  print tmpStr
  print '}'				# Urban Total

#----returnVal
print '  function returnVal() {'
#----Step5
for i in range(1,numWSD+1) :
  tmpStr = '    opener.document.inputMain.HSG_' + str('%02i'%i) + '.value = document.optMain.HSG_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    opener.document.inputMain.SoilN_' + str('%02i'%i) + '.value = document.optMain.SoilN_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    opener.document.inputMain.SoilP_' + str('%02i'%i) + '.value = document.optMain.SoilP_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    opener.document.inputMain.SoilB_' + str('%02i'%i) + '.value = document.optMain.SoilB_' + str('%02i'%i) + '.value '; 
  print tmpStr

#----Step6, Step6a, Step7, Step7a
print '    opener.document.inputMain.CN_urban_A.value = document.optMain.CN_urban_A.value ;'
print '    opener.document.inputMain.CN_urban_B.value = document.optMain.CN_urban_B.value ;'
print '    opener.document.inputMain.CN_urban_C.value = document.optMain.CN_urban_C.value ;'
print '    opener.document.inputMain.CN_urban_D.value = document.optMain.CN_urban_D.value ;'
print '    opener.document.inputMain.CN_crop_A.value = document.optMain.CN_crop_A.value ;'
print '    opener.document.inputMain.CN_crop_B.value = document.optMain.CN_crop_B.value ;'
print '    opener.document.inputMain.CN_crop_C.value = document.optMain.CN_crop_C.value ;'
print '    opener.document.inputMain.CN_crop_D.value = document.optMain.CN_crop_D.value ;'
print '    opener.document.inputMain.CN_past_A.value = document.optMain.CN_past_A.value ;'
print '    opener.document.inputMain.CN_past_B.value = document.optMain.CN_past_B.value ;'
print '    opener.document.inputMain.CN_past_C.value = document.optMain.CN_past_C.value ;'
print '    opener.document.inputMain.CN_past_D.value = document.optMain.CN_past_D.value ;'
print '    opener.document.inputMain.CN_frst_A.value = document.optMain.CN_frst_A.value ;'
print '    opener.document.inputMain.CN_frst_B.value = document.optMain.CN_frst_B.value ;'
print '    opener.document.inputMain.CN_frst_C.value = document.optMain.CN_frst_C.value ;'
print '    opener.document.inputMain.CN_frst_D.value = document.optMain.CN_frst_D.value ;'
print '    opener.document.inputMain.CN_user_A.value = document.optMain.CN_user_A.value ;'
print '    opener.document.inputMain.CN_user_B.value = document.optMain.CN_user_B.value ;'
print '    opener.document.inputMain.CN_user_C.value = document.optMain.CN_user_C.value ;'
print '    opener.document.inputMain.CN_user_D.value = document.optMain.CN_user_D.value ;'

print '    opener.document.inputMain.CN_comm_A.value = document.optMain.CN_comm_A.value ;'
print '    opener.document.inputMain.CN_comm_B.value = document.optMain.CN_comm_B.value ;'
print '    opener.document.inputMain.CN_comm_C.value = document.optMain.CN_comm_C.value ;'
print '    opener.document.inputMain.CN_comm_D.value = document.optMain.CN_comm_D.value ;'
print '    opener.document.inputMain.CN_indu_A.value = document.optMain.CN_indu_A.value ;'
print '    opener.document.inputMain.CN_indu_B.value = document.optMain.CN_indu_B.value ;'
print '    opener.document.inputMain.CN_indu_C.value = document.optMain.CN_indu_C.value ;'
print '    opener.document.inputMain.CN_indu_D.value = document.optMain.CN_indu_D.value ;'
print '    opener.document.inputMain.CN_inst_A.value = document.optMain.CN_inst_A.value ;'
print '    opener.document.inputMain.CN_inst_B.value = document.optMain.CN_inst_B.value ;'
print '    opener.document.inputMain.CN_inst_C.value = document.optMain.CN_inst_C.value ;'
print '    opener.document.inputMain.CN_inst_D.value = document.optMain.CN_inst_D.value ;'
print '    opener.document.inputMain.CN_tran_A.value = document.optMain.CN_tran_A.value ;'
print '    opener.document.inputMain.CN_tran_B.value = document.optMain.CN_tran_B.value ;'
print '    opener.document.inputMain.CN_tran_C.value = document.optMain.CN_tran_C.value ;'
print '    opener.document.inputMain.CN_tran_D.value = document.optMain.CN_tran_D.value ;'
print '    opener.document.inputMain.CN_mult_A.value = document.optMain.CN_mult_A.value ;'
print '    opener.document.inputMain.CN_mult_B.value = document.optMain.CN_mult_B.value ;'
print '    opener.document.inputMain.CN_mult_C.value = document.optMain.CN_mult_C.value ;'
print '    opener.document.inputMain.CN_mult_D.value = document.optMain.CN_mult_D.value ;'
print '    opener.document.inputMain.CN_sing_A.value = document.optMain.CN_sing_A.value ;'
print '    opener.document.inputMain.CN_sing_B.value = document.optMain.CN_sing_B.value ;'
print '    opener.document.inputMain.CN_sing_C.value = document.optMain.CN_sing_C.value ;'
print '    opener.document.inputMain.CN_sing_D.value = document.optMain.CN_sing_D.value ;'
print '    opener.document.inputMain.CN_urcu_A.value = document.optMain.CN_urcu_A.value ;'
print '    opener.document.inputMain.CN_urcu_B.value = document.optMain.CN_urcu_B.value ;'
print '    opener.document.inputMain.CN_urcu_C.value = document.optMain.CN_urcu_C.value ;'
print '    opener.document.inputMain.CN_urcu_D.value = document.optMain.CN_urcu_D.value ;'
print '    opener.document.inputMain.CN_vade_A.value = document.optMain.CN_vade_A.value ;'
print '    opener.document.inputMain.CN_vade_B.value = document.optMain.CN_vade_B.value ;'
print '    opener.document.inputMain.CN_vade_C.value = document.optMain.CN_vade_C.value ;'
print '    opener.document.inputMain.CN_vade_D.value = document.optMain.CN_vade_D.value ;'
print '    opener.document.inputMain.CN_open_A.value = document.optMain.CN_open_A.value ;'
print '    opener.document.inputMain.CN_open_B.value = document.optMain.CN_open_B.value ;'
print '    opener.document.inputMain.CN_open_C.value = document.optMain.CN_open_C.value ;'
print '    opener.document.inputMain.CN_open_D.value = document.optMain.CN_open_D.value ;'

print '    opener.document.inputMain.ntLcrop_1_N.value = document.optMain.ntLcrop_1_N.value ;'
print '    opener.document.inputMain.ntLcrop_1_P.value = document.optMain.ntLcrop_1_P.value ;'
print '    opener.document.inputMain.ntLcrop_1_B.value = document.optMain.ntLcrop_1_B.value ;'
print '    opener.document.inputMain.ntLcrop_2_N.value = document.optMain.ntLcrop_2_N.value ;'
print '    opener.document.inputMain.ntLcrop_2_P.value = document.optMain.ntLcrop_2_P.value ;'
print '    opener.document.inputMain.ntLcrop_2_B.value = document.optMain.ntLcrop_2_B.value ;'
print '    opener.document.inputMain.ntMcrop_1_N.value = document.optMain.ntMcrop_1_N.value ;'
print '    opener.document.inputMain.ntMcrop_1_P.value = document.optMain.ntMcrop_1_P.value ;'
print '    opener.document.inputMain.ntMcrop_1_B.value = document.optMain.ntMcrop_1_B.value ;'
print '    opener.document.inputMain.ntMcrop_2_N.value = document.optMain.ntMcrop_2_N.value ;'
print '    opener.document.inputMain.ntMcrop_2_P.value = document.optMain.ntMcrop_2_P.value ;'
print '    opener.document.inputMain.ntMcrop_2_B.value = document.optMain.ntMcrop_2_B.value ;'
print '    opener.document.inputMain.ntHcrop_1_N.value = document.optMain.ntHcrop_1_N.value ;'
print '    opener.document.inputMain.ntHcrop_1_P.value = document.optMain.ntHcrop_1_P.value ;'
print '    opener.document.inputMain.ntHcrop_1_B.value = document.optMain.ntHcrop_1_B.value ;'
print '    opener.document.inputMain.ntHcrop_2_N.value = document.optMain.ntHcrop_2_N.value ;'
print '    opener.document.inputMain.ntHcrop_2_P.value = document.optMain.ntHcrop_2_P.value ;'
print '    opener.document.inputMain.ntHcrop_2_B.value = document.optMain.ntHcrop_2_B.value ;'
print '    opener.document.inputMain.ntPast_N.value = document.optMain.ntPast_N.value ;'
print '    opener.document.inputMain.ntPast_P.value = document.optMain.ntPast_P.value ;'
print '    opener.document.inputMain.ntPast_B.value = document.optMain.ntPast_B.value ;'
print '    opener.document.inputMain.ntFrst_N.value = document.optMain.ntFrst_N.value ;'
print '    opener.document.inputMain.ntFrst_P.value = document.optMain.ntFrst_P.value ;'
print '    opener.document.inputMain.ntFrst_B.value = document.optMain.ntFrst_B.value ;'
print '    opener.document.inputMain.ntUser_N.value = document.optMain.ntUser_N.value ;'
print '    opener.document.inputMain.ntUser_P.value = document.optMain.ntUser_P.value ;'
print '    opener.document.inputMain.ntUser_B.value = document.optMain.ntUser_B.value ;'

print '    opener.document.inputMain.GntUrbn_N.value = document.optMain.GntUrbn_N.value ;'
print '    opener.document.inputMain.GntUrbn_P.value = document.optMain.GntUrbn_P.value ;'
print '    opener.document.inputMain.GntUrbn_B.value = document.optMain.GntUrbn_B.value ;'
print '    opener.document.inputMain.GntCrop_N.value = document.optMain.GntCrop_N.value ;'
print '    opener.document.inputMain.GntCrop_P.value = document.optMain.GntCrop_P.value ;'
print '    opener.document.inputMain.GntCrop_B.value = document.optMain.GntCrop_B.value ;'
print '    opener.document.inputMain.GntPast_N.value = document.optMain.GntPast_N.value ;'
print '    opener.document.inputMain.GntPast_P.value = document.optMain.GntPast_P.value ;'
print '    opener.document.inputMain.GntPast_B.value = document.optMain.GntPast_B.value ;'
print '    opener.document.inputMain.GntFrst_N.value = document.optMain.GntFrst_N.value ;'
print '    opener.document.inputMain.GntFrst_P.value = document.optMain.GntFrst_P.value ;'
print '    opener.document.inputMain.GntFrst_B.value = document.optMain.GntFrst_B.value ;'
print '    opener.document.inputMain.GntFeed_N.value = document.optMain.GntFeed_N.value ;'
print '    opener.document.inputMain.GntFeed_P.value = document.optMain.GntFeed_P.value ;'
print '    opener.document.inputMain.GntFeed_B.value = document.optMain.GntFeed_B.value ;'
print '    opener.document.inputMain.GntUser_N.value = document.optMain.GntUser_N.value ;'
print '    opener.document.inputMain.GntUser_P.value = document.optMain.GntUser_P.value ;'
print '    opener.document.inputMain.GntUser_B.value = document.optMain.GntUser_B.value ;'

#----Step8
for i in range(1,numWSD+1) :
  for j in range(1,9) :
    tmpStr = '    opener.document.inputMain.dist_' + str(j) + str('%02i'%i) + '.value = document.optMain.dist_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

#----Step9
for i in range(1,numWSD+1) :
  for j in range(1,5) :
    tmpStr = '    opener.document.inputMain.IrrVal_' + str(j) + str('%02i'%i) + '.value = document.optMain.IrrVal_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

print '  alert("Updated") ;'
print '  self.close();'
print '  }'				# returnVal
print '</script>'

print '</html>'















