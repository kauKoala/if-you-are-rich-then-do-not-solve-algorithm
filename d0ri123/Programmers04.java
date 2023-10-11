package d0ri123;

import java.util.HashMap;

/**
 * 완주하지 못한 선수
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
 */

public class Programmers04 {

  public static void main(String[] args) {
    Programmers04 sol = new Programmers04();
    String[] participant = {"leo", "kiki", "eden"};
    String[] completion = {"eden", "kiki"};

//    String[] participant = {"marina", "josipa", "nikola", "vinko", "filipa"};
//    String[] completion = {"josipa", "filipa", "marina", "nikola"};

//    String[] participant = {"mislav", "stanko", "mislav", "ana"};
//    String[] completion = {"stanko", "ana", "mislav"};

    System.out.println(sol.solution(participant, completion));
  }

  public String solution(String[] participant, String[] completion) {
    String answer = "";
    HashMap<String, Integer> list = new HashMap<>();
    // 참가선수 이름과 참가 인원수를 map에 넣는다.
    for(String name : participant) {
      list.put(name, list.getOrDefault(name,0)+1);
    }

    // completion 배열을 돌면서 차감한다.
    for(String winner : completion) {
      list.put(winner, list.get(winner)-1);
    }

    // 여전히 value가 남은 선수의 이름을 반환한다.
    for(String name : list.keySet()) {
      if(list.get(name) != 0) {
        answer = name;
      }
    }

    return answer;
  }

}
