import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] small = new int [9];
        int sum = 0;
        boolean flag = false;
        for(int i=0;i<9;i++){
            small[i] = sc.nextInt();
            sum += small[i];
        }
        for(int i=0;i<9;i++){
            if(flag){break;}
            for(int j=i+1;j<9;j++){
                int mid = sum - small[i] - small[j];
                if(mid == 100){
                    small[i]=0;
                    small[j]=0;
                    flag = true;
                }
            }
        }
        Arrays.sort(small);
        for(int ans:small){
            if(ans!=0){
                System.out.println(ans);
            }
        }
        
    }
}