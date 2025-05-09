package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class P2164 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        int num = N;
        for(int i=0;i<N;i++){
            queue.offer(num--);
        }
        while(queue.size()>1){
            queue.removeLast();
            int getOne = queue.removeLast();
            queue.addFirst(getOne);
        }
        System.out.println(queue.getLast());

    }
}
