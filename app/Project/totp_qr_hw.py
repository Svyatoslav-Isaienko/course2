import pyotp
import qrcode


USER_NAME = "petro@example.com"
ISSUER_NAME = "MyCoolApp"



secret = pyotp.random_base32()


totp = pyotp.TOTP(secret, digits=6, interval=30)
uri = totp.provisioning_uri(name=USER_NAME, issuer_name=ISSUER_NAME)


img = qrcode.make(uri)
img.save("totp_qr.png")
print("URI:   ", uri)
print("Secret:", secret)
print("QR збережено у totp_qr.png — скануйте його в додатку.")
img.show()


while True:
    code = input("Введіть 6-значний код із додатка (або 'q' для виходу): ").strip()
    if code.lower() == "q":
        break
    if totp.verify(code, valid_window=1):
        print("Код вірний — налаштування підтверджено!")
        break
    print("Невірний код, спробуйте ще раз.")