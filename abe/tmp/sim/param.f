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

