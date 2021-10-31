from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os","sys","pytube"]}

setup(
    name="youtubeDownloader",
    version=1,
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)