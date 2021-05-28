# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [

         ( '../../../test_internet_speed/drivers/IEDriverServer.exe', 'test_internet_speed/drivers' )
	
		]


a = Analysis(['..\\..\\..\\test_internet_speed\\test_internet_speed.py'],
             pathex=['..\\..\\test_internet_speed'],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='test_internet_speed',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
