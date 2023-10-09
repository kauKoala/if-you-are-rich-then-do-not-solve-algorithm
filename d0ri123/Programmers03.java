package d0ri123;

/**
 *  최소 직사각형
 *  문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491
 */

public class Programmers03 {

  public static void main(String[] args) {
    Programmers03 sol = new Programmers03();
    int[][] sizes = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
//    int[][] sizes = {{10, 7}, {12, 3}, {8, 15}, {14, 7}, {5, 15}};
//    int[][] sizes = {{14, 4}, {19, 6}, {6, 16}, {18, 7}, {7, 11}};
    System.out.println(sol.solution(sizes));
  }

  public int solution(int[][] sizes) {
    int[] height = new int[sizes.length];
    int[] width = new int[sizes.length];

    int maxW = Integer.MIN_VALUE;
    int maxH = Integer.MIN_VALUE;

    for(int i=0; i<sizes.length; i++) {
      width[i] = Math.max(sizes[i][0], sizes[i][1]);
      height[i] = Math.min(sizes[i][0], sizes[i][1]);
      maxH = Math.max(maxH, height[i]);
      maxW = Math.max(maxW, width[i]);
    }

    return maxW * maxH;
  }
}
