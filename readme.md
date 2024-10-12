# The Dorico Speedy Swapper

So the new "move shadow note" command in Dorico is a bit of a game changer, and that, along with a few other key command and preference alterations, allows you to more or less recreate Finale's speedy entry nearly exactly (a few small caveats there; will discuss below). 

The problem is that those "few other key command and preference alterations" don't play nicely when you want to go back to Dorico's standard duration-before-pitch mode. Specifically, setting the movement of the shadow note to 'up' and 'down' means up and down are then no longer available for cursor movement up and down. That's perfectly fine (and desired, obviously) in pitch-before-duration, but when you go back to duration-before-pitch, that's a pretty big bummer. 

So switching back and forth between Dorico's standard note entry method and our recreated Finale Speedy Entry requires at least four key command changes every time you want to switch. That's the bummer. There's also the preference to enter accidentals, rhythm dots, and articulations after entering the note (which is not a necessity, but does more closely replicate Finale's Speedy), which, if you want it one way in one mode and the other way in the other mode, would also need to switch. What is an engraver to do??? 

Well fear not, friends! This project provides a Python script and a batch file to quickly and easily swap Dorico key commands and preferences files. You can now have your cake and eat (at least some of) it too. Unfortunately, the swap doesn't take effect until Dorico restarts, but that's a limitation that there's really no way to work around on our side of things. Nonetheless, this allows for a user to have their standard note entry, untouched and unmodified, and then with a quick run of the script and restart of Dorico, they can also have access to a recreation of Finale's Speedy and all its associated commands and preference changes. Very handy. Also, the script doesn't actually care what key commands and preferences you're swapping, so if you had some other mutually exclusive set of configurations you'd like to implement, this will work for that too! 

## Contents

- `command_swapper.py`: The Python script that performs the file swapping.
- `run_command_swapper.bat`: The batch file to run the Python script.
- `config.txt`: Configuration file to specify user-specific paths.

## Setup

1. **Download and Install Python**: Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

2. **Clone or Download the Repository**: Place the `command_swapper.py`, `run_command_swapper.bat`, and `config.txt` files in a directory of your choice. I put mine in `C:\Users\<USERNAME>\dev\dorico_command_swapper`, but you do whatever works for you!

3. **Update `config.txt`**: Open `config.txt` in a text editor and specify your user folder name and Dorico version.
    ```plaintext
    user_folder=<USERNAME>
    dorico_version=<CURRENT_DORICO_VERSION>
    ```

4. **Optional: Create a Batch File Shortcut**: 
    - Right-click `run_command_swapper.bat` and select "Create shortcut".
    - Rename it something like "Speedy Swap"
    - Move the shortcut to wherever you'd like. Your desktop works fine, but I prefer your Start Menu folder:
        - Press `Windows + R`, type `shell:start menu`, and press Enter.
        - Drag your shortcut into the "Programs" folder.
    - You now have an entry in your Start menu called "Speedy Swap" which you can search for by typing it into the Start Menu


## Usage

1. **Initial Run**: Before making any changes to your key commands and preferences, run the script once to ensure the backup files are created.
    - Either run the Start Menu shortcut or double click `run_command_swapper.bat`.

2. **Edit Commands and Preferences**: Customize your key commands and preferences in Dorico to create your desired Speedy mode configuration.

3. **Switch Configurations**: From then on, whenever you need to switch from one config to the other, simply run the script and restart Dorico. It's that easy :-)

## Notes/caveats

- You will of course have already noticed, but this is for Windows only. It should be pretty transferrable to Mac with just a few adjustments, but I don't have one to install Dorico on and figure out the paths and other necessary modifications and so forth, so that'd need to be a task for someone else, at least at the moment. Sorry, Apple homies! 
- On first run, not only will the script create the swapper files, it will also store a long-term backup of the two files in the same directory where you run it from. That way if things just go way south, you'll always have a fallback and the option of a fresh start. **However**, I highly recommend also manually making a backup of your secondary commands/preferences after you've created them and switched back to your primary. I suppose I could've automated this. But I didn't. In my testing, I did run into a single situation where one of the preferences files got eaten (so both files became identical); it was maybe after Dorico crashed or something like that, not fully sure. Luckily for me there is only one different setting between the two, so it wasn't a huge deal to fix it, but it's easiest to just have all four files backed up for when you need them. 
- The recreation of Speedy is not perfect, which is unfortunate but to be expected. At the moment, if you set Dorico to let you enter rhythm dots, accidentals, and articulations after entering the note, which I do, **regardless of whether you have shadow note auditioning turned off** the previously entered note sounds **every time you move the shadow note**. You also can't use alt-up/down to edit the pitch of the just entered note; that's another big bummer there (though you can use alt-left/right to change the note value; silver lining I suppose). I understand why it's happening, but I contend this should be considered undesired behavior. I do intend to make a post in the Dorico forum about this, so, who knows, maybe this changes at some point.
- Chord mode is also a little screwy under the same circumstances. At the moment, chord mode freezes the shadow note after you've entered a note. The only really good way to work around this is to use note names when working in chord mode (which... sort of defeats the purpose, lol). You can also work around it by moving the cursor over with the left or right arrow keys and then just moving back. Basically, if you want to enter notes before accidentals etc., then you'd better hope you don't have too many chords. 
- Once you have things separated and so forth, any time you make changes to your key commands or preferences, it will only affect the configuration that you're currently using (meaning if your primary config is "stock" and your secondary config is geared towards Speedy, if you are currently working in your stock config, any preference changes will only affect said stock config, not your Speedy config. That is probably obvious, but it's worth saying once.

I think that's everything. Now, go forth and enjoy your new Speedy in Dorico experience!
