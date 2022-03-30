from bs4 import BeautifulSoup
import requests
from datetime import datetime

now = datetime.now()


html_text = requests.get('https://waitz.io/live/ucsd-rec/')
soup = BeautifulSoup(html_text.text, 'lxml')
test = soup.find("body").get_text(strip=True)

indexFirstBusyness = test.index("\"busyness\":")
rimacGym = test[indexFirstBusyness+11:indexFirstBusyness+14]
test = test[indexFirstBusyness+1:len(test)]
indexSecondBusyness = test.index("\"busyness\":")
mainGym = test[indexSecondBusyness+11:indexSecondBusyness+14]


# rimacGym = test[56:59]
rimacGymBusyCharLen = 0
if (rimacGym[0:3].isnumeric()) :
    rimacGymBusyCharLen = 3
elif (rimacGym[0:2].isnumeric()) :
    rimacGymBusyCharLen = 2
else :
    rimacGymBusyCharLen = 1

# mainGym = test[(361 + rimacGymBusyCharLen):(361 + rimacGymBusyCharLen)+3]
mainGymBusyCharLen = 0
if (mainGym[0:3].isnumeric()) :
    mainGymBusyCharLen = 3
elif (mainGym[0:2].isnumeric()) :
    mainGymBusyCharLen = 2
else :
    mainGymBusyCharLen = 1

def getWeekday(dayNum) :
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
 
    return switcher.get(dayNum, "error occurred")

rimacBusyness = rimacGym[0:rimacGymBusyCharLen]
mainBusyness = mainGym[0:mainGymBusyCharLen]



print(test[45:100])


current_time = now.strftime("%H:%M")
print(getWeekday(datetime.today().weekday()))
print(current_time)

# print("rimacGymBusyCharLen ")
# print(rimacGymBusyCharLen)
# print("mainGymBusyCharLen ")
# print(mainGymBusyCharLen)

print(rimacBusyness)
print(mainBusyness)
with open('txtfiles/day.txt', 'a') as f:
    f.write(getWeekday(datetime.today().weekday()))
    f.write("\n")
with open('txtfiles/time.txt', 'a') as f:
    f.write(current_time)
    f.write("\n")
with open('txtfiles/rimac.txt', 'a') as f:
    f.write(rimacBusyness)
    f.write("\n")
with open('txtfiles/main.txt', 'a') as f:
    f.write(mainBusyness)
    f.write("\n")