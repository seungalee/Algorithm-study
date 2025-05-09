package 자바;

import java.io.BufferedReader;
import java.io.IOException; 
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class P17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] seq = new int[N];
        int[] result = new int[N];
        for(int i=0;i<N;i++){
            seq[i] = Integer.parseInt(st.nextToken());
        }
        Stack<Integer> stack = new Stack<>();

        for(int i=N-1;i>=0;i--){
            while(!stack.isEmpty() && stack.peek()<=seq[i]){
                stack.pop();
            }
            if(stack.isEmpty()){
                result[i] = -1;
            } else{
                result[i] = stack.peek();
            }

            stack.push(seq[i]);
        }

        StringBuilder sb = new StringBuilder();
        for(int val : result){
            sb.append(val).append(" ");
        }
        System.out.println(sb.toString());
    }
}
