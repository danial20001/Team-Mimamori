from huggingface_hub import hf_hub_download
repo = 'LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF'
files = [
    'LFM2.5-Audio-1.5B-JP-Q4_0.gguf',
    'mmproj-LFM2.5-Audio-1.5B-JP-Q4_0.gguf',
    'vocoder-LFM2.5-Audio-1.5B-JP-Q4_0.gguf',
    'tokenizer-LFM2.5-Audio-1.5B-JP-Q4_0.gguf',
]
for f in files:
    print('Downloading', f)
    hf_hub_download(repo_id=repo, filename=f, local_dir='./models/audio_jp')
print('Done. You still need llama-liquid-audio-cli runner/exe from the repo runners folder or PATH.')
