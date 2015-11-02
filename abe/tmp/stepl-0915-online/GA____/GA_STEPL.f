
!-----------------------------------------------------------------
!	Programmed by Youn Shik Park
!-----------------------------------------------------------------

	include 'param.f'

      PROGRAM GATANK


      INTEGER NPARA, SEED, STATUS, FL
      PARAMETER (NPARA=50)
	REAL CTRL(12), XMP(50), F
      PARAMETER (N=5000)
      INTEGER(2) ICRI
      COMMON /CMOPT/ OBJFV,ICALL

C	FOR TEST
!      REAL QOBS(2,10000), MFLOW(2,10000), MPLT(2,10000), CF(14)
!	INTEGER*4 IYR(10000), IMO(10000), IDA(10000), ITIME(10000)
	
	REAL FinOptParm(10)

	open(80, file='GArunStatus.pys', status='replace')
	  write(80,*) '0'
	close(80)

	call ManOpt
	! Optimize OptParm(1) and OptParm(2) for Runoff and Baseflow
!	pause	

	do i = 1, 10
	  XMP(i) = 1.0
	enddo

C
      WRITE (*,*) ' ENTER THE GENETIC --- '

C     SET RANDOM NUMBER
      SEED=5
      CALL RNINIT(SEED)
C
C     SET CONTROL VARIABLES (USE DEFAULTS)
      DO 10 I=1,12
         CTRL(I) = -1
   10 CONTINUE
      CTRL(1)=100
      CTRL(2)=50				!! generation
      CTRL(3)=8
      CTRL(12)=2
C
C     NOW CALL PIKAIA
      ICALL=0
      CALL PIKAIA(NPARA,CTRL,XMP,F,STATUS)


	open(20, file='myOptParFinal.pys', status='old')
	  do i = 1, 6
	    read(20,*) FinOptParm(i)
	  enddo
	close(20)

	open(22, file='myOptPar.pys', status='replace')
	  do i = 1, 6
	    write(22,*) FinOptParm(i)
	  enddo
	close(22)
	call STEPL

!	write(*,*) FinOptParm(5)*(6044/640)**FinOptParm(6)

      END
C

C***********************************************************************
      SUBROUTINE PIKAIA(N,CTRL,X,F,STATUS)
C=======================================================================
C     OPTIMIZATION (MAXIMIZATION) OF USER-SUPPLIED "FITNESS" FUNCTION
C     FF  OVER N-DIMENSIONAL PARAMETER SPACE  X  USING A BASIC GENETIC
C     ALGORITHM METHOD.
C
C     PAUL CHARBONNEAU & BARRY KNAPP
C     HIGH ALTITUDE OBSERVATORY
C     NATIONAL CENTER FOR ATMOSPHERIC RESEARCH
C     BOULDER CO 80307-3000
C     <PAULCHAR@HAO.UCAR.EDU>
C     <KNAPP@HAO.UCAR.EDU>
C
C     VERSION 1.0   [ 1995 DECEMBER 01 ]
C
C     GENETIC ALGORITHMS ARE HEURISTIC SEARCH TECHNIQUES THAT
C     INCORPORATE IN A COMPUTATIONAL SETTING, THE BIOLOGICAL NOTION
C     OF EVOLUTION BY MEANS OF NATURAL SELECTION.  THIS SUBROUTINE
C     IMPLEMENTS THE THREE BASIC OPERATIONS OF SELECTION, CROSSOVER,
C     AND MUTATION, OPERATING ON "GENOTYPES" ENCODED AS STRINGS.
C
C     REFERENCES:
C
C        CHARBONNEAU, PAUL.  "GENETIC ALGORITHMS IN ASTRONOMY AND
C           ASTROPHYSICS."  ASTROPHYSICAL J. (SUPPLEMENT), VOL 101,
C           IN PRESS (DECEMBER 1995).
C
C        GOLDBERG, DAVID E.  GENETIC ALGORITHMS IN SEARCH, OPTIMIZATION,
C           & MACHINE LEARNING.  ADDISON-WESLEY, 1989.
C
C        DAVIS, LAWRENCE, ED.  HANDBOOK OF GENETIC ALGORITHMS.
C           VAN NOSTRAND REINHOLD, 1991.
C=======================================================================
C     USES: FF, URAND, SETCTL, REPORT, RNKPOP, SELECT, ENCODE, DECODE,
C           CROSS, MUTATE, GENREP, STDREP, NEWPOP, ADJMUT

C     INPUT:
      INTEGER   N
C
C      O INTEGER  N  IS THE PARAMETER SPACE DIMENSION, I.E., THE NUMBER
C        OF ADJUSTABLE PARAMETERS. 
C
C      O FUNCTION  FF  IS A USER-SUPPLIED SCALAR FUNCTION OF N VARI-
C        ABLES, WHICH MUST HAVE THE CALLING SEQUENCE F = FF(N,X), WHERE
C        X IS A REAL PARAMETER ARRAY OF LENGTH N.  THIS FUNCTION MUST
C        BE WRITTEN SO AS TO BOUND ALL PARAMETERS TO THE INTERVAL [0,1];
C        THAT IS, THE USER MUST DETERMINE A PRIORI BOUNDS FOR THE PARA-
C        METER SPACE, AND FF MUST USE THESE BOUNDS TO PERFORM THE APPRO-
C        PRIATE SCALINGS TO RECOVER TRUE PARAMETER VALUES IN THE
C        A PRIORI RANGES.
C
C        BY CONVENTION, FF SHOULD RETURN HIGHER VALUES FOR MORE OPTIMAL
C        PARAMETER VALUES (I.E., INDIVIDUALS WHICH ARE MORE "FIT").
C        FOR EXAMPLE, IN FITTING A FUNCTION THROUGH DATA POINTS, FF
C        COULD RETURN THE INVERSE OF CHI**2.
C
C        IN MOST CASES INITIALIZATION CODE WILL HAVE TO BE WRITTEN
C        (EITHER IN A DRIVER OR IN A SEPARATE SUBROUTINE) WHICH LOADS
C        IN DATA VALUES AND COMMUNICATES WITH FF VIA ONE OR MORE LABELED
C        COMMON BLOCKS.  AN EXAMPLE EXERCISE DRIVER AND FITNESS FUNCTION
C        ARE PROVIDED IN THE ACCOMPANYING FILE, XPKAIA.F.
C
C
C      INPUT/OUTPUT:
       REAL CTRL(12)
C
C      O ARRAY  CTRL  IS AN ARRAY OF CONTROL FLAGS AND PARAMETERS, TO
C        CONTROL THE GENETIC BEHAVIOR OF THE ALGORITHM, AND ALSO PRINTED
C        OUTPUT.  A DEFAULT VALUE WILL BE USED FOR ANY CONTROL VARIABLE
C        WHICH IS SUPPLIED WITH A VALUE LESS THAN ZERO.  ON EXIT, CTRL
C        CONTAINS THE ACTUAL VALUES USED AS CONTROL VARIABLES.  THE
C        ELEMENTS OF CTRL AND THEIR DEFAULTS ARE:
C
C           CTRL( 1) - NUMBER OF INDIVIDUALS IN A POPULATION (DEFAULT
C                      IS 100)
C           CTRL( 2) - NUMBER OF GENERATIONS OVER WHICH SOLUTION IS
C                      TO EVOLVE (DEFAULT IS 500)
C           CTRL( 3) - NUMBER OF SIGNIFICANT DIGITS (I.E., NUMBER OF
C                      GENES) RETAINED IN CHROMOSOMAL ENCODING (DEFAULT
C                      IS 6)  (NOTE: THIS NUMBER IS LIMITED BY THE
C                      MACHINE FLOATING POINT PRECISION.  MOST 32-BIT
C                      FLOATING POINT REPRESENTATIONS HAVE ONLY 6 FULL
C                      DIGITS OF PRECISION.  TO ACHIEVE GREATER PRECI-
C                      SION THIS ROUTINE COULD BE CONVERTED TO DOUBLE
C                      PRECISION, BUT NOTE THAT THIS WOULD ALSO REQUIRE
C                      A DOUBLE PRECISION RANDOM NUMBER GENERATOR, WHICH
C                      LIKELY WOULD NOT HAVE MORE THAN 9 DIGITS OF
C                      PRECISION IF IT USED 4-BYTE INTEGERS INTERNALLY.)
C           CTRL( 4) - CROSSOVER PROBABILITY; MUST BE  <= 1.0 (DEFAULT
C                      IS 0.85)
C           CTRL( 5) - MUTATION MODE; 1/2=STEADY/VARIABLE (DEFAULT IS 2)
C           CTRL( 6) - INITIAL MUTATION RATE; SHOULD BE SMALL (DEFAULT
C                      IS 0.005) (NOTE: THE MUTATION RATE IS THE PROBA-
C                      BILITY THAT ANY ONE GENE LOCUS WILL MUTATE IN
C                      ANY ONE GENERATION.)
C           CTRL( 7) - MINIMUM MUTATION RATE; MUST BE >= 0.0 (DEFAULT
C                      IS 0.0005)
C           CTRL( 8) - MAXIMUM MUTATION RATE; MUST BE <= 1.0 (DEFAULT
C                      IS 0.25)
C           CTRL( 9) - RELATIVE FITNESS DIFFERENTIAL; RANGE FROM 0
C                      (NONE) TO 1 (MAXIMUM).  (DEFAULT IS 1.)
C           CTRL(10) - REPRODUCTION PLAN; 1/2/3=FULL GENERATIONAL
C                      REPLACEMENT/STEADY-STATE-REPLACE-RANDOM/STEADY-
C                      STATE-REPLACE-WORST (DEFAULT IS 3)
C           CTRL(11) - ELITISM FLAG; 0/1=OFF/ON (DEFAULT IS 0)
C                      (APPLIES ONLY TO REPRODUCTION PLANS 1 AND 2)
C           CTRL(12) - PRINTED OUTPUT 0/1/2=NONE/MINIMAL/VERBOSE
C                      (DEFAULT IS 0)
C
C
C     OUTPUT:
      REAL      X(50), F
      INTEGER   STATUS
C
C      O ARRAY  X(1:N)  IS THE "FITTEST" (OPTIMAL) SOLUTION FOUND,
C         I.E., THE SOLUTION WHICH MAXIMIZES FITNESS FUNCTION FF
C
C      O SCALAR  F  IS THE VALUE OF THE FITNESS FUNCTION AT X
C
C      O INTEGER  STATUS  IS AN INDICATOR OF THE SUCCESS OR FAILURE
C         OF THE CALL TO PIKAIA (0=SUCCESS; NON-ZERO=FAILURE)
C
C
C     CONSTANTS
      INTEGER   NMAX, PMAX, DMAX
      PARAMETER (NMAX = 50, PMAX = 1024, DMAX = 50)
C
C      O NMAX IS THE MAXIMUM NUMBER OF ADJUSTABLE PARAMETERS
C        (N <= NMAX)
C
C      O PMAX IS THE MAXIMUM POPULATION (CTRL(1) <= PMAX)
C
C      O DMAX IS THE MAXIMUM NUMBER OF GENES (DIGITS) PER CHROMOSOME
C        SEGEMENT (PARAMETER) (CTRL(3) <= DMAX)
C
C
C     LOCAL VARIABLES
      INTEGER        NP, ND, NGEN, IMUT, IREP, IELITE, IVRB, K, IP, IG,
     +               IP1, IP2, NEW, NEWTOT
      REAL           PCROSS, PMUT, PMUTMN, PMUTMX, FDIF
C
      REAL           PH(NMAX,2), OLDPH(NMAX,PMAX), NEWPH(NMAX,PMAX)
C
      INTEGER        GN1(NMAX*DMAX), GN2(NMAX*DMAX)
      INTEGER        IFIT(PMAX), JFIT(PMAX)
      REAL           FITNS(PMAX),XTEMP(50)
C
C     USER-SUPPLIED UNIFORM RANDOM NUMBER GENERATOR
      REAL           URAND
      EXTERNAL       URAND
C

	REAL QOBS(2,10000), MFLOW(2,10000), MPLT(2,10000)
	
C
C     FUNCTION URAND SHOULD NOT TAKE ANY ARGUMENTS.  IF THE USER WISHES
C     TO BE ABLE TO INITIALIZE URAND, SO THAT THE SAME SEQUENCE OF
C     RANDOM NUMBERS CAN BE REPEATED, THIS CAPABILITY COULD BE IMPLE-
C     MENTED WITH A SEPARATE SUBROUTINE, AND CALLED FROM THE USER'S
C     DRIVER PROGRAM.  AN EXAMPLE URAND FUNCTION (AND INITIALIZATION
C     SUBROUTINE) WHICH USES THE FUNCTION RAN0 (THE "MINIMAL STANDARD"
C     RANDOM NUMBER GENERATOR OF PARK AND MILLER [COMM. ACM 31, 1192-
C     1201, OCT 1988; COMM. ACM 36 NO. 7, 105-110, JULY 1993]) IS
C     PROVIDED.
C
      COMMON /CMOPT/ OBJFV,ICALL,XMIN(30),XMAX(30) 
	CHARACTER(len=13) StatusFileName(10)
C
C     SET CONTROL VARIABLES FROM INPUT AND DEFAULTS

	StatusFileName(1) = 'status010.pys'
	StatusFileName(2) = 'status020.pys'
	StatusFileName(3) = 'status030.pys'
	StatusFileName(4) = 'status040.pys'
	StatusFileName(5) = 'status050.pys'
	StatusFileName(6) = 'status060.pys'
	StatusFileName(7) = 'status070.pys'
	StatusFileName(8) = 'status080.pys'
	StatusFileName(9) = 'status090.pys'
	StatusFileName(10) = 'status100.pys'


   
      CALL SETCTL
     +   (CTRL,N,NP,NGEN,ND,PCROSS,PMUTMN,PMUTMX,PMUT,IMUT,
     +    FDIF,IREP,IELITE,IVRB,STATUS)
      IF (STATUS .NE. 0) THEN
         WRITE(*,*) ' CONTROL VECTOR (CTRL) ARGUMENT(S) INVALID'
         RETURN
      ENDIF
 
C     MAKE SURE LOCALLY-DIMENSIONED ARRAYS ARE BIG ENOUGH
      IF (N.GT.NMAX .OR. NP.GT.PMAX .OR. ND.GT.DMAX) THEN
         WRITE(*,*)
     +      ' NUMBER OF PARAMETERS, POPULATION, OR GENES TOO LARGE'
         STATUS = -1
         RETURN
      ENDIF
 
C     COMPUTE INITIAL (RANDOM BUT BOUNDED) PHENOTYPES
      DO 1 IP=1,NP
C      DO 1 IP=1,50
         DO 2 K=1,N
            OLDPH(K,IP)=URAND()
            XTEMP(K)=OLDPH(K,IP)
    2    CONTINUE


         CALL FUNCTN(N,XTEMP)

         FITNS(IP) = OBJFV
    1 CONTINUE



C     RANK INITIAL POPULATION BY FITNESS ORDER
      CALL RNKPOP(NP,FITNS,IFIT,JFIT)
    

C     MAIN GENERATION LOOP
      DO 10 IG=1,NGEN

        WRITE(*,*) 'GENERATION :',IG,'* EI *' 
	  if ( mod(IG,5) == 0 ) then
	    open(80, file=StatusFileName(IG/5), status='replace')
	      write(80,*) IG
	    close(80)
	  endif




C        MAIN POPULATION LOOP
         NEWTOT=0
         DO 20 IP=1,NP/2

C           1. PICK TWO PARENTS
            CALL SELECT(NP,JFIT,FDIF,IP1)
   21       CALL SELECT(NP,JFIT,FDIF,IP2)
            IF (IP1.EQ.IP2) GOTO 21

C           2. ENCODE PARENT PHENOTYPES
            CALL ENCODE(N,ND,OLDPH(1,IP1),GN1)
            CALL ENCODE(N,ND,OLDPH(1,IP2),GN2)
 
C           3. BREED
            CALL CROSS(N,ND,PCROSS,GN1,GN2)
            CALL MUTATE(N,ND,PMUT,GN1)
            CALL MUTATE(N,ND,PMUT,GN2)
 
C           4. DECODE OFFSPRING GENOTYPES
            CALL DECODE(N,ND,GN1,PH(1,1))
            CALL DECODE(N,ND,GN2,PH(1,2))
 
C           5. INSERT INTO POPULATION
            IF (IREP.EQ.1) THEN
               CALL GENREP(NMAX,N,NP,IP,PH,NEWPH)
            ELSE
               CALL STDREP(NMAX,N,NP,IREP,IELITE,PH,OLDPH,FITNS,
     +            IFIT,JFIT,NEW)
               NEWTOT = NEWTOT+NEW
            ENDIF
C        END OF MAIN POPULATION LOOP
   20    CONTINUE

C        IF RUNNING FULL GENERATIONAL REPLACEMENT: SWAP POPULATIONS
         IF (IREP.EQ.1)
     +      CALL NEWPOP(IELITE,NMAX,N,NP,OLDPH,NEWPH,IFIT,JFIT,FITNS,
     +         NEWTOT)
C        ADJUST MUTATION RATE?

         IF (IMUT.EQ.2) CALL ADJMUT(NP,FITNS,IFIT,PMUTMN,PMUTMX,PMUT)
C
C        PRINT GENERATION REPORT TO STANDARD OUTPUT?
         IF (IVRB.GT.0) CALL REPORT
     +      (IVRB,NMAX,N,NP,ND,OLDPH,FITNS,IFIT,PMUT,IG,NEWTOT)
C     END OF MAIN GENERATION LOOP
   10 CONTINUE
C
C     RETURN BEST PHENOTYPE AND ITS FITNESS
      DO 30 K=1,N
         X(K) = OLDPH(K,IFIT(NP))
   30 CONTINUE
      F = FITNS(IFIT(NP))
C



      END


C********************************************************************
      SUBROUTINE SETCTL
     +   (CTRL,N,NP,NGEN,ND,PCROSS,PMUTMN,PMUTMX,PMUT,IMUT,
     +    FDIF,IREP,IELITE,IVRB,STATUS)
C===================================================================
C     SET CONTROL VARIABLES AND FLAGS FROM INPUT AND DEFAULTS
C===================================================================
C     INPUT
      INTEGER  N
C
      COMMON /IOPAR/ IDAT1,IDAT2,ILST,IORF
C
C     INPUT/OUTPUT
      REAL     CTRL(12)
C
C     OUTPUT
      INTEGER  NP, NGEN, ND, IMUT, IREP, IELITE, IVRB, STATUS
      REAL     PCROSS, PMUTMN, PMUTMX, PMUT, FDIF
C
C     LOCAL
      INTEGER  I
      REAL     DFAULT(12)
      SAVE     DFAULT
      DATA     DFAULT /100,500,5,.85,2,.005,.0005,.25,1,1,1,0/
C
      DO 1 I=1,12
         IF (CTRL(I).LT.0.) CTRL(I)=DFAULT(I)
    1 CONTINUE
 
      NP = CTRL(1)
      NGEN = CTRL(2)
      ND = CTRL(3)
      PCROSS = CTRL(4)
      IMUT = CTRL(5)
      PMUT = CTRL(6)
      PMUTMN = CTRL(7)
      PMUTMX = CTRL(8)
      FDIF = CTRL(9)
      IREP = CTRL(10)
      IELITE = CTRL(11)
      IVRB = CTRL(12)
      STATUS = 0
C
C     PRINT A HEADER
C      IF (IVRB.GT.0) THEN
 
C         WRITE(IORF,2) NGEN,NP,N,ND,PCROSS,PMUT,PMUTMN,PMUTMX,FDIF
C    2    FORMAT(/1X,60('*'),/,
C     +      ' *',13X,'PIKAIA GENETIC ALGORITHM REPORT ',13X,'*',/,
C     +           1X,60('*'),//,
C     +      '   NUMBER OF GENERATIONS EVOLVING: ',I4,/,
C     +      '       INDIVIDUALS PER GENERATION: ',I4,/,
C     +      '    NUMBER OF CHROMOSOME SEGMENTS: ',I4,/,
C     +      '    LENGTH OF CHROMOSOME SEGMENTS: ',I4,/,
C     +      '            CROSSOVER PROBABILITY: ',F9.4,/,
C     +      '            INITIAL MUTATION RATE: ',F9.4,/,
C     +      '            MINIMUM MUTATION RATE: ',F9.4,/,
C     +      '            MAXIMUM MUTATION RATE: ',F9.4,/,
C     +      '    RELATIVE FITNESS DIFFERENTIAL: ',F9.4)
C         IF (IMUT.EQ.1) WRITE(IORF,3) 'CONSTANT'
C         IF (IMUT.EQ.2) WRITE(IORF,3) 'VARIABLE'
C    3    FORMAT(
C     +      '                    MUTATION MODE: ',A)
C         IF (IREP.EQ.1) WRITE(IORF,4) 'FULL GENERATIONAL REPLACEMENT'
C         IF (IREP.EQ.2) WRITE(IORF,4) 'STEADY-STATE-REPLACE-RANDOM'
C         IF (IREP.EQ.3) WRITE(IORF,4) 'STEADY-STATE-REPLACE-WORST'
C    4    FORMAT(
C     +      '                REPRODUCTION PLAN: ',A)
C      ENDIF
 

      RETURN
      END
C*********************************************************************
      FUNCTION URAND()
C=====================================================================
C     RETURN THE NEXT PSEUDO-RANDOM DEVIATE FROM A SEQUENCE WHICH IS
C     UNIFORMLY DISTRIBUTED IN THE INTERVAL [0,1]
C
C     USES THE FUNCTION RAN0, THE "MINIMAL STANDARD" RANDOM NUMBER
C     GENERATOR OF PARK AND MILLER (COMM. ACM 31, 1192-1201, OCT 1988;
C     COMM. ACM 36 NO. 7, 105-110, JULY 1993).
C=====================================================================

C     INPUT - NONE
C
C     OUTPUT
      REAL     URAND
C
C     LOCAL
      INTEGER  ISEED
      REAL     RAN0
      EXTERNAL RAN0
C
C     COMMON BLOCK TO MAKE ISEED VISIBLE TO RNINIT (AND TO SAVE
C     IT BETWEEN CALLS)
      COMMON /RNSEED/ ISEED
C
      URAND = RAN0( ISEED )
      RETURN
      END
C*********************************************************************
      SUBROUTINE RNINIT( SEED )
C=====================================================================
C     INITIALIZE RANDOM NUMBER GENERATOR URAND WITH GIVEN SEED
C=====================================================================

C     INPUT
      INTEGER SEED
C
C     OUTPUT - NONE
C
C     LOCAL
      INTEGER ISEED
C
C     COMMON BLOCK TO COMMUNICATE WITH URAND
      COMMON /RNSEED/ ISEED
C
C     SET THE SEED VALUE
      ISEED = SEED
      IF(ISEED.LE.0) ISEED=123456
      RETURN
      END
C*********************************************************************
      FUNCTION RAN0( SEED )
C=====================================================================
C     "MINIMAL STANDARD" PSEUDO-RANDOM NUMBER GENERATOR OF PARK AND
C     MILLER.  RETURNS A UNIFORM RANDOM DEVIATE R S.T. 0 < R < 1.0.
C     SET SEED TO ANY NON-ZERO INTEGER VALUE TO INITIALIZE A SEQUENCE,
C     THEN DO NOT CHANGE SEED BETWEEN CALLS FOR SUCCESSIVE DEVIATES
C     IN THE SEQUENCE.
C
C     REFERENCES:
C        PARK, S. AND MILLER, K., "RANDOM NUMBER GENERATORS: GOOD ONES
C           ARE HARD TO FIND", COMM. ACM 31, 1192-1201 (OCT. 1988)
C        PARK, S. AND MILLER, K., IN "REMARKS ON CHOOSING AND IMPLE-
C           MENTING RANDOM NUMBER GENERATORS", COMM. ACM 36 NO. 7,
C           105-110 (JULY 1993)
C=====================================================================
C *** DECLARATION SECTION ***
C

C     INPUT/OUTPUT:
      INTEGER SEED
C
C     OUTPUT:
      REAL   RAN0
C
C     CONSTANTS:
      INTEGER A,M,Q,R
      PARAMETER (A=48271,M=2147483647,Q=44488,R=3399)
      REAL   SCALE,EPS,RNMX
      PARAMETER (SCALE=1./M,EPS=1.2E-7,RNMX=1.-EPS)
C
C     LOCAL:
      INTEGER J
C
C *** EXECUTABLE SECTION ***
C
      J = SEED/Q
      SEED = A*(SEED-J*Q)-R*J
      IF (SEED .LT. 0) SEED = SEED+M
      RAN0 = MIN(SEED*SCALE,RNMX)
      RETURN
      END
C**********************************************************************
      SUBROUTINE RQSORT(N,A,P)
C======================================================================
C     RETURN INTEGER ARRAY P WHICH INDEXES ARRAY A IN INCREASING ORDER.
C     ARRAY A IS NOT DISTURBED.  THE QUICKSORT ALGORITHM IS USED.
C
C     B. G. KNAPP, 86/12/23
C
C     REFERENCE: N. WIRTH, ALGORITHMS AND DATA STRUCTURES,
C     PRENTICE-HALL, 1986
C======================================================================

C     INPUT:
      INTEGER   N
      REAL      A(N)

C     OUTPUT:
      INTEGER   P(N)

C     CONSTANTS
      INTEGER   LGN, Q
      PARAMETER (LGN=32, Q=11)
C        (LGN = LOG BASE 2 OF MAXIMUM N;
C         Q = SMALLEST SUBFILE TO USE QUICKSORT ON)

C     LOCAL:
      REAL      X
      INTEGER   STACKL(LGN),STACKR(LGN),S,T,L,M,R,I,J

C     INITIALIZE THE STACK
      STACKL(1)=1
      STACKR(1)=N
      S=1

C     INITIALIZE THE POINTER ARRAY
      DO 1 I=1,N
         P(I)=I
    1 CONTINUE

    2 IF (S.GT.0) THEN
         L=STACKL(S)
         R=STACKR(S)
         S=S-1

    3    IF ((R-L).LT.Q) THEN

C           USE STRAIGHT INSERTION
            DO 6 I=L+1,R
               T = P(I)
               X = A(T)
               DO 4 J=I-1,L,-1
                  IF (A(P(J)).LE.X) GOTO 5
                  P(J+1) = P(J)
    4          CONTINUE
               J=L-1
    5          P(J+1) = T
    6       CONTINUE
         ELSE

C           USE QUICKSORT, WITH PIVOT AS MEDIAN OF A(L), A(M), A(R)
            M=(L+R)/2
            T=P(M)
            IF (A(T).LT.A(P(L))) THEN
               P(M)=P(L)
               P(L)=T
               T=P(M)
            ENDIF
            IF (A(T).GT.A(P(R))) THEN
               P(M)=P(R)
               P(R)=T
               T=P(M)
               IF (A(T).LT.A(P(L))) THEN
                  P(M)=P(L)
                  P(L)=T
                  T=P(M)
               ENDIF
            ENDIF

C           PARTITION
            X=A(T)
            I=L+1
            J=R-1
    7       IF (I.LE.J) THEN
    8          IF (A(P(I)).LT.X) THEN
                  I=I+1
                  GOTO 8
               ENDIF
    9          IF (X.LT.A(P(J))) THEN
                  J=J-1
                  GOTO 9
               ENDIF
               IF (I.LE.J) THEN
                  T=P(I)
                  P(I)=P(J)
                  P(J)=T
                  I=I+1
                  J=J-1
               ENDIF
               GOTO 7
            ENDIF

C           STACK THE LARGER SUBFILE
            S=S+1
            IF ((J-L).GT.(R-I)) THEN
               STACKL(S)=L
               STACKR(S)=J
               L=I
            ELSE
               STACKL(S)=I
               STACKR(S)=R
               R=J
            ENDIF
            GOTO 3
         ENDIF
         GOTO 2
      ENDIF
      RETURN
      END
C********************************************************************
      SUBROUTINE REPORT
     +   (IVRB,NDIM,N,NP,ND,OLDPH,FITNS,IFIT,PMUT,IG,NNEW)
C
C     WRITE GENERATION REPORT TO STANDARD OUTPUT
C
 
C     INPUT:
      INTEGER NP,IFIT(NP),IVRB,NDIM,N,ND,IG,NNEW
      REAL   OLDPH(NDIM,NP),FITNS(NP),PMUT
C
      COMMON /IOPAR/ IDAT1,IDAT2,ILST,IORF
      COMMON /CMOPT/ OBJFV,ICALL,XMIN(30),XMAX(30) 
C
C     OUTPUT: NONE
C
C     LOCAL
      REAL BESTFT,PMUTPV
      SAVE BESTFT,PMUTPV
      INTEGER NDPWR,K
      LOGICAL RPT
      DATA BESTFT,PMUTPV /0,0/
C
      RPT=.FALSE.
 
      IF (PMUT.NE.PMUTPV) THEN
         PMUTPV=PMUT
         RPT=.TRUE.
      ENDIF
 
      IF (FITNS(IFIT(NP)).NE.BESTFT) THEN
         BESTFT=FITNS(IFIT(NP))
         RPT=.TRUE.
      ENDIF
 
      IF (RPT .OR. IVRB.GE.2) THEN
 
C       POWER OF 10 TO MAKE INTEGER GENOTYPES FOR DISPLAY
        NDPWR = NINT(10.**ND)
C        WRITE(IORF,'(/I6,I6,I6,4(F17.4,1X))') IG,NNEW,ICALL,PMUT,
C     +      FITNS(IFIT(NP)), FITNS(IFIT(NP-1)), FITNS(IFIT(NP/2))
C        DO 15 K=1,N
C           WRITE(IORF,'(30X,3(I17,1X))')
C     +       NINT(NDPWR*OLDPH(K,IFIT(NP  ))),
C     +       NINT(NDPWR*OLDPH(K,IFIT(NP-1))),
C     +       NINT(NDPWR*OLDPH(K,IFIT(NP/2)))
   15   CONTINUE
 
      ENDIF
      END

C**********************************************************************
C                         GENETICS MODULE
C**********************************************************************
C
C     ENCODE:    ENCODES PHENOTYPE INTO GENOTYPE
C                CALLED BY: PIKAIA
C
C     DECODE:    DECODES GENOTYPE INTO PHENOTYPE
C                CALLED BY: PIKAIA
C
C     CROSS:     BREEDS TWO OFFSPRING FROM TWO PARENTS
C                CALLED BY: PIKAIA
C
C     MUTATE:    INTRODUCES RANDOM MUTATION IN A GENOTYPE
C                CALLED BY: PIKAIA
C
C     ADJMUT:    IMPLEMENTS VARIABLE MUTATION RATE
C                CALLED BY: PIKAIA
C
C**********************************************************************
      SUBROUTINE ENCODE(N,ND,PH,GN)
C======================================================================
C     ENCODE PHENOTYPE PARAMETERS INTO INTEGER GENOTYPE
C     PH(K) ARE X,Y COORDINATES [ 0 < X,Y < 1 ]
C======================================================================
C

C     INPUTS:
      INTEGER   N, ND
      REAL      PH(N)
C
C     OUTPUT:
      INTEGER   GN(N*ND)
C
C     LOCAL:
      INTEGER   IP, I, J, II
      REAL      Z
C
      Z=10.**ND
      II=0
      DO 1 I=1,N
         IP=INT(PH(I)*Z)
         DO 2 J=ND,1,-1
            GN(II+J)=MOD(IP,10)
            IP=IP/10
    2   CONTINUE
        II=II+ND
    1 CONTINUE
 
      RETURN
      END
 
C**********************************************************************
      SUBROUTINE DECODE(N,ND,GN,PH)
C======================================================================
C     DECODE GENOTYPE INTO PHENOTYPE PARAMETERS
C     PH(K) ARE X,Y COORDINATES [ 0 < X,Y < 1 ]
C======================================================================
C

C     INPUTS:
      INTEGER   N, ND, GN(N*ND)
C
C     OUTPUT:
      REAL      PH(N)
C
C     LOCAL:
      INTEGER   IP, I, J, II
      REAL      Z
C
      Z=10.**(-ND)
      II=0
      DO 1 I=1,N
         IP=0
         DO 2 J=1,ND
            IP=10*IP+GN(II+J)
    2    CONTINUE
         PH(I)=IP*Z
         II=II+ND
    1 CONTINUE
 
      RETURN
      END
C**********************************************************************
      SUBROUTINE CROSS(N,ND,PCROSS,GN1,GN2)
C======================================================================
C     BREEDS TWO PARENT CHROMOSOMES INTO TWO OFFSPRING CHROMOSOMES
C     BREEDING OCCURS THROUGH CROSSOVER STARTING AT POSITION ISPL
C======================================================================
C     USES: URAND

C     INPUTS:
      INTEGER        N, ND
      REAL           PCROSS
C
C     INPUT/OUTPUT:
      INTEGER        GN1(N*ND), GN2(N*ND)
C
C     LOCAL:
      INTEGER        I, ISPL, T
C
C     FUNCTION
      REAL           URAND
      EXTERNAL       URAND
 
 
C     USE CROSSOVER PROBABILITY TO DECIDE WHETHER A CROSSOVER OCCURS
      IF (URAND().LT.PCROSS) THEN
 
C        COMPUTE CROSSOVER POINT
         ISPL=INT(URAND()*N*ND)+1
 
C        SWAP GENES AT ISPL AND ABOVE
         DO 10 I=ISPL,N*ND
            T=GN2(I)
            GN2(I)=GN1(I)
            GN1(I)=T
   10    CONTINUE
      ENDIF
 
      RETURN
      END
 
C**********************************************************************
      SUBROUTINE MUTATE(N,ND,PMUT,GN)
C======================================================================
C     MUTATIONS OCCUR AT RATE PMUT AT ALL GENE LOCI
C======================================================================
C     USES: URAND

C     INPUT:
      INTEGER        N, ND
      REAL           PMUT
C
C     INPUT/OUTPUT:
      INTEGER        GN(N*ND)
C
C     LOCAL:
      INTEGER        I
C
C     FUNCTION:
      REAL           URAND
      EXTERNAL       URAND
C
C     SUBJECT EACH LOCUS TO MUTATION AT THE RATE PMUT
      DO 10 I=1,N*ND
         IF (URAND().LT.PMUT) THEN
            GN(I)=INT(URAND()*10.)
         ENDIF
   10 CONTINUE
 
      RETURN
      END
C**********************************************************************
      SUBROUTINE ADJMUT(NP,FITNS,IFIT,PMUTMN,PMUTMX,PMUT)
C======================================================================
C     DYNAMICAL ADJUSTMENT OF MUTATION RATE; CRITERION IS RELATIVE
C     DIFFERENCE IN ABSOLUTE FITNESSES OF BEST AND MEDIAN INDIVIDUALS
C======================================================================
C

C     INPUT:
      INTEGER        NP, IFIT(NP)
      REAL           FITNS(NP), PMUTMN, PMUTMX
C
C     INPUT/OUTPUT:
      REAL           PMUT
C
C     LOCAL:
      REAL           RDIF, RDIFLO, RDIFHI, DELTA
      PARAMETER      (RDIFLO=0.05, RDIFHI=0.25, DELTA=1.5)
 
      RDIF=ABS(FITNS(IFIT(NP))-FITNS(IFIT(NP/2)))/
     +        (FITNS(IFIT(NP))+FITNS(IFIT(NP/2)))
      IF(RDIF.LE.RDIFLO)THEN
         PMUT=MIN(PMUTMX,PMUT*DELTA)
      ELSE IF(RDIF.GE.RDIFHI)THEN
         PMUT=MAX(PMUTMN,PMUT/DELTA)
      ENDIF
 
      RETURN
      END
C**********************************************************************
C                       REPRODUCTION MODULE
C**********************************************************************
C
C     SELECT:   PARENT SELECTION BY ROULETTE WHEEL ALGORITHM
C               CALLED BY: PIKAIA
C
C     RNKPOP:   RANKS INITIAL POPULATION
C               CALLED BY: PIKAIA, NEWPOP
C
C     GENREP:   INSERTS OFFSPRING INTO POPULATION, FOR FULL
C               GENERATIONAL REPLACEMENT
C               CALLED BY: PIKAIA
C
C     STDREP:   INSERTS OFFSPRING INTO POPULATION, FOR STEADY-STATE
C               REPRODUCTION
C               CALLED BY: PIKAIA
C               CALLS:     FF
C
C     NEWPOP:   REPLACES OLD GENERATION WITH NEW GENERATION
C               CALLED BY: PIKAIA
C               CALLS:     FF, RNKPOP
C
C**********************************************************************
      SUBROUTINE SELECT(NP,JFIT,FDIF,IDAD)
C======================================================================
C     SELECTS A PARENT FROM THE POPULATION, USING ROULETTE WHEEL
C     ALGORITHM WITH THE RELATIVE FITNESSES OF THE PHENOTYPES AS
C     THE "HIT" PROBABILITIES [SEE DAVIS 1991, CHAP. 1].
C======================================================================
C     USES: URAND

C     INPUT:
      INTEGER        NP, JFIT(NP)
      REAL           FDIF
C
C     OUTPUT:
      INTEGER        IDAD
C
C     LOCAL:
      INTEGER        NP1, I
      REAL           DICE, RTFIT
C
C     FUNCTION:
      REAL           URAND
      EXTERNAL       URAND
C
C
      NP1 = NP+1
      DICE = URAND()*NP*NP1
      RTFIT = 0.
      DO 1 I=1,NP
         RTFIT = RTFIT+NP1+FDIF*(NP1-2*JFIT(I))
         IF (RTFIT.GE.DICE) THEN
            IDAD=I
            GOTO 2
         ENDIF
    1 CONTINUE
C     ASSERT: LOOP WILL NEVER EXIT BY FALLING THROUGH

    2 RETURN
      END
 
C**********************************************************************
      SUBROUTINE RNKPOP(N,ARRIN,INDX,RANK)
C======================================================================
C     CALLS EXTERNAL SORT ROUTINE TO PRODUCE KEY INDEX AND RANK ORDER
C     OF INPUT ARRAY ARRIN (WHICH IS NOT ALTERED).
C======================================================================
C     USES: RQSORT

C     INPUT
      INTEGER    N
      REAL       ARRIN(N)
C
C     OUTPUT
      INTEGER    INDX(N),RANK(N)
C
C     LOCAL
      INTEGER    I
C
C     EXTERNAL SORT SUBROUTINE
      EXTERNAL RQSORT
C
C
C     COMPUTE THE KEY INDEX
      CALL RQSORT(N,ARRIN,INDX)
C
C     ...AND THE RANK ORDER
      DO 1 I=1,N
         RANK(INDX(I)) = N-I+1
    1 CONTINUE
      RETURN
      END
 
C***********************************************************************
      SUBROUTINE GENREP(NDIM,N,NP,IP,PH,NEWPH)
C=======================================================================
C     FULL GENERATIONAL REPLACEMENT: ACCUMULATE OFFSPRING INTO NEW
C     POPULATION ARRAY
C=======================================================================
C
 
C     INPUT:
      INTEGER        NDIM, N, NP, IP
      REAL           PH(NDIM,2)
C
C     OUTPUT:
      REAL           NEWPH(NDIM,NP)
C
C     LOCAL:
      INTEGER        I1, I2, K
C
C
C     INSERT ONE OFFSPRING PAIR INTO NEW POPULATION
      I1=2*IP-1
      I2=I1+1
      DO 1 K=1,N
         NEWPH(K,I1)=PH(K,1)
         NEWPH(K,I2)=PH(K,2)
    1 CONTINUE
 
      RETURN
      END
 
C**********************************************************************
      SUBROUTINE STDREP(NDIM,N,NP,IREP,IELITE,PH,OLDPH,FITNS,IFIT,JFIT,
     +   NNEW)
C======================================================================
C     STEADY-STATE REPRODUCTION: INSERT OFFSPRING PAIR INTO POPULATION
C     ONLY IF THEY ARE FIT ENOUGH (REPLACE-RANDOM IF IREP=2 OR
C     REPLACE-WORST IF IREP=3).
C======================================================================
C     USES: FF, URAND

C     INPUT:
      INTEGER        NDIM, N, NP, IREP, IELITE
      REAL           PH(NDIM,2)
C
C     INPUT/OUTPUT:
      REAL           OLDPH(NDIM,NP), FITNS(NP)
      INTEGER        IFIT(NP), JFIT(NP)
C
C     OUTPUT:
      INTEGER        NNEW
 
C     LOCAL:
      INTEGER        I, J, K, I1, IF1
      REAL           FIT
      REAL(4)        XTEMP(50) 
      COMMON /CMOPT/ OBJFV,ICALL,XMIN(30),XMAX(30) 

C     VARIABLE FOR LTHIA
	REAL QOBS(2,10000), MFLOW(2,10000), MPLT(2,10000)
C
C     EXTERNAL FUNCTION
      REAL           URAND
      EXTERNAL       URAND

C
C
      NNEW = 0
      DO 1 J=1,2
         DO I=1,N
            XTEMP(I)=PH(I,J)
         ENDDO 
C        1. COMPUTE OFFSPRING FITNESS (WITH CALLER'S FITNESS FUNCTION)
         CALL FUNCTN(N,XTEMP)


C         CALL SACROUT(N,PH(1,J))
         FIT=OBJFV

C        2. IF FIT ENOUGH, INSERT IN POPULATION
         DO 20 I=NP,1,-1
            IF (FIT.GT.FITNS(IFIT(I))) THEN
 
C              MAKE SURE THE PHENOTYPE IS NOT ALREADY IN THE POPULATION
               IF (I.LT.NP) THEN
                  DO 5 K=1,N
                     IF (OLDPH(K,IFIT(I+1)).NE.PH(K,J)) GOTO 6
    5             CONTINUE
                  GOTO 1
    6             CONTINUE
               ENDIF
 
C              OFFSPRING IS FIT ENOUGH FOR INSERTION, AND IS UNIQUE
 
C              (I) INSERT PHENOTYPE AT APPROPRIATE PLACE IN POPULATION
               IF (IREP.EQ.3) THEN
                  I1=1
               ELSE IF (IELITE.EQ.0 .OR. I.EQ.NP) THEN
                  I1=INT(URAND()*NP)+1
               ELSE
                  I1=INT(URAND()*(NP-1))+1
               ENDIF
               IF1 = IFIT(I1)
               FITNS(IF1)=FIT
               DO 21 K=1,N
                  OLDPH(K,IF1)=PH(K,J)
   21          CONTINUE
 
C              (II) SHIFT AND UPDATE RANKING ARRAYS
               IF (I.LT.I1) THEN
 
C                 SHIFT UP
                  JFIT(IF1)=NP-I
                  DO 22 K=I1-1,I+1,-1
                     JFIT(IFIT(K))=JFIT(IFIT(K))-1
                     IFIT(K+1)=IFIT(K)
   22             CONTINUE
                  IFIT(I+1)=IF1
               ELSE
 
C                 SHIFT DOWN
                  JFIT(IF1)=NP-I+1
                  DO 23 K=I1+1,I
                     JFIT(IFIT(K))=JFIT(IFIT(K))+1
                     IFIT(K-1)=IFIT(K)
   23             CONTINUE
                  IFIT(I)=IF1
               ENDIF
               NNEW = NNEW+1
               GOTO 1
            ENDIF
   20    CONTINUE
 
    1 CONTINUE
 
      RETURN
      END
 
C**********************************************************************
      SUBROUTINE NEWPOP(IELITE,NDIM,N,NP,OLDPH,NEWPH,IFIT,JFIT,FITNS,
     +   NNEW)
C======================================================================
C     REPLACES OLD POPULATION BY NEW; RECOMPUTES FITNESSES & RANKS
C======================================================================
C     USES: FF, RNKPOP

C     INPUT:
      INTEGER        NDIM, NP, N, IELITE
C
C     INPUT/OUTPUT:
      REAL           OLDPH(NDIM,NP), NEWPH(NDIM,NP)
C
C     OUTPUT:
      INTEGER        IFIT(NP), JFIT(NP), NNEW
      REAL           FITNS(NP)
C
C     LOCAL:
      INTEGER        I, K
      REAL(4)        XTEMP(50)

C
C
	REAL QOBS(30,366), MFLOW(2,10000), MPLT(2,10000)
C 
      COMMON /CMOPT/ OBJFV,ICALL,XMIN(30),XMAX(30) 
C
C
      NNEW = NP
 
C     IF USING ELITISM, INTRODUCE IN NEW POPULATION FITTEST OF OLD
C     POPULATION (IF GREATER THAN FITNESS OF THE INDIVIDUAL IT IS
C     TO REPLACE)
      DO K=1,N
         XTEMP(K)=NEWPH(K,1)
      ENDDO
      CALL FUNCTN(N,XTEMP)
C      CALL SACROUT(N,NEWPH(1,1))
      FTEMP=OBJFV 
      IF (IELITE.EQ.1 .AND. FTEMP.LT.FITNS(IFIT(NP))) THEN
         DO 1 K=1,N
            NEWPH(K,1)=OLDPH(K,IFIT(NP))
    1    CONTINUE
         NNEW = NNEW-1
      ENDIF
 
C     REPLACE POPULATION
      DO 2 I=1,NP
         DO 3 K=1,N
            OLDPH(K,I)=NEWPH(K,I)
            XTEMP(K)=OLDPH(K,I) 
    3    CONTINUE
 
C        GET FITNESS USING CALLER'S FITNESS FUNCTION
         CALL FUNCTN(N,XTEMP)
C         CALL SACROUT(N,OLDPH(1,I))
         FITNS(I)=OBJFV
    2 CONTINUE
 
C     COMPUTE NEW POPULATION FITNESS RANK ORDER
      CALL RNKPOP(NP,FITNS,IFIT,JFIT)
 
      RETURN
      END  


CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
	SUBROUTINE CALDECTIME(IYR,IMO,IDA,TIME,DECTIME)

	INTEGER*4 DATE,IYR,TIME,PBMON,PEMON,MODNO
	INTEGER*4 IDA,IMI,IMO,LEAP,NDAY,IDAYS(12)
	DOUBLE PRECISION DECTIME,PERIOD
	DATA IDAYS / 0,31,59,90,120,151,181,212,243,273,304,334 /

      IMI = ((TIME/100)*60)+MOD(TIME,100)

      LEAP = 0
      IF (MOD(IYR,4).EQ.0) LEAP = 1
      IF ((MOD(IYR,100).EQ.0).AND.(MOD(IYR,400).NE.0)) LEAP = 0

      NDAY = IDAYS(IMO)+IDA
      IF (IMO.GE.3) NDAY = NDAY + LEAP

      IF (LEAP.EQ.1) THEN
         DECTIME = (DBLE(NDAY)-
     &        1.D0+(DBLE(IMI)/1440.D0))/366.D0
      ELSE
         DECTIME = (DBLE(NDAY) -
     &        1.D0+(DBLE(IMI)/1440.D0))/365.D0
      ENDIF

	RETURN
	END



CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      SUBROUTINE FUNCTN(NOPT,X)

      DIMENSION X(50)
      INTEGER(4) I

      COMMON /CMOPT/ OBJFV,ICALL,XMIN(30),XMAX(30)
	REAL STEPLrst(6), STEPLobs(6), FixPar(2)
	INTEGER ObjPar
	! FixPar(2)				| Optimized by ManOpt Subroutine
	!						| 1: Runoff, 2: Baseflow
	! ObjPar				| 3: N, 4: P, 5: BOD, 6: S


	X(1) = X(1) * 10.0		! for NtConcRunoff
	X(2) = X(2) * 10.0		! for NtConcGW
	X(3) = X(3) * 5.0		! DREC
	X(4) = X(4) * 5.0		! DREC
!	X(5) = X(5) * 5.0		! DREC
!	X(6) = X(6) * 5.0		! DREC

	
	open(8, file='stepl_obs.pys', status='old')
	  do i = 1, 6
	    read(8,*) STEPLobs(i)
	  enddo
	  read(8,*) ObjPar
	close(8)

	open(10, file='myOptPar.pys', status='old')
	  read(10,*) FixPar(1)
	  read(10,*) FixPar(2)
	close(10)

	open(12, file='myOptPar.pys', status='replace')
	  write(12,*) FixPar(1)
	  write(12,*) FixPar(2)
	  do i = 1, 4
	    write(12,*) X(i)
	  enddo
	close(12)
	
	call STEPL

	open(6, file='stepl_rst.pys', status='old')
	  do i = 1, 6
	    read(6,*) STEPLrst(i)
	  enddo
	close(6)

	OBJFV = abs(STEPLobs(ObjPar) - STEPLrst(ObjPar))

	if ( ICALL == 0 ) then
	  OPTNF = OBJFV
	endif

C
C	SELECT AND WRITE THE HIGHEST NE VALUE AND OPTIMIZED X VALUE
	IF (OBJFV .LE. OPTNF) THEN
	  OPTNF=OBJFV
	  write(*,*) OPTNF
	!----write good parameters
	  open(14, file='myOptParFinal.pys', status='replace')
	    write(14,*) FixPar(1)
	    write(14,*) FixPar(2)
	    do i = 1, 4
	      write(14,*) X(i)
	    enddo
	  close(14)

	ENDIF

    1 FORMAT(3F8.4)
        ICALL=ICALL+1

      RETURN
      END

!------------------------------------------------------------
! The subroutine optimizes OptParm(1) and OptParm(2).
	SUBROUTINE ManOpt

	REAL SimRunoff, ObsRunoff, ObsBaseflow, SimBaseflow
	REAL MyParm(2), TmpParm(20), Diff(20), CurDiff, CurIdx

	open(2, file='stepl_obs.pys', status='old')
	  read(2,*) ObsRunoff
	  read(2,*) ObsBaseflow
	close(2)

	! Optimize Runoff ----------------------------------------------------------
	CurDiff = 9999999999.99
	do i = 1, 15
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) i/10.0
	    do j = 1, 5
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*) SimRunoff
	  close(6)
	  Diff(i) = abs(SimRunoff-ObsRunoff)
!	  write(*,*) i/10.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo

	MyParm(1) = (CurIdx-1) / 10.0

!	write(*,*) '==========================='
	do i = 1, 20
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) MyParm(1) + i/100.0
	    do j = 1, 5
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*) SimRunoff
	  close(6)
	  Diff(i) = abs(SimRunoff-ObsRunoff)
!	  write(*,*) MyParm(1) + i/100.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo
	
	MyParm(1) = MyParm(1) + (CurIdx-1)/100.0

!	write(*,*) '==========================='
	do i = 1, 20
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) MyParm(1) + i/1000.0
	    do j = 1, 5
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*) SimRunoff
	  close(6)
	  Diff(i) = abs(SimRunoff-ObsRunoff)
!	  write(*,*) MyParm(1) + i/1000.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo

	MyParm(1) = MyParm(1) + (CurIdx-1)/1000.0

!	write(*,*) '==========================='
	do i = 1, 20
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) MyParm(1) + i/10000.0
	    do j = 1, 5
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*) SimRunoff
	  close(6)
	  Diff(i) = abs(SimRunoff-ObsRunoff)
!	  write(*,*) MyParm(1) + i/10000.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo

	MyParm(1) = MyParm(1) + CurIdx/10000.0
!	write(*,*) 'RUNOFF:', MyParm(1)

	! Optimize Baseflow --------------------------------------------------------
	CurDiff = 9999999999.99
	do i = 1, 15
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) MyParm(1)
	    write(4,*) i/10.0
	    do j = 1, 4
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*) 
	    read(6,*) SimBaseflow
	  close(6)
	  Diff(i) = abs(SimBaseflow-ObsBaseflow)
!	  write(*,*) i/10.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo

	MyParm(2) = (CurIdx-1) / 10.0

!	write(*,*) '==========================='
	do i = 1, 20
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) MyParm(1)
	    write(4,*) MyParm(2) + i/100.0
	    do j = 1, 4
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*)
	    read(6,*) SimBaseflow
	  close(6)
	  Diff(i) = abs(SimBaseflow-ObsBaseflow)
!	  write(*,*) MyParm(2) + i/100.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo
	
	MyParm(2) = MyParm(2) + (CurIdx-1)/100.0

!	write(*,*) '==========================='
	do i = 1, 20
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) MyParm(1)
	    write(4,*) MyParm(2) + i/1000.0
	    do j = 1, 4
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*)
	    read(6,*) SimBaseflow
	  close(6)
	  Diff(i) = abs(SimBaseflow-ObsBaseflow)
!	  write(*,*) MyParm(2) + i/1000.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo

	MyParm(2) = MyParm(2) + (CurIdx-1)/1000.0

!	write(*,*) '==========================='
	do i = 1, 20
	  open(4, file='myOptPar.pys', status='replace')
	    write(4,*) MyParm(1)
	    write(4,*) MyParm(2) + i/10000.0
	    do j = 1, 4
	      write(4,*) '1.0'
	    enddo
	  close(4)
	  call STEPL
	  open(6, file='stepl_rst.pys', status='old')
	    read(6,*)
	    read(6,*) SimBaseflow
	  close(6)
	  Diff(i) = abs(SimBaseflow-ObsBaseflow)
!	  write(*,*) MyParm(2) + i/10000.0, Diff(i)
	  if ( Diff(i) < CurDiff ) then
	    CurDiff = Diff(i)
	    CurIdx = i
	  endif
	enddo

	MyParm(2) = MyParm(2) + CurIdx/10000.0
!	write(*,*) 'BASEFLOW:', MyParm(2)

	!---------------- RE-RUN ------------------------------
	open(4, file='myOptPar.pys', status='replace')
	  write(4,*) MyParm(1)
	  write(4,*) MyParm(2)
	  do j = 1, 4
	    write(4,*) '1.0'
	  enddo
	close(4)
	call STEPL

	END
!------------------------------------------------------------
!------------------------------------------------------------
!------------------------------------------------------------
!-------------------STEPL------------------------------------
!------------------------------------------------------------
!------------------------------------------------------------
	SUBROUTINE STEPL
	
	use parm
		
	REAL :: AnnualRunoff(3), AnnualBaseflow
	! AnnualRunoff(2)		| Sum of Direct Runoff
	!						|  1: Other Landuse
	!						|  2: Urban
	!						|  3: Sum of 1 and 2
	! AnnualBaseflow		| Sum of Baseflow

!----------------------------------------------S read OptParm-------------------
	open(2, file='myOptPar.pys', status='old')
	  do i = 1, 6
	    read(2,*) OptParm(i)
	  enddo 
	close(2)
!----------------------------------------------E read OptParm-------------------

!----------S read main input file (mainINP.txt)---------------------------------
	open(1, file='mainINP.txt', status='old')
	  read(1,*) num, swsOpt
	  read(1,*)										! Table 1 
	  do i = 1, num
	    read(1,*) (LuseAreaWS(j,i),j=1,6), PctFeedlot(i), TAreaWS(i)
!     &			  AnnualR(i), RDays(i), AvgR(i)
	  enddo
!	  read(1,*) AnnualRF, RDaysF
	  read(1,*)										! Table 2
	  do i =1, num
	    read(1,*) (Animals(j,i),j=1,8), NumMonManure(i)
	  enddo
	  read(1,*)										! Table 3
	  do i = 1, num
	    read(1,*) NumSpSys(i), PpSpSys(i),SpFailRate(i), 
     &		      NumPpDrtDc(i), RdcDrtDc(i)
	  enddo
	  read(1,*)										! Table 4
	  do i = 1, num
	    read(1,*) (usleCropland(j,i),j=1,5)
	  enddo
	  read(1,*)
	  do i = 1, num
	    read(1,*) (uslePasture(j,i),j=1,5)
	  enddo
	  read(1,*)
	  do i = 1, num
	    read(1,*) (usleForest(j,i),j=1,5)
	  enddo	
	  read(1,*)
	  do i = 1, num
	    read(1,*) (usleUser(j,i),j=1,5)
	  enddo
	  read(1,*)										! Table 5
	  do i = 1, num
	    read(1,*) SHG(i), SoilNconc(i), SoilPconc(i), SoilBODconc(i)
	  enddo
	  read(1,*)										! Table 6
	  do i = 1, 5
	    read(1,*) (CN(j,i),j=1,4)
	  enddo
	  read(1,*)										! Table 6a
	  do i = 1, 9
	    read(1,*) (UrbanCN(j,i),j=1,4)
	  enddo
	  read(1,*)										! Table 7
	  do i = 1, 9
	    read(1,*) (NtConcRunoff(j,i),j=1,3)
	  enddo
	  read(1,*)										! Table 7a
	  do i = 1, 6
	    read(1,*) (NtConcGW(j,i),j=1,3)
	  enddo
	  read(1,*)										! Table 8
	  do i = 1, num
	    read(1,*) (UrbanDst(j,i),j=1,11)
	  enddo
	  read(1,*)										! Table 9
	  do i = 1, num
	    read(1,*) (Irrigation(j,i),j=1,5)
	  enddo

	close(1)

!----------E read main input file (mainINP.txt)---------------------------------
!----------------------------------------------S GW1 (LandRain_GW1.txt)---------
	open(2, file='LandRain_GW1.txt', status='old')
	  read(2,*)
	  do i = 1, 5
	    read(2,*) (GW1(j,i),j=1,4)
	  enddo
	close(2)
!----------------------------------------------E GW1 (LandRain_GW1.txt)---------
!------S update parameters by OptParm()-----------------------------------------
	do i = 1, 4
	  do j = 1, 5
	    CN(i,j) = CN(i,j) * OptParm(1)
	    if ( 100.0 < CN(i,j) ) CN(i,j) = 100.0
	  enddo
	  do j = 1, 9
	    UrbanCN(i,j) = UrbanCN(i,j) * OptParm(1)
	    if ( 100.0 < UrbanCN(i,j) ) UrbanCN(i,j) = 100.0
	  enddo
	  do j = 1, 5
	    GW1(i,j) = GW1(i,j) * OptParm(2)
	    if ( 0.9 < GW1(i,j) ) GW1(i,j) = 0.9
	  enddo
	enddo

	do i = 1, 3
	  do j = 1, 9
	    NtConcRunoff(i,j) = NtConcRunoff(i,j) * OptParm(3)
	  enddo
	  do j = 1, 6
	    NtConcGW(i,j) = NtConcGW(i,j) * OptParm(4)
	  enddo
	enddo

!	DREC(1) = 0.417662 * OptParm(5)
!	DREC(2) = -0.134958 * OptParm(6)
!	DREC(3) = 0.42 * OptParm(7)
!	DREC(4) = -0.125 * OptParm(8)
	DREC(1) = OptParm(5)
	DREC(2) = OptParm(6)
	DREC(3) = OptParm(7)
	DREC(4) = OptParm(8)

!------E update parameters by OptParm()-----------------------------------------

	Lambda = 0.2				! LandRain, shoud be 0.2
	call ANRUNOFF
	call LANDRAIN
	call BMPS
	call ANIMAL
	call FEEDLOTS
	call SEPTIC
	call SEDIMENT
	call URBAN
	call GULLY
	call TOTALLOAD

!!	open(10, file='myRST.csv', status='replace', recl=9999999)
!!	write(10,*) 'Watershed,N Load (no BMP),P Load (no BMP),
!!     &BOD Load (no BMP),Sediment Load (no BMP),N Reduction,
!!     &P Reduction,BOD Reduction,Sediment Reduction,N Load (with BMP),
!!     &P Load (with BMP),BOD (with BMP),Sediment Load (with BMP),	
!!     &%N Reduction,%P Reduction,%BOD Reduction,%Sed Reduction'

!	do i = 1, num
!	  write(10,*) i, (TL1(j,i),j=1,4)
!	enddo
!	do i = 1, num
!	  write(10,*) i, (TL1(j,i),j=5,8)
!        enddo
!	do i = 1, num
!          write(10,*) i, (TL1(j,i),j=9,12)
!	enddo
!	do i = 1, num
!	  write(10,*) i, (TL1(j,i),j=13,16)
!	enddo

!!	do i = 1, num
!!	  write(10,*) i, (TL1(j,i),j=1,16)
!!	enddo
!!	write(10,*) 'Total', (TL1(j,31),j=1,16)
!!	write(10,*) (TL1(j,31),j=1,16)
!!	close(10)
	
	AnnualRunoff(1) = 0.0
	AnnualRunoff(2) = 0.0
	AnnualRunoff(3) = 0.0
	AnnualBaseflow = 0.0
	do i = 1, num
	  AnnualRunoff(1) = AnnualRunoff(1) + VRunoff(6,i)
	  do j = 1, 9
	    AnnualRunoff(2) = AnnualRunoff(2) + VUrbanRunoff(j,i)
	  enddo
	  do j = 1, 6
	    AnnualBaseflow = AnnualBaseflow + GW4(j,i)
	  enddo
	enddo
	AnnualRunoff(3) = AnnualRunoff(1) + AnnualRunoff(2)

	! Runoff, Baseflow, N, P, BOD, S
	open(10, file='stepl_rst.pys', status='replace', recl=9999999)
	  write(10,*) AnnualRunoff(3)
	  write(10,*) AnnualBaseflow
	  do i = 1, 4
	    write(10,*) TL1(i,31)
	  enddo
	close(10)
	
	END

!---------------------------S SUBROUTINES---------------------------------------

!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE ANRUNOFF
	use parm
	INTEGER :: pcpCount, tmpVal
	REAL :: myS, myS2, myS8, depth, depthSum
	! depth: daily runoff depth
	! depthSum: sum of daily runoff depth
	
	pcpCount = 0
	open(13, file='pcp.txt', status='old')
	  do i=1, 40000
	    read(13,*,end=1001) tmpVal, Rainfall(i)
	    pcpCount = pcpCount + 1
	  enddo
1001    continue
	close(13)

      !write(*,*) pcpCount 
	
	! General Luse
	do i=1, 5								! luse
	  do j=1, 4								! hsg
	    if ( 0.0 < CN(j,i) ) then
	      myS = 25400.0 / CN(j,i) - 254.0
	    else
	      myS = 10000000000000.0 
	    endif	    
	    myS2 = myS * 0.2
	    myS8 = myS * 0.8
	    depth = 0.0
	    depthSum = 0.0
	    do k=1, pcpCount							! pcp
	      if ( myS2 < Rainfall(k) ) then
	        depth = ( (Rainfall(k)-myS2)**2 )/(Rainfall(k)+myS8)	
	      else
	        depth = 0.0
	      endif
	      depthSum = depthSum + depth
	    enddo								! k, pcp
	    depthSum = depthSum / pcpCount * 365
	    anDepth(j,i) = depthSum
	  enddo									! j, hsg
	enddo									! i, luse

	! Urban Luse
	do i=1, 9								! luse
	  do j=1, 4								! hsg
	    if ( 0.0 < UrbanCN(j,i) ) then
	      myS = 25400.0 / UrbanCN(j,i) - 254.0
	    else
	      myS = 10000000000000.0
	    endif	    
	    myS2 = myS * 0.2
	    myS8 = myS * 0.8
	    depth = 0.0
	    depthSum = 0.0
	    do k=1, pcpCount							! pcp
	      if ( myS2 < Rainfall(k) ) then
	        depth = ( (Rainfall(k)-myS2)**2 )/(Rainfall(k)+myS8)	
	      else
	        depth = 0.0
	      endif
	      depthSum = depthSum + depth
	    enddo								! k, pcp
	    depthSum = depthSum / pcpCount * 365
	    anDepth(j,i+5) = depthSum
	  enddo									! j, hsg
	enddo									! i, luse


	! Feedlot
	feCN(1) = 91
	feCN(2) = 92
	feCN(3) = 93
	feCN(4) = 94

	do j=1, 4								! hsg
	  if ( 0.0 < feCN(j) ) then
	    myS = 25400.0 / feCN(j) - 254.0
	  else
	    myS = 10000000000000.0
	  endif	    
	  myS2 = myS * 0.2
	  myS8 = myS * 0.8
	  depth = 0.0
	  depthSum = 0.0
	  do k=1, pcpCount							! pcp
	    if ( myS2 < Rainfall(k) ) then
	      depth = ( (Rainfall(k)-myS2)**2 )/(Rainfall(k)+myS8)	
	    else
	      depth = 0.0
	    endif
	    depthSum = depthSum + depth
	  enddo									! k, pcp
	  depthSum = depthSum / pcpCount * 365
	  feDepth(j) = depthSum / 25.4						! mm -> in
	enddo									! j, hsg

		
	! Calculate Annual Precipitation
	anPcpDepth = 0.0
	do i=1, pcpCount
	  anPcpDepth = anPcpDepth + Rainfall(i)
	enddo
	anPcpDepth = anPcpDepth / pcpCount * 365

!	do i=1, 14
!	  write(*,*) anDepth(1,i),anDepth(2,i),anDepth(3,i),anDepth(4,i)
!	enddo
!	write(*,*) anPcpDepth
	
		
	END ! ANRUNOFF
	 
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE LANDRAIN
	use parm
!	REAL :: anDepth(4,15)				! array of anDepth.txt

	! Table 1a, Detailed urban land use area (ac)
	do i = 1, num
	  UrbanArea(10,i) = 0.0
	  UrbanArea(11,i) = 0.0
	  do j = 1, 9
	    UrbanArea(j,i) = UrbanDst(j+1,i) * UrbanDst(1,i) / 100
	    UrbanArea(10,i) = UrbanArea(10,i) + UrbanArea(j,i)
	  enddo
	  UrbanArea(11,i) = UrbanArea(10,i) - ( UrbanArea(1,i) * 0.85 +
     &		UrbanArea(2,i) * 0.7  + UrbanArea(3,i) * 0.5  +
     &		UrbanArea(4,i) * 0.95 + UrbanArea(5,i) * 0.75 +
     &		UrbanArea(6,i) * 0.3  + UrbanArea(7,i) * 0.01 +
     &		UrbanArea(8,i) * 0.7  + UrbanArea(9,i) * 0.01 )
	enddo

	! Table 2.1, Curve Number
	do i = 1, num
	  do j = 1, 5
	    myCN(j,i) = CN(SHG(i),j)
	  enddo
	enddo

!!!!	open(11, file='anDepth.txt', status='old')
!!!!	  do i = 1, 14
!!!!	    read(11,*) anDepth(1,i), anDepth(2,i), 
!!!!     &               anDepth(3,i), anDepth(4,i)
!!!!	  enddo
!!!!	 read(11,*) anPcpDepth
!!!!	close(11)
	anPcpDepth = anPcpDepth * 0.03937
	! inch     = mm * 0.03937

	! Table 2.2, Calculated runoff (in)
!	do i = 1, num
!	  do j = 1, 5
!	    if ( 0 < (AvgR(i)-Lambda*(1000/myCN(j,i)-10)) ) then
!	      Runoff(j,i) = 
!     &		  ( AvgR(i)-Lambda*(1000/myCN(j,i)-10) )**2 /
!     &		  ( AvgR(i)+(1-Lambda)*(1000/myCN(j,i)-10) )
!	    else
!	      Runoff(j,i) = 0.0
!	    endif
!	  enddo
!	enddo


	do i = 1, num
	  do j = 1, 5
	    Runoff(j,i) = anDepth(SHG(i),j) * 0.03937
		  !      in = mm * 0.03937 
	  enddo
	enddo

	! Table 2.1a, Urban Runoff Curve Number
	do i = 1, num
	  do j = 1, 9
	    myUrbanCN(j,i) = UrbanCN(SHG(i),j)
	  enddo
	enddo

	! Table 2.2a, Runoff by urban landuse (in)
!	do i = 1, num
!	  do j = 1, 9
!	    if ( 0 < (AvgR(i)-Lambda*(1000/myUrbanCN(j,i)-10)) ) then
!	      UrbanRunoff(j,i) = 
!     &		  ( AvgR(i)-Lambda*(1000/myUrbanCN(j,i)-10) )**2 /
!     &		  ( AvgR(i)+(1-Lambda)*(1000/myUrbanCN(j,i)-10) )
!	    else
!	      UrbanRunoff(j,i) = 0.0
!	    endif
!	  enddo
!	enddo
	do i = 1, num
	  do j = 6, 14
	    UrbanRunoff(j-5,i) = anDepth(SHG(i),j) * 0.03937
		  !      in = mm * 0.03937 
	  enddo
	enddo
	
	! Table 2.3, Irrigation runoff (in)
	do i = 1, num
	  if ( 0 < (Irrigation(3,i)-Lambda*(1000/myCN(2,i)-10)) ) then
	    IrRunoff(1,i) =
     &        (Irrigation(3,i)-Lambda*(1000/myCN(2,i)-10)) ** 2 /
     &		(Irrigation(3,i)+(1-Lambda)*(1000/myCN(2,i)-10))
	  else
	    IrRunoff(1,i) = 0.0
	  endif
	  if ( 0 < (Irrigation(4,i)-Lambda*(1000/myCN(2,i)-10)) ) then
	    IrRunoff(2,i) =
     &        (Irrigation(4,i)-Lambda*(1000/myCN(2,i)-10)) ** 2 /
     &		(Irrigation(4,i)+(1-Lambda)*(1000/myCN(2,i)-10))
	  else
	    IrRunoff(2,i) = 0.0
	  endif
	  IrRunoff(3,i) = IrRunoff(1,i) - IrRunoff(2,i)
	enddo

	! Table GW2, Infiletation Fraction Based on SHG
	do i = 1, num
	  do j = 1, 5
	    GW2(j,i) = GW1(SHG(i),j)
	  enddo
	enddo	

	! Table GW3, Calculated Infiltration (in)
	do i = 1, num
	  do j = 1, 5
!	    GW3(j,i) = GW2(j,i) * AvgR(i)
	    GW3(j,i) = GW2(j,i) * anPcpDepth
	    ! in     = fraction * inch
	  enddo
	enddo	

	! Table GW4, Calculated infiltration volume (ac-ft)
	do i = 1, num
!	  GW4(1,i) = (GW3(1,i)/12) * RDays(i) * RDaysF * UrbanArea(11,i)
	  GW4(1,i) = (GW3(1,i)/12) * UrbanArea(11,i)
	  do j = 2, 5
!	    GW4(j,i) = (GW3(j,i)/12) * RDays(i) * RDaysF 
!     &					* LuseAreaWS(j,i)
	    GW4(j,i) = (GW3(j,i)/12) * LuseAreaWS(j,i)
	  enddo
	enddo
	! GW4(6,i) is calculated in "FEEDLOTS subroutine".


	! Table 4, Annual runoff by land uses (ac-ft)
	do i = 1, num
	  VRunoff(6,i) = 0.0
	  do j = 1, 5
	    VRunoff(j,i) = Runoff(j,i) / 12 * LuseAreaWS(j,i)
!     &				   LuseAreaWS(j,i) * RDays(i) * RDaysF
	  enddo
	  VRunoff(2,i) = VRunoff(2,i) + 
     &			IrRunoff(1,i) / 12 * Irrigation(2,i) * Irrigation(5,i)
	  do j = 1, 5
     	    VRunoff(6,i) = VRunoff(6,i) + VRunoff(j,i)
	  enddo
	enddo


	! Table 4a, Urban annual runoff (ac-ft)
	do i = 1, num
	  do j = 1, 9
	    VUrbanRunoff(j,i) = UrbanRunoff(j,i) / 12 * UrbanArea(j,i)
!     &					    UrbanArea(j,i) * RDays(i) * RDaysF
	  enddo
	enddo


	! Table 6, Runoff reduction by land uses (ac-ft)(for irrigation reduction in cropland)
	do i = 1, num
	  RdcIrRunoff(1,i) = IrRunoff(3,i) / 12 *
     &				Irrigation(2,i) * Irrigation(5,i)
	  RdcIrRunoff(2,i) = RdcIrRunoff(1,i)
	enddo	


!	do i = 1, num
!	  write(*,*) RdcIrRunoff(1,i)
!	enddo
!	write(*,*) '----------'

!	do i = 1, num
!	  write(*,*) VRunoff(6,i)
!	  do j = 1, 9
!	    write(*,*) VUrbanRunoff(j,i)
!	  enddo
!	enddo
!	write(*,*) '----'
!	do i = 1, num
!	  do j = 1, 6
!	    write(*,*) GW4(j,i)
!	  enddo
!	enddo



	RETURN
	END	! LandRain



!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE FEEDLOTS
	use parm
	REAL PrvAreaF

	! Table 1, Select a range of paved percentage for feedlots
	do i = 1, num
	  Feedlots_1(1,i) = LuseAreaWS (6,i)
	  Feedlots_1(2,i) = PctFeedlot(i)
!	  Feedlots_1(3,i) = AvgR(i)
	  Feedlots_1(4,i) = BMPeff_FL(1,i)
	  Feedlots_1(5,i) = BMPeff_FL(2,i)
	  Feedlots_1(6,i) = BMPeff_FL(3,i)
	  if ( Feedlots_1(2,i) < 25 ) then
	    PrvAreaF = 0.125
	    Feedlots_4(i,1) = feCN(1)
	  elseif ( 25 <= Feedlots_1(2,i) .and. Feedlots_1(2,i) < 50 ) then
	    PrvAreaF = 0.375
	    Feedlots_4(i,1) = feCN(2)
	  elseif ( 50 <= Feedlots_1(2,i) .and. Feedlots_1(2,i) < 75 ) then
	    PrvAreaF = 0.625
	    Feedlots_4(i,1) = feCN(3)
	  else
	    PrvAreaF = 0.875
	    Feedlots_4(i,1) = feCN(4)
	  endif
	  Feedlots_1(7,i) = Feedlots_1(1,i) * PrvAreaF
!	  GW4(6,i) = (GW3(1,i)/12) * RDays(i) * RDaysF * Feedlots_1(7,i) 
	  GW4(6,i) = (GW3(1,i)/12) * Feedlots_1(7,i)
	enddo

	! Table 2, Agricultural animals
	do i = 1, num
	  do j = 1, 11
	    Feedlots_2(j,i) = 0
	  enddo
	  Feedlots_2(1,i) = Animals(1,i)
	  Feedlots_2(3,i) = Animals(2,i)
	  Feedlots_2(5,i) = Animals(3,i)
	  Feedlots_2(7,i) = Animals(4,i)
	  Feedlots_2(8,i) = Animals(5,i)
	  Feedlots_2(9,i) = Animals(6,i)
	  Feedlots_2(10,i) = Animals(7,i)
	  Feedlots_2(11,i) = Animals(8,i)
	enddo

	! Table 5, Ratio of nutrients produced by animals relative to 1000 lb of slaughter steer
	open(6, file='Feedlot.txt', status='old')
	  read(6,*)
	  do i = 1, 11
	    read(6,*) (Feedlots_5(j,i),j=1,4)
	  enddo
	close(6)


	! Table 4, Feedlot load calculation
	do i = 1, num
	  ! Feedlots_4(i,1) was calculated at Table 1
	  Feedlots_4(i,2) = 1000 / Feedlots_4(i,1) - 10
	  if ( PctFeedlot(i) < 25 ) then
	    Feedlots_4(i,3) = feDepth(1)
	  elseif ( 25 <= PctFeedlot(i) .and. PctFeedlot(i) < 50 ) then
	    Feedlots_4(i,3) = feDepth(2)
	  elseif ( 50 <= PctFeedlot(i) .and. PctFeedlot(i) < 75 ) then
	    Feedlots_4(i,3) = feDepth(3)
	  else
	    Feedlots_4(i,3) = feDepth(4)
	  end if
	  Feedlots_4(i,4) = Feedlots_4(i,3) * Feedlots_1(1,i)
	  Feedlots_4(i,5) = 0.0
	  do j = 1, 11
	    Feedlots_4(i,5) = Feedlots_4(i,5) + 
     &					  Feedlots_2(j,i) * Feedlots_5(1,j) 
	  enddo
	  Feedlots_4(i,6) = 0.0
	  do j = 1, 11
	    Feedlots_4(i,6) = Feedlots_4(i,6) + 
     &					  Feedlots_2(j,i) * Feedlots_5(2,j) 
	  enddo
	  Feedlots_4(i,7) = 0.0
	  do j = 1, 11
	    Feedlots_4(i,7) = Feedlots_4(i,7) + 
     &					  Feedlots_2(j,i) * Feedlots_5(3,j) 
	  enddo
	  Feedlots_4(i,8) = 0.0
	  do j = 1, 11
	    Feedlots_4(i,8) = Feedlots_4(i,8) + 
     &					  Feedlots_2(j,i) * Feedlots_5(4,j) 
	  enddo
	  if ( 0 < Feedlots_1(1,i) ) then
	    Feedlots_4(i,9) = Feedlots_4(i,5) / Feedlots_1(1,i)
	    Feedlots_4(i,10) = Feedlots_4(i,6) / Feedlots_1(1,i)
	    Feedlots_4(i,11) = Feedlots_4(i,7) / Feedlots_1(1,i)
	    Feedlots_4(i,12) = Feedlots_4(i,8) / Feedlots_1(1,i)
	  else
	    Feedlots_4(i,9) = 0.0
	    Feedlots_4(i,10) = 0.0
	    Feedlots_4(i,11) = 0.0
	    Feedlots_4(i,12) = 0.0
	  endif
	  Feedlots_4(i,13) = min(Feedlots_4(i,9),100.0) / 100
	  Feedlots_4(i,14) = min(Feedlots_4(i,10),100.0) / 100
	  Feedlots_4(i,15) = min(Feedlots_4(i,11),100.0) / 100
	  Feedlots_4(i,16) = min(Feedlots_4(i,12),100.0) / 100
	  Feedlots_4(i,17) = Feedlots_4(i,13) * 1500
	  Feedlots_4(i,18) = Feedlots_4(i,14) * 300
	  Feedlots_4(i,19) = Feedlots_4(i,15) * 2000
	  Feedlots_4(i,20) = Feedlots_4(i,16) * 4500
	enddo

	! Table 3, Load from feedlot (lb/yr) (1 ac x in x mg/l = 0.227 lb)
	! Load_Fdl(6,30)
	do i = 1, num
	  if ( 0 < Feedlots_1(1,i) ) then
	    Load_Fdl(1,i) = Feedlots_4(i,4) * Feedlots_4(i,17) * 0.227
	    Load_Fdl(2,i) = Feedlots_4(i,4) * Feedlots_4(i,18) * 0.227
	    Load_Fdl(3,i) = Feedlots_4(i,4) * Feedlots_4(i,19) * 0.227
	    Load_Fdl(4,i) = Load_Fdl(1,i) * Feedlots_1(4,i)
	    Load_Fdl(5,i) = Load_Fdl(2,i) * Feedlots_1(5,i)
	    Load_Fdl(6,i) = Load_Fdl(3,i) * Feedlots_1(6,i)
	  else
	    Load_Fdl(1,i) = 0.0
	    Load_Fdl(2,i) = 0.0
	    Load_Fdl(3,i) = 0.0
	    Load_Fdl(4,i) = 0.0
	    Load_Fdl(5,i) = 0.0
	    Load_Fdl(6,i) = 0.0
	  endif
	enddo


!	do i = 1, num
!	  write(*,*) (Load_Fdl(j,i),j=1,6)
!	enddo

	RETURN
	END

!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE BMPS
	use parm

	open(3,file='BMPs.txt',status='old')
	  read(3,*)
	  do i = 1, num
	    read(3,*) (BMPeff_C(j,i),j=1,5)
	  enddo
	  read(3,*)
	  read(3,*)
	  do i = 1, num
	    read(3,*) (BMPeff_P(j,i),j=1,5)
	  enddo
	  read(3,*)
	  read(3,*)
	  do i = 1, num
	    read(3,*) (BMPeff_F(j,i),j=1,5)
	  enddo
	  read(3,*)
	  read(3,*)
	  do i = 1, num
	    read(3,*) (BMPeff_U(j,i),j=1,5)
	  enddo
	  read(3,*)
	  read(3,*)
	  do i = 1, num
	    read(3,*) (BMPeff_FL(j,i),j=1,5)
	  enddo

	close(3)

	

!	do i = 1, num
!	  write(*,*) (BMPeff_F(j,i),j=1,5)
!	enddo
	
	RETURN
	END

!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE ANIMAL
	use parm
	
	open(4, file='Reference.txt',status='old')
	  read(4,*)
	  do i = 1, 13
	    read(4,*) (Ref(j,i),j=1,4)
	  enddo	
	close(4)	

	! Table 1, Agricultural animals
	do i = 1, num
	  if ( 0 < LuseAreaWS(2,i) ) then
	    AEU(i) = (Animals(1,i) * Ref(1,1) + Animals(2,i) * Ref(1,2) +
     &			  Animals(3,i) * Ref(1,3) + Animals(4,i) * Ref(1,4) +
     &			  Animals(5,i) * Ref(1,5) + Animals(6,i) * Ref(1,6) +
     &			  Animals(7,i) * Ref(1,7) + Animals(8,i) * Ref(1,8) )/
     &			  1000 / LuseAreaWS(2,i)
	  else
	    AEU(i) = 0.0
	  endif
	enddo

	! Table 2, Wildlife density in cropland
	open(5, file='WildLife.txt',status='old')
	  do i = 1, 5
	    read(5,*) WildLifeD(1,i)
	    WildLifeD(2,i) = WildLifeD(1,i) / 640
	  enddo
	close(5)

	! Table 3, Estimated wildlife and AEU in watersheds
	do i = 1, num
	  do j = 1, 5
	    AEUwl(j,i) = LuseAreaWS(2,i) * WildLifeD(2,j)
	  enddo
	  if ( 0 < LuseAreaWS(2,i) ) then
	    AEUwl(6,i) = (AEUwl(1,i) * Ref(1,9) + AEUwl(2,i) * Ref(1,10) + 
     &				 AEUwl(3,i) * Ref(1,11) + AEUwl(4,i) * Ref(1,12) + 
     &				 AEUwl(5,i) * Ref(1,13) ) / 1000 /  LuseAreaWS(2,i)
	  else
	    AEUwl(6,i) = 0.0
	  endif
	enddo

	! Table 4, Total animal equivalent units and nutrient concentrations 
	do i = 1, num
	  AnimalPNB(1,i) = AEU(i) + AEUwl(6,i)
	  if ( AnimalPNB(1,i) <= 1.5 ) then
	    AnimalPNB(2,i) = NtConcRunoff(1,1)
	    AnimalPNB(3,i) = NtConcRunoff(1,2)
	    AnimalPNB(4,i) = NtConcRunoff(2,1)
	    AnimalPNB(5,i) = NtConcRunoff(2,2)
	    AnimalPNB(6,i) = NtConcRunoff(3,1)
	    AnimalPNB(7,i) = NtConcRunoff(3,2)
	  elseif ( 1.5 < AnimalPNB(1,i) .and. AnimalPNB(1,i) < 2.5 ) then
	    AnimalPNB(2,i) = NtConcRunoff(1,3)
	    AnimalPNB(3,i) = NtConcRunoff(1,4)
	    AnimalPNB(4,i) = NtConcRunoff(2,3)
	    AnimalPNB(5,i) = NtConcRunoff(2,4)
	    AnimalPNB(6,i) = NtConcRunoff(3,3)
	    AnimalPNB(7,i) = NtConcRunoff(3,4)
	  else
	    AnimalPNB(2,i) = NtConcRunoff(1,5)
	    AnimalPNB(3,i) = NtConcRunoff(1,6)
	    AnimalPNB(4,i) = NtConcRunoff(2,5)
	    AnimalPNB(5,i) = NtConcRunoff(2,6)
	    AnimalPNB(6,i) = NtConcRunoff(3,5)
	    AnimalPNB(7,i) = NtConcRunoff(3,6)
	  endif 

	enddo

!	do i = 1, num
!	  write(*,*) (AnimalPNB(j,i),j=1,5)
!	enddo
!	do i = 1, num
!	  write(*,*) (AnimalPNB(j+5,i),j=1,2)
!	enddo

	RETURN
	END

!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE SEPTIC
	use parm

	! A table between Table 1 and 2
	open(7, file='Septic.txt', status='old')
	  do i = 1, 8
	    read(7,*) SpDB(i)
	  enddo
	close(7)
	
	! Table 1, Nutrient load from septic systems
	do i = 1, num
	  Septic_1(1,i) = NumSpSys(i)
	  Septic_1(2,i) = PpSpSys(i)
	  Septic_1(3,i) = SpFailRate(i)
	  Septic_1(4,i) = Septic_1(1,i) * Septic_1(3,i) / 100
	  Septic_1(5,i) = Septic_1(1,i) * Septic_1(2,i) *Septic_1(3,i)/100
	  Septic_1(6,i) = NumPpDrtDc(i)
	  Septic_1(7,i) = Septic_1(5,i) * SpDB(4)
	  Septic_1(8,i) = Septic_1(6,i) * SpDB(8)
	  Septic_1(9,i) = Septic_1(7,i) * 3.785412 / 24
	  Septic_1(10,i) = Septic_1(8,i) * 3.785412/24
	  Septic_1(11,i) = (Septic_1(9,i) * SpDB(1) + 
     &	                Septic_1(10,i) * SpDB(5)) / 453592.4
	  Septic_1(12,i) = (Septic_1(9,i) * SpDB(2) + 
     &	                Septic_1(10,i) * SpDB(6)) / 453592.4
	  Septic_1(13,i) = (Septic_1(9,i) * SpDB(3) + 
     &	                Septic_1(10,i) * SpDB(7)) / 453592.4
	  Septic_1(14,i) = RdcDrtDc(i) * Septic_1(10,i) / 100
	  Septic_1(15,i) = SpDB(5) * Septic_1(14,i) / 453592.4
	  Septic_1(16,i) = SpDB(6) * Septic_1(14,i) / 453592.4
	  Septic_1(17,i) = SpDB(7) * Septic_1(14,i) / 453592.4
	enddo

	! Table 2, Septic nutrient load in lb/yr	
	do i = 1, num
	  SepticPNB(1,i) = Septic_1(11,i) * 24 * 365
	  SepticPNB(2,i) = Septic_1(12,i) * 24 * 365
	  SepticPNB(3,i) = Septic_1(13,i) * 24 * 365
	  SepticPNB(4,i) = Septic_1(15,i) * 24 * 365
	  SepticPNB(5,i) = Septic_1(16,i) * 24 * 365
	  SepticPNB(6,i) = Septic_1(17,i) * 24 * 365
	  SepticPNB(7,i) = SepticPNB(1,i) - SepticPNB(4,i)
	  SepticPNB(8,i) = SepticPNB(2,i) - SepticPNB(5,i)
	  SepticPNB(9,i) = SepticPNB(3,i) - SepticPNB(6,i)
	enddo



!	do i = 1, num
!	  write(*,*) (SepticPNB(j,i),j=1,5)
!	enddo
!	write(*,*) '-------------------------'
!	do i = 1, num
!	  write(*,*) (SepticPNB(j,i),j=6,9)
!	enddo


	RETURN
	END
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE SEDIMENT
	use parm
	
	! Table 1, Input USLE parameters
	do i = 1, num
	  do j = 1, 5
	    Sed_1(j,i) = usleCropland(j,i)
	    Sed_1(j+5,i) = uslePasture(j,i)
	    Sed_1(j+10,i) = usleForest(j,i)
	    Sed_1(j+15,i) = usleUser(j,i)
	  enddo
	  Sed_1(22,i) = 0
	  if ( swsOpt < 2 ) then
	    do j = 1, 6
	      do k = 1, num
	        Sed_1(22,i) = Sed_1(22,i) + LuseAreaWS(j,k)
	      enddo
	    enddo	    
	  else
	    do j = 1, 6
	        Sed_1(22,i) = Sed_1(22,i) + LuseAreaWS(j,i)
	    enddo
	  endif
	  if ( Sed_1(22,i) <= 0 ) then
	    Sed_1(21,i) = 0
	  elseif ( 200 < Sed_1(22,i) ) then
	    Sed_1(21,i) = 0.417662*(Sed_1(22,i)/640)**(-0.134958)-0.127097
	    Sed_1(21,i) = Sed_1(21,i) * DREC(1)
	  else 
		Sed_1(21,i) = 0.42*(Sed_1(22,i)/640)**(-0.125)
	    Sed_1(21,i) = Sed_1(21,i) * DREC(2)
	  endif
	enddo

	! Table 1a, BMP and efficiency, C=Cropland, P=Pastureland,F=Forest,U=Urban
	do i = 1, num
	  Sed_1a(1,i) = BMPeff_C(4,i)
	  Sed_1a(2,i) = BMPeff_P(4,i)
	  Sed_1a(3,i) = BMPeff_F(4,i)
	  Sed_1a(4,i) = BMPeff_U(4,i)
	  Sed_1a(5,i) = BMPeff_C(1,i)
	  Sed_1a(6,i) = BMPeff_P(1,i)
	  Sed_1a(7,i) = BMPeff_F(1,i)
	  Sed_1a(8,i) = BMPeff_U(1,i)
	  Sed_1a(9,i) = BMPeff_C(2,i)
	  Sed_1a(10,i) = BMPeff_P(2,i)
	  Sed_1a(11,i) = BMPeff_F(2,i)
	  Sed_1a(12,i) = BMPeff_U(2,i)
	  Sed_1a(13,i) = BMPeff_C(3,i)
	  Sed_1a(14,i) = BMPeff_P(3,i)
	  Sed_1a(15,i) = BMPeff_F(3,i)
	  Sed_1a(16,i) = BMPeff_U(3,i)
	enddo

	! Table 2, Erosion and sediment delivery (ton/year)
	do i = 1, num
	  do j = 1, 4
	    Sed_2(j,i) = Sed_1(5*j-4,i) * Sed_1(5*j-3,i) * Sed_1(5*j-2,i)*
     &		  	     Sed_1(5*j-1,i) * Sed_1(5*j,i)
	  enddo
	  Sed_2(1,i) = Sed_2(1,i) * LuseAreaWS(2,i)
	  Sed_2(2,i) = Sed_2(2,i) * LuseAreaWS(3,i)
	  Sed_2(3,i) = Sed_2(3,i) * LuseAreaWS(4,i)
	  Sed_2(4,i) = Sed_2(4,i) * LuseAreaWS(5,i)
	  Sed_2(5,i) = 0.0
	  do j = 1, 4
	    Sed_2(5,i) = Sed_2(5,i) + Sed_2(j,i)
	  enddo
	  Sed_2(6,i) = Sed_2(5,i) * Sed_1(21,i)
	  ! Sed_2(7,i) , Sed_2(8,i) are calculated after Table 2a.
	enddo

	! Table 2a, Erosion and sediment delivery after BMP (ton/year)
	do i = 1, num
	  Sed_2a(5,i) = 0.0
	  do j = 1, 4
	    Sed_2a(j,i) = Sed_2(j,i) * (1-Sed_1a(j,i))
	    Sed_2a(5,i) = Sed_2a(5,i) + Sed_2a(j,i)
	    Sed_2a(6,i) = Sed_2a(5,i) * Sed_1(21,i)
	  enddo
	  Sed_2(7,i) = Sed_2(6,i) - Sed_2a(6,i)				! Table 2
	  if ( Sed_2(6,i) <= 0.0 ) then
	    Sed_2(8,i) = 0.0
	   else
	    Sed_2(8,i) = Sed_2(7,i) / Sed_2(6,i) * 100
	  endif
	enddo

	! Table 3, Nutrient load from sediment (ton/year)
	do i = 1, num
	  Sed_3(1,i) = SoilNconc(i)
	  Sed_3(2,i) = SoilPconc(i)
	  Sed_3(3,i) = SoilBODconc(i)
	  Sed_3(4,i) = Sed_3(1,i) * Sed_2(6,i) * 2 / 100
	  Sed_3(5,i) = Sed_3(2,i) * Sed_2(6,i) * 2 / 100
	  Sed_3(6,i) = Sed_3(3,i) * Sed_2(6,i) * 2 / 100
	  Sed_3(7,i) = Sed_3(4,i) * Sed_2(8,i) / 100
	  Sed_3(8,i) = Sed_3(5,i) * Sed_2(8,i) / 100
	  Sed_3(9,i) = Sed_3(6,i) * Sed_2(8,i) / 100
	enddo

	! Table 3a, Sediment and sediment nutrients by land uses with BMP (ton/year)
		! Sed_3a(16,30)
	do i = 1, num
	  Sed_3a(4,i) = Sed_1(21,i) * Sed_2(1,i) * (1-Sed_1a(1,i)) 
	  Sed_3a(8,i) = Sed_1(21,i) * Sed_2(2,i) * (1-Sed_1a(2,i))
	  Sed_3a(12,i) = Sed_1(21,i) * Sed_2(3,i) * (1-Sed_1a(3,i))
	  Sed_3a(16,i) = Sed_1(21,i) * Sed_2(4,i) * (1-Sed_1a(4,i))

	  do j = 1, 3
	    Sed_3a(j,i) = Sed_3a(4,i) * Sed_3(j,i) * 2 / 100
	    Sed_3a(j+4,i) = Sed_3a(8,i) * Sed_3(j,i) * 2 / 100
	    Sed_3a(j+8,i) = Sed_3a(12,i) * Sed_3(j,i) * 2 / 100
	    Sed_3a(j+12,i) = Sed_3a(16,i) * Sed_3(j,i) * 2 / 100
	  enddo
	enddo




!	do i = 1, num
!	  write(*,*) (Sed_3a(j,i),j=1,5)
!	enddo
!	write(*,*) '--------------------------'
!	do i = 1, num
!	  write(*,*) (Sed_3a(j,i),j=6,10)
!	enddo
!	write(*,*) '--------------------------'
!	do i = 1, num
!	  write(*,*) (Sed_3a(j,i),j=11,15)
!	enddo
!	write(*,*) '--------------------------'
!	do i = 1, num
!	  write(*,*) Sed_3a(16,i)
!	enddo



	RETURN
	END

!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE URBAN
	use parm

	! Table 1, 2a, 3.2a, 3.3a, 3.4a, 3.5a
	open(8, file='BMPs.txt', status='old')
	  do i = 1, num * 5 + 9
	    read(8,*)
	  enddo
	  read(8,*)
	  
	  do i = 1, 4
	    read(8,*) (ub1(j,i),j=1,9)
	  enddo
	  read(8,*)

	  do i = 1, num
	    read(8,*) (ub2a(j,i),j=1,9)
	  enddo
	  read(8,*)

	  do i = 1, num
	    read(8,*) (ub32a(j,i),j=1,9)
	  enddo
	  read(8,*)
	  	
	  do i = 1, num
	    read(8,*) (ub33a(j,i),j=1,9)
	  enddo
	  read(8,*)

	  do i = 1, num
	    read(8,*) (ub34a(j,i),j=1,9)
	  enddo
	  read(8,*)

	  do i = 1, num
	    read(8,*) (ub35a(j,i),j=1,9)
	  enddo
	close(8)	

	! Table 2, Urban landuse distribution
		! UrbanArea(j,i) : j(1-9) are each area (ac).	

	! Table 3a, Percentage of BMP effective area (%)
	do i = 1, num
	  do j = 1, 9
	    if ( 0 < UrbanArea(j,i) ) then
	      ub3a(j,i) = ub2a(j,i) / UrbanArea(j,i) * 100
	    else
	      ub3a(j,i) = 0.0
	    endif
	  enddo
	enddo

	! Table 3.1,Urban runoff (ac-ft)
		! = VUrbanRunoff(j,i)

	! Table 3.2, 3.3, 3.4, 3.5
	do i = 1, num
	  do j = 1, 9
	    ub32(j,i) = 4047 * 0.3048 * VUrbanRunoff(j,i) * ub1(j,1)/1000
	    ub33(j,i) = 4047 * 0.3048 * VUrbanRunoff(j,i) * ub1(j,2)/1000
	    ub34(j,i) = 4047 * 0.3048 * VUrbanRunoff(j,i) * ub1(j,3)/1000
	    ub35(j,i) = 4047 * 0.3048 * VUrbanRunoff(j,i) * ub1(j,4)/1000
	  enddo
	enddo

	! Table 3.2b, 3.3b, 3.4b, 3.5b
	do i = 1, num
	  do j = 1, 9
	    ub32b(j,i) = ub32a(j,i) * ub32(j,i) * ub3a(j,i) / 100
	    ub33b(j,i) = ub33a(j,i) * ub33(j,i) * ub3a(j,i) / 100
	    ub34b(j,i) = ub34a(j,i) * ub34(j,i) * ub3a(j,i) / 100
	    ub35b(j,i) = ub35a(j,i) * ub35(j,i) * ub3a(j,i) / 100
	  enddo
	enddo

	! Table 4, Pollutant loads from urban in lb/year
	do i = 1, num
	  do j = 1, 12
	    ub4(j,i) = 0.0
	  enddo
	enddo

	do i = 1, num
	  do j = 1, 9
	    ub4(1,i) = ub4(1,i) + ub32(j,i)
	    ub4(2,i) = ub4(2,i) + ub33(j,i)
	    ub4(3,i) = ub4(3,i) + ub34(j,i)
	    ub4(4,i) = ub4(4,i) + ub35(j,i)
	    ub4(5,i) = ub4(5,i) + ub32b(j,i)
	    ub4(6,i) = ub4(6,i) + ub33b(j,i)
	    ub4(7,i) = ub4(7,i) + ub34b(j,i)
	    ub4(8,i) = ub4(8,i) + ub35b(j,i)
	  enddo
	  do j = 1, 8
	    ub4(j,i) = ub4(j,i) * 2.203
	  enddo
	  do j = 1, 4
	    ub4(j+8,i) = ub4(j,i) - ub4(j+4,i)
	  enddo

	enddo


!	do i = 1, num
!	  write(*,*) (ub4(j,i),j=1,5)
!	enddo
!	write(*,*) '--------------------'
!	do i = 1, num
!	  write(*,*) (ub4(j,i),j=6,10)
!	enddo
!	write(*,*) '--------------------'
!	do i = 1, num
!	  write(*,*) (ub4(j,i),j=11,12)
!	enddo
!	write(*,*) '--------------------'

	RETURN
	END

!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE GULLY
	use parm

	open(9, file='Gully.txt', status='old')
	  do i = 1, 10
	    read(9,*) GSDB1(1,i), GSDB1(2,i)
	  enddo
	  read(9,*)
	  do i = 1, 4
	    read(9,*) GSDB2(i)
	  enddo
	  read(9,*)
	  read(9,*) numGully
	  do i = 1, numGully
	    read(9,*) GS1t(i), (GS1(j,i),j=1,7), GS1_soil(i)
	  enddo
	  read(9,*)

	  read(9,*) numStr
	  do i = 1, numStr
	    read(9,*) GS2t(i), (GS2(j,i),j=1,3), GS2_LtRc(i), GS2(6,i),
     &			  GS2_soil(i)
	  enddo
	close(9)
	
	! Table 1, Gully dimensions in the different watersheds
	do i = 1, numGully
	  GS1(8,i) = GSDB1(1,GS1_soil(i))
	  GS1(9,i) = GSDB1(2,GS1_soil(i))
	  if ( 0 < GS1(6,i) ) then
	    GS1(10,i) = (GS1(2,i) + GS1(3,i)) * GS1(4,i) * GS1(5,i) *
     &				GS1(8,i) / GS1(6,i) / 2
	  else 
	    GS1(10,i) = 0.0
	  endif
	  GS1(11,i) = GS1(7,i) * GS1(10,i)
	  if ( 0 < GS1(6,i) ) then
	    GS1(12,i) = (GS1(2,i) + GS1(3,i)) * GS1(4,i) * GS1(5,i) *
     &				GS1(8,i) * GS1(9,i) / GS1(6,i) / 2
	  else
	    GS1(12,i) = 0.0
	  endif
	  GS1(13,i) = GS1(7,i) * GS1(12,i)	
	enddo

	! Table 2, Impaired streambank dimensions in the different watersheds
	do i = 1, numStr
	  GS2(4,i) = GSDB2(GS2_LtRc(i))
	  GS2(5,i) = GSDB2(GS2_LtRc(i))
	  GS2(7,i) = GSDB1(1,GS2_soil(i))
	  GS2(8,i) = GSDB1(2,GS2_soil(i))
	  GS2(9,i) = GS2(2,i) * GS2(3,i) * GS2(5,i) * GS2(7,i)
	  GS2(10,i) = GS2(6,i) * GS2(9,i)
	  GS2(11,i) = GS2(2,i) * GS2(3,i) * GS2(5,i) *
     &			  GS2(7,i) * GS2(8,i)
	  GS2(12,i) = GS2(6,i) * GS2(11,i)
	enddo

	! Table 3, Load and load reduction (lb/year, GU=Gully; SB=Streambank) in the different watersheds
	do i = 1, 30
	  do j = 1, 20
	    GS3(j,i) = 0.0
	  enddo
	enddo
	do i = 1, numGully
	  GS3(4,GS1t(i)) = GS3(4,GS1t(i)) + GS1(10,i)
	  GS3(8,GS1t(i)) = GS3(8,GS1t(i)) + GS1(11,i)
	  GS3(17,GS1t(i)) = GS3(17,GS1t(i)) + GS1(12,i)
	  GS3(18,GS1t(i)) = GS3(18,GS1t(i)) + GS1(13,i)
	enddo
	do i = 1, numStr
	  GS3(12,GS2t(i)) = GS3(12,GS2t(i)) + GS2(9,i)
	  GS3(16,GS2t(i)) = GS3(16,GS2t(i)) + GS2(10,i)
	  GS3(19,GS2t(i)) = GS3(19,GS2t(i)) + GS2(11,i)
	  GS3(20,GS2t(i)) = GS3(20,GS2t(i)) + GS2(12,i)
	enddo	
	do i = 1, num
	  GS3(4,i) = GS3(4,i) * 2000
	  GS3(8,i) = GS3(8,i) * 2000
	  GS3(12,i) = GS3(12,i) * 2000
	  GS3(16,i) = GS3(16,i) * 2000
	  GS3(17,i) = GS3(17,i) * 2000
	  GS3(18,i) = GS3(18,i) * 2000
	  GS3(19,i) = GS3(19,i) * 2000
	  GS3(20,i) = GS3(20,i) * 2000
	  
	  GS3(1,i) = GS3(17,i) * SoilNconc(i) / 100
	  GS3(2,i) = GS3(17,i) * SoilPconc(i) / 100
	  GS3(3,i) = GS3(17,i) * SoilBODconc(i) / 100
	  GS3(5,i) = GS3(18,i) * SoilNconc(i) / 100
	  GS3(6,i) = GS3(18,i) * SoilPconc(i) / 100
	  GS3(7,i) = GS3(18,i) * SoilBODconc(i) / 100
	  GS3(9,i) = GS3(19,i) * SoilNconc(i) / 100
	  GS3(10,i) = GS3(19,i) * SoilPconc(i) / 100
	  GS3(11,i) = GS3(19,i) * SoilBODconc(i) / 100
	  GS3(13,i) = GS3(20,i) * SoilNconc(i) / 100
	  GS3(14,i) = GS3(20,i) * SoilPconc(i) / 100
	  GS3(15,i) = GS3(20,i) * SoilBODconc(i) / 100
	enddo
	! SoilNconc(i), SoilPconc(i), SoilBODconc(i)



!	do i = 1, num
!	  write(*,*) (GS3(j,i),j=1,5)
!	enddo
!	write(*,*) '----------------------------------'
!	do i = 1, num
!	  write(*,*) (GS3(j,i),j=6,10)
!	enddo
!	write(*,*) '----------------------------------'
!	do i = 1, num
!	  write(*,*) (GS3(j,i),j=11,15)
!	enddo
!	write(*,*) '----------------------------------'
!	do i = 1, num
!	  write(*,*) (GS3(j,i),j=16,20)
!	enddo
!	write(*,*) '----------------------------------'


!	do i = 1, numGully
!	  write(*,*) GS1t(i), (GS1(j,i),j=1,4)
!	enddo
!	write(*,*) '----------------------------------'
!	do i = 1, numGully
!	  write(*,*) (GS1(j,i),j=5,7), GS1_soil(i), GS1(8,i)
!	enddo
!	write(*,*) '----------------------------------'
!	do i = 1, numGully
!	  write(*,*) (GS1(j,i),j=9,13)
!	enddo
!	write(*,*) '-----------------------------------------------'
!	write(*,*) '-----------------------------------------------'
!	write(*,*) '-----------------------------------------------'
!	write(*,*) '-----------------------------------------------'
!	do i = 1, numStr
!	  write(*,*) GS2t(i), (GS2(j,i),j=1,3), GS2_LtRc(i)
!	enddo
!	write(*,*) '----------------------------------'
!	do i = 1, numStr
!	  write(*,*) (GS2(j,i),j=4,6), GS2_soil(i), GS2(7,i)
!	enddo
!	write(*,*) '----------------------------------'
!	do i = 1, numStr
!	  write(*,*) (GS2(j,i),j=8,12)
!	enddo
!	write(*,*) '----------------------------------'


	RETURN
	END
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
	SUBROUTINE TOTALLOAD
	use parm

	! Table a, Nutrient load from runoff (lb/year) without BMPs
	do i = 1, 31
	  do j = 1, 15
	    TLa(j,i) = 0.0
	  enddo
	enddo
	do i = 1, num
	  TLa(1,i) = VRunoff(2,i) * (( 1 - NumMonManure(i) / 12.0 ) * 
     &	 AnimalPNB(2,i) + ( NumMonManure(i) / 12.0 ) * AnimalPNB(3,i))
     &	 * 4047 * 0.3048 / 454
	  TLa(2,i) = VRunoff(2,i) * (( 1 - NumMonManure(i) / 12.0 ) * 
     &	 AnimalPNB(4,i) + ( NumMonManure(i) / 12.0 ) * AnimalPNB(5,i))
     &	 * 4047 * 0.3048 / 454
	  TLa(3,i) = VRunoff(2,i) * (( 1 - NumMonManure(i) / 12.0 ) * 
     &	 AnimalPNB(6,i) + ( NumMonManure(i) / 12.0 ) * AnimalPNB(7,i))
     &	 * 4047 * 0.3048 / 454
	  TLa(4,i) = VRunoff(3,i) * NtConcRunoff(1,7)*4047*0.3048/454
	  TLa(5,i) = VRunoff(3,i) * NtConcRunoff(2,7)*4047*0.3048/454
	  TLa(6,i) = VRunoff(3,i) * NtConcRunoff(3,7)*4047*0.3048/454
	  TLa(7,i) = VRunoff(4,i) * NtConcRunoff(1,8)*4047*0.3048/454
	  TLa(8,i) = VRunoff(4,i) * NtConcRunoff(2,8)*4047*0.3048/454
	  TLa(9,i) = VRunoff(4,i) * NtConcRunoff(3,8)*4047*0.3048/454
	  TLa(10,i) = VRunoff(5,i) * NtConcRunoff(1,9)*4047*0.3048/454
	  TLa(11,i) = VRunoff(5,i) * NtConcRunoff(2,9)*4047*0.3048/454
	  TLa(12,i) = VRunoff(5,i) * NtConcRunoff(3,9)*4047*0.3048/454
	  TLa(13,i) = TLa(1,i) + TLa(4,i) + TLa(7,i) + TLa(10,i)
	  TLa(14,i) = TLa(2,i) + TLa(5,i) + TLa(8,i) + TLa(11,i)
	  TLa(15,i) = TLa(3,i) + TLa(6,i) + TLa(9,i) + TLa(12,i)	  
	  do j = 1, 15
	    TLa(j,31) = TLa(j,31) + TLa(j,i)
	  enddo
	enddo

	! Table b, Nutrient load reduction in runoff with BMPs (lb/year)
	do i = 1, 31
	  do j = 1, 15
	    TLb(j,i) = 0.0
	  enddo
	enddo
	do i = 1, num
	  TLb(1,i) = ( TLa(1,i) - RdcIrRunoff(1,i) * AnimalPNB(2,i) 
     &		* 4047 * 0.3048 / 454 ) * Sed_1a(5,i) +
     &		RdcIrRunoff(1,i) * AnimalPNB(2,i) * 4047 * 0.3048 / 454 
	  TLb(2,i) = ( TLa(2,i) - RdcIrRunoff(1,i) * AnimalPNB(4,i) 
     &		* 4047 * 0.3048 / 454 ) * Sed_1a(9,i) +
     &		RdcIrRunoff(1,i) * AnimalPNB(4,i) * 4047 * 0.3048 / 454 
    	  TLb(3,i) = ( TLa(3,i) - RdcIrRunoff(1,i) * AnimalPNB(6,i) 
     &		* 4047 * 0.3048 / 454 ) * Sed_1a(13,i) +
     &		RdcIrRunoff(1,i) * AnimalPNB(6,i) * 4047 * 0.3048 / 454
        TLb(4,i) = TLa(4,i) * Sed_1a(6,i)
	  TLb(5,i) = TLa(5,i) * Sed_1a(10,i)
	  TLb(6,i) = TLa(6,i) * Sed_1a(14,i)
	  TLb(7,i) = TLa(7,i) * Sed_1a(7,i)
	  TLb(8,i) = TLa(8,i) * Sed_1a(11,i)
	  TLb(9,i) = TLa(9,i) * Sed_1a(15,i)
	  TLb(10,i) = TLa(10,i) * Sed_1a(8,i)
	  TLb(11,i) = TLa(11,i) * Sed_1a(12,i)
	  TLb(12,i) = TLa(12,i) * Sed_1a(16,i)
	  TLb(13,i) = TLb(1,i) + TLb(4,i) + TLb(7,i) + TLb(10,i)
	  TLb(14,i) = TLb(2,i) + TLb(5,i) + TLb(8,i) + TLb(11,i)
	  TLb(15,i) = TLb(3,i) + TLb(6,i) + TLb(9,i) + TLb(12,i)	  
	  do j = 1, 15
	    TLb(j,31) = TLb(j,31) + TLb(j,i)
	  enddo
	enddo

	! Table c, Nutrient and sediment load by land uses with BMP (lb/year)
	do i = 1, 31
	  do j = 1, 36
	    TLc(j,i) = 0.0
	  enddo
	enddo
	do i = 1, num
	  TLc(1,i) = ub4(9,i)
	  TLc(2,i) = ub4(10,i)
	  TLc(3,i) = ub4(11,i)
	  TLc(4,i) = ub4(12,i)
	  TLc(5,i) = TLa(1,i) - TLb(1,i) + Sed_3a(1,i) * 2000
	  TLc(6,i) = TLa(2,i) - TLb(2,i) + Sed_3a(2,i) * 2000
	  TLc(7,i) = TLa(3,i) - TLb(3,i) + Sed_3a(3,i) * 2000
	  TLc(8,i) = Sed_3a(4,i) * 2000
	  TLc(9,i) = TLa(4,i) - TLb(4,i) + Sed_3a(5,i) * 2000
	  TLc(10,i) = TLa(5,i) - TLb(5,i) + Sed_3a(6,i) * 2000
	  TLc(11,i) = TLa(6,i) - TLb(6,i) + Sed_3a(7,i) * 2000
	  TLc(12,i) = Sed_3a(8,i) * 2000
	  TLc(13,i) = TLa(7,i) - TLb(7,i) + Sed_3a(9,i) * 2000
	  TLc(14,i) = TLa(8,i) - TLb(8,i) + Sed_3a(10,i) * 2000
	  TLc(15,i) = TLa(9,i) - TLb(9,i) + Sed_3a(11,i) * 2000
	  TLc(16,i) = Sed_3a(12,i) * 2000
	  TLc(17,i) = Load_Fdl(1,i) - Load_Fdl(4,i)
	  TLc(18,i) = Load_Fdl(2,i) - Load_Fdl(5,i)
	  TLc(19,i) = Load_Fdl(3,i) - Load_Fdl(6,i)
	  TLc(20,i) = 0.0
	  TLc(21,i) = TLa(10,i) - TLb(10,i) + Sed_3a(13,i) * 2000
	  TLc(22,i) = TLa(11,i) - TLb(11,i) + Sed_3a(14,i) * 2000
	  TLc(23,i) = TLa(12,i) - TLb(12,i) + Sed_3a(15,i) * 2000
	  TLc(24,i) = Sed_3a(16,i) * 2000
	  TLc(25,i) = SepticPNB(7,i)
	  TLc(26,i) = SepticPNB(8,i)
	  TLc(27,i) = SepticPNB(9,i)
	  TLc(28,i) = 0.0
	  TLc(29,i) = GS3(1,i) - GS3(5,i)
	  TLc(30,i) = GS3(2,i) - GS3(6,i)
	  TLc(31,i) = GS3(3,i) - GS3(7,i)
	  TLc(32,i) = GS3(4,i) - GS3(8,i)
	  TLc(33,i) = GS3(9,i) - GS3(13,i)
	  TLc(34,i) = GS3(10,i) - GS3(14,i)
	  TLc(35,i) = GS3(11,i) - GS3(15,i)
	  TLc(36,i) = GS3(12,i) - GS3(16,i)	 
	  do j = 1, 36
	    TLc(j,31) = TLc(j,31) + TLc(j,i)
	  enddo 
	enddo


	! Table d, Load from groundwater by land uses with BMP (lb/year)
	do i = 1, 31
	  do j = 1, 28
	    TLd(j,i) = 0.0
	  enddo
	enddo
	do i = 1, num
	  TLd(1,i) = GW4(1,i) * NtConcGW(1,1) * 4047 * 0.3048 / 454
	  TLd(2,i) = GW4(1,i) * NtConcGW(2,1) * 4047 * 0.3048 / 454
	  TLd(3,i) = GW4(1,i) * NtConcGW(3,1) * 4047 * 0.3048 / 454
	  TLd(4,i) = 0.0
	  TLd(5,i) = GW4(2,i) * NtConcGW(1,2) * 4047 * 0.3048 / 454
	  TLd(6,i) = GW4(2,i) * NtConcGW(2,2) * 4047 * 0.3048 / 454
	  TLd(7,i) = GW4(2,i) * NtConcGW(3,2) * 4047 * 0.3048 / 454
	  TLd(8,i) = 0.0
	  TLd(9,i) = GW4(3,i) * NtConcGW(1,3) * 4047 * 0.3048 / 454
	  TLd(10,i) = GW4(3,i) * NtConcGW(2,3) * 4047 * 0.3048 / 454
	  TLd(11,i) = GW4(3,i) * NtConcGW(3,3) * 4047 * 0.3048 / 454
	  TLd(12,i) = 0.0
	  TLd(13,i) = GW4(4,i) * NtConcGW(1,4) * 4047 * 0.3048 / 454
	  TLd(14,i) = GW4(4,i) * NtConcGW(2,4) * 4047 * 0.3048 / 454
	  TLd(15,i) = GW4(4,i) * NtConcGW(3,4) * 4047 * 0.3048 / 454
	  TLd(16,i) = 0.0
	  TLd(17,i) = GW4(6,i) * NtConcGW(1,5) * 4047 * 0.3048 / 454
	  TLd(18,i) = GW4(6,i) * NtConcGW(2,5) * 4047 * 0.3048 / 454
	  TLd(19,i) = GW4(6,i) * NtConcGW(3,5) * 4047 * 0.3048 / 454
	  TLd(20,i) = 0.0
	  TLd(21,i) = GW4(5,i) * NtConcGW(1,6) * 4047 * 0.3048 / 454
	  TLd(22,i) = GW4(5,i) * NtConcGW(2,6) * 4047 * 0.3048 / 454
	  TLd(23,i) = GW4(5,i) * NtConcGW(3,6) * 4047 * 0.3048 / 454
	  TLd(24,i) = 0.0	
	  TLd(25,i) = TLd(1,i) + TLd(5,i) + TLd(9,i) + 
     &			  TLd(13,i) + TLd(17,i) + TLd(21,i)
	  TLd(26,i) = TLd(2,i) + TLd(6,i) + TLd(10,i) + 
     &			  TLd(14,i) + TLd(18,i) + TLd(22,i)
	  TLd(27,i) = TLd(3,i) + TLd(7,i) + TLd(11,i) + 
     &			  TLd(15,i) + TLd(19,i) + TLd(23,i)
	  TLd(28,i) = TLd(4,i) + TLd(8,i) + TLd(12,i) + 
     &			  TLd(16,i) + TLd(20,i) + TLd(24,i)
	  do j = 1, 28
	    TLd(j,31) = TLd(j,31) + TLd(j,i)
	  enddo
	enddo
	

	! Table 1, Total load by subwatershed(s)
	do i = 1, 31
	  do j = 1, 16
	    TL1(j,i) = 0.0
	  enddo
	enddo
	do i = 1, num
	  TL1(1,i) = TLa(13,i) + Load_Fdl(1,i) + Sed_3(4,i) * 2000 +
     &	ub4(1,i) + SepticPNB(1,i) + TLd(25,i) + GS3(1,i) + GS3(9,i)
	  TL1(2,i) = TLa(14,i) + Load_Fdl(2,i) + Sed_3(5,i) * 2000 +
     &	ub4(2,i) + SepticPNB(2,i) + TLd(26,i) + GS3(2,i) + GS3(10,i)
	  TL1(3,i) = TLa(15,i) + Load_Fdl(3,i) + Sed_3(6,i) * 2000 +
     &	ub4(3,i) + SepticPNB(3,i) + TLd(27,i) + GS3(3,i) + GS3(11,i)
	  TL1(4,i) = Sed_2(6,i) + ub4(4,i) / 2000 + TLd(28,i) / 2000 +
     &			 GS3(4,i) / 2000 + GS3(12,i) / 2000
	  TL1(5,i) = TLb(13,i) + Sed_3(7,i) * 2000 + ub4(5,i) +
     &		Load_Fdl(4,i) + SepticPNB(4,i) + GS3(5,i) + GS3(13,i)
	  TL1(6,i) = TLb(14,i) + Sed_3(8,i) * 2000 + ub4(6,i) +
     &		Load_Fdl(5,i) + SepticPNB(5,i) + GS3(6,i) + GS3(14,i)
	  TL1(7,i) = TLb(15,i) + Sed_3(9,i) * 2000 + ub4(7,i) +
     &		Load_Fdl(6,i) + SepticPNB(6,i) + GS3(7,i) + GS3(15,i)
	  TL1(8,i) = Sed_2(7,i) + ub4(8,i) / 2000 + TLd(28,i) / 2000 +
     &			 GS3(8,i) / 2000 + GS3(16,i) / 2000
	  do j  = 1, 4
	    TL1(8+j,i) = TL1(j,i) - TL1(j+4,i)
	    if ( 0 < TL1(j,i) ) then
	      TL1(12+j,i) = TL1(j+4,i) / TL1(j,i) * 100
	    else
	      TL1(12+j,i) = 0.0
	    endif
	  enddo
	  do j = 1, 12
	    TL1(j,31) = TL1(j,31) + TL1(j,i)
	  enddo
	enddo
	do j = 1, 4
	  if ( 0 < TL1(j,31) ) then
	    TL1(12+j,31) = TL1(j+4,31) / TL1(j,31) * 100
	  else
	    TL1(12+j,31) = 0.0
	  endif
	enddo


	! Table 2, Total load by land uses (with BMP)
	do i = 1, 10
	  do j = 1, 4
	    TL2(j,i) = 0.0
	  enddo	  
	enddo
	do i = 1, 9
	  do j = 1, 3
	    TL2(j,i) = TLc(4*i+j-4,31)
	  enddo
	  TL2(4,i) = TLc(4*i,31) / 2000
	enddo
	do j = 1, 4
	  TL2(j,10) = TLd(24+j,31)
	enddo
	do i = 1, 10
	  do j = 1, 4
	    TL2(j,11) = TL2(j,11) + TL2(j,i)
	  enddo	  
	enddo


!	do i = 1, num
!	  write(*,*) (TL1(j,i),j=1,5)
!	enddo
!	write(*,*) (TL1(j,31),j=1,5)
!	write(*,*) '-----------------------------'
!	do i = 1, num
!	  write(*,*) (TL1(j,i),j=6,10)
!	enddo
!	write(*,*) (TL1(j,31),j=6,10)
!	write(*,*) '-----------------------------'
!	do i = 1, num
!	  write(*,*) (TL1(j,i),j=11,15)
!	enddo
!	write(*,*) (TL1(j,31),j=11,15)
!	write(*,*) '-----------------------------'
!	do i = 1, num
!	  write(*,*) TL1(16,i)
!	enddo
!	write(*,*) TL1(16,31)

	RETURN 
	END










