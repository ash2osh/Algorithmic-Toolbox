from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def points_in_segment(points, s):
    for p in points:
        if s.start <= p <= s.end:  # current segment intersect with prev point
            return 1
    return 0


def optimal_points(segments):
    points = []
    segs = []
    for s in sorted(segments):
        segs.append(Segment(s.start, s.end))

    while len(segs) > 0:
        if len(segs) == 1:
            if points_in_segment(points, segs[0]) == 1:
                break
            else:
                points.append(segs[0].end)
                break
        prevSeg = segs[0]
        currSeg = segs[1]
        if points_in_segment(points, prevSeg) == 1:  # current segment intersect with prev point
            segs.remove(prevSeg)
            if points_in_segment(points, currSeg) == 1:
                segs.remove(currSeg)
            continue
        if prevSeg.start <= currSeg.end <= prevSeg.end:  # current segment end between prev segment
            points.append(currSeg.end)
            segs.remove(currSeg)
            segs.remove(prevSeg)
        elif currSeg.start <= prevSeg.end <= currSeg.end:  # prev segment end between current segment
            points.append(prevSeg.end)
            segs.remove(prevSeg)
            segs.remove(currSeg)
        else:
            points.append(prevSeg.end)
            segs.remove(prevSeg)
    return list(set(points)) # unique list


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(0, n):
        s = list(map(int, input().split()))
        segments.append(Segment(s[0], s[1]))
    # n, *data = map(int, input().split())
    # segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
