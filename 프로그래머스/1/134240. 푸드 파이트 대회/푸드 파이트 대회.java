class Solution {
    public String solution(int[] food) {
        String answer = "";
        int cnt = 0;
        for(int i=1;i<food.length;i++){
            cnt = food[i]/2;
            for(int j=0;j<cnt;j++){
                answer+=i;
            }
        }
        answer+="0";
        for(int i=food.length-1;i>0;i--){
            cnt = food[i]/2;
            for(int j=0;j<cnt;j++){
                answer+=i;
            }
        }
        return answer;
    }
}

// 배열 첫번째 무시 
// 배열 두번째부터 2로 나눠