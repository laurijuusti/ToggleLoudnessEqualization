## Toggle Loudness Equalization

### Python script to toggle Windows LE on when a certain app is running. Useful for games with loud gunshots to save hearing eg. PUBG.

### Usage:

- Download or clone repository
- Find out the correct audio device registry key, found in `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Render\`.
- Look for value changes in the registry when toggling loudness equalization off & on manually, that's the value you need to change.
- Edit script with your values and run, should work.
