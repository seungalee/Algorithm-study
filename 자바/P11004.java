package 자바;

import java.util.Scanner;

public class P11004 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0;i<N;i++){
            arr[i] = sc.nextInt();
        }
        quickSort(arr, 0, N-1, K-1);
        System.out.println(arr[K-1]);
    }


    public static void quickSort(int[] array, int start, int end, int K){
        if(start < end){
            int pivot = partition(array, start, end);
            if(pivot == K) 
                return;
            else if(pivot > K){
                quickSort(array, start, pivot-1, K);
            }
            else{
                quickSort(array, pivot+1, end, K);
            }
            
        }

    }

    public static int partition(int[] array, int start, int end){
        if(start+1 == end){
            if(array[start] > array[end]){
                swap(array, start, end);
                return end;
            }
        }
        int middle = (start + end) / 2;
        swap(array, start, middle);
        int pivot = array[start];
        int i = start + 1;
        int j = end;
        while(i<=j){
            while(j>=start+1 && pivot<array[j]){
                j--;
            }
            while(i<=end && pivot>array[i]){
                i++;
            }
            if(i<=j){
                swap(array, i++, j--);
            }
        }
        array[start] = array[j];
        array[j] = pivot;
        return j;
    }
    public static void swap(int[] array, int i, int j){
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
