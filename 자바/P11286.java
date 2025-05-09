package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P11286 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (a, b) -> {
                int absA = Math.abs(a);
                int absB = Math.abs(b);
                if(absA==absB) return a - b;
                return absA - absB;
            }
        );
        for(int i=0; i<N;i++){
            int nowNum = arr[i];
            if(nowNum==0){
                if(pq.size()==0){
                    System.out.println(0);
                }
                else{
                    System.out.println(pq.poll());
                }
            } else{
                pq.offer(nowNum);
            }
        }

        
    }
}
