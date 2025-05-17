package 자바;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1204 {
	public static void main(String[] args) throws FileNotFoundException {
		
		System.setIn(new FileInputStream("자바/res/input.txt"));
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=Integer.parseInt(sc.nextLine());
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int testNum = sc.nextInt(); // 테스트케이스 번호

            int[] scores = new int[101]; // 점수 빈도수 배열

            // 점수 1000개 입력 받기
            for (int i = 0; i < 1000; i++) {
                int score = sc.nextInt();
                scores[score]++;
            }

            // 최빈값 찾기
            int maxCount = 0;
            int answer = 0;
            for (int i = 0; i <= 100; i++) {
                if (scores[i] >= maxCount) {
                    maxCount = scores[i];
                    answer = i; // 점수가 더 크면 갱신
                }
            }

            // 출력
            System.out.println("#" + testNum + " " + answer);
        
			
			
			
		}
	}

}
