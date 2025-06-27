package 자바;

import java.util.Scanner;

//삽입 정렬 방식으로 문제 해결
public class P11399 {
    public static void main(String[] args) {
        //N 입력받기
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        //Pi 배열 입력받기
        int[] times = new int[N];
        for(int i=0;i<N;i++){
            times[i] = sc.nextInt();
        }

        //삽입 정렬 구현
        //index= 1부터 시작~N-1까지
        for(int index = 1;index<N;index++){
            int num = times[index];
            int where = index;
            for(int j=index-1;j>=0;j--){
                if(times[j]<num){
                    where = j+1;
                    break;
                }
                if(j==0){
                    where = 0;
                }
            }
            for(int k=index;k>where;k--){
                    times[k] = times[k-1];
                }
                times[where] = num;
        }
        //index가 들어가야할 위치 찾기
        //index를 거기 넣5고 switch해가며 정렬 완료

        //정렬된 array에서 계산
        int total = 0;
        for(int i=0;i<N;i++){
            total += (times[i]*(N-i));
        }
        System.out.println(total);
    }
}
