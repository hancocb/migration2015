	module parm
!--------------------S Input Sheet----------------------------------------------
	! maximum num of subwatershed is 30
	INTEGER :: num, swsOpt
	REAL :: LuseAreaWS(6,30), PctFeedlot(30), TAreaWS(30)
	REAL :: AnnualR(30), RDays(30), AvgR(30), AnnualRF, RDaysF
	INTEGER :: BeefCattle(30), DairyCattle(30), Swine(30), Sheep(30)
	INTEGER :: Animals(8,30), NumMonManure(30)
	!INTEGER :: NumSpSys(30), NumPpDrtDc(30)
        REAL :: NumSpSys(30), NumPpDrtDc(30)
	REAL :: PpSpSys(30), SpFailRate(30), RdcDrtDc(30)
	REAL :: usleCropland(5,30), uslePasture(5,30)
	REAL :: usleForest(5,30), usleUser(5,30)
	INTEGER :: SHG(30)
	REAL :: SoilNconc(30), SoilPconc(30), SoilBODconc(30), feCN(4)
	REAL :: CN(4,5), UrbanCN(4,9), NtConcRunoff(3,9), NtConcGW(3,6)
	REAL :: UrbanDst(11,30), Irrigation(5,30), Rainfall(40000)


	!---- Variables in SUNROUTINES
	REAL :: UrbanArea(11,30), myCN(5,30), myUrbanCN(9,30)
	REAL :: Runoff(5,30), VRunoff(6,30)
	REAL :: Lambda, GW1(4,5), GW2(5,30), GW3(5,30), GW4(6,30)
	REAL :: UrbanRunoff(9,30), VUrbanRunoff(9,30)
	REAL :: IrRunoff(3,30)
	REAL :: RdcIrRunoff(2,30)
	
	REAL :: Feedlots_1(7,30), Feedlots_2(11,30), Feedlots_4(30,20)
	REAL :: Feedlots_5(4,11), Load_Fdl(6,30)
	REAL :: feDepth(5)
	
	REAL :: BMPeff_C(5,30), BMPeff_P(5,30), BMPeff_F(5,30)
	REAL :: BMPeff_FL(5,30), BMPeff_U(5,30)
	
	REAL :: AEU(30), Ref(4,13)
	REAL :: WildLifeD(2,5), AEUwl(6,30), AnimalPNB(7,30)
	
	REAL :: Septic_1(17,30), SpDB(8), SepticPNB(9,30)
	
	REAL :: Sed_1(22,30), Sed_1a(16,30), Sed_2(8,30)
	REAL :: Sed_2a(6,30), Sed_3(9,30), Sed_3a(16,30)
	
	REAL :: ub1(9,4), ub2a(9,30), ub3a(9,30), ub4(12,30)
	REAL :: ub32(9,30), ub33(9,30), ub34(9,30), ub35(9,30)
	REAL :: ub32a(9,30), ub33a(9,30), ub34a(9,30), ub35a(9,30)
	REAL :: ub32b(9,30), ub33b(9,30), ub34b(9,30), ub35b(9,30)
	
	REAL :: GS1(13,30), GS2(12,30), GS3(20,30), GSDB1(2,10), GSDB2(4)
	INTEGER :: numGully, numStr, GS1t(30), GS2t(30)
	INTEGER :: GS1_soil(30), GS2_LtRc(30), GS2_soil(30)
	
	REAL :: TLa(15,31), TLb(15,31), TL1(16,31), TLc(36,31)
	REAL :: TLd(28,31), TL2(4,11)
	
	REAL :: anDepth(4,15), anPcpDepth
	REAL :: OptParm(10), DREC(4)

	! num					| Number of subwatershed
	! swsOpt				| Subwatershed option, (1=checked, 2=unchecked)
	! LuseAreaWS(6,30)		| T1, landuse area(ac)
	! PctFeedlot(30)		| T1, Feedlot Percent Paved
	! TAreaWS(30)			| T1, Total area of each subwatershed
	! AnnualR(30)			| T1, Annual Rainfall
	! RDays(30)				| T1, Rain Days
	! AvgR(30)				| T1, Average Rain/Event
	! AnnualRF				| T1, Rain correction factors for annual rainfall
	! RDaysF				| T1, Rain correction factors for rain days
	! Animals(8,30)			| T2, 1 = Beef Cattle
	!						|	  2 = Dairy Cattle
	!							  3 = Swine (Hog)
	!							  4 = Sheep
	!							  5 = Horse
	!							  6 = Chicken
	!							  7 = Turkey
	!							  8 = Duck
	! NumMonManure(30)		| T2, Number of months manure applied
	! NumSpSys(30)			| T3, Num. of Septic Systems
	! PpSpSys(30)			| T3, Population per septic system
	! SpFailRate(30)		| T3, Septic Failure Rate (%)
	! NumPpDrtDc(30)		| T3, Num. of people, wastewater direct discharge
	! RdcDrtDc(30)			| T3, Direct Discharge Reduction (%)
	! usleCropland(5,30)	| T4, USLE factor for cropland
	! uslePasture(5,30)		| T4, USLE factor for Pastureland 
	! usleForest(5,30)		| T4, USLE factor for Forest
	! usleUser(5,30)		| T4, USLE factor for User defined land
	!						      1=R, 2=K, 3=LS, 4=C, 5=P
	! SHG(30)				| T5, Average Soil Hydrologic Group
	! SoilNconc(30)			| T5, Soil N conc. (%)
	! SoilPconc(30)			| T5, Soil P conc. (%)
	! SoilBODconc(30)		| T5, Soil BOD conc. (%)
	! CN(4,5)				| T6, Curve Number
	! UrbanCN(4,9)			| T6a, Curve Number for detailed urban 
	! feCN(4)				| Curve Number for feedlot
	! NtConcRunoff(3,9)		| T7, Nutrient conc. in runoff (mg/L)
	! NtConcGW(3,6)			| T7a, Nutrient conc. in shallow groundwater (mg/L)
	! UrbanDst(11,30)		| T8, Urban landuse distribution
	! Irrigation(5,30)		| T9, Irrigation area(ac) and amount(in)
	!							  1 = Total Cropland (ac)
	!							  2 = Cropland : Acres irrigated
	!							  3 = Water depth(in) per irrigation before BMP
	!							  4 = Water depth(in) per irrigation after BMP
	!							  5 = Irrigation frequency (Num. of year)

	! UrbanArea(11,30)		| LandRain (T1a), Urban Area (ac)
	! myCN(5,30)			| LandRain (T2.1), Curve Number 
	! myUrbanCN(9,30)		| LandRain (T2.1a), Urban Curve Numner
	! Runoff(5,30)			| LandRain (T2.2), Calculated runoff (in)
	! UrbanRunoff(9,30)		| LandRain (T2.2a), Urban Runoff
	! IrRunoff(3,30)		| LandRain (T2.3), Irrigation runoff (in)
	! Lambda				| LandRain (T1), Rainfall Initial Abstraction Factor (0.2)
	! GW1(4,5)				| LandRain (TGW1), Reference soil infiltration fraction for precipitation
	! GW2(5,30)				| LandRain (TGW2), Infiltration fraction based on SHG
	! GW3(5,30)				| LandRain (TGW3),  Calculated infiltration (in)
	! GW4(6,30)				| LandRain (TGW4), Calculated infiltration volume (ac-ft)
	! VRunoff(6,30)			| LandRain (T4), Annual runoff by land uses (ac-ft)
	! VUrbanRunoff(9,30)	| LandRain (T4a), Urban annual runoff (ac-ft)
	! RdcIrRunoff(2,30)		| LandRain (T6), Runoff reduction by land uses (ac-ft)(for irrigation reduction in cropland)

	! Feedlots_1(7,30)		| Feedlots (T1), Select a range of paved percentage for feedlots
	! Feedlots_2(11,30)		| Feedlots (T2), Agricultural animals
	! Feedlots_4(30,20)		| Feedlots (T4), Feedlot load calculation
	! Feedlots_5(4,11)		| Feedlots (T5), Ratio of nutrients produced by animals relative to 1000 lb of slaughter steer
	! Load_Fdl(6,30)		| Feedlots (T3), Load from feedlot (lb/yr) 
	! feDepth(5)			| Feedlots (T4), Runoff depth (mm) in feedlots
	
	! BMPeff_C(5,30)		| BMPs (T1), BMP efficiencies for Cropland
	! BMPeff_P(5,30)		| BMPs (T1), BMP efficiencies for Pastureland
	! BMPeff_F(5,30)		| BMPs (T1), BMP efficiencies for Forest
	! BMPeff_U(5,30)		| BMPs (T1), BMP efficiencies for User Defined
	! BMPeff_FL(5,30)		| BMPs (T1), BMP efficiencies for Feedlots
	
	! AEU(30)				| Animal (T1), Animal Equivalent Unit
	! WildLifeD(2,5)			| Animal (T2), Wildlife density in cropland
	! AEUwl(6,30)			| Animal (T3), Estimated wildlife and AEU in watersheds
	! AnimalPNB(7,30)		| Animal (T4), Total animal equivalent units and nutrient concentrations
	
	! Ref(4,13)				| Reference, Table Data
	
	! Septic_1(17,30)		| Septic (T1), Nutrient load from septic systems
	! SpDB(8)				| Septic (text), A table between Table 1 and 2
	! SepticPNB(9,30)		| Septic (T2), Septic nutrient load in lb/yr
	
	! Sed_1(22,30)			| Sediment (T1), Input USLE parameters
	! Sed_1a(16,30)			| Sediment (T), BMP and efficiency, C=Cropland, P=Pastureland,F=Forest,U=Urban
	! Sed_2(8,30)			| Sediment (T2), Erosion and sediment delivery (ton/year)
	! Sed_2a(6,30)			| Sediment (T), Erosion and sediment delivery after BMP (ton/year)
	! Sed_3(9,30)			| Sediment (T3), Nutrient load from sediment (ton/year)
	! Sed_3a(16,30)			| Sediment (T), Sediment and sediment nutrients by land uses with BMP (ton/year)

	! ub1(9,4)				| Urban (T1), Urban pollutant concentration in runoff (mg/l)	
	! ub2a(9,30)			| Urban (T2a), Effective BMP application area (ac)
	! ub3a(9,30)			| Urban (T3a), Percentage of BMP effective area (%)
	! ub32(9,30)			| Urban (T3.2), Total urban N load (kg)
	! ub33(9,30)			| Urban (T3.3), Total urban P load (kg)
	! ub34(9,30)			| Urban (T3.4), Total urban BOD load (kg)
	! ub35(9,30)			| Urban (T3.5), Total urban TSS load (kg)
	! ub32a(9,30)			| Urban (T3.2a), Selected urban N reduction efficiency
	! ub33a(9,30)			| Urban (T3.3a), Selected urban P reduction efficiency
	! ub34a(9,30)			| Urban (T3.4a), Selected urban BOD reduction efficiency
	! ub35a(9,30)			| Urban (T3.5a), Selected urban TSS reduction efficiency
	! ub32b(9,30)			| Urban (T3.2b), Urban N reduction (kg)
	! ub33b(9,30)			| Urban (T3.3b), Urban P reduction (kg)
	! ub34b(9,30)			| Urban (T3.4b), Urban BOD reduction (kg)
	! ub35b(9,30)			| Urban (T3.5b), Urban TSS reduction (kg)
	! ub4(12,30)			| Urban (T4), Pollutant loads from urban in lb/year

	! GS1t(30)				| Gully&Stream (T1), Watershed number of gully
	! GS1(13,30)			| Gully&Stream (T1), Gully dimensions in the different watersheds
	! GS2t(30)				| Gully&Stream (T2), Watershed number of impaired stream
	! GS2(12,30)			| Gully&Stream (T2), Impaired streambank dimensions in the different watersheds
	! GS3(20,30)			| Gully&Stream (T3), Load and load reduction (lb/year, GU=Gully; SB=Streambank) in the different watersheds
	! GSDB1(2,10)			| Gully&Stream, Gully&Stream DB
	! GSDB2(4)				| Gully&Stream, Gully&Stream DB
	! numGully				| Gully&Stream, Number of Gully
	! numStr				| Gully&Stream, Number of impaired stream
	! GS1_soil(30)			| Gully&Stream (T1), Gully dimensions in the different watersheds, Soil Textural Class
	! GS2_LtRc(30)			| Gully&Stream (T2), Impaired streambank dimensions in the different watersheds, Lateral Recession
	! GS2_soil(30)			| Gully&Stream (T1), Impaired streambank dimensions in the different watersheds, Soil Textural Class
	
	! TLa(15,31)			| TotalLoad (Ta), Nutrient load from runoff (lb/year) without BMPs
	! TLb(15,31)			| TotalLoad (Tb), Nutrient load reduction in runoff with BMPs (lb/year)
	! TL1(16,31)			| TotalLoad (T1), Total load by subwatershed(s)
	! TLc(36,31)			| TotalLoad (Tc), Nutrient and sediment load by land uses with BMP (lb/year)
	! TLd(28,31)			| TotalLoad (Td), Load from groundwater by land uses with BMP (lb/year)
	! TL2(4,11)				| TotalLoad (T2), Total load by land uses (with BMP)
	
	! anDepth(4,15)			| Annual Runoff Depth based on CLIGEN, array of anDepth.txt (mm)
	! anPcpDepth			| Annual Precipitation Depth based on CLIGEN, the last value of anDepth.txt (mm)
	! Rainfall(40000)		| Daily Rainfall Depth (mm), defined by file.
	! OptParm(10)			| Parameters to be Optimized by SCE
	! DREC(4)				| Coefficients and Exponents for Delivery Ratio in the Subroutine Sediment
	
!--------------------E Input Sheet----------------------------------------------
	END module parm
