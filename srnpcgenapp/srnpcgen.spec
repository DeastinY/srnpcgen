# -*- mode: python -*-
from kivy.deps import sdl2, glew
from plyer import accelerometer

block_cipher = None


a = Analysis(['..\\main.py'],
             pathex=['D:\\git\\srnpcgen\\srnpcgenapp'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='srnpcgen',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe, Tree('D:\\git\\srnpcgen\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
			   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='srnpcgen')
