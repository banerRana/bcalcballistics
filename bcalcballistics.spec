# -*- mode: python ; coding: utf-8 -*-
# bcalcballistics.spec

a = Analysis(
    ['startprogram.py'],
    pathex=[],
    binaries=[
        ('/usr/lib64/libpython3.11.so.1.0', '_internal'),
    ],
    datas=[
        ('datacartcal.csv', '.'),
        ('datagameclass.csv', '.'),
        ('bcalcexticon.png', '.'),
        ('quail-silhouette.png', '.'),
    ],
    hiddenimports=[
        'ttkbootstrap',
        'matplotlib.backends.backend_tkagg',
        'pandas',
        'numpy',
        'tkinter.ttk'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    name='bcalcballistics',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=False,
    icon='bcalcexticon.png',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app'
)

