# 프로그래머스 스킬체크 level 2

###### 문제 설명

스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

| 종류 | 이름                       |
| ---- | -------------------------- |
| 얼굴 | 동그란 안경, 검정 선글라스 |
| 상의 | 파란색 티셔츠              |
| 하의 | 청바지                     |
| 겉옷 | 긴 코트                    |

스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
- 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
- 같은 이름을 가진 의상은 존재하지 않습니다.
- clothes의 모든 원소는 문자열로 이루어져 있습니다.
- 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
- 스파이는 하루에 최소 한 개의 의상은 입습니다.

##### 입출력 예

| clothes                                                      | return |
| ------------------------------------------------------------ | ------ |
| [[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]] | 5      |
| [[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]] | 3      |

##### 입출력 예 설명

예제 #1
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

```
1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
```

예제 #2
face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

```
1. crow_mask
2. blue_sunglasses
3. smoky_makeup
```



# 코드

```python
def solution(clothes):
    dict={}
    sum=1
    for i in range(len(clothes)):
        if dict.get(clothes[i][1], 0) == 0:
            dict[clothes[i][1]]=1
        else:
            dict[clothes[i][1]]+=1

    for i in dict.values():
        sum*=i+1

    return sum-1
```



# 설명

경우의 수를 구하는 문제인데 이렇게 생각했다.

만약 얼굴 , 상의, 하의 이렇게 있다고 했을때

얼굴 3가지의 경우의 수는 0,1,2,3

상의 2가지의 경우의 수는 0,1,2

하의 1가지의 경우의수 0,1

0은 아무것도 안쓸때 1,2,3은 각각의 인덱스의 값 이라고 생각하면 되겠다.

이럴경우 4 * 3* 2 = 24 인데 이떄 000은 빼야되니까 -1을 해준다.

이렇게 예제에 대입했을때

[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]

headgear 은 2개

eyewear 은 1개이다

안쓸경우를 계산해서 3* 2 하고 00의 경우를 빼면 5개가 나온다.



그래서 for문을 통해서 각 카테고리 별로 딕셔너리에 값을 넣어 개수를 새주고

위에서 정의한 계산식을 대입하여 리턴한다.