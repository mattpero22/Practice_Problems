'''
Problem: https://www.codewars.com/kata/513e08acc600c94f01000001/solutions/python

Plan of Attack:
    1. Verify that the input numbers are in the range 0 - 255 and fix them if not
    2. convert each decimal value into a hex value
    3. format the hex value as a string in uppercase chars for each value (r,g,and b)
    4. concatenate the three hex strings together for the overall hex color code
'''


def rgb(r, g, b):
    # check for valid range of input between 0 and 255
    r = 255 if r > 255 else r
    r = 0 if r < 0 else r
    g = 255 if g > 255 else g
    g = 0 if g < 0 else g
    b = 255 if b > 255 else b
    b = 0 if b < 0 else b

    # convert and replace the preceding hex identifier on the value
    r_hex = str(hex(r).replace("0x", ""))
    g_hex = str(hex(g).replace("0x", ""))
    b_hex = str(hex(b).replace("0x", ""))
    
    # if value is only one digit of length, precede it with a 0
    r_hex = "0" + r_hex if len(r_hex) == 1 else r_hex
    g_hex = "0" + g_hex if len(g_hex) == 1 else g_hex
    b_hex = "0" + b_hex if len(b_hex) == 1 else b_hex
    
    color_hex = r_hex.upper() + g_hex.upper() + b_hex.upper()

    return color_hex

'''
Results: COMPLETED 25 minutes
Notes: 
    * code could be more DRY but this gets the job done, could have leveraged lambda functions better

'''