from cx_Freeze import setup, Executable

setup (
    name="MoutainShooter",
    version="1.1",
    description="Mountain Shooter app",
    option= {"build_exe": {"packages": ["pygame"]}},
    executables=[Executable("main.py")]
)