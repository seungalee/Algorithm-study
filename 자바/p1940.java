package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class p1940 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[N];
        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        //정렬 후 투 포인트 방식으로 문제 해결
        Arrays.sort(arr);
        int left = 0;
        int right = N-1;
        int count = 0;

        while(left < right){
            int sum = arr[left] + arr[right];
            if(sum == M){
                
                int a = 1;
                int b = 1;
                //문제에서 두 숫자는 고유하다고 한 걸 놓치고 쓸데없는 예외 처리를 함
                while(arr[left]==arr[left+1]){
                    a++;
                    left++;
                }
                while(arr[right] == arr[right-1]){
                    b++;
                    right--;
                }
                count += (a*b);
                left++;
                right--;
            }
            else if(sum < M){
                left++;
            }
            else{
                right--;
            }
        }
    System.out.println(count);
    }
}
