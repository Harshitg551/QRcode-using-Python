import qrcode as qr #imp #as (alias)
#make func: is used to make qr code 
#save function: it will give us in png format

img=qr.make("https://www.linkedin.com/in/harshit-gupta-ba49321a9/")#Enter the link here or you can type any string 
img.save("myqr.png")#Enter the name of the file with extension
