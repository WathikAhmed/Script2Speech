#!/usr/bin/env python3
try:
    print("Testing TTS import...")
    from TTS.api import TTS
    from tqdm import tqdm
    import time
    print("✅ TTS imported successfully!")
    
    print("Testing TTS initialization...")
    tts = TTS(model_name="tts_models/en/jenny/jenny")
    print("✅ TTS model loaded successfully!")
    
    print("Reading script from file...")
    with open("script.txt", "r") as f:
        text = f.read().strip()
    
    print("Generating speech...")
    with tqdm(total=100, desc="Processing", unit="%") as pbar:
        pbar.update(20)
        time.sleep(0.1)
        tts.tts_to_file(text=text, file_path="test_output.wav")
        pbar.update(80)
    
    print("✅ Audio generated successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()