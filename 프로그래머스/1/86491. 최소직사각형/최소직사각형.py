def solution(sizes):
    for size in sizes:
        if size[0] != max(size):
            size.reverse()
    return max([size[0] for size in sizes]) * max([size[1] for size in sizes])
