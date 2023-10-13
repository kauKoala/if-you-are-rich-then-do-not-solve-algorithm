import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2661_좋은수열 {
    static int N;
    static int [] arr;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        arr = new int[N+1];
        recur(1, arr);

    }
    static void recur(int k, int [] arr) throws IOException {
        if (k == N+1){
            StringBuilder sb =new StringBuilder();
            for (int i =1; i<=N; i++){
                sb.append(arr[i]);
//                bw.write(arr[i]+"");
            }
//            bw.flush();
//            bw.close();
            System.out.println(sb);
            System.exit(0);
        }
        for (int i =1; i<=3; i++){
            if (arr[k-1] == i) continue;
            arr[k] = i;
            if (isBad(k, arr)) continue;
            recur(k+1, arr);
        }
        arr[k] = 0;
    }
    static boolean isBad(int k, int [] arr){
        //가능한 최대 길이를 구한다.
        int maxLen = k/2;
        //긴 길이부터 길이를 감소해가면서 일치하지 않으면 건너뛴다.
        Loop: for (int l = maxLen; l >=2 ; l--) {
            int L = k - l * 2 + 1;
            int R = k - l + 1;
            while (R <= k){
                if (arr[L] != arr[R]) continue Loop; //길이 l만큼은 일치하지 않는 것.
                L++; R++;
            }
            if (R == k+1){ // k까지 모두 같다는 것
                return true;
            }
        }
        return false; //어떤 연속된 부분수열도 반복되지 않으므로 good
    }
}
