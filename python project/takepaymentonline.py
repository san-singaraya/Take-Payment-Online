import qrcode
upi_id = input("Enter your UPI ID : ")

# TO fetch the UPI details Formula
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# to Create the QR CODE
phonepe_qr = qrcode.make(phonepe_url) 

# to save the photo format
phonepe_qr.save('phonepe_qr.png') 
phonepe_qr.show()