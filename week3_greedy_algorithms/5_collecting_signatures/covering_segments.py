from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def points_in_segment(points, s):
    for p in points:
        if s.start <= p <= s.end:  # current segment intersect with prev point
            return 1
    return 0


def optimal_points(segments):
    points = []
    prevSeg = Segment(0, 0)
    while len(segments) > 0:
        if len(segments) == 1:
            if points_in_segment(points, segments[0]) == 1:
                break
            else:
                points.append(segments[0].end)
                break
        for s in segments:
            if (prevSeg.start == 0 and prevSeg.end == 0) or (prevSeg.start == s.start and prevSeg.end == s.end):
                prevSeg = s
                continue
            if points_in_segment(points, s) == 1:  # current segment intersect with prev point
                segments.remove(s)
                if prevSeg.start == s.start and prevSeg.end == s.end:
                    prevSeg = Segment(0, 0)
                continue
            if prevSeg.start <= s.end <= prevSeg.end:  # current segment end between prev segment
                points.append(s.end)
                segments.remove(s)
                continue
            elif s.start <= prevSeg.end <= s.end:  # prev segment end between current segment
                points.append(prevSeg.end)
                segments.remove(prevSeg)
            prevSeg = s

    return points


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
