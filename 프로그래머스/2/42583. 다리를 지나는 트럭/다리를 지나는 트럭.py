from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    d = deque(truck_weights)
    bridge = deque([0]*bridge_length, maxlen=bridge_length)
    bridge_sum = 0 
    while bridge:
        item = bridge.popleft()
        time += 1
        bridge_sum -= item
        if d:
            if bridge_sum + d[0] <= weight:
                dweight = d.popleft()
                bridge.append(dweight)
                bridge_sum += dweight
            else:
                bridge.append(0)
    return time