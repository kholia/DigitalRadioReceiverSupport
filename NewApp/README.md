#### Help File

Note: Please use the `BETA` version from the Google Play Store - it works much
better!

The `FT8 Radio` app allows operating FT8 on your radio in a portable
(field/remote locations) fashion using an Android phone.

Note: It is meant for remote, digital SOTA / POTA activations. It 'sucks' for
indoors use - use WSJT-X at home instead ;)

Note 2: I recommend getting familiar with FT8 QSOs with WSJT-X on a PC (or RPi)
first. The app is like a simpler (and poorer version) of WSJT-X. If you are not
familiar with WSJT-X, and rig interfacing, you are likely to have a tough time
with this app. See https://github.com/kholia/DigitalRadioReceiverSupport#new-to-ft8
for some help on this topic.

The app handles FT8 RX, TX, QSO logging, and CAT control all by itself. No PC
or Raspberry Pi is required!

Note 3: The app uses an optimized message sequencing to have quick, legit QSOs.
More specifically, we use the recommended practice of omitting the `TX 1`
message.

HELP REQUIRED: We are looking for Icom IC-9700 users to test this app. Please
reach out to us if you have access to a IC-9700 rig - thank you! :)

TIP: To build a 20 to 35 USD `Complete HF FT8 setup`, please see our free
https://github.com/kholia/DDX project. It works great with this `FT8 Radio`
app. Get in touch with us for any help required.


#### Instructions

- Ensure that the Android phone has the correct time on it. This is critical to get right.

  To correct the time on your phone WITHOUT root access, copy the `Local offset`
  value from the [ClockSync app](https://m.apkpure.com/clocksync/ru.org.amip.ClockSync)
  into the `Time Delta` field in the app settings (keeping the negative sign as
  it is, if present).

  Example:

  The `ClockSync` app shows `-0.501` as the `Local offset`.

  ![ClockSync 1](../screenshots/ClockSync-1.png)

  So enter the same exact `-0.501` value in the `Time Delta` field in the app
  settings.

  ![App Settings 1](../screenshots/App-Settings-1.png)

  Update 1: The app now supports getting the time from the phone's GPS
  subsystem. This feature is only activated when the user clicks the `GPS
  button` manually.

  To test and debug the GPS functionality on your phone, please use [the `GPSTest` app](https://github.com/barbeau/gpstest).

  Update 2: You may use the https://time.is/ website on your phone instead of
  ClockSync to get the `Time Delta` value.

  Update 3: You may also use the [AtomicClock: NTP Time](https://play.google.com/store/apps/details?id=partl.atomicclock) app to get the `Time Delta` value.

- Disconnect the rig from the phone.

- Launch the `FT8 Radio` app.

- In `App -> Settings`, select your rig model.

  General example: When using AF (VOX) mode with IC-7300, select `VOX` as the
  radio model in the app settings. When using CAT mode with IC-7300, select
  `IC-7300` as the radio model.

  Set your callsign, grid, and band as well.

  ATTENTION: The callsign, and grid values need to be in UPPERCASE (CAPITAL LETTERS).

  Example: VU3CER (callsign) and MK68 (grid).

- Configure the rig for FT8.

  For IC-705 / IC-7300, select the `FT8 mode preset`. This is explained on [this page](https://www.icomjapan.com/news/3208/).

- Connect the rig to the phone.

  For IC-705, connect the rig to the phone via a Micro-USB cable + an OTG-adapter.

- [IMPORTANT] Note: Force kill the app (yes please...).

- Start the app manually again.

- IMPORTANT: Once you are in the app, increase the volume to the maximum (or to
  a level appropriate for your rig). This is required for getting the correct
  audio drive (AF drive) for the radio.

- You are good to go. All the best, and good DX!

- You can check (debug) your FT8 transmissions on the https://pskreporter.info/
  site. Doing so is highly recommended!

  If you can't see your signal on this site, please double-check the time on
  your phone, and also double-check the volume on the phone for the app.

  I also use the IC-705's inbuilt monitor to see that the radio is consuming
  appropriate (and large) amount of current when TX'ing.

  You may find http://beta.reversebeacon.net/main.php useful too.

- Note: The application doesn't run any (background) services. It can be
  exited from or killed like any other regular Android app.

- TIP: If you do NOT use USB for CAT control, you can choose the `VOX` or
  `Unknown` radio model in app settings to avoid annoying pop-up messages.


#### Usage

Thanks for taking the time to set up the app.

The `App Settings -> PTT ON (Test CAT)` button can be used to quickly check
that CAT control is working (or not).

The app will automatically start decoding FT8 messages, and the newest
messages are on the top (of the screen).

To respond to a particular callsign, just click on that callsign. The app
will automatically determine the correct message to send. The app will also
turn on the `TX` button to say `TX ON`. The actual FT8 TX will happen at
the next appropriate FT8 timing window.

The app has a smart `state machine` feature (auto-sequencing feature) built
into it. This means that once the QSO process has been started, the app will
automatically try to finish the QSO without requiring further manual human
action.

Note: The TX LED on the radio will automatically turn RED when the transmission
is taking place.

If you would like to cancel an upcoming transmission, just press the `TX ON`
button once - this button will now say `TX OFF` and the upcoming transmission
will be canceled. If the `TX` button says `TX OFF` already, then no
transmission event is upcoming.

If you would like to send a particular FT8 message manually, then select the
FT8 message from the dropdown list of predefined messages, and then turn on the
`TX` button by pressing it - a turned on `TX` button says `TX ON`.

The `RST` (RESET) button enables own CQ-calling when the `TX ON` appears.


#### What's New? (March 2023)

- Experimental CAT support for FT-891 radio
- Experimental CAT support for FT-710 AESS radio
- Experimental support for "DDX v3" radio
- (tr)uSDX radio is fully supported now
- CAT PTT support for Elecraft radios
- Experimental CAT PTT support for IC-7100
- Support for Digirig Mobile (RTS as PTT) is here!
- 'Dark Mode' is here (see documentation)
- Xiegu X6100 radio is fully supported now
- Xiegu G90 radio is fully supported now
- QDX radio is fully supported now


#### Known Bugs / Issues / "Features"

- The app doesn't handle screen rotations well - so please disable screen
  rotation on your phone.

- The app maintains very little state about the ongoing QSO. As such, the app
  can start replying to a stronger station without finishing the ongoing QSO.

- This app only allows responding to the latest decoded FT8 messages. You can't
  respond to old messages (yet).

  The app is unable to enable `callsign highlighting` for older decoded
  messages.

- The app doesn't show the FT8 messages being transmitted by the user (on most
  rigs).

- ATTENTION: After changing the app settings, a manual app restart may be
  needed.

- The usability is NOT great, primarily because of strict FT8 timing
  requirements and the ergonomics involved with small touch screens.

- The app currently ONLY supports the following radios:

  - Generic radio support using VOX
  - Generic radio support via Digirig Mobile (RTS as PTT) support
  - Icom IC-705 - Uses Micro-USB cable with OTG adapter - use baud rate 9600
  - Icom IC-7300 - Uses USB cable with OTG adapter - use baud rate 4800
  - uBITX (various versions) - Needs a suitable digital interface (like LiDi v2)
  - Xiegu G90 - USB audio interface wired directly to the ACC port on the radio
  - Xiegu G1M - Works with an USB interface
  - Xiegu X6100 - Works fine in CAT mode and also in VOX mode (keep`Port Number` 1 in App Settings)
  - (tr)uSDX - Simple homebrew audio cable works great in VOX mode
  - (tr)uSDX - Works great with CAT PTT, and CAT-frequency-changing support
    with BETA version >= 120 - Use TS-480 (38400) as the radio model for
    (tr)uSDX.
  - Yaesu FT-857D - Works fine with DigiRig interface (from K6ARK)
  - Yaesu FT-991A - Tested with Galaxy Tab A 2016 by David (F4DVX). FT-450D
    also works with FT-991A settings!
  - Kenwood TS-590S - Currently untested
  - Yaesu FT-817 / FT-818 -  SignaLink USB connected via OTG cable + using the DATA socket on radio
  - Yaesu FT-897 - Currently untested
  - QDX - CAT PTT support tested by HB9TXB, CAT Band Switching tested by ND7Y (Tyler)
  - Lab599 Discovery TX-500 - Experimental CAT support untested by us so far
  - Elecraft KX3 - Tested with DigiLink Nano interface (www.hb9zhk.ch) + a
    Lenovo tablet (M10 FHD Plus 2nd Gen. LTE)
  - ADX (LU7DID firmware emulating TS-480 @ 19200 bps) - Basic CAT PTT support works
  - Icom IC-703 - works fine in VOX mode with `ZLP Electronics MiniProSC` interface
  - Icom IC-7100 - works with Samsung Galaxy Tab S6 Lite (2020) after fiddling
    a bit with CI-V settings on the radio

  NOTE: Please reach out to us to get support for more radios.

- CAT control support for some radios is incomplete - only the PTT
  functionality is implemented. This is because we don't have access to these
  radios ourselves for development and testing purposes.

  NOTE: Please reach out to us to get better CAT support for such radios.

- The `signal strength` values shown (and used) by the app are different
  from the WSJT-X SNR values.

  Can we bring these different 'value systems' together?

- The seconds-timer is a bit wobbly. Please excuse it. It is meant for rough
  visual timing debugging.

- On Android, we can't easily use the 3.5mm audio jack (TRRS) for audio input.

  So rigs without inbuilt sounds cards will need a digital interface / USB
  sound card for audio reception.

  Reference: https://www.epanorama.net/blog/2014/09/15/android-device-external-mic-wiring/

  Update: To use the 3.5mm audio jack on the phone, see the following project:

  Note: https://github.com/4x1md/phone_rtty_interface - use this open-source
  project.

- It can be difficult to reply back when multiple responses ("calls") are
  received at once.

  Tip: Let the app handle the pileup (multiple responses) on its own.

- Keeping the volume on the phone too high might trigger ALC on Icom radios.

  Solution: Experiment with various volume levels, and choose an appropriate
  volume level.


#### Debugging Tips

- Increase the volume after launching the app.

- Check if your phone supports `USB OTG` using this [free app](https://play.google.com/store/apps/details?id=com.faitaujapon.otg&hl=en_US&gl=US).

- Make sure that your `Callsign` value is in UPPERCASE in App Settings.

  Example: `VU3CER` is correct but `vu3cer` isn't!

- Make sure that your `Grid` value is in UPPERCASE in App Settings.

  Example: `ML76` is correct but `ml76` isn't!

- My app has suddenly stopped decoding FT8 messages!?

  - Please ensure correct time on your phone or the correct `Time Delta` value
    in the App Settings. Visit https://time.is/ on your mobile phone to your
    time offset.

    Alternatively, use the app's `GPS Time Synchronization` feature.

  - Ensure that the app still has `microphone permissions`!

- Please put your radio in the `USB (upper sideband)` mode manually - the app
  doesn't do this on its own.

- Note: Enable the `OTG` option in your phone settings. This is required on
  phones like `Google Pixel 4 XL`, OnePlus 6, and so on.

  If this option is not enabled, then the phone doesn't detect any connected
  USB devices like a USB stick or the radio!

  Tested cable:

  - RAMPOW USB C Cable 3.3ft (56k Ohm Type C Charging Cable)

  Tested OTG adapter:

  - USB C to USB Adapter - compatible with MacBook Pro, various Samsung phones,
    Pixel phones, ETC.

  - USB C TYPE OTG ADAPTER METAL 30MM

- RX is working but TX seems to be a problem (on IC-7300, for example).

  We have had multiple cases where this was caused by actual physical
  connection issues - loose contacts, not enough stable connection.

  Retest your cables, OTG adapter, and the connections!

  Test with other Android devices - this is important. In one case, Note 9 and
  an old Samsung tablet had `loose connection` issues - shifting to an old Asus
  tablet fixed the problem straight away!

  Tip: To test your OTG adapter try connecting a USB stick to it and see if
  your phone can access the USB stick.

  Recently, an OTG-pigtail-cable caused the attached sound card to malfunction
  (with errors logged in `dmesg`). Replacing this OTG-pigtail-cable with a `USB
  C TYPE OTG ADAPTER METAL 30MM` immediately solved the connectivity issue.

  In another recent case, rebooting the phone immediately solved the bizarre
  connectivity issues. Oh well, software is hard!


#### Safety / Operating Tips

Use a common mode choke (CMC) near the rig. This solves a lot of bizarre issues
caused by `Common Mode Current`, especially when using unbalanced antennas.

https://github.com/kholia/HF-Balcony-Antenna-System has some details on this topic.

For ICOM-7300, we recommend using the `Tripp Lite USB 2.0 Hi-Speed A/B Cable
with Ferrite Chokes (M/M) 3-ft. (U023-003)` cable.

Add a CMC (choke) to the regular USB cables by making 10 turns of the USB
cable on a FT240-43 toroid core.

Tip: To rule out bizarre issues (e.g. radio hanging or disconnecting from USB)
due to CMC, test the radio with a dummy load.

Some versions of WSJT-X are known to be broken (especially for FT-817
emulation). Do report such (new) issues to the upstream WSJT-X project.


#### Antenna Recommendations

- https://www.kk5jy.net/three-wire-gp/ - superb for DX contacts - give it a try!

- https://k6ark.com/ antennas cannot be beaten when it comes to portability - try them out!

- https://github.com/kholia/HF-Balcony-Antenna-System - Use higher bands in
  small, constricted spaces!


#### FAQ

1. What does the `31 +0.32 1753 ~ CQ AP2IN MM63` line actually mean?

   - The first column (31) is the relative `signal strength` - a higher number
     means a stronger signal.

   - The second column (+0.32) is the `DT` value (time delay), which is similar to
     WSJT-X.

   - The third column (1753) is the frequency offset.

   - After the `~` character we have the FT8 message, which is `CQ AP2IN MM63` in
     this case.

2. I see a green microphone icon appear near the battery amount in the upper
   right corner of the screen. Is this OK?

   Yep - this is the expected behavior.

3. RX and TX are working fine. Now, how do I have a QSO!?

   Click on a callsign from the latest decoded FT8 messages. The app will turn
   on the TX mode, and send an appropriate message at the correct time.

   After this initial action, the rest of the QSO process is automatically
   handled by the app, just like WSJT-X.

   I recommend getting familiar with FT8 QSOs with WSJT-X on a PC (or RPi)
   first. The app is like a simpler (and poorer version) of WSJT-X.

4. What kind of a sound card do I need?

   Modern rigs (e.g. IC-705, IC-7300) have in-built sound cards, and with such
   rigs a separate sound card is NOT needed.

   E.g. For IC-705, I use an old phone charging Micro USB cable along with a small
   USB-C OTG adapter.

   ![USB-C OTG Adapter](../images/type-c-mini-otg-250x250-1.png)

   If your rig doesn't have an in-built sound card, you can buy a cheap (1 to 2
   USD) USB sound card.

   https://github.com/kholia/DigitalRadioReceiverSupport URL has a picture
   of a suitable sound card. These are available easily on AliExpress and
   Amazon.

   This sound card is connected to the following `USB OTG Hub (Type-C)`.

   ![USB Hub Type C](../misc/Portronics_USB_3.0_Hub_Type_C_Cable.jpg)

   The USB Hub is required as we need to connect two things (the CAT cable and
   the sound card) to a single USB port of the phone.

   Update: `Sound Blaster PLAY! 3` is strangely buggy on Android, and causes ~3
   second delays during transmissions.

   Update: `ROCCAT Juke` has pretty low mic gain and can't be recommended.

5. How do I upload the QSO logs to QRZ.com or LoTW?

   Install a file manager app like `Cx File Explorer` on your phone.

   In the `FT8 Radio` app, click on the `Share` icon. This will allow you to
   export the QSO logs in a file named `qso_logs.adi`.

   This ADIF file can then be uploaded to LoTW or QRZ.com as usual.

6. What does the `SPX` (SIMPLEX) button do in the app?

   `SPX OFF` means that the app will work in `split mode` where the RX and TX
   frequencies are different.

   And so on.

7. What does the `CLS` button do in the app?

   The `CLS` button clears the app's display. Just like the DOS command ;)

8. How do I call with `CQ SOTA <callsign> <grid>` or `CQ POTA <callsign>
   <grid>` message?

   Please select the appropriate pre-prepared SOTA/POTA message from the
   'message dropdown list' in the app, and then click on the `TX OFF` button
   once.

   The app will then send the SOTA/POTA message in the upcoming FT8 TX cycle.

9. How do I request support for a particular radio model (rig)?

   Once you have connected the rig to the Android phone using a suitable cable
   or digital interface, please run the [USB Device Info](https://play.google.com/store/apps/details?id=aws.apps.usbDeviceEnumerator)
   app on your phone, and share the app screenshots with us.

   Essentially, we are looking for the USB-serial port details (Speed, VID,
   PID, CDC or not).

10. How do I use the `GPS Time Synchronization` feature of the app?

    - Click on the `location` icon in the app. Give approval for the `Location
      Permissions` needed by the app.

    - Click again on the `location` icon again.

    - Let the app sit here for a while. Wait for the `Time Delta` value to
      stabilize well. I usually give it around a minute or more to settle down.

    - Click on the `STOP CONTINUOUS SYNC` button and press the back button on
      the phone.

    - You are done ;)

    Note: This feature automatically updates the `Time Delta` value in the App
    Settings.

11. How do I activate the `Dark Mode` in the app?

    `Dark Mode` is automatically activated depending on your phone settings.

    On your phone, please enable the `Settings -> Display -> Dark theme` option,
    and relaunch the app.

12. What does the `Enable Spotting` option do? What is `spotting`?

    The `spotting` feature uploads your FT8 decodes to the https://pskreporter.info/ site.

    Note: This is an optional feature.

13. What is that `counter` in the upper left hand corner of the app's display?

    This `counter` is simply the `seconds` counter. It helps with debugging
    timing related problems on the phone / tablet.

    If this counter is not aligned with the timing of the FT8 sequences, then
    please double-check the time on your device.

14. What does the `Tune ON` menu option do?

    It turns on the PTT, and transmits a `VVV` FT8 message for approximately
   ~13 seconds after which it turns off the PTT.


#### Radio Setup Instructions


1. How do I configure `Xiegu X6100` in CAT mode?

   - Select `Xiegu X6100` as the `Radio` in App Settings.

   - Set `Port Number` value to `1`.

   - Restart the FT8 app by force killing it first, and then relaunching it.

   - You are done ;)

2. How do I configure `Elecraft KX3` in CAT mode?

   - Use the original KXUSB cable from Elecraft.

   - Select the `TS-590S (38400)` model in the `Radio` field in the App Settings.

   - Restart the FT8 app by force killing it first, and then relaunching it.

   - You are done ;)

3. How do I configure `IC-706` (or IC-706MKIIG) to work with the app?

   Set the radio model to `VOX` or `Unknown` in the App Settings.

   Use one of the following digital interfaces:

   - SignaLink USB Interface

   - RIGblaster Advantage

   - DigiMaster MiniProSC (https://www.g4zlp.co.uk/unified/DM_MiniPro_SC.shtml)

   Note: [IC-706 does NOT support PTT functionality via CAT control](https://github.com/Hamlib/Hamlib/blob/ea9257db45231d8fef6a64b7e7086f63b996af2a/rigs/icom/ic706.c#L158).

4. How do I configure IC-7100 to work with the app?

   The app uses the default 19200 baud rate and the default 0x88 CI-V address
   for IC-7100.

   On the IC-7100 rig, please change the following settings:

   ```
   SET/Connectors/DATA MOD -> USB
   ```

   ```
   Set SSB mode to USB
   ```

   Note: You may have to do this multiple times for it to work. Oh, Icom...

   Reference: https://2e0pgs.github.io/blog/hamradio/2020/07/29/ic-7100-usb-data-mode-operation/


#### Phone (Device) Gotchas

The Samsung Galaxy S22 Ultra phone doesn't seem to emit audio properly to drive
the connected IC-705 radio. To fix this problem, give the following steps a
try:

- Go to Settings > Device Care > Battery > Charging. Set `Fast charging` to
  OFF.

- Enable `Developer Options` on your phone. Google search to find the steps
  involved.

- Ensure that the `Disable USB audio routing` is OFF in `Developer Options`.

- Granting storage permissions to the `Samsung USB-C Headset` app can also
  help in some cases.

- Restart the app (this may perhaps be required?).

- Google for `samsung usb-c no audio` - this results in many hits!

- Note: If the phone is emitting audio correctly, the IC-705 will consume over
  2A current when TX'ing at 10W level!

- Alternate solution: Buy a mid-segment Xiaomi phone (e.g. Redmi Note 11 Pro).
  They just work without problems.

Samsung S7: In CAT mode, Audio TX works but audio RX only works sporadically
with IC-7300. We suspect that Android is using a low volume for the USB audio
input device on S7 phone. For now, we recommend using the `VOX` mode (AF mode)
when using Samsung S7 phone (and similar phones) along with a VOX based digital
interface.

Samsung Galaxy models running Android 9 may be problematic as they can't find
connected USB devices like Arduino Nano (using FT232 chip). In contrast, newer
Galaxy phones - like Galaxy A52 running Android 11 - work just fine.

Recommended phones: Any of the low-range / mid-range Xiaomi phones with 3.5mm
jack should be OK.


#### Tested Phones + Tablets

- Redmi Note 7

- Redmi Note 7 Pro

- Redmi Note 8 Pro - 1080 x 2340 pixels

- Redmi Note 8 Pro Max

- Google Pixel 2 XL - works with IC-7300, and FT-857D (via DigiRig interface from K6ARK)

- Google Pixel 4 (Android 12) - comes without 3.5mm audio jack

- Google Pixel 6 (Android 14)

- OnePlus Nord N10 - has 3.5mm headphone jack - 1080 x 2400 pixels

- Samsung S21 Ultra 5G - tested with `USB C Type Male Plug to Micro B Data Sync
  & Charge Cable` (from eBay) and IC-705.

- Samsung S10 - works fine with IC-7300 over a USB cable.

- Samsung Galaxy S20 FE (Spanish) - with uSDX+ radio

- Xiaomi Mi A2

- Galaxy S10 and S21 - in VOX mode with Yaesu FT-897 and FT-817ND

- Huawei MediaPad 10" tablet - works fine with 'FT8 Radio'

- Samsung Tab A (8.0", 2019) running Android 11 - tested with FT-817ND + SignaLink USB

- Samsung S4 (Lineage 14.1 - Android 7.1) - tested with QDX

- OnePlus 6 (Android 10) - tested with QDX - please enable the `OTG setting / mode` in your phone

- Samsung Galaxy Tab S6 + Samsung A90 5G phone - tested with `Xiegu X6100` in CAT mode

- LG K42 - A simple TRRS cable to the Xiegu G90's mini DIN Aux socket works
  fine with the G90 set to VOX.

- Nokia 5.3 (2020) - Works fine with IC-7300 + USB + OTG cable

- Samsung Galaxy S6 Lite (2020) - Works fine with IC-7300 + USB + OTG cable

- Samsung Galaxy S9+ - Works fine with Digirig Mobile 1.9 (+ FT-818 cable) with
  Yaesu FT-818. Similar combination of Yaesu FT-818ND + Digirig Mobile +
  Google Pixel 4a also works fine.

- Samsung Galaxy S8 - Works fine with FT-818, SB-2000 transceiver interface,
  and a OTG cable

- Samsung Galaxy A12 - Works fine with DIGIVOX-2 modem

- Motorola Moto G 5G Plus - Works fine with Xiegu X6100 and Icom IC-7300.

- Moto G6 - Works fine with FT-891 operating in VOX mode.

  We will be testing FT-891 in CAT mode via the following 'digital interface' cables.

  - `USB CAT control Cord Cable for Yaesu FT-891 HF Transceiver` (bd7-maple on
    eBay)

  - FT8/FT4/JT65/PSK Audio Interface 6-Pin Mini DIN Cable DC-11F for YAESU
    (bd7-maple on eBay)

Note: We need your feedback in expanding this list - thank you!


#### Digital Interfaces

If your rig doesn't have an inbuilt sound card, you will need a digital
interface to connect the rig to the PC / RPi / Android phone.

- [LiDi](https://github.com/kholia/Light-Intuitive-Digital-Interface) works
  fine for uBITX radios.

- https://www.wolphi.com/interface/ works for a variety of rigs (Yaesu FT-817,
  FT-857 and FT-897 as well as IC-703, IC-706 and IC-7300).

  Note: https://github.com/4x1md/phone_rtty_interface - use this open-source
  project.

  If your phone doesn't have the sound-card drivers for IC-7300 (an example),
  then you may need such an interface as well.

  If you are running into USB CAT issues, try this interface method as well.

- [Yaesu SCU-17](https://www.wimo.com/en/scu-17) should work fine for Yaesu
  radios - it has been untested by the developers so far though.

  Yaesu SCU-17 with CT-62 cable should work for FT-817ND / FT-818.

- `USB C Type Male Plug to Micro B Data Sync & Charge Cable` - This single
  cable works great for IC-705.

- `SignaLink USB Interfaces` should also work. See https://www.tigertronics.com/pricing.htm
  for details.

- DIY digital interface (Yaesu): https://www.yo3ggx.ro/ft8x7datav2/FT817_DIY_data_modes_interface_v2.0.pdf

- Another DIY digital interface: https://morsetutor.com/2015/01/yaesu-ft-450d-digital-interface/

- Icom IC-718 needs a SignaLink interface or IC-718 needs to operate in VOX mode.

  - https://github.com/Hamlib/Hamlib/blob/master/rigs/icom/ic718.c#L86 (RIG_PTT_NONE)

    The SignaLink cable will set PTT (to GND) on Pin 3 in the ACC socket (port)
    when you use the VOX mode SignaLink.

  - https://static.dxengineering.com/global/images/instructions/ico-ic-718.pdf

    Alternatively, turn on the VOX mode on the radio.

- We support Digirig Mobile (RTS as PTT) digital interface as well for various radios.

Currently, the authors of this app don't have access to Yaesu, and Kenwood
rigs. Please reach out to us to help us improve support for these radios.

Note: Once you have a digital interface working with a PC (or RPi), the same
setup should carry over to the Android phone.


#### Planned Features / Future Ideas

- [Done in BETA 145] More time to select a callsign.

  Dhiru: Relax TX timing a bit. We are producing DT values of 0.0 to 0.2. We
  can relax our TX timing a bit ;)

- [LP] Wireless (WiFi) support for Icom IC-705.

  - This will be a new app called `FT8 705` or `FT8 Radio WiFi` to keep
    software complexity under control.

  - Note: WiFi on IC-705 is pretty poor. Even cheap ESP8266 does better !?

- [NP] JS8Call support - will probably be another app.

- [NP] FT4 support - will probably be another app (!?)

- Log the `remote grid` natively in the app itself instead of relying on QRZ /
  LoTW to provide this value.

  This would be helpful for park to park, or summit to summit QSOs.

- UI suggestions:

  - Make the red/green lines in the buttons TX OFF/ON and SPX OFF/ON thicker.
    They are very small and their color is not really visible (Samsung S7 and
    S10).

  - [High Priority] App Settings -> Put one space line between decoded
    messages. This will make selecting calls, and replying easier.

  - The app should return to the main screen automatically after having
    selected one of the recommended frequencies.

  - Better colors overall! Improve readability and contrast.

- [NP] Different colors for new, and worked stations.

- [LP] The color of the own CQ line first is violet, and then it changes to red
  after having received some stations. Fix this cosmetic bug.

- [CORE] Add support for special callsigns.

  Examples: LW8EUA/A, LW8EUA/H, VU3CER/P

  Counterpoint: Use of `/P` or `/QRP` modifiers is frowned upon at times!?

  Also, `ft8code "CQ LW8EUA/H MK68"` decodes as `CQ LW8EUA MK68` only (with
  'err' indicated) and so on!

  Note: I recommend using `CQ PORT LW8EUA grid` or `CQ FLD LW8EUA grid`
  messages instead.

  Note 2: See if `SP3LRS/P`, `OK/SP3LRS`, `DL/SP3LRS/P` callsigns can be sent
  via WSJT-X or not.

- Repeat sending, as long as the other station does not answer.

- Allow switching on / off the `Tx 1` (WSJT-X like) message.

- Better correct support for `WWFF` program.

  - Make logging require a manual step at the end of the QSO

  - Respond to ONLY the first response to a CQ call, or a selected responder to/or from a CQ call

- 'Logbook Browser'

  Enable the user to see the callsigns and countries worked so far.

- Show contacted countries on a map.

- Add a filter to only show `CQ` calls.

  This filter has be smart enough to show the messages from the
  QSO-in-progress.

Thanks to our app users for all these awesome ideas, feedback, and
encouragement!

All the best and 73s from Dhiru - VU3CER!


#### References

- https://www.qsl.net/wm2u/interface.html
