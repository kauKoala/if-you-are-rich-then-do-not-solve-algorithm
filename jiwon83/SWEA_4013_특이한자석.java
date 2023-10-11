import java.awt.Point;
import java.io.*;
import java.util.*;

public class Solution {

	static class Magnet {
		int[] mag;
		int red;
		int left;
		int right;

		public Magnet(String input) {
			this.mag = new int[8];
			StringTokenizer st = new StringTokenizer(input, " ");
			for (int i = 0; i < 8; i++) {
				this.mag[i] = Integer.parseInt(st.nextToken());
			}
			this.red = 0;
			this.left = 6;
			this.right = 2;
		}

		@Override
		public String toString() {
			return "Magnet [red=" + red + ", left=" + left + ", right=" + right + "]";
		}

	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int[] works; // 회전해야할 작업 : idx = 번호, 회전 방향
	static boolean[] ch;
	static int K;
	static List<Magnet> magnets;

	public static void main(String[] args) throws IOException {

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {

			K = Integer.parseInt(br.readLine());
			magnets = new ArrayList<>();

			for (int i = 0; i < 4; i++) {
				String temp = br.readLine();
				magnets.add(new Magnet(temp));
			}

			for (int k = 0; k < K; k++) {
				// 회전
				works = new int[4];
				ch = new boolean[8];
				st = new StringTokenizer(br.readLine());
				int num = Integer.parseInt(st.nextToken()) - 1;
				int rot = Integer.parseInt(st.nextToken());

				getRotateInfo(magnets, num, rot, works, ch);

				doRotate(magnets, works);

			}

			int ans = getScore(magnets);
			System.out.println("#" + tc + " " + ans);

		}

	}

	private static int getScore(List<Magnet> magnets) {
		int result = 0;
		int[] score = { 1, 2, 4, 8 };
		for (int i = 0; i < 4; i++) {

			if (magnets.get(i).mag[magnets.get(i).red] == 1)
				result += score[i];
		}
		return result;
	}

	private static void doRotate(List<Magnet> magnets, int[] works) {
		for (int i = 0; i < 4; i++) {
			int r = works[i];
			if (r == 0)
				continue; // 어느 회전도 없는 상태
			if (r == 1) { // 시계 방향이면
				magnets.get(i).red = magnets.get(i).red - 1 == -1 ? 7 : magnets.get(i).red - 1;
				magnets.get(i).left = magnets.get(i).left - 1 == -1 ? 7 : magnets.get(i).left - 1;
				magnets.get(i).right = magnets.get(i).right - 1 == -1 ? 7 : magnets.get(i).right - 1;
			}
			if (r == -1) { // 반시계 방향이면
				magnets.get(i).red = (magnets.get(i).red + 1) % 8;
				magnets.get(i).left = (magnets.get(i).left + 1) % 8;
				magnets.get(i).right = (magnets.get(i).right + 1) % 8;
			}

		}

	}

	private static void getRotateInfo(List<Magnet> magnets, int num, int rot, int[] works, boolean[] ch2) {

		// 저장된 회전 정보를 시작으로 양 옆 자석의 맞닿은 위치 확인
		ArrayDeque<int[]> q = new ArrayDeque<>(); // [0] = 자석번호, [1] = 방향

		q.add(new int[] { num, rot });
		ch[num] = true;

		while (!q.isEmpty()) {
			int[] now = q.pollFirst();
			int n = now[0]; // 자석 번호
			int r = now[1]; // 방향 1 or -1
			works[n] = r; // 작업 목록에 저장
			Magnet m = magnets.get(n);
			// 양 쪽 방향 확인
			if (n != 0 && !ch[n - 1]) { // left

				Magnet mLeft = magnets.get(n - 1);
				if (mLeft.mag[mLeft.right] != m.mag[m.left]) { // 왼쪽 자석의 오른쪽 면과 현재 자석의 왼쪽 면이 다르다면
					ch[n - 1] = true;
					q.addLast(new int[] { n - 1, -1 * r });
				}

			}
			if (n != 3) { // right
				if (ch[n + 1])
					continue;
				Magnet mRight = magnets.get(n + 1);
				if (mRight.mag[mRight.left] != m.mag[m.right]) { // 왼쪽 자석의 오른쪽 면과 현재 자석의 왼쪽 면이 다르다면
					ch[n + 1] = true;
					q.addLast(new int[] { n + 1, -1 * r });
				}
			}
		}

	}

}
