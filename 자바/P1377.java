package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P1377 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] nums = new int[N][2];

        for(int i=0;i<N;i++){
            nums[i][0] = Integer.parseInt(br.readLine());
            nums[i][1] = i;
        }

       //버블 정렬 시 몇번째에 정렬 완료되었는지를 출력
       //이걸 직접 버블 정렬 해보지 않고 어떻게 알 수 있을까?
       //몇 개가 원래와 순서 다른지 따지면 될까
       Arrays.sort(nums, (a, b) -> Integer.compare(a[0], b[0]));

       int answer = 0;

       for(int i=0;i<N;i++){
        int now = nums[i][1] - i;
        answer = Integer.max(answer, now);
       }
       answer++;
       System.out.println(answer);
        
    }
}
