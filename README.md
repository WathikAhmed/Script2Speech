# Script2Speech

Convert text files to speech using Coqui TTS engine.

## Setup

1. Install Miniconda:
```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh -b -p $HOME/miniconda3
```

2. Create conda environment:
```bash
$HOME/miniconda3/bin/conda create -n tts python=3.11 -y
```

3. Install dependencies:
```bash
source $HOME/miniconda3/bin/activate tts
pip install -r requirements.txt
```

## Usage

1. Edit `script.txt` with your text
2. Run the converter:
```bash
source $HOME/miniconda3/bin/activate tts
python test_tts.py
```

Output audio will be saved as `test_output.wav`.

## Issue & Fix

**Problem**: `ModuleNotFoundError: No module named '_lzma'`

**Cause**: macOS system Python lacks the lzma compression module needed by TTS dependencies.

**Solution**: Used Miniconda Python distribution which includes all standard library modules including `_lzma`.