'''
부분 수열의 합은 k
우선순위1) 합이 k에서 길이가 가장 짧은 수열
우선순위2) 길이가 같으면 가장 앞쪽에 있는 수열

투포인터
'''

def solution(sequence, k):
    l, r = 0, -1
    val = 0
    ans = [0, 1000000]
    for i in range(len(sequence)):
        r += 1
        val += sequence[i]
        if val > k:
            while l < r:
                if val <= k: break
                val -= sequence[l]
                l += 1
        if val == k and (ans[1] - ans[0] + 1) > (r - l + 1):
            ans = [l, r]
    return ans