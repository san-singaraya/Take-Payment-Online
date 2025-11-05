# Take-Payment-Online
Take Payment Online Description

[2b530c89-130f-4496-b0cb-aeb3a8c54810.txt](https://github.com/user-attachments/files/23357575/2b530c89-130f-4496-b0cb-aeb3a8c54810.txt)
Repository: san-singaraya/take-payment-online
Files analyzed: 2

Estimated tokens: 173

Directory structure:
└── san-singaraya-take-payment-online/
    ├── README.md
    └── python project/
        └── takepaymentonline.py


================================================
FILE: README.md
================================================
# Take-Payment-Online
Take Payment Online Description



================================================
FILE: python project/takepaymentonline.py
================================================
import qrcode
upi_id = input("Enter your UPI ID : ")

# TO fetch the UPI details Formula
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# to Create the QR CODE
phonepe_qr = qrcode.make(phonepe_url) 

# to save the photo format
phonepe_qr.save('phonepe_qr.png') 
phonepe_qr.show()

<img width="1292" height="960" alt="Screenshot 2025-11-05 at 4 08 51 AM" src="https://github.com/user-attachments/assets/b10c440a-97c8-46f0-829d-27e68fb74a13" />

