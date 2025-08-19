# Video Transcriber

A Python GUI application that extracts audio from video files and transcribes speech to Word documents using OpenAI Whisper AI.

## Features

- 🎥 **Extract audio** from various video formats (MP4, AVI, MOV, MKV, etc.)
- 🎵 **Audio format options**: MP3 or WAV output
- 🤖 **AI transcription** using OpenAI Whisper (multiple model sizes)
- 📄 **Word document output** with both clean text and timestamped transcript
- 🖱️ **Drag & drop** video files (when tkinterdnd2 is available)
- 🎯 **User-friendly GUI** with progress tracking and detailed logging

## Repository Structure

```
video-transcriber/
├── video_transcriber.py    # Main application
├── build_exe.py           # Build script for creating .exe
├── README.md              # This file
├── .gitignore            # Git ignore rules
└── ffmpeg.exe            # ⚠️ You need to download this separately
```

**Note:** `ffmpeg.exe` is not included in this repository due to size constraints. Please download it following the installation instructions below.

## Installation

### Requirements
- Python 3.7 or higher
- FFmpeg (for audio extraction)

### Quick Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/video-transcriber.git
   cd video-transcriber
   ```

2. **Install dependencies:**
   ```bash
   pip install --user openai-whisper python-docx tkinterdnd2 numpy
   ```

3. **Download FFmpeg:**
   
   **Easy Method:**
   - Download: [FFmpeg Windows Build](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
   - Extract the zip file
   - Copy `ffmpeg.exe` from the `bin/` folder
   - Place `ffmpeg.exe` in the same folder as `video_transcriber.py`
   
   **Alternative:**
   - Go to [FFmpeg Downloads](https://ffmpeg.org/download.html)
   - Choose "Windows" → "More downloading options"
   - Download a static build and extract `ffmpeg.exe`

4. **Run the application:**
   ```bash
   python video_transcriber.py
   ```

## Building Executable

To create a standalone .exe file:

1. **Ensure FFmpeg is downloaded** (see installation instructions above)

2. **Run the build script:**
   ```bash
   python build_exe.py
   ```

3. **Find your executable:**
   - The .exe will be created in the `dist/` folder
   - File size will be 1-2GB (includes AI models)
   - The built .exe will include FFmpeg automatically if present

**Note:** The built executable can be shared via GitHub Releases (supports larger files) rather than committing to the repository.

## Usage

1. **Select video file** using Browse button or drag & drop
2. **Choose output folder** for generated files
3. **Select options:**
   - Audio extraction (MP3 or WAV)
   - AI transcription (choose Whisper model size)
4. **Click "Start Processing"**
5. **Wait for completion** - transcription time varies by model:
   - Tiny: ~20-30 min for 1 hour video
   - Base: ~30-60 min for 1 hour video  
   - Large: ~3-10 hours for 1 hour video

## Output

The transcription creates a Word document with:
- **Clean text section** - Full transcript in paragraph format
- **Timestamped section** - Table with timestamps and corresponding text

## Supported Formats

**Input Video:** MP4, AVI, MOV, MKV, WMV, FLV, WebM, M4V
**Output Audio:** MP3, WAV
**Output Transcript:** Microsoft Word (.docx)

## Whisper Model Comparison

| Model | Speed | Accuracy | File Size | Best For |
|-------|-------|----------|-----------|----------|
| Tiny | Fastest | Good | ~39MB | Quick drafts |
| Base | Fast | Better | ~142MB | Balanced use |
| Small | Medium | Better | ~466MB | Quality focus |
| Medium | Slow | High | ~1.5GB | Professional use |
| Large | Slowest | Highest | ~2.9GB | Maximum accuracy |

## Troubleshooting

### Common Issues

**"FFmpeg not found" error:**
- **Download ffmpeg.exe** from [this link](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
- Extract the zip and copy `ffmpeg.exe` from the `bin/` folder
- Place `ffmpeg.exe` in the same folder as your Python scripts
- **OR** install FFmpeg system-wide and add to PATH

**"OpenAI Whisper not available" error:**
- Run: `pip install --user openai-whisper`

**Long transcription times:**
- Use smaller Whisper models (tiny/base) for faster processing
- Ensure sufficient disk space for model downloads

**Large executable size:**
- This is normal - AI models are large
- Executable includes all necessary AI models

## Dependencies

- [OpenAI Whisper](https://github.com/openai/whisper) - AI transcription
- [FFmpeg](https://ffmpeg.org) - Audio/video processing
- [python-docx](https://python-docx.readthedocs.io) - Word document creation
- [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2) - Drag & drop support
- tkinter - GUI framework (included with Python)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for the Whisper speech recognition model
- FFmpeg team for audio processing capabilities
- Python community for excellent libraries

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. [Open an issue](https://github.com/yourusername/video-transcriber/issues) on GitHub
3. Provide error logs and system information

---

**Note:** First run may take longer as Whisper downloads AI models (140MB-1.5GB depending on selected model).
