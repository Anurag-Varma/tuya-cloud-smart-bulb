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
