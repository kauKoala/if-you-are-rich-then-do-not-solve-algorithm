package d0ri123;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 가장 가까운 같은 글자
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/142086?language=java
 *
 */
public class Programmers01 {
  public static void main(String[] args) {
    Programmers01 sol = new Programmers01();

    int[] ans = sol.solution("banana");
//    int[] ans = sol.solution("foobar");

    System.out.println(Arrays.toString(ans));
  }

  public int[] solution(String s) {
    int length = s.length();

    //글자수가 1밖에 되지 않을 때, -1이 담긴 배열을 바로 반환
    if(length == 1) {
      return new int[]{-1};
    }

    //반환할 배열을 생성한다.
    int[] answer = new int[length];

    Map<Character, Integer> map = new HashMap<>();

    //map은 문자들의 갱신되는 위치 정보를 저장하는 역할을 한다.
    for(int i=0; i<length; i++) {
      char ch = s.charAt(i);
      if(map.containsKey(ch)) {
        Integer value = map.get(ch);
        answer[i] = (i+1) - value;
      } else {
        answer[i] = -1;
      }
      map.put(ch, i+1);
    }
    return answer;
  }

}
