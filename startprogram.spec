# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['startprogram.py'],
    pathex=[],
    binaries=[],
    datas=[('dataentry.py', '.'), ('example.py', '.'), ('dataformulas.py', '.'), ('dataoutputgui.py', '.'), ('datacartcal.csv', '.'), ('datagameclass.csv', '.'), ('bcalcexticon.png', '.'), ('quail-silhouette.png', '.'), ('angles.py', '.'), ('atmosphere.py', '.'), ('ballistics.py', '.'), ('bdc.py', '.'), ('constants.py', '.'), ('dataholder.py', '.'), ('dataholder2.py', '.'), ('drag.py', '.'), ('holdover.py', '.'), ('points.py', '.'), ('utils.py', '.'), ('windage.py', '.'), ('screenshots', 'screenshots')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='startprogram',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='startprogram',
)
