package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
//병합 정렬 통한 문제 해결
//재귀 활용
public class P2751 {
    public static int[] nums, temp;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        nums = new int[N];
        temp = new int[N];

        for(int i=0;i<N;i++){
            nums[i] = Integer.parseInt(br.readLine());
        }
        merge_sort(0, N-1);
        for(int i=0;i<N;i++){
            System.out.println(nums[i]);
        }
    }

    private static void merge_sort(int s, int e){
        if(e-s<1) return;
        int m = s+(e-s)/2;
        merge_sort(s, m);
        merge_sort(m+1, e);
        for(int i=s;i<=e;i++){
            temp[i] = nums[i];
        }
        int k = s;
        int index1 = s;
        int index2 = m+1;
        while(index1<=m && index2<=e){
           if(temp[index1]>temp[index2]){
            nums[k] = temp[index2];
            k++;
            index2++;
           } 
           else{
            nums[k] = temp[index1];
            k++;
            index1++;
           }
        }
        while (index1<=m) {
            nums[k] = temp[index1];
            k++;
            index1++;
        }
        while (index2<=e) {
            nums[k] = temp[index2];
            k++;
            index2++;
        }
    }
}
