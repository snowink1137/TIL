from datetime import datetime
import time
from queue import PriorityQueue


def solution(n, customers):
    answer = 0
    kiosk = [[0, i+1] for i in range(n)]
    check = [0 for _ in range(n+1)]

    kiosk_queue = PriorityQueue(maxsize=3)
    for k in kiosk:
        kiosk_queue.put(k)

    for i in range(len(customers)):
        time_obj = datetime.strptime(customers[i][:14], '%m/%d %H:%M:%S').replace(year=1970)
        process_time = int(customers[i][15:])
        timestamp = time.mktime(time_obj.timetuple())

        kiosk_now = kiosk_queue.get()
        check[kiosk_now[1]] += 1
        kiosk_now[0] = timestamp + process_time * 60
        kiosk_queue.put(kiosk_now)

    answer = max(check)

    return answer


n = 2
customers = ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]
print(solution(n, customers))
