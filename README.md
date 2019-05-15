Power Plug RESTful call to Western Telematic Inc. (WTI) devices.

This is a Simple Python3 script for controlling the power plugs on WTI Power devices with RESTful calls.

This works on any modern WTI device with power plugs, the power plug RESTful call is universal on all WTI type devices with power plugs.

To Configure:

To change the default values modify SITE_NAME to the address of your WTI device. Change the USERNAME and PASSWORD to the correct values for your WTI device.

To Run: python3 plugreboot.py

After asking you if you want to change any of the default values (hit enter to accept the defaults), the program will connect to the WTI device, change the plug states and return the current power plug information.

Documentation:

The HTML, RAML and OpenAPI file relating to the RESTful API calls can be found here:

https://www.wti.com/t-wti-restful-api-download.aspx

Contact WTI:

If you have any questions, comments or suggestions you can email us at kenp@wti.com

About WTI:

WTI - Western Telematic, Inc. 5 Sterling, Irvine, California 92618

Western Telematic Inc. was founded in 1964 and is an industry leader in designing and manufacturing power management and remote console management solutions for data centers and global network locations. Our extensive product line includes Intelligent PDUs for remote power distribution, metering, reporting and control, Serial Console Servers, RJ45 A/B Fallback Switches and Automatic Power Transfer Switches.
