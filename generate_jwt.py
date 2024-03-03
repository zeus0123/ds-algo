import hashlib

import jwt

new_token = jwt.encode({"username": "Nurture User"}, "Fd@p!#2018", algorithm="HS256")
email = "placid_admin@clout.com"
hashed_email = hashlib.md5(email.encode("utf-8")).hexdigest().lower()
print(hashed_email)