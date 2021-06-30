# tuya-cloud-smart-bulb
This project is developed using Tuya SDK, which enables you to quickly    develop smart devices, branded APP, cloud development project, etc.

For more information, please check Tuya Developer Click and Connect      Challenge: https://pages.tuya.com/develop/ClickAndConnect_TuyaDeveloper?_source=e9684c7ca6b31e7221c8420f5af94631 


Full documentation for this package can be found here: <a href="https://github.com/Octoober/tuya-bulb-control">Link</a><br />
(Use that for API documentation)

<h2>Installation:</h2>
<h4>pip install tuya-bulb-control --upgrade</h4>

<h3>Sample Code:</h3>

```Python
from tuya_bulb_control import Bulb

CLIENT_ID = ''    # Access ID or Client ID
SECRET_KEY = ''   # Access Secret or Client Secret
DEVICE_ID = ''    # Devise id which is online to control
REGION_KEY = ''   # Region key eg: in for india, eu for europe, us for usa, cn for china, etc based on region where the device is there 

bulb = Bulb(
    client_id=CLIENT_ID,
    secret_key=SECRET_KEY,
    device_id=DEVICE_ID,
    region_key=REGION_KEY
)

# Turn on the bulb
bulb.turn_on()

# Change the color to green
bulb.set_colour_v2(rgb=(0, 255, 0))

# Turn off the light bulb after 5 minutes
bulb.set_toggle_timer(value=5)
```


<br>
<h2>Steps for doing the project:</h2>
1)Make an account here: <a href="https://iot.tuya.com/">New Account</a><br />
2)Go to cloud development, and make a project.<a href="https://iot.tuya.com/cloud/">Cloud->Project</a><br />
3)Fill the details asked and make the project.<br />
4)You can see the new project as the below image.<br />
<img src="https://user-images.githubusercontent.com/62068859/123901442-909e3880-d988-11eb-98a2-593d376baef6.png">
<br>

5)Add a device, I am using a smart bulb with WIFI.<br />
<img src="https://user-images.githubusercontent.com/62068859/123899898-b413b400-d985-11eb-9918-34f6db60de03.png">

<br>
6)Save all the details like client id,client secret key, device id, to be used in the project. Dont share these to others.
<br>
7)From the tuna_bulb_control folder you can see all the different functions available with python codes.<br>
8)Enter the client id,client secret key, device id, region code in the fields for each program which you want to execute.<br>
9)After that run the code, see that the device is online and connected to app.
<br>
<br>
<h3>Function available:</h3>
bulb_on<br>
bulb_off<br>
set_bright<br>
set_bright_v2<br>
set_color<br>
set_color_v2<br>
set_color_temp<br>
set_color_temp_v2<br>
set_work_mode<br>
state<br>
functions<br>
toggle<br>
toggle_timer<br>
<br>
<h4>More Info:</h4>
All the details of the device can be found here using device id, for all differen controls and function.
<br>
<br>
<img src="https://user-images.githubusercontent.com/62068859/123900800-613afc00-d987-11eb-8e5a-d8e2b552289d.png">
<br>
You can control device from the below pic by sending data to the id, if success then it is executed.
<br>
<br>
<img src="https://user-images.githubusercontent.com/62068859/123900902-95aeb800-d987-11eb-8f9c-7504ed077256.png">
<br>
<h3>Note:</h3>
Tutorial videos can be seen in youtube for sample ones to connect.<br>
Even i will upload a video soon to show the demo.


