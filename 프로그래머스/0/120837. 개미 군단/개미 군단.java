class Solution {
    public int solution(int hp) {
        int answer = 0;
        int a =0;
        int b=0;
        a=hp/5;
        b=(hp-(5*a))/3;
        answer+=(hp-(5*a)-(3*b))/1;
        return answer+a+b;
    }
}