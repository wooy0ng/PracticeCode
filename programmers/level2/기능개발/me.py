from collections import deque


'''
내 코드는 복잡도가 O(n^2)임.
'''
def solution(progresses, speeds):
    non_complete = deque([n for n in range(len(progresses))])
    complete_stack = []
    answer = []
    while non_complete:
        progresses = [progress + speed if progress < 100 else 200 for progress, speed in zip(progresses, speeds)]   
        for idx, progress in enumerate(progresses):
            if progress > 99 and progress < 200:
                complete_stack.append(idx)
        cnt = 0
        complete_stack.sort(reverse=True)
        for n in non_complete:
            if n in complete_stack:
                complete_stack.pop()
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
            for _ in range(cnt):
                non_complete.popleft()
    return answer



progresses = [93, 30, 55]	
speeds = [1, 30, 5]	
print(solution(progresses, speeds))