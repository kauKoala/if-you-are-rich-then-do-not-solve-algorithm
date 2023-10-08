import java.awt.*;
import java.io.*;
import java.util.*;

class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static boolean [][] apple, snakeVisit;
    static int sDir, N;
    static ArrayList<Point> snake = new ArrayList<>();
    static HashMap<Integer, Character> hm = new HashMap<>();
    static int [] dx = {0,1,0,-1}, dy = {1, 0, -1,0};

    /*
    6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
     */
    public static void main(String[] args) throws IOException {
        //input
        N = Integer.parseInt(br.readLine());
        snakeVisit = new boolean[N+1][N+1];
        apple = new boolean[N+1][N+1];
        int appleSize = Integer.parseInt(br.readLine());
        while (appleSize-- > 0){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            apple[x][y] = true;

        }
        int times = Integer.parseInt(br.readLine());
        while (times-- > 0){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            char y = st.nextToken().charAt(0);
            hm.put(x, y);
        }

        snake.add(new Point(1,1));
        snakeVisit[1][1] = true;

        int time= 0;
        while (true){
            time++;

            Point head = snake.get(0);
            int nx = head.x + dx[sDir];
            int ny = head.y + dy[sDir];
            if (nx <= 0 || ny <= 0 || nx > N || ny > N || snakeVisit[nx][ny]){
                break;
            }

            snakeVisit[nx][ny] = true;
            snake.add(0, new Point(nx, ny));

            if (!apple[nx][ny]){
                Point tail = snake.remove(snake.size()-1);
                snakeVisit[tail.x][tail.y]=false;
            }
            if (apple[nx][ny]) apple[nx][ny] = false;

            System.out.println("======= "+time+" =========");
            System.out.println(snake);
            printMap(snakeVisit);
            System.out.println("apple==========================");
            printMap(apple);

            if (hm.containsKey(time)){
                char key = hm.get(time);
                if (key == 'L'){
                    sDir = sDir - 1 == 0? 3: sDir - 1;
                }else{
                    sDir = ( sDir + 1 ) % 4;
                }
            }
        }
        System.out.println(time);


    }
    static void printMap(boolean [][] map){
        for (int i = 1; i<=N; i++){
            for (int j = 1; j <= N; j++) {
                if (map[i][j]) System.out.printf("T");
                else System.out.printf("F");

            }
            System.out.println();
        }
    }
    static void printApple(){

    }


}