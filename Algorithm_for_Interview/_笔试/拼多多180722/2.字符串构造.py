"""
�ַ�������

����������
    һ��������һ���ִ�ѭ�����ɣ��� s[i]=t[i%n]������ "abcabc" �� "abc" ����

    ע�⣺"abcabcab" Ҳ���� "abc" ���ɵģ�����ʱûע�������ֻ����һ����

    *����ʹ�� Python ����ַ���������⣬����Ҳֻ�� Python ����
"""

s = input()

n = len(s)
for i in range(1, n + 1) :
    base = s[:i]
    if base * (n // i) + base[:n % i] == s:
        print(base)
        break



'''
�����ݹ�
'''

testCases = ['aaaaa', 'aabaaba', 'abaabaa', 'abcabca', 'abcabcab', 'abcabceabcabceabc', 'abcabcefabcabcefabc']

'''
1�������ַ���ʼ�������ظ����ֵ��ִ��Ҹ���ִ�������ǡ�����ظ��ִ����ɣ�
1-1������������ֲ��ң�����,'abcabcab'
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
    �㷨2
    ����һ���⣬ͨ����ѧ��ʽ������

    �߶ȵĸ����ԡ���ʽ�ĵȼ��ԡ���ʽ�ı�Ҫ�����
    '''
    n = len(s)
    for i in range(1, n + 1):
        base = s[:i]
        if base * (n // i) + base[:n % i] == s:
            print(base)
            break
