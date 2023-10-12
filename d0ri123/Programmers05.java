package d0ri123;

import java.util.HashMap;

/**
 * 전화번호 목록
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577
 */

public class Programmers05 {

  public static void main(String[] args) {
    Programmers05 sol = new Programmers05();
//    String[] phone_book = {"119", "97674223", "1195524421"};
//     String[] phone_book = {"123","456","789"};
     String[] phone_book = {"12","123","1235","567","88"};
    System.out.println(sol.solution(phone_book));

  }

  public boolean solution(String[] phone_book) {
    boolean answer = true;
    HashMap<String, Integer> map = new HashMap<>();

    for(int i=0; i<phone_book.length; i++) {
      map.put(phone_book[i], i);
    }

    for(int i=0; i<phone_book.length; i++) {
      for(int j=1; j<phone_book[i].length(); j++) {
        if(map.containsKey(phone_book[i].substring(0, j))) return false;
      }
    }
    return answer;
  }

}
