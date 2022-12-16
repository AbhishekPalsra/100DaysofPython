#https://ascii.co.uk/art ascii art
# for printig multiple lins in py we use ''' '''
print('''                      .
                       M
                      dM
                      MMr
                     4MMML                  .
                     MMMMM.                xf
     .              "MMMMM               .MM-
      Mh..          +MMMMMM            .MMMM
      .MMM.         .MMMMML.          MMMMMh
       )MMMh.        MMMMMM         MMMMMMM
        3MMMMx.     'MMMMMMf      xnMMMMMM"
        '*MMMMM      MMMMMM.     nMMMMMMP"
          *MMMMMx    "MMMMM\    .MMMMMMM=
           *MMMMMh   "MMMMM"   JMMMMMMP
             MMMMMM   3MMMM.  dMMMMMM            .
              MMMMMM  "MMMM  .MMMMM(        .nnMP"
  =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*
    "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"
     "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
       ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"
          *PMMMMMMhn. *x > M  .MMMM**""
             ""**MMMMhx/.h/ .=*"
                      .3P"%....
                    nP"     "*MMnx                \n''')
print("Welcome Stoners to the weed World!!!")
a=input("Which ways you are gonna go? R or L?\n")
a=a.upper()
if a=='R':
    print("Game Over. Right is not always Right!")
elif a=='L':
    print("Dont be too happy! Not everyone makes it to the Cr**m?")
    b=input("Choose one weed or alcohol W for weed and A for alcohol?")
    b=b.upper()
    if b=='W':
        print("Great Work!")
        c=int(input("How much money you got to score?"))
        d=c/300 # t rate 3000 1 gm =300
        print(f"you get {d+10} gm of crazy stuff! Be aware of police on the way!")



    elif b=='A':
        print('Game Over!! You\'ve The one who drink sinks.... the one who smoke the weed stays high..')
        #use \ to escape the string





