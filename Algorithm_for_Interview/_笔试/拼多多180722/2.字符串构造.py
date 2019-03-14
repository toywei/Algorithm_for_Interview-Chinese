"""
字符串构造

问题描述：
    一个长串由一个字串循环构成，即 s[i]=t[i%n]，比如 "abcabc" 由 "abc" 构成

    注意："abcabcab" 也是由 "abc" 构成的，答题时没注意这个又只过了一部分

    *建议使用 Python 解决字符串相关问题，下面也只贴 Python 代码
"""

s = input()

n = len(s)
for i in range(1, n + 1) :
    base = s[:i]
    if base * (n // i) + base[:n % i] == s:
        print(base)
        break



'''
借助递归
'''

testCases = ['aaaaa', 'aabaaba', 'abaabaa', 'abcabca', 'abcabcab', 'abcabceabcabceabc', 'abcabcefabcabcefabc']

'''
1、从首字符开始，求出最长重复出现的字串且该最长字串自身不是恰好由重复字串即可；
1-1、不能依赖半分查找，例如,'abcabcab'
'''


def getLongestRepeat(s):
    toChk, i, limit = '', 1, len(s)
    while i <= limit:
        toChk = s[0:i]
        if toChk in s[i:]:
            i += 1
        else:
            toChk = toChk[0:-1]
            break
    toChkLen = len(toChk)
    if toChkLen > 1 and toChkLen % 2 == 0:
        halfLen = int(toChkLen / 2)
        if toChk[0:halfLen] == toChk[halfLen:]:
            if halfLen == 1:
                return toChk[0:halfLen]
            else:
                getLongestRepeat(toChk[0:halfLen])
    return toChk


for s in testCases:
    res = getLongestRepeat(s)
    print(s, '--->', res)

    '''
    算法2
    将这一问题，通过数学等式表达出来

    高度的概括性、等式的等价性、等式的必要充分性
    '''
    n = len(s)
    for i in range(1, n + 1):
        base = s[:i]
        if base * (n // i) + base[:n % i] == s:
            print(base)
            break
