A = {'A+':4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0,}
score_전공평점 = []
score_학점=0
for i in range(20):
  a,b,c = input().split()
  if c == "P":
    pass
  else:
    score_학점 = score_학점 + float(b)
    학점 = float(b)
    등급 = A[c]
    전공평점 = 학점 * 등급
    score_전공평점.append(전공평점)
    
a = sum(score_전공평점)/score_학점

print('%.6f' % a)