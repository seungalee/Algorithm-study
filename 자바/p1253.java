package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class p1253 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int count = 0;
        for(int i=0;i<N;i++){
            int left = 0;
            int right = N-1;
            while(left<right){
                int sum = arr[left] + arr[right];
                if(sum == arr[i]){
                    if(left!=i && right !=i){
                        count++;
                        break;
                    } else if(left==i){
                        left++;
                    } else if(right==i){
                        right--;
                    }
                    
                }
                else if(sum < arr[i]){
                    left++;
                }
                else{
                    right--;
                }
            }
        }


        System.out.println(count);
    }
}
