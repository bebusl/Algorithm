from collections import defaultdict

def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = map(int,fees)

    stack = set()
    receipt = defaultdict(int)
    for record in records:
        time, number, status = record.split()
        hour, minute= map(int, time.split(":"))
        convert_to_minute = hour*60 + minute

        if(status=='IN'):
            stack.add(number)
            receipt[number] -= convert_to_minute
        if(status=="OUT"):
            stack.remove(number)
            receipt[number] += convert_to_minute
    for last in stack:
        receipt[last] += 24*60-1
    for i in receipt:
        if(receipt[i] <= default_time):
            receipt[i] = default_fee
            continue
        last_time = (receipt[i]-default_time)//unit_time if (receipt[i]-default_time)%unit_time == 0 else (receipt[i]-default_time)//unit_time +1
        receipt[i] = default_fee + last_time*unit_fee

    answer = list(map(lambda item : item[1],sorted(receipt.items())))

    return answer

print(solution([180, 5000, 10, 600]	,["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	 ))
print("ANSWER : ", [14600, 34400, 5000])
print("-==========")
# 해결 함