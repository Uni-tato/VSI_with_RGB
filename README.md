# VSI_with_RGB
View System Information with RGB: allows you to sync RGB products to system information eg: cpu temp.

Are you sick of all those terrible rgb controllers with equally terrible software, well here's some more!
At least making your own gives you more creativity, *and* lets you take any info you want from the system to use to control your RGB.
Ever wanted your case to glow in a soft blue when it's cool, but turn into a blazing inferno when under heavy load? Well this is the basic code you'll need. Go knock yourself out.

Note: not everything here is my own work, I accept no resposibility for your usage of other peoples work.

**Hardware guide:**
\**WIP*
For now the best I can give you is this: https://learn.adafruit.com/tlc5947-tlc59711-pwm-led-driver-breakout/connecting-to-the-arduino

**Install guide (Windows)**
1. Download everything to your desired folder.
2. Run "pip install -r requirements.txt", "python -m pip install -r requirements.txt" or equivalent.
3. Open vsirgb\arduino\vsirgb\vsirgb.ino (ide found here: https://www.arduino.cc/en/software), enter the pins you're using and change the board type if necessary.
4. Plug in your arduino then upload, take note of the port you're using (bottom right corner or Tools > Port.)
5. Create a shortcut to vsirgb.py (rename vsirgb.pyw to run without a window) and place this shortcut in "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp".
6. Create a copy of config_template.py, and settings_template.json named config.py and settings.json.

**Install guide (Linux):**
1. Good luck; have fun. Some things won't work, let me know how it goes.

Good to go, everything will work now, but you'll want to change the settings and config file to customise everything.

**The settings file:**
For now the only way to change your settings is to edit the settings.json file, don't worry if you don't know how json works; I'll explain what to edit here.
The first thing you'll want to do is run "index and info help.py", this will bring up a list of information you can use to control your RGB devices.
The number in each heading is the hardware index (eg: `2` in `CPU (2), Intel Co...`), you do not need to remember this as it is labeled in the settings file.
After each heading there will be 3 columns of info, each row is an individual sensor you can use. The first column shows what the sensor measures, this is the sensor type.
Next is the sensor name and sensor index, this is what you'll need to know to edit your settings file.
And the last column is simply the value from the sensor. Note: if some values are `None` then this may be resolved by launching the program as administrator. If you choose to use a value that you can only get when run this way then you will need change `REQUIRE_ADMIN` to `True` in config.py, it will also mean that you will get a popup whenever the app launches.
Now you know everything you need to know to actually jump in and edit the settings.
First locate the hardware that your sensor falls under eg: CPU or Motherboard, Then find the sensor type that is within that list (the `[]`s represent a list if you were unsure).
If the sensor index of your chosen sensor is not 0 then you will need to put in some empty lists/objects (objects are represented by `{}`) make sure to separate each item with a comma.
the sensor you want to use must have n items before it in the sensor type list, for example if you wanted to use CPU package temp which has a sensor index of 4 then it must be the 5th item in the list:
```
...
[ // Temperature
  {}, // Core #1
  {}, // #2
  {}, // #3
  {}, // #4
  { // Package
    "colourmap": "default\\white_red",
    "lower_bound": 20,
    "upper_bound": 70
  }
],
[ // Load
],
...
```
Once you have these curly brackets in place you can decide how you want your leds to light up. (Leave the ones you don't care about blank.)
inside of these brackets you need 3 things: the colourmap (a list of maps can be found in colourmaps/default, or you can make your own if none of these suit your use), the lower_bound and the_upper bound. Colourmap is in essence a list of colours, when deciding what colour to set your RGB to the value is mapped from within lower and upper bound to a value within your chosen colourmap. For example if you upper bound was 50 and your sensor is reading a temperature (or some other type) of 50 (or greater) then the RGB will be set to the very last colour in your colourmap, if your lower bound is 10 and the sensor reads 30 then the RGB will be set to whatever colour is in the middle of your colourmap.

for now each sensor must control a different RGB device/port, I will improve this soon.
