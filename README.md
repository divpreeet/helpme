# helpme
> an automatic screenshot to answer spoken tool, that helps me do other stuff while im in online classes, only for macos.

> [!NOTE]
> this project does not condone cheating, or voice cloning and use by AI. It is just a project that I found interesting to build.

## installation
> this would only work on macos!

make sure you have python3 and the required deps installed - 
```sh
brew install python3 switchaudio-osx
```
---
you also need zoom, and be in a meeting for it to work obviously.


then download the zip from the releases.


note - you need a hc api key, which you can get if you are part of hackclub at https://ai.hackclub.com/

---
### local tts model
make sure that you install `f5_tts_mlx`, as that is the local model used for tts - 
```sh
pip install f5_tts_mlx
```
also, currently the tts is cloning my voice, from the `voice.wav`, to make it clone your voice, replace the current `voice.wav` with you saying - "Hey, miss, I'm getting the answers forty two. No, wait, forty five".

### zoom mic routing
to make the mic work properly you require blackhole2ch, which can be installed with - 
```sh
brew install blackhole-2ch
```
then, go to the "Audio MiDi Setup" app on macos and create a multioutput device called `Zoom Output` with your speaker, and blackhole checked, and an aggregate device with the name `Zoom Audio` with your microphone and blackhole!

---
then, make sure you export the api key in the same terminal session as `KEY` - 
```sh
export KEY=your_api_key
```

you also need to create a python env and install `f5_tts_mlx` in the same session -
```sh
python3 -m venv venv
source venv/bin/activate
pip install f5_tts_mlx
```

then just run executable from the terminal and provide the permissions it asks for!
```sh
./helpme
```
### troubleshooting
- make sure your terminal emulator, from which you run the exectuable has permissions for screen recording, accessibility and microphone
- make sure that the `KEY` variable is exported in the same terminal
- also, `voice.wav` must be in the same directory with the executable!