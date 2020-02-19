def compute_min_refills(distance, tank, stops):
    refill = 0
    stops.append(distance)  # adding last stop
    ok = 0
    remainingTank = tank
    currentStop = 0
    prevRefillStop = 0
    while len(stops) > 0:
        if remainingTank > distance:
            ok = 1
            break
        #     remaining fuel at this stop
        remainingTank = tank - (stops[currentStop] - prevRefillStop)
        if remainingTank < 0 and currentStop == 0:
            break  # IMPOSSIBLE
        if remainingTank <= 0:
            if remainingTank == 0:
                idx = 1
            else:
                idx = 0
            distance = distance - (stops[currentStop - 1 + idx] - prevRefillStop)
            prevRefillStop = stops[currentStop - 1 + idx]
            #     remove stops prev stops and refill tank
            del stops[0:currentStop + idx]
            refill += 1
            currentStop = 0
            remainingTank = tank
        else:
            currentStop += 1

    if ok == 1:
        return refill

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, input().split())
    print(d, m, stops)
    print(compute_min_refills(d, m, stops))
