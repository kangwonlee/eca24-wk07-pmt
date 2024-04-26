wk08 disc_prob

# Probability Analysis with Probability Mass Functions<br>확률질량함수 확률 해석

* This is your assignment repository for Week 8 of Engineering Computational Analysis.<br>이것은 공학전산해석 8주차 과제 저장소이다.
* The focus of this assignment is understanding probability mass functions (PMFs) and how to calculate probabilities within intervals.<br>이 과제는 확률질량함수(PMF)의 이해와 구간 내 확률을 계산하는 방법에 관한 것이다.

## Instructions<br>지시사항

* Do not rename any of the provided files.<br>제공된 파일의 이름을 변경하지 마시오.
* Your primary coding work will be within the `main.py` file. Complete the implementation of the `wk08()` function according to the assignment instructions.<br>주요 코딩 작업은 `main.py` 파일 내에서 이루어질 것임. 과제 지시에 따라 `wk08()` 함수를 완성하시오.
* The `sample.py` file demonstrates how to import and call your wk08() function.<br>`wk08()` 함수를 import 하여 호출하는 방법에 대해서는 `sample.py` 파일을 참고하시오.

## Problem Description<br>문제 설명
* Let's say we are trying to mass produce gears for a precision machine.<br>정밀기계 부품으로 사용할 톱니바퀴를 대량생산하려고 한다고 가정하자.
* Due to slight variations in the manufacturing process, a small percentage of the gears may have defects.<br>생산 공정상의 미세한 가변성으로 일부 톱니바퀴에는 결함이 있을 수 있다.
* The following PMF represents the probability of having a specific number of defects in a single gear.<br>아래 PMF 는 단일 톱니바퀴에 특정 결함 수가 생길 확률의 예를 나타낸다.
    * here, keys are the number of defects per gear<br>여기서 key는 각 톱니바퀴에 나타날 수 있는 결함의 수이며
    * and values are the probability of a gear having that number of defects<br>value 는 해당 결함 수를 가진 톱니바퀴가 만들어질 확률이다.

``` python
pmf = {0: 0.8, 1: 0.15, 2: 0.04, 3: 0.01}
```
* Function `wk08()` will take the following arguments (see table below).<br>함수 `wk08()` 는 다음과 같은 인자를 받아들이도록 작성하시오 (아래 표 참조).

| Argument<br>인자 | Data Type<br>자료형 | Description<br>설명 
|:---:|:---:|---
| `pmf` | dict | A dictionary representing the probability mass function.<br>pmf 를 담은 딕셔너리
| `lower_bound` | int | The lower bound of the **closed** interval.<br>구간의 하한 (**닫힌** 구간으로 하한을 포함)
| `upper_bound` | int | The upper bound of the **closed** interval.<br>구간의 상한 (**닫힌** 구간으로 상한을 포함)

* The function should return the probability of gears with number of defects within the **inclusive** (closed) interval.<br>해당 함수가 톱니바퀴에 결함 수가 주어진 **닫힌** 구간 내에 포함될 확률을 반환하도록 구현하시오.

| Return Value<br>반환값 | Data Type<br>자료형 | Description<br>설명
|:---:|:---:|---|
| `p` | `float` | The probability that the gear has the number of defects within the closed interval <br>톱니바퀴에 결함 수가 구간 내에 포함되는 확률

## Rubric<br>채점기준

Task<br>항목 | Points<br>점수 | Description<br>설명
:---:|:---:|---
grammar<br>문법 | 2 | The code is free of grammatical errors<br>코드에 문법적 오류가 없음
all lines in the function<br>모든 코드가 함수 내 포함 | 2 | All lines of code are within the function<br>모든 코드가 함수 내에 위치함
result<br>결과 | 2 | The code produces the correct result<br>코드가 올바른 결과를 내 놓음

## How to use Github web editor<br>Github 웹 편집기 사용법
* Press <kbd>.</kbd> key to start MS VS Code web editor<br><kbd>.</kbd> 키를 누르면 MS VS Code 의 Web version 이 시작됨
* Make changes to the file<br>파일을 수정
* From the left bar with the three horizontal lines at the top, (right below the magnifying glass) choose third icon, Source Control<br>왼쪽에서 줄 셋 아래 (확대경 다음) 세번째 가지치기 아이콘 선택
* Choose filename to see changes<br>변경 사항을 보려면 파일 이름 선택
* To stage changes to commit, choose + on the right side of the filename <br>수정 사항을 commit 등록 대상으로 add 추가 하려면 파일 이름의 오른쪽 + 기호 선택
* Describe the changes in the blank above<br>위 빈칸에 변경 사항 설명 입력
* Choose Commit<br>[커밋 및 푸시] 선택
* To return to the repository, use the command in the three horizontal lines<br>줄 셋 의 [리포지토리로 이동] 선택하여 저장소로 복귀
