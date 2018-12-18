from darksky import forecast

multicampus = forecast('8758cf6f122cbe554eadad7e18376b95', 37.501528, 127.039692)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])
