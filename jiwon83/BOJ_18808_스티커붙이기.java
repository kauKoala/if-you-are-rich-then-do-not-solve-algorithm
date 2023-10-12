import java.awt.Point;
import java.io.*;
import java.util.*;


public class BOJ_18808_스티커붙이기 {
    static class Sticker{
        int r,c;
        List<Point> contents;
        public Sticker(int r, int c){
            this.r = r;
            this.c  = c;
            contents = new ArrayList<>();
        }
        void rotate(){

                for (int i = 0; i<contents.size(); i++){
                    Point p = contents.get(i);
                    int rX = r-1 - p.x;
                    contents.get(i).setLocation(p.y, rX);
                }
                int tmp = r;
                this.r = c;
                this.c = tmp;
        }
    }

    static int [][] board;
    static int N, M, K;
    static List<Sticker> stickers;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        input();
        for (Sticker sticker : stickers){
            attach(sticker, board);
        }
        System.out.println(countAttached(board));
    }

    private static int countAttached(int[][] board) {
        int cnt = 0;
        for (int i = 0; i< N; i++){
            for(int j = 0; j< M; j++){
                if(board[i][j] == 1) cnt++;
            }
        }
        return cnt;
    }

    private static void input() throws IOException{
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        K = Integer.parseInt(st.nextToken());
        stickers = new ArrayList<>();
        for (int i = 0; i<K ; i++){

            st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
            stickers.add(new Sticker(R, C));

            for (int r = 0; r <R; r++){
                st = new StringTokenizer(br.readLine());
                for (int c = 0; c <C; c++){
                    int n = Integer.parseInt(st.nextToken());
                    if(n == 1) stickers.get(i).contents.add(new Point(r, c));
                }
            }
        }

    }

    private static void attach(Sticker sticker, int[][] board) {
        //공간을 찾는다.
        for (int rot = 0; rot < 4; rot++){ // 4번 rot 만큼 회전해본다.
            if (rot != 0) sticker.rotate();
            for (int i = 0; i<N; i++){
                for(int j = 0; j<M; j++){
                    boolean find = true;
                    for (Point p : sticker.contents){
                        int nx = i + p.x;
                        int ny = j + p.y;
                        if (!inArea(nx, ny) || board[nx][ny] == 1){
                            find = false;
                            break;
                        }
                    }
                    if (find) { // 스티커를 붙인다.
                        for (Point p : sticker.contents){
                            board[p.x + i][p.y + j] = 1;
                        }
                        return;
                    }
                }
            }
        }

    }
    static boolean inArea(int x, int y){
        return x >=0 && y >=0 && x < N && y < M;
    }
}