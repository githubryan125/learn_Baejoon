import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = sc.nextInt();
        int burger = a;
        int drink = d;
        burger = Math.min(a,b);
        burger = Math.min(burger,c);
        drink = Math.min(d,e);
        System.out.println(burger+drink -50);
        
        
    }
}