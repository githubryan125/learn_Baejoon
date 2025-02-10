import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = n;
        int c = 0;
        int d = 0;
        int answer = 0;
        for(int i=0;i<99;i++){
            c = k%10;
            d = (k%10)*10 + (k/10+c)%10;
            answer++;
            if(d==n){
                break;
            }
            k = d;
        }
    System.out.println(answer);
    }
}