# build_exe.py - Build script for managed/corporate computers
import subprocess
import sys
import os
from pathlib import Path
import site

def find_pyinstaller():
    """Find PyInstaller executable in user directory"""
    # Get user site-packages directory
    user_site = site.getusersitepackages()
    
    # Possible PyInstaller locations
    possible_paths = [
        Path(user_site).parent / "Scripts" / "pyinstaller.exe",
        Path(user_site).parent / "bin" / "pyinstaller",
        Path(sys.executable).parent / "Scripts" / "pyinstaller.exe"
    ]
    
    for path in possible_paths:
        if path.exists():
            return str(path)
    
    return None

def install_and_build():
    """Install PyInstaller with --user flag and build the executable"""
    
    print("🔧 Installing PyInstaller to user directory...")
    print("ℹ️  Note: Building with AI models creates large executables (1-2GB)")
    try:
        # Install PyInstaller with --user flag (works on managed computers)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pyinstaller"])
        print("✅ PyInstaller installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install PyInstaller")
        input("Press Enter to exit...")
        return
    
    # Find PyInstaller executable
    pyinstaller_path = find_pyinstaller()
    
    if not pyinstaller_path:
        print("❌ Could not find PyInstaller executable")
        print("💡 Try running: python -m PyInstaller instead")
        print("📁 You can also try using: python -m pip show pyinstaller")
        input("Press Enter to exit...")
        return
    
    print(f"✅ Found PyInstaller at: {pyinstaller_path}")
    
    print("\n🏗️ Building executable...")
    print("⏰ This may take 5-10 minutes and create a large file (1-2GB) due to AI models...")
    
    # Check if ffmpeg.exe exists
    if not os.path.exists("ffmpeg.exe"):
        print("⚠️  ffmpeg.exe not found in current directory")
        print("The executable will still be created, but you'll need to provide ffmpeg.exe later")
        build_cmd = [
            pyinstaller_path,
            "--onefile",
            "--windowed", 
            "--name=VideoTranscriber",
            "--hidden-import=whisper",
            "--hidden-import=torch",
            "--hidden-import=numpy", 
            "--hidden-import=tkinterdnd2",
            "--collect-all=whisper",
            "--collect-all=torch",
            "--noconfirm",
            "video_transcriber.py"
        ]
    else:
        print("✅ Found ffmpeg.exe - including in build")
        build_cmd = [
            pyinstaller_path,
            "--onefile",
            "--windowed",
            "--name=VideoTranscriber", 
            "--add-data", "ffmpeg.exe;.",
            "--hidden-import=whisper",
            "--hidden-import=torch",
            "--hidden-import=numpy",
            "--hidden-import=tkinterdnd2", 
            "--collect-all=whisper",
            "--collect-all=torch",
            "--noconfirm",
            "video_transcriber.py"
        ]
    
    print(f"\nRunning: {' '.join(build_cmd)}")
    
    try:
        result = subprocess.run(build_cmd, check=True, capture_output=True, text=True)
        print("\n🎉 Build successful!")
        print("📁 Your executable is in: dist\\VideoTranscriber.exe")
        
        if not os.path.exists("ffmpeg.exe"):
            print("\n📥 Don't forget to:")
            print("1. Download ffmpeg.exe from https://ffmpeg.org")
            print("2. Place it in the same folder as VideoTranscriber.exe")
        
        print("\n📋 Next steps:")
        print("1. Test the executable: dist\\VideoTranscriber.exe")
        print("2. Copy dist\\VideoTranscriber.exe to wherever you want to use it")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed!")
        print(f"Error: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
            
        # Alternative method suggestion
        print("\n💡 Alternative: Try using Python module directly:")
        print("python -m PyInstaller --onefile --windowed video_transcriber.py")
    
    input("\nPress Enter to exit...")

def alternative_build():
    """Alternative build method using Python module directly"""
    print("🔧 Trying alternative build method...")
    
    # First ensure PyInstaller is installed
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pyinstaller"])
    except:
        pass
    
    # Enhanced build using Python module with all necessary includes
    build_cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=VideoTranscriber",
        "--hidden-import=whisper",
        "--hidden-import=torch",
        "--hidden-import=numpy",
        "--hidden-import=tkinterdnd2",
        "--collect-all=whisper",
        "--collect-all=torch",
        "--noconfirm"
    ]
    
    if os.path.exists("ffmpeg.exe"):
        build_cmd.extend(["--add-data", "ffmpeg.exe;."])
    
    build_cmd.append("video_transcriber.py")
    
    try:
        subprocess.run(build_cmd, check=True)
        print("✅ Alternative build successful!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Alternative build also failed")
        return False

if __name__ == "__main__":
    print("Video Transcriber - Executable Builder (Corporate Edition)")
    print("=" * 55)
    
    # Try main method first
    install_and_build()
    
    # If user wants to try alternative
    print("\nIf the build failed, you can also try this enhanced command:")
    print("python -m PyInstaller --onefile --windowed --collect-all=whisper --collect-all=torch --hidden-import=whisper --hidden-import=torch video_transcriber.py")