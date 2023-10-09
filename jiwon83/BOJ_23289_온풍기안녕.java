import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_23289_온풍기안녕 {
    static class Machine{
        int x,y,dir;
        public Machine(int x, int y, int dir){
            this.x = x;
            this.y = y;
            this.dir = dir;
        }
    }
    static class Wind{
        int x, y, temp, pass;

        public Wind(int x, int y, int temp, int pass){
            this.x = x;
            this.y = y;
            this.temp = temp;
            this.pass = pass;
        }
    }
    static class Space{
        int temp;
        boolean [] wall; // 0 , 1, 2, 3 시계 방향으로 벽의 존재를 표현
        public Space(){
            temp=0;
            wall = new boolean[4];
        }

    }

    static List<Machine> machines;
    static Space [][] temp;
    static List<Point> checkList;
    static int R,C, K;
    static int[][] dirs = {{-1,0}, {0,1}, {1,0}, {0,-1}};
    static StringTokenizer st;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static void input() throws IOException{
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        temp = new Space[R+1][C+1];
        for (int i = 1; i <= R ; i++) {
            for (int j = 1; j <= C; j++){
                temp[i][j] = new Space();
            }

        }

        machines = new ArrayList<>();
        checkList = new ArrayList<>();

        for (int i = 1; i <= R ; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= C; j++) {
                int num = Integer.parseInt(st.nextToken());
                switch (num){
                    case 1 :
                        machines.add(new Machine(i, j,1));
                        break;
                    case 2 :
                        machines.add(new Machine(i, j,3));
                        break;
                    case 3 :
                        machines.add(new Machine(i, j,0));
                        break;
                    case 4 :
                        machines.add(new Machine(i, j,2));
                        break;
                    case 5 :
                        checkList.add(new Point(i, j));
                        break;
                    default:
                        break;
                }
            }
        }

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            if (k == 0){
                temp[x][y].wall[0]=true;
                temp[x-1][y].wall[2]=true;
            }else{
                temp[x][y].wall[1]=true;
                temp[x][y+1].wall[3]=true;
            }
        }

    }

    public static void main(String[] args) throws IOException{
        input();

        int ate = 0;
        while (ate <= 100){
            //1. 모든 온풍기에 대해 온도 상승을 계산
            for (Machine m : machines){
                updateTempByMachine(m, temp);
            }

            //2. temp에 대해 온도 조절
            flatten(temp);

            //3. 바깥쪽 온도 하락
            downSideTemp(temp);

            ate++;

            //4. 모든 칸 검사
            int checked = 0;
            for ( Point p : checkList){
                if (temp[p.x][p.y].temp >= K) checked++;
            }
            //5. 종료 조건
            if (checked == checkList.size()) break;
        }
        System.out.println(ate);
    }
    private static void downSideTemp(Space[][] temp){
        for (int i = 1; i<=R; i++){
            if (temp[i][1].temp != 0) temp[i][1].temp--;
            if (temp[i][C].temp != 0) temp[i][C].temp-- ;
        }
        for (int i = 2; i <= C-1; i++){
            if (temp[1][i].temp != 0) temp[1][i].temp--;
            if (temp[R][i].temp != 0) temp[R][i].temp--;
        }
    }
    private static void flatten(Space[][] temp){
        int [][] quan = new int[R+1][C+1];
        for (int i = 1; i<= R; i++){
            for (int j = 1; j<=C; j++){
                for (int d = 0; d <4; d++){
                    int nx = i + dirs[d][0];
                    int ny = j + dirs[d][1];
                    if(inArea(nx, ny)){
                        int wallDir = (d + 2) % 4;
                        if (temp[nx][ny].wall[wallDir]) continue;
                        int gap = Math.abs(temp[i][j].temp - temp[nx][ny].temp);
                        if (temp[i][j].temp > temp[nx][ny].temp){
                            quan[i][j] -= gap / 4;
                        }
                        if (temp[i][j].temp < temp[nx][ny].temp){
                            quan[i][j] += gap / 4;
                        }
                    }
                }
            }
        }
        for (int i = 1; i<= R; i++) {
            for (int j = 1; j <= C; j++) {
                temp[i][j].temp += quan[i][j];
            }
        }
    }

    private static void updateTempByMachine(Machine m,  Space[][] temp) {
        int [][] nowTemp = new int[R+1][C+1];
        ArrayDeque<Wind> q = new ArrayDeque<>();
        boolean [][] ch = new boolean[R+1][C+1];
        int sx = m.x + dirs[m.dir][0];
        int sy = m.y + dirs[m.dir][1];
        q.addLast(new Wind(sx, sy, 5, 0));
//        ch[sx][sy] = true;

        while (!q.isEmpty()){
            Wind now = q.pollFirst();

            if (now.pass == 0 ) nowTemp[now.x][now.y] = now.temp; //이동중이 아니라면 온도 상승에 갱신

            if (now.pass == 1){ // 이동 중인 위치였다면, 머신 방향 탐색
                int nx = now.x + dirs[m.dir][0];
                int ny = now.y + dirs[m.dir][1];
                if( !inArea(nx, ny)) continue;
                int wallDir = (m.dir + 2) % 4;
                if (ch[nx][ny]) continue;
                if (temp[nx][ny].wall[wallDir]){
                    continue; // 벽이 있다면 가지 않는다.
                }
                ch[nx][ny] = true; //방문체크
                q.addLast(new Wind(nx, ny, now.temp, 0));

            }else{ //머신 방향, 양방향 탐색
                int sideDir[] = new int[3]; //탐색 방향
                if (m.dir % 2 == 0){
                    sideDir[0] = 1; sideDir[1]=3; sideDir[2] = m.dir;
                }else{
                    sideDir[0] = 0; sideDir[1]=2; sideDir[2] = m.dir;
                }

//
                // 양방향으로는 pass를 1으로, 머신방향으로는 pass를 0으로 다음 좌표 탐색
                for (int i = 0; i < 3; i++){
                    int dir = sideDir[i];
                    int nx = now.x + dirs[dir][0];
                    int ny = now.y + dirs[dir][1];
                    if( !inArea(nx, ny) || now.temp == 1) continue;
                    int wallDir = (dir + 2) % 4;
                    if (temp[nx][ny].wall[wallDir]) continue;
                    if (i == 2){
//                    if (i == 2  && !ch[nx][ny] ){
                        ch[nx][ny] = true;
                        q.addLast(new Wind(nx, ny, now.temp-1, 0)); //머신 방향 탐색
                    }
                    else q.addLast(new Wind(nx, ny, now.temp-1, 1)); //양쪽 방향 탐색

                }
            }
        }
        //temp에 더한다.
        for (int i = 1; i <=R ; i++){
            for(int j = 1; j<=C; j++){
                temp[i][j].temp += nowTemp[i][j];
            }
        }
    }

    static boolean inArea(int x, int y){
        return x >= 1 && y >= 1 && x <= R && y <= C;
    }
    static void printSpaceMapTemp(Space [][] temp){
        System.out.println("-----------temp-----------");
        for (int i = 1; i <=R ; i++){
            for(int j = 1; j<=C; j++){
                System.out.printf(temp[i][j].temp+" ");
            }
            System.out.println();
        }
        System.out.println("------------------------");
    }
    static void printMap(int [][] nowTemp){
        System.out.println("-----------print-----------");
        for (int i = 1; i <=R ; i++){
            for(int j = 1; j<=C; j++){
                System.out.printf(nowTemp[i][j]+"");
            }
            System.out.println();
        }
        System.out.println("------------------------");
    }
}
