


from multiprocessing.sharedctypes import Value


def solution(numbers, hand):
    answer = ''
    left_hand, right_hand = 10, 12
    left_list, right_list = [1, 4, 7], [3, 6, 9]
    for choice in numbers:
        if choice == 0:
            choice = 11

        if choice in left_list:
            answer += 'L'
            left_hand = choice
        elif choice in right_list:
            answer += 'R'
            right_hand = choice
        else:
            l_abs = abs(left_hand - choice)
            r_abs = abs(right_hand - choice)
            l_diff = (l_abs // 3) + (l_abs % 3)     # 몫 -> layer, 나머지 -> position
            r_diff = (r_abs // 3) + (r_abs % 3)

            if l_diff < r_diff:
                answer += 'L'
                left_hand = choice
            elif l_diff > r_diff:
                answer += 'R'
                right_hand = choice
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = choice
                else:
                    answer += 'R'
                    right_hand = choice

    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	
hand = "left"	

solution(numbers, hand)