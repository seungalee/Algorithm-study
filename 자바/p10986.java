package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p10986 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] sum = new int[N+1];
        int[] remainder = new int[M];
        int answer = 0;


        for(int i=1;i<=N;i++){
            sum[i] = sum[i-1] + Integer.parseInt(st.nextToken());
        }
        for(int i=1;i<=N;i++){
            int rem = sum[i] % M;
            if(rem==0){
                answer+=1;
            }
            remainder[rem]+=1;
        }

        for(int i=0; i<M;i++){
            answer += (remainder[i]*(remainder[i]-1))/2;
        }
       
        System.out.print(answer);
    }
}
