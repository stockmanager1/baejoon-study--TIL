# 문제점 - 8/31

내가 set함수에 대해 잘 모르고 익숙하지가 않다. 항상 중복을 제거할때 not in 방법을 사용했는데 set을 사용하면 코드를 더 간결하게 만들 수 있다.

나는 2차원 리스트로 어찌 비벼보려고 했는데 처음부터 발상이 틀렸다.

이렇게 append((len(i),i))로 문제를 해결하는 걸 처음 해봄.

항상 단어만 나오면 split해서 어찌 하려고 했는데 이런 방법도 시도해보자.


# 문제점 - 9/7

sorted함수에 대해서 잘못 이해함. 

내장 함수는 파이썬에서 순회가 가능한(iterable) 객체를 인자로 받아 데이터를 정렬

sorted 내장 함수는 인자로 넘오온 객체의 원래 순서를 건드리지 않고 새로운 객체에 담아서 반환해준다.

파이썬에서는 리스트(list) 뿐만 아니라, 터플(tuple), 세트(set), 문자열(string)과 같은 다른 자료형도 순회가 가능

즉 별도로 갯수와 단어를 분리해서 정렬해줄 필요가 없다.

# 문제점 - 9/13
sorted 함수를 이용해서 풀었고 답이 나왔지만 여전히 출력 초과가 뜬다.

내가 푼 코드

    n = int(input())
    old_list = []
    for i in range(n):
      old_list.append(input())

    old_list = set(old_list)
    new_list = list(old_list)

    for i in new_list:
      new_list = sorted(new_list)

    count_list = []
    for i in new_list:
      a = list(i)
      count_list.append(len(a))

    final_list= []
    for len,word in zip(count_list,new_list):
      final = (len,word)
      final_list.append(final)
    
    final_list = sorted(final_list, key=lambda x:x[0])

    for len, word in final_list:
      print(word)
      
출력 초과가 나왔다.

처음 내가 찾은 풀이대로(물론 풀때 풀이를 참고한적은 없음.) sorted함수를 사용해서 잘 풀었다고 생각되는데...

아마 len을 구하는 부분에서 초과가 나왔을거 같다.

음.. 새로운 리스트를 통해 len을 구하는 방법 말고 sort함수를 사용해서 바로 len을 정렬하는 방법을 찾아야겠다.
