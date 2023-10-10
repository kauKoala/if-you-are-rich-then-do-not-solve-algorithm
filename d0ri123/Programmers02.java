package d0ri123;

import java.util.HashMap;
import java.util.Map;

/**
 * 폰켓몬
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845
 */
public class Programmers02 {
  public static void main(String[] args) {
    Programmers02 sol = new Programmers02();
    int[] nums = {3,1,2,3};
//    int[] nums = {3,3,3,2,2,4};
//    int[] nums = {3,3,3,2,2,2};
    System.out.println(sol.solution(nums));
  }

  public int solution(int[] nums) {
    int answer = 0;
    int len=nums.length/2;
    Map<Integer, Integer> map = new HashMap<>();
    for(int i=0; i<nums.length; i++) {
      map.put(nums[i], i+1);
    }
    for(int x: map.keySet()){
      answer = Math.min(len, map.size());
    }
    return answer;
  }
}
