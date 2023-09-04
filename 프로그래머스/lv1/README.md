# Lv1 문제 풀면서 알게된 점들

### 1. `isNaN()`

`isNaN()`은 매개변수에 들어간 값이 `Not a Number`인지를 판별해주는 메서드다.  
얘를 쓰면 문자열에 있는 값이 숫자인지 아닌지를 판별하기 쉬울 것 같으나, 사실 이상한(?) 규칙들을 가지고 있는 친구인지라 완벽히 내 맘에 드는 결과가 나오지 않을 수 있다.  
예를 들어 `isNaN('')`는 false가 나온다. 빈 문자열은 문자열이 아니라 0으로 변환된 후, 체크하기 때문이다. 매개변수에 `'1e10'`같은 값이 들어가도 숫자로 인식한다. 따라서 12918번 문자열 다루기 기본 문제를 풀 때는 `isNaN()`을 사용하는 대신, `Number(s[i]) != s[i]`을 사용하여 문자열의 문자 하나하나에 접근해서 int형으로 바꿨을 때 같은 값이 나오는지 아닌지를 통해 숫자인지 아닌지를 판별하도록 했다.

- [Number에 대한 설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number)
- [isNaN에 대한 설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
- [Number.isNaN에 대한 설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
