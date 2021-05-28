# -*- mode: python -*-

block_cipher = None

added_files = [
         ( '../../../password_generator/images/SKYCOMP.ico', 'password_generator/images' ),
         ( '../../../password_generator/images/SkycompMainLogo.PNG', 'password_generator/images' )
         ]


a = Analysis(['..\\..\\..\\password_generator\\password_generator.py'],
             pathex=['D:\\Scripts\\Python\\password_generator\\bin\\compile_executable\\make_spec'],
             binaries=[],
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
          name='password_generator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='program_icon\\iconName.ico')
