import qrcode #imp #as (alias)
from PIL import Image #this lib used for formating

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,     #there are several versions you can also check it out
    error_correction=qrcode.constants.ERROR_CORRECT_H,      #H is for high you can also change if you want...
    box_size=15,   #QRCode is used for changing the qr colour background etc...
    border=5,
)

# Add the data to the QRCode object
qr.add_data("https://www.linkedin.com/in/harshit-gupta-ba49321a9/")

# Make the QRCode
qr.make(fit=True)

# Create an image from the QRCode with specified colors
img = qr.make_image(fill_color="Purple", back_color="White")  # Use the color code for Silver Gray(#C0C0C0)# #FFD700 golden

# Save the image
img.save("advanceQR.png")

# in previous version the qrcode is working as alias and above we have data stored in QRCode: 
# previous form:
# img=qr.make("https://www.linkedin.com/in/harshit-gupta-ba49321a9/")#Enter the link here or you can type any string 
# img.save("myqr.png")#Enter the name of the file with extension
