!define APPNAME "SRNPCGen"
!define COMPANYNAME "Ars-Artificia"
!define DESCRIPTION "A Shadowrun NPC Generator"

!define VERSIONMAJOR 1
!define VERSIONMINOR 0
!define VERSIONBUILD 4

OutFile "SRNPCGenInstaller.exe"
InstallDIR "$PROGRAMFILES\${COMPANYNAME}\${APPNAME}"
Name "${COMPANYNAME} - ${APPNAME}"

Section

SetOutPath $INSTDIR

# Start Menu
createDirectory "$SMPROGRAMS\${COMPANYNAME}"
createShortCut "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk" "$INSTDIR\srnpcgen.exe"

File /r srnpcgenapp\dist\srnpcgen\*

WriteUninstaller $INSTDIR\uninstaller.exe

SectionEnd

Section "Uninstall"

Delete "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk"
rmDir "$SMPROGRAMS\${COMPANYNAME}"

rmDir /r $INSTDIR

SectionEnd